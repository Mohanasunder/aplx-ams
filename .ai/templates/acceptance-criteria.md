---
id: ACC
id_prefix: ACC
title: <fill: "Project Name: Acceptance Criteria">
phase: 2
version: 0.1
template: acceptance-criteria
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

> **Collection file.** All supplemental acceptance criteria sets live in this one file. Add one `## Criteria Set AC-N` section per set; never create a separate ACC-NNN file. Downstream artifacts reference a specific set as `ACC AC-N` (e.g. `ACC AC-2`). Note: acceptance criteria for individual user stories are embedded inline within `user-stories.md` and cited as `REQ S-N AC-n`; this file holds extended or cross-story criteria sets.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Criteria Set AC-1: <fill: title>

### Scenarios
<!-- guidance: Given/When/Then, numbered -->
<fill: scenarios>

### Edge Cases
<!-- guidance: Boundary, error, and permission cases -->
<fill: edge cases>

---

<!-- Repeat the block above (from "## Criteria Set AC-N:" to the closing ---) for each additional set.
     Increment the number: AC-2, AC-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual criteria sets as ACC AC-N (e.g. ACC AC-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every criteria set has a unique AC-N ID; IDs are consecutive and never reused
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
