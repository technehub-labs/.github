#!/usr/bin/env python3
"""Generate TechNeHub Labs portfolio pages from the portfolio registry.

Implements CR-TNH-README-07 generation scope. The registry
(registry/repositories.yaml) is the single source of truth; this script
rewrites only the marked GENERATED regions of the portfolio pages and never
touches authored narrative outside the markers.

Marker convention (in each target page):

    <!-- GENERATED:START <region> (source: registry/repositories.yaml) -->
    ... generated content ...
    <!-- GENERATED:END <region> -->

Usage:
    python3 scripts/generate_portfolio.py            # rewrite pages in place
    python3 scripts/generate_portfolio.py --check    # exit 1 if pages are stale

Presentation conventions:
  * descriptions are mirrored from GitHub verbatim in the registry, but
    rendered in docs with en/em dashes normalized to colons per the
    organization language convention;
  * hyperlinks attach to the conceptual role (Asset column), with the raw
    repository name kept visible in its own column.
"""
import argparse
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

REGISTRY = "registry/repositories.yaml"
ORG_URL = "https://github.com/technehub-labs"

FAMILY_ORDER = ["foundation", "concepts", "catalogs", "assessment",
                "tooling", "applications", "governance", "archive"]

DOMAIN_ORDER = [
    ("ecosystem-value", "L1 Ecosystem & Value Network"),
    ("strategy-governance", "L2 Strategic & Governance"),
    ("business-operating", "L3 Business Operating Model"),
    ("digital-intelligence", "L4 Digital & Intelligence"),
    ("technology-execution", "L5 Technology & Execution"),
    (None, "Cross-cutting & Semantic"),
]

STATUS_LABEL = {"proposed": "Proposed", "experimental": "Experimental",
                "active": "Active", "stable": "Stable",
                "deprecated": "Deprecated", "archived": "Archived"}


def clean(s):
    """Normalize org language conventions for presentation."""
    return (s or "").replace("—", ":").replace("–", ":").replace("|", "\\|").strip()


def repo_link(r, text=None):
    return f"[`{text or r['name']}`]({ORG_URL}/{r['name']})"


def asset_link(r):
    return f"[{clean(r['role'])}]({ORG_URL}/{r['name']})"


def by_family(doc, family):
    return sorted((r for r in doc["repositories"] if r["family"] == family),
                  key=lambda r: r["name"])


def render_families_table(doc):
    rows = ["| Family | Purpose | Repositories |", "|---|---|---|"]
    for fam in FAMILY_ORDER:
        d = doc["family_details"][fam]
        n = len(by_family(doc, fam))
        count = str(n) if n else "0 (planned)"
        # page paths are repo-root-relative; this table renders inside portfolio/
        page = d["page"].removeprefix("portfolio/")
        rows.append(f"[**{d['title']}**]({page}) | {clean(d['purpose'])} | {count}")
    return "\n".join(rows)


def render_lifecycle_summary(doc):
    counts = {}
    for r in doc["repositories"]:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    rows = ["| Lifecycle | Repositories |", "|---|---|"]
    for s in doc["lifecycle"]:
        if counts.get(s):
            rows.append(f"{STATUS_LABEL[s]} | {counts[s]}")
    rows.append(f"**Total** | **{len(doc['repositories'])}**")
    return "\n".join(rows)


def render_featured_list(doc):
    rows = []
    for r in doc["repositories"]:
        if r.get("featured"):
            rows.append(f"- {asset_link(r)} ({repo_link(r)}): {clean(r['description'])}")
    return "\n".join(rows)


def render_family_table(doc, family):
    recs = by_family(doc, family)
    if not recs:
        d = doc["family_details"][family]
        return (f"_No repositories are currently classified under "
                f"**{d['title']}**. This family is part of the approved "
                f"portfolio taxonomy and activates as repositories are "
                f"established through the change-request process._")
    rows = ["| Asset | Repository | Status | Canonical | Description |",
            "|---|---|---|---|---|"]
    for r in recs:
        rows.append(f"{asset_link(r)} | {repo_link(r)} | "
                    f"{STATUS_LABEL[r['status']]} | {r['canonical'].title()} | "
                    f"{clean(r['description'])}")
    return "\n".join(rows)


def render_catalog_index(doc):
    recs = by_family(doc, "catalogs")
    parts = []
    for domain, title in DOMAIN_ORDER:
        group = [r for r in recs if r.get("domain") == domain]
        if not group:
            continue
        parts.append(f"### {title}\n")
        rows = ["| Entity | Repository | Status | Description |", "|---|---|---|---|"]
        for r in group:
            entity = clean(r.get("entity") or r["role"])
            rows.append(f"[{entity}]({ORG_URL}/{r['name']}) | {repo_link(r)} | "
                        f"{STATUS_LABEL[r['status']]} | {clean(r['description'])}")
        parts.append("\n".join(rows))
        parts.append("")
    return "\n".join(parts).strip()


REGION_RENDERERS = {
    ("portfolio/README.md", "families-table"): render_families_table,
    ("portfolio/README.md", "lifecycle-summary"): render_lifecycle_summary,
    ("portfolio/README.md", "featured-list"): render_featured_list,
    ("portfolio/foundation.md", "family-table"): lambda d: render_family_table(d, "foundation"),
    ("portfolio/concepts.md", "family-table"): lambda d: render_family_table(d, "concepts"),
    ("portfolio/catalogs.md", "catalog-index"): render_catalog_index,
    ("portfolio/assessment.md", "family-table"): lambda d: render_family_table(d, "assessment"),
    ("portfolio/tooling.md", "family-table"): lambda d: render_family_table(d, "tooling"),
    ("portfolio/applications.md", "family-table"): lambda d: render_family_table(d, "applications"),
    ("portfolio/governance.md", "family-table"): lambda d: render_family_table(d, "governance"),
    ("portfolio/archive.md", "family-table"): lambda d: render_family_table(d, "archive"),
}


def replace_region(text, region, content):
    pat = re.compile(
        r"(<!--\s*GENERATED:START\s+" + re.escape(region) +
        r"[^>]*-->)(.*?)(<!--\s*GENERATED:END\s+" + re.escape(region) + r"\s*-->)",
        re.S)
    if not pat.search(text):
        raise RuntimeError(f"GENERATED markers for region '{region}' not found")
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(3), text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if any page is stale")
    args = ap.parse_args()

    doc = yaml.safe_load(open(REGISTRY, encoding="utf-8"))
    stale, touched = [], 0
    for (page, region), renderer in REGION_RENDERERS.items():
        try:
            text = open(page, encoding="utf-8").read()
        except FileNotFoundError:
            print(f"ERROR: {page} not found", file=sys.stderr)
            return 2
        new = replace_region(text, region, renderer(doc))
        if new != text:
            if args.check:
                stale.append(f"{page} [{region}]")
            else:
                open(page, "w", encoding="utf-8").write(new)
                touched += 1
    if args.check:
        if stale:
            print("STALE generated regions:")
            for s in stale:
                print(f"  {s}")
            print("Run scripts/generate_portfolio.py to regenerate.")
            return 1
        print("All generated regions are current.")
        return 0
    print(f"Regenerated {touched} region(s) across {len(REGION_RENDERERS)} targets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
