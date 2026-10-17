---
id: NFR
id_prefix: NFR
title: <fill: "Project Name: Non-Functional Requirements">
phase: 2
version: 0.1
template: nfr
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

> **Collection file.** All non-functional requirements for this project live in this one file. Add one `## NFR N-N` section per NFR; never create a separate NFR-NNN file. Downstream artifacts reference a specific NFR as `NFR N-N` (e.g. `NFR N-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## NFR N-1: <fill: title>

### Category
<!-- guidance: Performance, security, availability, accessibility, compliance, etc. -->
<fill: category>

### Requirement
<!-- guidance: One testable statement -->
<fill: requirement>

### Measurable Target
<!-- guidance: Number and unit (e.g. p95 under 300 ms at 200 concurrent users) -->
<fill: measurable target>

### Verification Method
<!-- guidance: How it will be tested -->
<fill: verification method>

---

<!-- Repeat the block above (from "## NFR N-N:" to the closing ---) for each additional NFR.
     Increment the number: N-2, N-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual NFRs downstream as NFR N-N (e.g. NFR N-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every NFR has a unique N-N ID; IDs are consecutive and never reused
- [ ] Every NFR has a measurable target with a number and unit
- [ ] Every NFR has a verification method
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
