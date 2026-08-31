# TechNeHub Labs Portfolio Taxonomy

Established by CR-TNH-README-02 (implements CR-TNH-README-01). This document is the canonical specification of the portfolio taxonomy: families, lifecycle vocabulary, canonical-status vocabulary, classification rules, and recorded anomalies.

## 1. Portfolio Families

Repositories are classified by architectural and organizational role, not by technology, implementation language or naming convention.

| Family | Purpose |
|---|---|
| Foundation | Authoritative architectural, conceptual, semantic and metamodel foundations |
| Concepts | Conceptual and exploratory models representing domains, patterns and emerging areas |
| Catalogs | Reference catalogs instantiated from or aligned with the canonical model |
| Assessment | Assessment models, assessment mechanisms, measurement and evidence assets |
| Tooling | Software supporting modeling, validation, generation, transformation, visualization or consumption |
| Applications | Demonstrations and practical realizations of the architecture |
| Governance | Governance, lifecycle, contribution, standards and organizational control assets |
| Archive | Superseded, deprecated or retired repositories retained for historical or compatibility purposes |

## 2. Classification Rules

1. Every repository has exactly one **primary family**.
2. Every repository has a **lifecycle status**, an **architectural role** and a **description**.
3. Optional metadata: domain, entity, class alias, canonical status, dependencies, related repositories, documentation, featured flag.
4. Classification is independent of GitHub popularity, stars or activity ranking.
5. Classification ambiguities are recorded in this document (Section 6) rather than silently resolved.
6. Archive is separated from active portfolio presentation; archived repositories carry `family: archive` and `status: archived`.

## 3. Lifecycle Vocabulary

| Status | Meaning |
|---|---|
| Proposed | Approved in principle; implementation not started |
| Experimental | Pre-release or exploratory; interfaces may change without notice |
| Active | Publicly maintained and evolving |
| Stable | Versioned 1.0 or later; compatibility commitments apply |
| Deprecated | Superseded; consumers should migrate |
| Archived | Read-only; retained for historical or compatibility purposes |

### Initial derivation rule (bootstrap classification)

For the initial population of the registry, lifecycle status was derived mechanically and may be refined by governance per repository:

- `archived`: the repository is archived on GitHub.
- `stable`: the repository has a versioned 1.0 (or later) release.
- `active`: the repository is public and not archived.
- `experimental`: the repository is private and not archived (pre-public-release).

## 4. Canonical-Status Vocabulary

| Value | Meaning |
|---|---|
| Canonical | The authoritative home for its subject matter |
| Supporting | Operational or organizational support for the portfolio |
| Reference | Exploratory or reference material; not normative |
| Experimental | Pre-release; classification provisional |
| Historical | Superseded; retained for reference |

Canonical status is never inferred solely from repository age or popularity.

## 5. Registry Record

Minimum record (required): `name`, `family`, `status`, `role`, `canonical`, `visibility`, `description`.

Extensible fields: `entity`, `layer`, `class_alias`, `domain`, `depends_on`, `related`, `documentation`, `website`, `featured`, `deprecated_by`, `supersedes`.

The machine-readable records live in [repositories.yaml](repositories.yaml). The registry schema and maintenance contract are specified in [registry/README.md](README.md).

## 6. Classification Anomalies (recorded, not silently resolved)

| # | Repository | Anomaly | Provisional classification | Required governance decision |
|---|---|---|---|---|
| A1 | `dea-catalog-agent-foundry` | `metamodel-pointer.yaml` maps it to class alias `DI` / entity "Digital Identity: Bot (Agent) Subtype", colliding with `dea-catalog-digital-identities` (alias `DI`); the repository scope (agent patterns, orchestration, governance) is wider than the pointer entity. Pointer self-notes: "repo predates Phase 1". | catalogs / experimental | Re-map the pointer entity or re-scope the repository through a CR. |
| A2 | `dea-catalog-metrics` | GitHub description ("assessment models and tools") overlaps the Assessment family boundary, but its pointer entity is Performance Metric (alias `MTR`, no architecture layer). | catalogs / active | Confirm catalog vs assessment-family placement when standalone assessment repositories are established. |
| A3 | `technehub-labs.github.io` | No Site or Documentation family exists in the approved taxonomy. | governance (role: Site) | Add a Site family, or accept the Governance classification permanently. |
| A4 | `dea-catalog-ontologies`, `dea-catalog-reference-architecture`, `dea-catalog-solution-hub` | No `metamodel-pointer.yaml`; entity and layer metadata unavailable. | catalogs (no entity metadata) | Add pointer files through the root-model generation process. |
| A5 | `dea-catalog-taxonomy` | Archived (ADR-0004 D2: Taxonomy Node merged into Concept) but retains a live pointer file. | archive / historical | None required; archived pointers are frozen by definition. |

## 7. Flagged, Not Fixed (outside this programme's scope)

- Catalog `metamodel-pointer.yaml` files pin an old root-model generation (OpenDEAM v0.2.1 era) while the root model is at v0.5.0 and the metamodel is at v1.0.0. Pointer files are auto-generated and marked "do not edit"; regeneration belongs to the root-model release process.

## 8. Non-Goals (per CR-TNH-README-02)

This taxonomy does not rename, move, archive or change ownership of repositories; does not alter repository content; and does not establish semantic authority for repository artifacts.
