# Reference Catalogs

OpenDEAM maintains a governed collection of reference catalogs derived from the canonical model: one repository per first-level entity, each entry typed against the metamodel with relationships and provenance metadata, version-pinned to the root model through `metamodel-pointer.yaml`.

Catalogs are grouped below by OpenDEAM architecture layer (L1 to L5), plus a cross-cutting group for semantic-dimension catalogs that sit outside the layer structure. The centrepiece is DERA, the Digital Enterprise Reference Architecture (`dea-catalog-reference-architecture`), a synthesizing blueprint that assembles the other catalogs into a coherent delivery programme.

<!-- GENERATED:START catalog-index (source: registry/repositories.yaml) -->
### L1 Ecosystem & Value Network

| Entity | Repository | Status | Description |
|---|---|---|---|
[Ecosystem Platform](https://github.com/technehub-labs/dea-catalog-ecosystem-platforms) | [`dea-catalog-ecosystem-platforms`](https://github.com/technehub-labs/dea-catalog-ecosystem-platforms) | Active | A standing multi-sided structure the enterprise hosts for repeated exchange among many ecosystem actors (marketplace, partner API program, developer portal).
[Journey Touchpoint](https://github.com/technehub-labs/dea-catalog-journey-touchpoints) | [`dea-catalog-journey-touchpoints`](https://github.com/technehub-labs/dea-catalog-journey-touchpoints) | Active | Journey Touchpoint : point of interaction on a customer or user journey.
[Stakeholder](https://github.com/technehub-labs/dea-catalog-stakeholders) | [`dea-catalog-stakeholders`](https://github.com/technehub-labs/dea-catalog-stakeholders) | Experimental | Stakeholders catalog : DEA L1 catalog repository for external/affected parties whose relationship with the enterprise is engaged in or affected by enterprise processes.

### L2 Strategic & Governance

| Entity | Repository | Status | Description |
|---|---|---|---|
[Blueprint](https://github.com/technehub-labs/dea-catalog-blueprints) | [`dea-catalog-blueprints`](https://github.com/technehub-labs/dea-catalog-blueprints) | Active | DEA catalog: Blueprint (BLU) : composed target-state designs from Architecture Patterns. OpenDEAM v0.4.0 (ADR-0004; renamed from dea-catalog-reference-models)
[Control](https://github.com/technehub-labs/dea-catalog-controls) | [`dea-catalog-controls`](https://github.com/technehub-labs/dea-catalog-controls) | Active | A mechanism (process, technical, or organizational) that mitigates a Risk or enforces a Regulation.
[Experiment](https://github.com/technehub-labs/dea-catalog-experiments) | [`dea-catalog-experiments`](https://github.com/technehub-labs/dea-catalog-experiments) | Active | A bounded, time-boxed test of a Signal's relevance to the enterprise before committing investment.
[Guardrail](https://github.com/technehub-labs/dea-catalog-guardrails) | [`dea-catalog-guardrails`](https://github.com/technehub-labs/dea-catalog-guardrails) | Experimental | DEA catalog: Guardrail (GRD) : enforceable constraints with enforcement maturity. OpenDEAM v0.4.0 (ADR-0004; renamed from dea-catalog-standards)
[Investment Initiative](https://github.com/technehub-labs/dea-catalog-investment-initiatives) | [`dea-catalog-investment-initiatives`](https://github.com/technehub-labs/dea-catalog-investment-initiatives) | Active | Investment Initiative : funded programme that realises strategic objectives.
[Architecture Pattern](https://github.com/technehub-labs/dea-catalog-patterns) | [`dea-catalog-patterns`](https://github.com/technehub-labs/dea-catalog-patterns) | Active | Reusable architecture patterns for enterprise digital platforms
[Regulation](https://github.com/technehub-labs/dea-catalog-regulations) | [`dea-catalog-regulations`](https://github.com/technehub-labs/dea-catalog-regulations) | Active | An externally imposed obligation (law, industry standard with force, contractual mandate) the enterprise must comply with.
[Risk](https://github.com/technehub-labs/dea-catalog-risk-register) | [`dea-catalog-risk-register`](https://github.com/technehub-labs/dea-catalog-risk-register) | Active | A condition or event that threatens the enterprise's ability to persist or to realize a capability/objective.
[Signal](https://github.com/technehub-labs/dea-catalog-signals) | [`dea-catalog-signals`](https://github.com/technehub-labs/dea-catalog-signals) | Active | A weak or early indicator of environmental change (market, technology, regulatory, competitive) worth tracking before it forces adaptation.
[Strategic Objective](https://github.com/technehub-labs/dea-catalog-strategic-objectives) | [`dea-catalog-strategic-objectives`](https://github.com/technehub-labs/dea-catalog-strategic-objectives) | Active | Strategic Objective : high-level outcomes the enterprise seeks to achieve.
[Technology Radar Entry](https://github.com/technehub-labs/dea-catalog-technology-radar) | [`dea-catalog-technology-radar`](https://github.com/technehub-labs/dea-catalog-technology-radar) | Active | An emerging technology or technique being tracked (assess/trial/adopt/hold) prior to becoming a governed L5 Technology.
[Tenet](https://github.com/technehub-labs/dea-catalog-tenets) | [`dea-catalog-tenets`](https://github.com/technehub-labs/dea-catalog-tenets) | Experimental | DEA catalog: Tenet (TNT) : non-binding beliefs that inform Guardrails. OpenDEAM v0.4.0 (ADR-0004; renamed from dea-catalog-principles)

### L3 Business Operating Model

| Entity | Repository | Status | Description |
|---|---|---|---|
[Actor](https://github.com/technehub-labs/dea-catalog-actors) | [`dea-catalog-actors`](https://github.com/technehub-labs/dea-catalog-actors) | Experimental | Actors catalog : DEA L1 catalog repository for performers of enterprise processes (humans, teams, systems, AI agents).
[Digital Identity : Bot (Agent) Subtype](https://github.com/technehub-labs/dea-catalog-agent-foundry) | [`dea-catalog-agent-foundry`](https://github.com/technehub-labs/dea-catalog-agent-foundry) | Experimental | Agent Foundry : catalogue of autonomous agent patterns, agent platform specifications, multi-agent orchestration frameworks, and operational governance policies.
[Business Capability](https://github.com/technehub-labs/dea-catalog-business-capabilities) | [`dea-catalog-business-capabilities`](https://github.com/technehub-labs/dea-catalog-business-capabilities) | Active | Business Capability, the ability to deliver value, mapped to ECF coordinates.
[Business Object](https://github.com/technehub-labs/dea-catalog-business-objects) | [`dea-catalog-business-objects`](https://github.com/technehub-labs/dea-catalog-business-objects) | Experimental | L1 reference catalog for Business Objects (BO) : the atoms of the ECF matrix. Each entry is a real-world entity of interest to the business, classified by (ecf_domain, ecf_stage) coordinates plus a free-form object_class label.
[Change Initiative](https://github.com/technehub-labs/dea-catalog-change-initiatives) | [`dea-catalog-change-initiatives`](https://github.com/technehub-labs/dea-catalog-change-initiatives) | Active | A deliberate effort to shift Skills, Roles, or culture within an Organizational Unit, typically funded by an Investment Initiative.
[Business Service](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) | [`dea-catalog-digital-business-service-factory`](https://github.com/technehub-labs/dea-catalog-digital-business-service-factory) | Experimental | Digital Business Service Factory : catalogue of enterprise business service definitions, capabilities, and their decomposition into solution components, with governance contracts.
[Organizational Unit](https://github.com/technehub-labs/dea-catalog-organizational-units) | [`dea-catalog-organizational-units`](https://github.com/technehub-labs/dea-catalog-organizational-units) | Experimental | L1 reference catalog for Organizational Units (OU) : accountability containers that own capabilities, run processes, and are custodians for business objects. Classified by (ou_type, ou_scope, ou_lifecycle) structural axes plus optional ECF coordinates.
[Business Process](https://github.com/technehub-labs/dea-catalog-processes) | [`dea-catalog-processes`](https://github.com/technehub-labs/dea-catalog-processes) | Active | Processes catalog : DEA L1 catalog repository for business and operational processes, classified by intent (operational/support/management) and audience (ECF domain).
[Role](https://github.com/technehub-labs/dea-catalog-roles) | [`dea-catalog-roles`](https://github.com/technehub-labs/dea-catalog-roles) | Active | A defined set of required Skills and responsibilities that an Actor fulfills within an Organizational Unit.
[Skill](https://github.com/technehub-labs/dea-catalog-skills) | [`dea-catalog-skills`](https://github.com/technehub-labs/dea-catalog-skills) | Active | A capability an individual Actor possesses or must develop.
[Value Stream](https://github.com/technehub-labs/dea-catalog-value-streams) | [`dea-catalog-value-streams`](https://github.com/technehub-labs/dea-catalog-value-streams) | Active | Value Stream : end-to-end collection of value-creating activities.

### L4 Digital & Intelligence

| Entity | Repository | Status | Description |
|---|---|---|---|
[AI/ML Model](https://github.com/technehub-labs/dea-catalog-ai-ml-models) | [`dea-catalog-ai-ml-models`](https://github.com/technehub-labs/dea-catalog-ai-ml-models) | Active | AI / ML Model : trained model that augments or automates a system function.
[Data Entity](https://github.com/technehub-labs/dea-catalog-data-entities) | [`dea-catalog-data-entities`](https://github.com/technehub-labs/dea-catalog-data-entities) | Active | Data Entity : typed, persisted structure used by application components.
[Data Product](https://github.com/technehub-labs/dea-catalog-data-products) | [`dea-catalog-data-products`](https://github.com/technehub-labs/dea-catalog-data-products) | Active | Data Product : domain-owned, SLA-backed dataset exposed as a product.
[Digital Identity](https://github.com/technehub-labs/dea-catalog-digital-identities) | [`dea-catalog-digital-identities`](https://github.com/technehub-labs/dea-catalog-digital-identities) | Active | Digital Identity : Customer, Partner, or Bot representation in the ecosystem.
[Event](https://github.com/technehub-labs/dea-catalog-event-streams) | [`dea-catalog-event-streams`](https://github.com/technehub-labs/dea-catalog-event-streams) | Active | Event / Event Stream : discrete state changes with topic and schema.
[Information Class](https://github.com/technehub-labs/dea-catalog-information-classes) | [`dea-catalog-information-classes`](https://github.com/technehub-labs/dea-catalog-information-classes) | Active | Information Class : classification of data entities by sensitivity.
[Model Deployment](https://github.com/technehub-labs/dea-catalog-model-deployments) | [`dea-catalog-model-deployments`](https://github.com/technehub-labs/dea-catalog-model-deployments) | Active | A running instance of an AI/ML Model, hosted on an Application Component, with its own version, monitoring state, and health.

### L5 Technology & Execution

| Entity | Repository | Status | Description |
|---|---|---|---|
[API](https://github.com/technehub-labs/dea-catalog-api-contracts) | [`dea-catalog-api-contracts`](https://github.com/technehub-labs/dea-catalog-api-contracts) | Active | API / Service Contract : versioned contract exposing a system function.
[Application Component](https://github.com/technehub-labs/dea-catalog-application-components) | [`dea-catalog-application-components`](https://github.com/technehub-labs/dea-catalog-application-components) | Active | Application Component : deployable unit hosting system functions.
[Platform Service](https://github.com/technehub-labs/dea-catalog-platform-services) | [`dea-catalog-platform-services`](https://github.com/technehub-labs/dea-catalog-platform-services) | Active | Platform Service : compute, database, or network foundation service.
[System Function](https://github.com/technehub-labs/dea-catalog-system-functions) | [`dea-catalog-system-functions`](https://github.com/technehub-labs/dea-catalog-system-functions) | Active | System Function : capability that automates a business process.

### Cross-cutting & Semantic

| Entity | Repository | Status | Description |
|---|---|---|---|
[Concept](https://github.com/technehub-labs/dea-catalog-concepts) | [`dea-catalog-concepts`](https://github.com/technehub-labs/dea-catalog-concepts) | Experimental | DEA catalog: Concept (CON) : semantic-dimension concept graph. OpenDEAM v0.4.0 (ADR-0004; renamed from dea-catalog-glossary, absorbs dea-catalog-taxonomy)
[Performance Metric](https://github.com/technehub-labs/dea-catalog-metrics) | [`dea-catalog-metrics`](https://github.com/technehub-labs/dea-catalog-metrics) | Active | Assessment models and tools for evaluating business ecosystem health and maturity
[Ontologies](https://github.com/technehub-labs/dea-catalog-ontologies) | [`dea-catalog-ontologies`](https://github.com/technehub-labs/dea-catalog-ontologies) | Experimental | Domain OWL/RDF ontologies : fintech and healthcare. DEA L1 catalog repository.
[Reference Architecture](https://github.com/technehub-labs/dea-catalog-reference-architecture) | [`dea-catalog-reference-architecture`](https://github.com/technehub-labs/dea-catalog-reference-architecture) | Experimental | Digital Enterprise Reference Architecture : canonical reference model assembling all DEA framework layers into a practical delivery blueprint.
[Solution Hub](https://github.com/technehub-labs/dea-catalog-solution-hub) | [`dea-catalog-solution-hub`](https://github.com/technehub-labs/dea-catalog-solution-hub) | Experimental | Solution Hub : catalogue of solution archetypes, delivery templates, and implementation accelerators for recurring enterprise technology challenges.
<!-- GENERATED:END catalog-index -->


---

[Portfolio Index](README.md) · [Registry](../registry/repositories.yaml) · [Organization Profile](../profile/README.md)
