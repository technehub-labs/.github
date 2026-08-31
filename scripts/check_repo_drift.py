#!/usr/bin/env python3
"""Drift check: profile/README.md repositories table vs live org repo list.

Compares the curated table in profile/README.md (between REPO-TABLE markers)
against the GitHub API's repository list for the org. On drift, opens or
updates a tracking issue; when back in sync, closes it.

Usage:
    python3 scripts/check_repo_drift.py              # check + manage issue
    python3 scripts/check_repo_drift.py --check-only # check, no issue writes

Env:
    GH_TOKEN         GitHub token used for issue management and (fallback)
                     repo listing. The Actions GITHUB_TOKEN only sees public
                     repos, which makes every private repo look like a dead
                     link; set ORG_REPOS_TOKEN for full visibility.
    ORG_REPOS_TOKEN  Token that can list all org repos, including private
                     (classic PAT with repo scope, or fine-grained PAT with
                     metadata:read on all org repos). Preferred for listing.
    ORG           Org login (default: technehub-labs)
    REPO          Repo hosting the README/issue (default: .github)
    README_PATH   Path to README (default: profile/README.md)

Exit codes: 0 = in sync, 1 = drift detected, 2 = error.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

ORG = os.environ.get("ORG", "technehub-labs")
REPO = os.environ.get("REPO", ".github")
README_PATH = os.environ.get("README_PATH", "profile/README.md")
API = "https://api.github.com"
ISSUE_TITLE = "[drift] profile README repositories table out of sync"
ISSUE_LABEL = "readme-drift"


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


def parse_readme_table(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"<!--\s*REPO-TABLE:START.*?-->(.*?)<!--\s*REPO-TABLE:END\s*-->",
                  text, re.S)
    if not m:
        raise RuntimeError("REPO-TABLE markers not found in README")
    rows = {}
    for line in m.group(1).splitlines():
        link = re.search(
            r"\[`[^`]+`\]\(https://github\.com/[^/]+/([^)/)]+)\)", line)
        if link:
            name = link.group(1)
            rows[name] = {"archived": "archived" in line.lower(),
                          "private": "\U0001f512" in line}
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true",
                    help="report drift but do not create/update/close issues")
    args = ap.parse_args()
    token = os.environ.get("GH_TOKEN")
    list_token = os.environ.get("ORG_REPOS_TOKEN") or token

    try:
        repos = list_org_repos(list_token)
        table = parse_readme_table(README_PATH)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    live = {r["name"]: {"archived": r["archived"], "private": r["private"]}
            for r in repos}

    # Degraded-visibility detection: if table rows marked private are absent
    # from the listing, the listing token cannot see private repos (e.g. the
    # Actions GITHUB_TOKEN). In that mode, skip stale/flag checks for rows
    # that are not visible instead of reporting them as dead links.
    invisible_private = sorted(
        n for n, flags in table.items() if flags["private"] and n not in live)
    degraded = bool(invisible_private)
    if degraded:
        print(f"WARNING: {len(invisible_private)} private table rows are not "
              "visible to the listing token; skipping stale/flag checks for "
              "them. Set ORG_REPOS_TOKEN (org-wide read) for full checks.")

    missing = sorted(set(live) - set(table))       # in org, not in table
    stale = sorted(n for n in set(table) - set(live)
                   if n not in invisible_private)  # in table, not in org
    flag_diff = sorted(
        n for n in set(live) & set(table)
        if live[n]["archived"] != table[n]["archived"]
        or live[n]["private"] != table[n]["private"])

    if not (missing or stale or flag_diff):
        print(f"IN SYNC: {len(table)} table rows == {len(live)} org repos.")
        drift_body = None
    else:
        lines = ["The repositories table in `profile/README.md` has drifted "
                 "from the live organisation repository list.", ""]
        if missing:
            lines.append("**In the org but missing from the table:**")
            lines += [f"- `{n}`" for n in missing] + [""]
        if stale:
            lines.append("**In the table but no longer in the org (dead links):**")
            lines += [f"- `{n}`" for n in stale] + [""]
        if flag_diff:
            lines.append("**Flag mismatch** (conventions: private repos carry "
                         "\"🔒\" in the Group cell; archived repos carry the "
                         "word \"archived\"):")
            for n in flag_diff:
                lines.append(
                    f"- `{n}` — org: private={live[n]['private']}, "
                    f"archived={live[n]['archived']} · table: "
                    f"{'🔒' if table[n]['private'] else 'public'}, "
                    f"{'archived' if table[n]['archived'] else 'active'}")
            lines.append("")
        lines.append("Edit `profile/README.md` between the `REPO-TABLE` markers "
                     "to resolve. This issue auto-closes when the table is back in sync.")
        drift_body = "\n".join(lines)
        print("DRIFT DETECTED:\n" + drift_body)

    if args.check_only:
        return 1 if drift_body else 0

    if not token:
        print("ERROR: GH_TOKEN required for issue management", file=sys.stderr)
        return 2

    try:
        return manage_issue(token, drift_body)
    except RuntimeError as e:
        if "410" in str(e):
            print(f"ERROR: issue management failed: {e}\n"
                  f"Issues appear to be disabled on {ORG}/{REPO}. Enable "
                  "Issues on that repo, or set REPO to a repository with "
                  "Issues enabled.", file=sys.stderr)
            return 2
        raise


def manage_issue(token, drift_body):
    # Ensure label exists (ignore 422 already_exists)
    try:
        gh("POST", f"/repos/{ORG}/{REPO}/labels", token,
           {"name": ISSUE_LABEL, "color": "F6B35C",
            "description": "README repositories table drift"})
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
           token, {"body": "Table is back in sync — closing automatically."})
        gh("PATCH", f"/repos/{ORG}/{REPO}/issues/{existing['number']}",
           token, {"state": "closed"})
        print(f"Closed resolved issue #{existing['number']}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
