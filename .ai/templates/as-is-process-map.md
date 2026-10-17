---
id: PRC
id_prefix: PRC
title: <fill: "Project Name: As-Is Process Maps">
phase: 1
version: 0.1
template: as-is-process-map
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Business owner / BA
default_approver: Business owner / BA
default_folder: docs/01-discovery
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All as-is process maps for this project live in this one file. Add one `## Process M-N` section per process; never create a separate PRC-NNN file for an additional process. Downstream artifacts reference a specific process as `PRC M-N` (e.g. `PRC M-2`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Process M-1: <fill: process name>

### Process Overview
<!-- guidance: Purpose, owner, trigger, outcome -->
<fill: process overview>

### Steps
<!-- guidance: Table: step, actor, system, pain point -->
<fill: steps>

### Diagram
<!-- guidance: Mermaid flowchart block -->
<fill: diagram>

### Pain Points
<!-- guidance: Ranked, each linked to a step -->
<fill: pain points>

---

<!-- Repeat the block above (from "## Process M-N:" to the closing ---) for each additional process.
     Increment the number: M-2, M-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual processes downstream as PRC M-N (e.g. PRC M-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every process has a unique M-N ID; IDs are consecutive and never reused
- [ ] Every step has an actor
- [ ] Pain points ranked and each linked to a step
- [ ] Diagram matches the step table for each process
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
