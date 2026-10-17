---
id: BKL
id_prefix: BKL
title: <fill: "Project Name: Backlog">
phase: 2
version: 0.1
template: backlog-entry
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

> **Collection file.** The full prioritised backlog lives in this one file. Add one `## Entry BL-N` section per backlog item; never create a separate BKL-NNN file. Downstream artifacts reference a specific entry as `BKL BL-N` (e.g. `BKL BL-4`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Entry BL-1: <fill: title>

### Item
<!-- guidance: Linked story or epic reference (REQ S-N or EPC E-N) -->
<fill: item>

### Priority
<!-- guidance: MoSCoW or rank, with reason -->
<fill: priority>

### Release
<!-- guidance: Target release or MVP flag -->
<fill: release>

---

<!-- Repeat the block above (from "## Entry BL-N:" to the closing ---) for each additional backlog item.
     Increment the number: BL-2, BL-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual backlog entries as BKL BL-N (e.g. BKL BL-3). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every entry has a unique BL-N ID; IDs are consecutive and never reused
- [ ] Every entry links to a story (REQ S-N) or epic (EPC E-N)
- [ ] Every entry has a priority and a release target
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
