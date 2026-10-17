---
id: ADR
id_prefix: ADR
title: <fill: title>
phase: 3
version: 0.1
template: adr
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Architect / tech lead
default_approver: Architect / tech lead
default_folder: docs/03-architecture
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All architectural decision records for the project live in this single file. Always use `--out docs/03-architecture/adrs.md` when calling `new_artifact.py`. Each decision is a `## ADR A-N: [Title]` section (A-1, A-2, …). A specific ADR is cited downstream as `ADR A-N`. Never renumber after approval — append new decisions at the end; mark a superseded one `Superseded by ADR A-M - SCR S-N`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this collection covers and what it does not -->
<fill: purpose and scope>

---

## ADR A-1: <fill: decision title>

### Status And Date
<!-- guidance: Proposed | Accepted | Superseded, with date -->
<fill: status and date>

### Context
<!-- guidance: Forces and constraints driving this decision -->
<fill: context>

### Options Considered
<!-- guidance: At least two options with trade-offs -->
<fill: options considered>

### Decision
<!-- guidance: The chosen option and the reason -->
<fill: decision>

### Consequences
<!-- guidance: Positive, negative, and follow-ups -->
<fill: consequences>

### Traceability Links
<!-- guidance: Upstream IDs (NFR N-N, REQ S-N, SPK S-N) and downstream IDs this decision constrains -->
<fill: traceability links>

---
<!-- Add further ## ADR A-N: sections here as new decisions arise -->

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md (collection-level) -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md (collection-level) -->
<fill: open questions>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] Every ADR has at least two options and a rationale for the chosen one
- [ ] Every ADR has its own Traceability Links citing upstream NFR/REQ/SPK S-N IDs
- [ ] ADR sub-IDs (A-1, A-2, …) are consecutive from 1 with no gaps
- [ ] No separate ADR-NNN.md files exist; all decisions are sections in this file
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
