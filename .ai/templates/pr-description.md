---
id: PRD
id_prefix: PRD
title: <fill: title>
phase: 6
version: 0.1
template: pr-description
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All PR descriptions for the project live in this single file at `docs/06-build/pr-descriptions.md`. Each PR is a `## PR FEAT-NNN: [feature title]` section. A specific PR description is cited as `PRD FEAT-NNN`. Never create a separate `PRD-NNN.md` file. The documentation-writer appends a new `## PR FEAT-NNN:` section for each feature after implementation. Approve each PR section individually with `/approve docs/06-build/pr-descriptions.md --sub-id FEAT-NNN`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this collection covers: one PR description per feature, accumulating across all Phase 6 builds -->
<fill: purpose and scope>

---

## PR FEAT-000: <fill: feature title>

<!-- pr_status: Draft -->
<!-- pr_approver: -->
<!-- pr_depth: -->
<!-- pr_review_minutes: -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used for this PR -->
<fill: input references>

### Summary
<!-- guidance: What changed and why, in 3 sentences -->
<fill: summary>

### Linked Artifacts
<!-- guidance: FEAT, REQ, API, DBD IDs -->
<fill: linked artifacts>

### Changes
<!-- guidance: By area: database, backend, frontend, tests, docs -->
<fill: changes>

### Tests
<!-- guidance: What was added and how to run them -->
<fill: tests>

### Requirements Covered
<!-- guidance: One line per criterion in acceptance.md: 'REQ S-N AC-n: `test name` (passing)', test names from the approved FEAT-NNN-TESTS. Checked by scripts/pr_summary.py -->
<fill: requirements covered>

### Known Gaps
<!-- guidance: What this change does not do yet, limits found, follow-ups (with OQ- or DEF- IDs); or 'None' -->
<fill: known gaps>

### Deviations From Plan
<!-- guidance: Any difference from plan.md (files, approach, sequence) and why; or 'None'. Must not be 'None' if files changed outside the plan -->
<fill: deviations from plan>

### Blockers
<!-- guidance: Anything that stopped the work within scope (spec conflict, missing context, environment) with its OQ- or SCR- ID; must be 'None' before human review -->
<fill: blockers>

### Risk Tier And Review Depth
<!-- guidance: First line: the tier from the plan (Standard | High | Critical) and the required review depth (Deep for High and Critical; Standard; or Light only for Standard changes limited to docs, UI copy and layout, or refactors covered by existing tests), with the reason. Then the depth checklist from .ai/standards/review-and-approval.md for the reviewer to tick -->
<fill: risk tier and review depth>

### Reviewer Checklist
<!-- guidance: Checklist from .ai/standards/review-and-approval.md -->
<fill: reviewer checklist>

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
<fill: traceability links>

### Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)

---
<!-- Add further ## PR FEAT-NNN: sections here as new features are built -->

## Assumptions
<!-- guidance: Collection-level assumptions logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Collection-level open questions logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
