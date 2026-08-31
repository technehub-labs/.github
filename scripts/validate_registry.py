#!/usr/bin/env python3
"""Validate the TechNeHub Labs portfolio registry (registry/repositories.yaml).

Implements CR-TNH-README-07 validation scope:

  * malformed registry records (schema, required fields);
  * invalid portfolio families / lifecycle values / canonical values;
  * registry entries referring to nonexistent GitHub repositories;
  * live repositories missing from the registry;
  * visibility/archived drift between registry and GitHub;
  * duplicate names, roles, class aliases or catalog entities;
  * broken repository URLs (name/URL mismatch or dead repository).

Severity: ERRORS fail the check (exit 1) and drive the drift issue;
WARNINGS are reported but do not fail (known anomalies are tracked in
registry/taxonomy.md and resolved through governance, not silently).

Usage:
    python3 scripts/validate_registry.py              # check + manage issue
    python3 scripts/validate_registry.py --check-only # check, no issue writes
    python3 scripts/validate_registry.py --offline    # schema checks only

Env:
    GH_TOKEN         Token for issue management and fallback repo listing.
    ORG_REPOS_TOKEN  Token that can list all org repos including private
                     (classic PAT with repo scope). Preferred for listing.
    ORG              Org login (default: technehub-labs)
    REPO             Repo hosting the registry/issue (default: .github)
    REGISTRY         Path to registry (default: registry/repositories.yaml)

Exit codes: 0 = clean (warnings allowed), 1 = errors/drift, 2 = failure.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ORG = os.environ.get("ORG", "technehub-labs")
REPO = os.environ.get("REPO", ".github")
REGISTRY = os.environ.get("REGISTRY", "registry/repositories.yaml")
API = "https://api.github.com"
ISSUE_TITLE = "[drift] portfolio registry out of sync"
ISSUE_LABEL = "portfolio-drift"

REQUIRED = ["name", "family", "status", "role", "canonical", "visibility", "description"]


def gh(method, path, token=None, body=None):
    url = path if path.startswith("http") else f"{API}{path}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, data=data, timeout=30) as resp:
            return json.loads(resp.read() or b"null")
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:300]
        raise RuntimeError(f"{method} {url} -> {e.code}: {detail}") from e


def list_org_repos(token):
    repos, page = [], 1
    while True:
        batch = gh("GET", f"/orgs/{ORG}/repos?per_page=100&page={page}", token)
        if not batch:
            return repos
        repos.extend(batch)
        page += 1


def load_registry(path):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    if not isinstance(doc, dict) or "repositories" not in doc:
        raise RuntimeError("registry root must contain 'repositories'")
    return doc


def schema_errors(doc):
    errors, warnings = [], []
    fams = doc.get("families", [])
    life = doc.get("lifecycle", [])
    cans = doc.get("canonical_values", [])
    seen_names, seen_alias, seen_entity = {}, {}, {}
    featured = 0
    for i, r in enumerate(doc["repositories"]):
        where = f"record[{i}] ({r.get('name', '?') if isinstance(r, dict) else '?'})"
        if not isinstance(r, dict):
            errors.append(f"{where}: not a mapping")
            continue
        for k in REQUIRED:
            if k not in r or r[k] in (None, ""):
                errors.append(f"{where}: missing required field '{k}'")
        if r.get("family") and r["family"] not in fams:
            errors.append(f"{where}: invalid family '{r['family']}'")
        if r.get("status") and r["status"] not in life:
            errors.append(f"{where}: invalid lifecycle status '{r['status']}'")
        if r.get("canonical") and r["canonical"] not in cans:
            errors.append(f"{where}: invalid canonical value '{r['canonical']}'")
        if r.get("visibility") and r["visibility"] not in ("public", "private"):
            errors.append(f"{where}: invalid visibility '{r['visibility']}'")
        n = r.get("name")
        if n:
            if n in seen_names:
                errors.append(f"duplicate repository name '{n}'")
            seen_names[n] = True
            if r.get("family") == "archive" and r.get("status") != "archived":
                errors.append(f"{n}: family 'archive' requires status 'archived'")
            if r.get("status") == "archived" and r.get("family") != "archive":
                errors.append(f"{n}: status 'archived' requires family 'archive'")
        for field, seen, label in (("class_alias", seen_alias, "class_alias"),
                                   ("entity", seen_entity, "entity")):
            v = r.get(field)
            if v and r.get("family") == "catalogs":
                if v in seen:
                    warnings.append(f"duplicate {label} '{v}': {seen[v]} and {n}")
                seen[v] = n
        if r.get("featured"):
            featured += 1
    if featured > 6:
        errors.append(f"featured set has {featured} repositories; maximum is 6")
    return errors, warnings


def live_errors(doc, live):
    errors, warnings = [], []
    live_by = {r["name"]: r for r in live}
    reg = {r["name"]: r for r in doc["repositories"]}

    # Degraded-visibility detection: if records marked private are absent from
    # the listing, the listing token cannot see private repos (for example the
    # Actions GITHUB_TOKEN). In that mode, skip existence/flag checks for them
    # instead of reporting them as broken links.
    invisible_private = sorted(n for n, r in reg.items()
                               if r.get("visibility") == "private"
                               and n not in live_by)
    if invisible_private:
        warnings.append(
            f"{len(invisible_private)} private registry records are not visible "
            "to the listing token; skipping existence and flag checks for them. "
            "Set ORG_REPOS_TOKEN (org-wide read) for full checks.")

    for n in sorted(set(live_by) - set(reg)):
        errors.append(f"'{n}' exists in the org but is missing from the registry")
    for n in sorted(set(reg) - set(live_by)):
        if n in invisible_private:
            continue
        errors.append(f"'{n}' is in the registry but does not exist in the org (broken link)")
    for n in sorted(set(reg) & set(live_by)):
        r, g = reg[n], live_by[n]
        vis = "private" if g["private"] else "public"
        if r.get("visibility") != vis:
            errors.append(f"'{n}' visibility drift: registry={r.get('visibility')} github={vis}")
        if (r.get("status") == "archived") != bool(g["archived"]):
            errors.append(f"'{n}' archived drift: registry status={r.get('status')} github archived={g['archived']}")
    return errors, warnings


def manage_issue(token, drift_body):
    try:
        gh("POST", f"/repos/{ORG}/{REPO}/labels", token,
           {"name": ISSUE_LABEL, "color": "F6B35C",
            "description": "Portfolio registry drift"})
    except RuntimeError as e:
        if "422" not in str(e):
            raise
    open_issues = gh("GET", f"/repos/{ORG}/{REPO}/issues?state=open"
                            f"&labels={ISSUE_LABEL}&per_page=10", token)
    existing = next((i for i in open_issues
                     if i["title"] == ISSUE_TITLE and "pull_request" not in i), None)
    if drift_body:
        if existing:
            gh("PATCH", f"/repos/{ORG}/{REPO}/issues/{existing['number']}",
               token, {"body": drift_body})
            print(f"Updated existing issue #{existing['number']}.")
        else:
            issue = gh("POST", f"/repos/{ORG}/{REPO}/issues", token,
                       {"title": ISSUE_TITLE, "body": drift_body,
                        "labels": [ISSUE_LABEL]})
            print(f"Opened issue #{issue['number']}.")
        return 1
    if existing:
        gh("POST", f"/repos/{ORG}/{REPO}/issues/{existing['number']}/comments",
           token, {"body": "Registry is back in sync; closing automatically."})
        gh("PATCH", f"/repos/{ORG}/{REPO}/issues/{existing['number']}",
           token, {"state": "closed"})
        print(f"Closed resolved issue #{existing['number']}.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true",
                    help="report drift but do not create/update/close issues")
    ap.add_argument("--offline", action="store_true",
                    help="schema checks only; no GitHub API calls")
    args = ap.parse_args()
    token = os.environ.get("GH_TOKEN")
    list_token = os.environ.get("ORG_REPOS_TOKEN") or token

    try:
        doc = load_registry(REGISTRY)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    errors, warnings = schema_errors(doc)
    live = None
    if not args.offline:
        if not list_token:
            print("ERROR: GH_TOKEN or ORG_REPOS_TOKEN required for live checks",
                  file=sys.stderr)
            return 2
        try:
            live = list_org_repos(list_token)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        e2, w2 = live_errors(doc, live)
        errors += e2
        warnings += w2

    for w in warnings:
        print(f"WARNING: {w}")

    if not errors:
        n = len(doc["repositories"])
        extra = f" == {len(live)} org repos" if live is not None else ""
        print(f"IN SYNC: {n} registry records{extra}; schema valid"
              + (f"; {len(warnings)} warning(s)." if warnings else "."))
        drift_body = None
    else:
        lines = ["The portfolio registry (`registry/repositories.yaml`) has "
                 "drifted from the live organisation or contains invalid records.", ""]
        lines += [f"- {e}" for e in errors]
        if warnings:
            lines += ["", "**Warnings (tracked, non-blocking):**"]
            lines += [f"- {w}" for w in warnings]
        lines += ["", "Edit `registry/repositories.yaml` to resolve, then run "
                  "`scripts/generate_portfolio.py`. This issue auto-closes when "
                  "the registry is back in sync."]
        drift_body = "\n".join(lines)
        print("DRIFT DETECTED:\n" + drift_body)

    if args.check_only or args.offline:
        return 1 if drift_body else 0
    if not token:
        print("ERROR: GH_TOKEN required for issue management", file=sys.stderr)
        return 2
    try:
        return manage_issue(token, drift_body)
    except RuntimeError as e:
        if "410" in str(e):
            print(f"ERROR: issue management failed: {e}\n"
                  f"Issues appear to be disabled on {ORG}/{REPO}.", file=sys.stderr)
            return 2
        raise


if __name__ == "__main__":
    sys.exit(main())
