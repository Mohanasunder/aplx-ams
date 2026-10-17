---
id: EPC
id_prefix: EPC
title: <fill: "Project Name: Epics">
phase: 2
version: 0.1
template: epic
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Product owner / BA
default_approver: Product owner / BA
default_folder: docs/02-requirements
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All epics for this project live in this one file. Add one `## Epic E-N` section per epic; never create a separate EPC-NNN file for an additional epic. Downstream artifacts reference a specific epic as `EPC E-N` (e.g. `EPC E-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Epic E-1: <fill: title>

### Description
<!-- guidance: What capability this epic delivers -->
<fill: description>

### Business Value
<!-- guidance: Brief goals this epic serves, one per line as 'BRF G-n' (at least one; checked by scripts/traceability.py check --phase 2). Then one or two sentences on the value, naming the KPI it moves -->
<fill: business value>

### Stories
<!-- guidance: List of story references as REQ S-N. At least one story that is not Won't priority, or the goals above count as uncovered -->
<fill: stories>

---

<!-- Repeat the block above (from "## Epic E-N:" to the closing ---) for each additional epic.
     Increment the number: E-2, E-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual epics downstream as EPC E-N (e.g. EPC E-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every epic has a unique E-N ID; IDs are consecutive and never reused
- [ ] Business Value cites at least one brief goal as 'BRF G-n' for each epic
- [ ] Stories section lists REQ S-N references for each epic
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
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
