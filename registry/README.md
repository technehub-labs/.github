# Portfolio Registry

Established by CR-TNH-README-03 (implements CR-TNH-README-01). The registry is the machine-readable source for TechNeHub Labs portfolio classification and presentation metadata.

## 1. Purpose

The registry answers:

- Which repositories exist in the portfolio?
- Which portfolio family does each belong to?
- What is its lifecycle status?
- What architectural role does it perform?
- Is it canonical?
- Which repositories does it depend on or relate to?
- How should it appear in portfolio navigation?

## 2. Authority Boundary

The registry is not a second repository-management system.

```text
GitHub
  |  authoritative for: repository existence, visibility, archived state
  v
Portfolio Registry (this file)
  |  authoritative for: classification, lifecycle, role, relationships, presentation
  v
Organization README / Portfolio Index / Website
```

Repository existence is detected from GitHub; classification requires explicit metadata in this registry. Automation detects unclassified repositories but never infers normative classification (CR-TNH-README-07 governance boundary).

## 3. Schema

Root fields:

| Field | Type | Meaning |
|---|---|---|
| `version` | integer | Registry format version |
| `organization` | string | GitHub organization login |
| `families` | list | Approved family vocabulary (CR-TNH-README-02) |
| `lifecycle` | list | Approved lifecycle vocabulary |
| `canonical_values` | list | Approved canonical-status vocabulary |
| `family_details` | map | Per-family title, purpose and portfolio page |
| `repositories` | list | One record per repository |

Repository record:

| Field | Required | Meaning |
|---|---|---|
| `name` | yes | GitHub repository name |
| `family` | yes | Primary portfolio family (from `families`) |
| `status` | yes | Lifecycle status (from `lifecycle`) |
| `role` | yes | Architectural or organizational role, presentation label |
| `canonical` | yes | Canonical status (from `canonical_values`) |
| `visibility` | yes | `public` or `private`; validated against GitHub |
| `description` | yes | Mirrors the GitHub repository description verbatim |
| `entity` | catalogs | First-level entity the catalog governs (from `metamodel-pointer.yaml`) |
| `layer` | catalogs | OpenDEAM architecture layer (L1 to L5) where allocated |
| `class_alias` | catalogs | Metamodel class alias (for example `CAP`) |
| `domain` | optional | Presentation domain derived from the architecture layer |
| `depends_on` | optional | Principal upstream repositories |
| `featured` | optional | `true` for the featured set (maximum 6) |
| `related`, `documentation`, `website`, `deprecated_by`, `supersedes` | optional | Reserved extension fields |

## 4. Maintenance

Adding or reclassifying a repository:

```text
Repository created or changed on GitHub
        |
        v
Nightly validation detects missing or drifted record
        |
        v
Classification decision (human, governed)
        |
        v
Edit registry/repositories.yaml
        |
        v
python3 scripts/validate_registry.py --check-only
        |
        v
python3 scripts/generate_portfolio.py
        |
        v
Pull request with registry + regenerated pages
```

## 5. Validation and Generation

- `scripts/validate_registry.py`: schema checks, vocabulary checks, duplicate detection, and a live cross-check against the GitHub organization (existence, visibility, archived state). Errors fail the check; warnings report known anomalies tracked in [taxonomy.md](taxonomy.md).
- `scripts/generate_portfolio.py`: regenerates the marked GENERATED regions of the portfolio pages from this registry. `--check` verifies pages are current without writing.
- `.github/workflows/portfolio-check.yml`: nightly CI running both, opening or closing a `portfolio-drift` tracking issue.

## 6. Conventions

- `description` mirrors the GitHub repository description verbatim so that drift between presentation and source is visible; presentation layers normalize organization language conventions (en/em dashes render as colons in generated documents).
- One primary family per repository; secondary relationships use `depends_on` or `related`.
- The featured set is deliberately small (maximum 6) and represents the strategic OpenDEAM entry points.
