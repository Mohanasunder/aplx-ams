# Phase 1: Business Discovery

Understand the problem, goals, stakeholders, and scope before writing requirements.

- **Command:** `/run-discovery`
- **Human approver:** Business owner / BA
- **Output folder:** `docs/01-discovery/`

## Required inputs

- Problem or opportunity statement (even rough)
- Stakeholder interviews, meeting transcripts, workshop notes (drop files in docs/01-discovery/inputs/)
- Existing documents: SOPs, proposals, RFPs
- Current systems and tools in use
- Business goals, KPIs, budget and timeline constraints
- Regulatory and policy constraints
- Market or competitor information (if relevant)

## Producer agents

- `discovery-analyst`
- `process-mapper`
- `research-analyst`

## Deliverable templates

- `.ai/templates/business-brief.md`
- `.ai/templates/persona.md`
- `.ai/templates/scope-statement.md`
- `.ai/templates/as-is-process-map.md`
- `.ai/templates/risk-register-entry.md`
- `.ai/templates/research-summary.md`

## How it runs

discovery-analyst first (brief, personas, scope, risks; owns the open questions log); process-mapper can run in parallel from the same inputs; research-analyst only if the human asks for market or domain research.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
