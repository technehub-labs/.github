# TechNeHub Labs

> **Digital Enterprise Architecture — open reference framework for enterprise architects, solutions architects, and technology leaders.**

[![org](https://img.shields.io/badge/TechNeHub%20Labs-DEA-0088CC?style=flat-square&logo=github)](https://github.com/technehub-labs)
[![Stage: Alpha](https://img.shields.io/badge/Stage-Alpha-FF6B35?style=flat-square)](https://github.com/technehub-labs/dea-metamodel)
[![License: MIT](https://img.shields.io/badge/License-MIT-44CC11?style=flat-square)](LICENSE)

---

## What is TechNeHub Labs?

TechNeHub Labs is an open-source, vendor-neutral reference framework for Digital Enterprise Architecture (DEA). It provides structured definitions, reusable patterns, and tooling to help architects model, govern, and evolve enterprise technology landscapes.

The framework is built in layers — from a shared metamodel that defines the core concepts, through curated reference catalogs, to developer tooling and governance policies.

---

## The DEA Framework

```
L0 — Metamodel         Core entity definitions, relationships, JSON Schema, TTL ontology, SQLite schema
L1 — Reference Catalogs  Principles · Standards · Patterns · Glossary · Taxonomies · Ontologies · Metrics · Reference Models
L2 — Tooling           CLI · Code generators · Web viewer · Scripts · Packaging
L3 — Governance        Branch strategy · Release process · SBOM · CODEOWNERS · PR templates · MIT licensing
```

### Repositories

| Repo | Layer | Description |
|------|-------|-------------|
| [`dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) | L0 | Core entity definitions, JSON Schema, TTL ontology, SQLite schema, TypeScript interfaces |
| [`dea-catalog-principles`](https://github.com/technehub-labs/dea-catalog-principles) | L1 | Architecture principles (API-first, Zero Trust, etc.) |
| [`dea-catalog-standards`](https://github.com/technehub-labs/dea-catalog-standards) | L1 | Technical standards (REST, GraphQL, OAuth2, etc.) |
| [`dea-catalog-patterns`](https://github.com/technehub-labs/dea-catalog-patterns) | L1 | Architecture patterns (CQRS, Saga, Strangler Fig, etc.) |
| [`dea-catalog-glossary`](https://github.com/technehub-labs/dea-catalog-glossary) | L1 | Shared terminology and definitions |
| [`dea-catalog-taxonomy`](https://github.com/technehub-labs/dec-catalog-taxonomy) | L1 | Classification hierarchies (capabilities, domains, technology) |
| [`dea-catalog-ontologies`](https://github.com/technehub-labs/dea-catalog-ontologies) | L1 | OWL/RDF ontologies formalising the DEA domain |
| [`dea-catalog-metrics`](https://github.com/technehub-labs/dea-catalog-metrics) | L1 | Business & technology KPIs and measurement frameworks |
| [`dea-catalog-reference-models`](https://github.com/technehub-labs/dea-catalog-reference-models) | L1 | Reference architectures (TOGAF, Zachman,KEA) |
| [`dea-catalog-digital-business-service-factory`](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) | L1 | Enterprise business services, capability maps, SLA governance (Customer, Finance, Product, Order, Supply Chain, HR) |
| [`dea-catalog-agent-foundry`](https://github.com/technehub-labs/dea-catalog-agent-foundry) | L1 | Autonomous agent patterns, platform specs, orchestration frameworks, AI governance |
| [`dea-catalog-solution-hub`](https://github.com/technehub-labs/dea-catalog-solution-hub) | L1 | Solution archetypes, delivery templates, IaC accelerators for CDP, API Gateway, Event Streaming, Identity, Workflow |
| [`dea-catalog-reference-architecture`](https://github.com/technehub-labs/dea-catalog-reference-architecture) | L1 | DERA — canonical delivery blueprint assembling all layers into a four-phase adoption programme |
| [`dea-cli`](https://github.com/technehub-labs/dea-cli) | L2 | DEA CLI — query, validate, generate viewpoints |
| [`dea-scripts`](https://github.com/technehub-labs/dea-scripts) | L2 | Automation scripts, code generators, migrators |
| [`dea-code-gen`](https://github.com/technehub-labs/dea-code-gen) | L2 | Config-driven code generation from catalog entries |
| [`dea-web-viewer`](https://github.com/technehub-labs/dea-web-viewer) | L2 | Interactive web viewer for DEA catalogs |
| [`technehub-labs.github.io`](https://github.com/technehub-labs/technehub-labs.github.io) | L3 | GitHub Pages — framework landing site |

---

## Architecture

### Layer 0 — Metamodel

The metamodel defines the canonical entities and relationships used across all catalogs.

**Entity types:** `Principle` · `ArchitecturePattern` · `Standard` · `ReferenceModel` · `BusinessCapability` · `BusinessService` · `SolutionComponent` · `Technology` · `MeasurementMetric` · `TaxonomyNode` · `GlossaryTerm` · `Relationship`

**Formats:** YAML (authoritative) · JSON Schema · TTL/OWL (ontology) · SQLite · TypeScript interfaces · Python (Pydantic)

### Layer 1 — Reference Catalogs

Structured collections of architecture assets, each entry typed against the metamodel, with relationships and provenance metadata. The centrepiece is **DERA** — the Digital Enterprise Reference Architecture — a synthesising blueprint that assembles all other catalogs into a coherent delivery programme.

### Layer 2 — Tooling

Developer-facing tools to query, validate, generate, and visualise the catalog.

- **`dea-cli`** — `dea query`, `dea validate`, `dea viewpoint`, `dea generate`
- **`dea-scripts`** — catalog seeding, migration, bulk operations
- **`dea-code-gen`** — generate Pydantic models, API stubs, ADR stubs from catalog entries
- **`dea-web-viewer`** — interactive browser for the catalog portfolio

### Layer 3 — Governance

Policies, processes, and standards that govern contributions and releases across the framework.

---

## Status

TechNeHub Labs is in **alpha**. The metamodel and core tooling are functional. Catalogs are being populated. The 5-project structure is active — see the GitHub Projects tab.

---

## Projects

Tracking all deliverables via GitHub Projects:

| # | Project | Focus |
|---|---------|-------|
| 3 | [Foundation Core](https://github.com/orgs/technehub-labs/projects/3) | Metamodel v1.0 — entities, schema, ontology, CI |
| 4 | [Catalog Ecosystem](https://github.com/orgs/technehub-labs/projects/4) | All L1 reference catalogs |
| 5 | [Developer Tooling](https://github.com/orgs/technehub-labs/projects/5) | CLI, scripts, code-gen, web viewer |
| 6 | [Web Viewer & Packaging](https://github.com/orgs/technehub-labs/projects/6) | Docker, npm, PyPI packaging + GitHub Pages |
| 7 | [Governance & Standards](https://github.com/orgs/technehub-labs/projects/7) | Contributing, PR templates, branch protection, SBOM, MIT |

*(Project #2 — the original DEA Roadmap — is now closed.)*

---

## Quick Start

```bash
# Install the CLI
npm install -g @technehub-labs/dea-cli

# Query the metamodel
dea query --type ArchitecturePattern

# Validate a catalog entry
dea validate --entity Principle

# Generate a viewpoint for a stakeholder
dea viewpoint --stakeholder SolutionsArchitect

# Generate an ADR from a catalog entry
dea generate --template adr --id dea:pattern-cqrs
```

---

## Contributing

See [`CONTRIBUTING.md`](https://github.com/technehub-labs/dea-metamodel/blob/main/CONTRIBUTING.md) in the metamodel repo for how to propose new entities, patterns, and standards.

---

## License

All TechNeHub Labs repositories are MIT licensed unless otherwise noted.

```
MIT License — see individual repo LICENSE files
```
