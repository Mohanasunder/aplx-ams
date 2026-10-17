---
id: BR
id_prefix: BR
title: <fill: "Project Name: Business Rules">
phase: 2
version: 0.1
template: business-rule
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

> **Collection file.** All business rules for this project live in this one file. Add one `## Rule B-N` section per rule; never create a separate BR-NNN file. Downstream artifacts reference a specific rule as `BR B-N` (e.g. `BR B-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Rule B-1: <fill: title>

### Rule
<!-- guidance: One unambiguous statement -->
<fill: rule>

### Source
<!-- guidance: Stakeholder, document, regulation -->
<fill: source>

### Applies To
<!-- guidance: Stories (REQ S-N) or features (FEAT-NNN) -->
<fill: applies to>

---

<!-- Repeat the block above (from "## Rule B-N:" to the closing ---) for each additional rule.
     Increment the number: B-2, B-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual rules downstream as BR B-N (e.g. BR B-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every rule has a unique B-N ID; IDs are consecutive and never reused
- [ ] Every rule has a source (stakeholder, document, or regulation)
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
