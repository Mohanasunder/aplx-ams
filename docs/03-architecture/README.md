# Phase 3: Solution Architecture

Choose the stack, structure, integrations, security model, and deployment topology.

- **Command:** `/run-architecture`
- **Human approver:** Architect / tech lead
- **Output folder:** `docs/03-architecture/`

## Required inputs

- Approved requirements (especially NFRs and integrations)
- Enterprise architecture standards and approved technology list
- Team skills and preferred stack
- Hosting and cloud constraints
- Documentation of systems to integrate with
- Security policies
- Budget limits
- Expected scale: users, data volume, traffic

## Producer agents

- `solution-architect`
- `security-architect`
- `infra-cost-analyst`

## Deliverable templates

- `.ai/templates/architecture-overview.md`
- `.ai/templates/adr.md`
- `.ai/templates/technology-comparison.md`
- `.ai/templates/threat-model.md`
- `.ai/templates/deployment-topology.md`
- `.ai/templates/cost-estimate.md`

## How it runs

solution-architect first (overview, technology comparison, ADRs); then security-architect (threat model) and infra-cost-analyst (topology, cost) in parallel; the checker applies the architecture review rules.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
