---
id: REQ
id_prefix: REQ
title: <fill: "Project Name: User Stories">
phase: 2
version: 0.1
template: user-story
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

> **Collection file.** All user stories for this project live in this one file. Add one `## Story S-N` section per story; never create a separate REQ-NNN file for an additional story. Downstream artifacts reference a specific story as `REQ S-N` (e.g. `REQ S-3`) and a specific acceptance criterion as `REQ S-N AC-n` (e.g. `REQ S-3 AC-2`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Story S-1: <fill: title>

### Story Statement
<!-- guidance: As a <persona (cite as PER P-N)>, I want <capability>, so that <benefit> -->
<fill: story statement>

### Acceptance Criteria
<!-- guidance: Given/When/Then scenarios, each testable, as a numbered list ('1. Given ... when ... then ...'). Item n is cited downstream as REQ S-N AC-n (feature acceptance, test sets, test cases; checked by scripts/traceability.py), so never renumber after approval: add new criteria at the end and mark a dropped one 'Removed - SCR S-N' instead of deleting it -->
<fill: acceptance criteria>

### Business Rules
<!-- guidance: BR B-N references that apply -->
<fill: business rules>

### NFR References
<!-- guidance: NFR N-N references that apply -->
<fill: nfr references>

### Priority
<!-- guidance: MoSCoW with reason -->
<fill: priority>

---

<!-- Repeat the block above (from "## Story S-N:" to the closing ---) for each additional story.
     Increment the number: S-2, S-3, … Never reuse a number. Never renumber criteria within a story after approval. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual stories as REQ S-N; cite individual criteria as REQ S-N AC-n. -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every story has a unique S-N ID; IDs are consecutive and never reused
- [ ] Every story has at least one Given/When/Then acceptance criterion
- [ ] Criteria are numbered AC-1, AC-2, … within each story; never renumbered after approval
- [ ] Business rules reference BR B-N; NFRs reference NFR N-N
- [ ] Persona citations use PER P-N format
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
