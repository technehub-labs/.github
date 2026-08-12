# TechNeHub Labs

> **Digital Enterprise Architecture — open reference framework for enterprise architects, solutions architects, and technology leaders.**

[![org](https://img.shields.io/badge/TechNeHub%20Labs-DEA-0088CC?style=flat-square&logo=github)](https://github.com/technehub-labs)
[![Stage: Alpha](https://img.shields.io/badge/Stage-Alpha-FF6B35?style=flat-square)](https://github.com/technehub-labs/dea-metaframework)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)

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
L3 — Governance        Branch strategy · Release process · SBOM · CODEOWNERS · PR templates · Apache 2.0 licensing
```

### Repositories

<!-- REPO-TABLE:START — maintained manually; drift-checked nightly by .github/workflows/repo-drift-check.yml -->
<!-- Conventions: private repositories carry "🔒" in the Group cell; archived repositories carry the word "archived". -->
| Repo | Group | Description |
|------|-------|-------------|
| [`dea-metaframework`](https://github.com/technehub-labs/dea-metaframework) | Core | Enterprise Concept Framework — the 7×7 axiom-derived matrix that the DEA metamodel and catalogs instantiate |
| [`dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) | Core 🔒 | Digital Enterprise Architecture Metamodel — canonical entity definitions, relationships, and schemas for all DEA catalog repositories |
| [`autonomous-enterprise`](https://github.com/technehub-labs/autonomous-enterprise) | Concept | Umbrella concept repository for the Autonomous Enterprise pattern — composes references, tools, and artifacts on top of the DEA catalogs and the four sibling concept repositories |
| [`agentic-workflows`](https://github.com/technehub-labs/agentic-workflows) | Concept 🔒 | Agent-task concept repository for the Agentic Workflows pattern — agent roles, tools, prompts, orchestration patterns, and evaluation harnesses |
| [`autonomous-flow`](https://github.com/technehub-labs/autonomous-flow) | Concept 🔒 | Cross-system flow concept repository for the Autonomous Flow pattern — event streaming, data pipelines, change data capture, event-driven integration |
| [`autonomous-networks`](https://github.com/technehub-labs/autonomous-networks) | Concept 🔒 | Network-layer concept repository for the Autonomous Networks pattern — intent-based networking, service mesh, zero-trust, self-healing transport |
| [`autonomous-operations`](https://github.com/technehub-labs/autonomous-operations) | Concept 🔒 | Ops-layer concept repository for the Autonomous Operations pattern — incident response, change, observability, capacity, reliability, compliance |
| [`agentic-enterprise-innovation`](https://github.com/technehub-labs/agentic-enterprise-innovation) | Concept — archived | AI agent-driven approaches to enterprise innovation and automation |
| [`ea-foundation`](https://github.com/technehub-labs/ea-foundation) | Concept — archived | Enterprise Architecture foundation: models, principles, and reference frameworks |
| [`ecosystem-architecture`](https://github.com/technehub-labs/ecosystem-architecture) | Concept — archived | Architecture framework for business and technology ecosystems |
| [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors) | Catalog 🔒 | Actors catalog — performers of enterprise processes (humans, teams, systems, AI agents) |
| [`dea-catalog-agent-foundry`](https://github.com/technehub-labs/dea-catalog-agent-foundry) | Catalog 🔒 | Autonomous agent patterns, agent platform specifications, multi-agent orchestration frameworks, operational governance |
| [`dea-catalog-ai-ml-models`](https://github.com/technehub-labs/dea-catalog-ai-ml-models) | Catalog | AI / ML Model — trained model that augments or automates a system function |
| [`dea-catalog-api-contracts`](https://github.com/technehub-labs/dea-catalog-api-contracts) | Catalog | API / Service Contract — versioned contract exposing a system function |
| [`dea-catalog-application-components`](https://github.com/technehub-labs/dea-catalog-application-components) | Catalog | Application Component — deployable unit hosting system functions |
| [`dea-catalog-business-capabilities`](https://github.com/technehub-labs/dea-catalog-business-capabilities) | Catalog | Business Capability — ability to deliver value, mapped to ECF coordinates |
| [`dea-catalog-business-objects`](https://github.com/technehub-labs/dea-catalog-business-objects) | Catalog 🔒 | Business Objects — the atoms of the ECF matrix, classified by (ecf_domain, ecf_stage) coordinates |
| [`dea-catalog-data-entities`](https://github.com/technehub-labs/dea-catalog-data-entities) | Catalog | Data Entity — typed, persisted structure used by application components |
| [`dea-catalog-data-products`](https://github.com/technehub-labs/dea-catalog-data-products) | Catalog | Data Product — domain-owned, SLA-backed dataset exposed as a product |
| [`dea-catalog-digital-business-service-factory`](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) | Catalog 🔒 | Enterprise business service definitions, capabilities, decomposition into solution components, governance contracts |
| [`dea-catalog-digital-identities`](https://github.com/technehub-labs/dea-catalog-digital-identities) | Catalog | Digital Identity — Customer, Partner, or Bot representation in the ecosystem |
| [`dea-catalog-event-streams`](https://github.com/technehub-labs/dea-catalog-event-streams) | Catalog | Event / Event Stream — discrete state changes with topic and schema |
| [`dea-catalog-glossary`](https://github.com/technehub-labs/dea-catalog-glossary) | Catalog 🔒 | Controlled vocabulary and glossary catalog |
| [`dea-catalog-information-classes`](https://github.com/technehub-labs/dea-catalog-information-classes) | Catalog | Information Class — classification of data entities by sensitivity |
| [`dea-catalog-investment-initiatives`](https://github.com/technehub-labs/dea-catalog-investment-initiatives) | Catalog | Investment Initiative — funded programme that realises strategic objectives |
| [`dea-catalog-journey-touchpoints`](https://github.com/technehub-labs/dea-catalog-journey-touchpoints) | Catalog | Journey Touchpoint — point of interaction on a customer or user journey |
| [`dea-catalog-metrics`](https://github.com/technehub-labs/dea-catalog-metrics) | Catalog | Assessment models and tools for evaluating business ecosystem health and maturity |
| [`dea-catalog-ontologies`](https://github.com/technehub-labs/dea-catalog-ontologies) | Catalog 🔒 | Domain OWL/RDF ontologies — fintech and healthcare |
| [`dea-catalog-organizational-units`](https://github.com/technehub-labs/dea-catalog-organizational-units) | Catalog 🔒 | Organizational Units — accountability containers that own capabilities, run processes, and are custodians for business objects |
| [`dea-catalog-patterns`](https://github.com/technehub-labs/dea-catalog-patterns) | Catalog | Reusable architecture patterns for enterprise digital platforms |
| [`dea-catalog-platform-services`](https://github.com/technehub-labs/dea-catalog-platform-services) | Catalog | Platform Service — compute, database, or network foundation service |
| [`dea-catalog-principles`](https://github.com/technehub-labs/dea-catalog-principles) | Catalog 🔒 | Architecture principles catalog — versioned against dea-metamodel |
| [`dea-catalog-processes`](https://github.com/technehub-labs/dea-catalog-processes) | Catalog 🔒 | Business and operational processes, classified by intent (operational/support/management) and ECF domain |
| [`dea-catalog-reference-architecture`](https://github.com/technehub-labs/dea-catalog-reference-architecture) | Catalog 🔒 | Digital Enterprise Reference Architecture — canonical reference model assembling all DEA layers into a delivery blueprint |
| [`dea-catalog-reference-models`](https://github.com/technehub-labs/dea-catalog-reference-models) | Catalog | Core digital platform systems and reference architectures |
| [`dea-catalog-solution-hub`](https://github.com/technehub-labs/dea-catalog-solution-hub) | Catalog 🔒 | Solution archetypes, delivery templates, and implementation accelerators for recurring enterprise technology challenges |
| [`dea-catalog-stakeholders`](https://github.com/technehub-labs/dea-catalog-stakeholders) | Catalog 🔒 | External/affected parties engaged in or affected by enterprise processes |
| [`dea-catalog-standards`](https://github.com/technehub-labs/dea-catalog-standards) | Catalog 🔒 | Industry standards catalog — TOGAF, Zachman, NIST, ISO |
| [`dea-catalog-strategic-objectives`](https://github.com/technehub-labs/dea-catalog-strategic-objectives) | Catalog | Strategic Objective — high-level outcomes the enterprise seeks to achieve |
| [`dea-catalog-system-functions`](https://github.com/technehub-labs/dea-catalog-system-functions) | Catalog | System Function — capability that automates a business process |
| [`dea-catalog-taxonomy`](https://github.com/technehub-labs/dea-catalog-taxonomy) | Catalog 🔒 | Capability and technology taxonomy catalog |
| [`dea-catalog-value-streams`](https://github.com/technehub-labs/dea-catalog-value-streams) | Catalog | Value Stream — end-to-end collection of value-creating activities |
| [`dea-cli`](https://github.com/technehub-labs/dea-cli) | Tooling 🔒 | Digital Enterprise Architecture CLI — query, validate, and generate viewpoints from DEA catalogs |
| [`dea-code-gen`](https://github.com/technehub-labs/dea-code-gen) | Tooling 🔒 | Code generation from DEA catalog entries — ADR, component spec, and API contract generators |
| [`dea-scripts`](https://github.com/technehub-labs/dea-scripts) | Tooling | Tools and playbooks for digital transformation initiatives |
| [`dea-web-viewer`](https://github.com/technehub-labs/dea-web-viewer) | Tooling | Visual canvas and tooling for enterprise architecture modeling |
| [`technehub-labs.github.io`](https://github.com/technehub-labs/technehub-labs.github.io) | Site | GitHub Pages — Techne Research & Dev. Labs landing site |
| [`.github`](https://github.com/technehub-labs/.github) | Governance | Organisation profile and community health files |
<!-- REPO-TABLE:END -->

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
| 7 | [Governance & Standards](https://github.com/orgs/technehub-labs/projects/7) | Contributing, PR templates, branch protection, SBOM, Apache 2.0 |

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

Contribution guidelines are being formalised under [Project #7 — Governance & Standards](https://github.com/orgs/technehub-labs/projects/7). In the meantime, open an issue in the relevant repository to propose new entities, patterns, or standards.

---

## License

All TechNeHub Labs repositories are licensed under the Apache License 2.0 unless otherwise noted.

```
Apache License 2.0 — see individual repo LICENSE files
```
