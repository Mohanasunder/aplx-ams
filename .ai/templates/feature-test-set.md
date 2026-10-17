---
id: FEAT-000
id_prefix: FEAT
title: <fill: title>
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Draft
author_agent: <fill: agent name>
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved): FEAT-NNN plan, FEAT-NNN-ACC, API, DBD, UIS -->
<fill: input references>

## Purpose And Scope
<!-- guidance: The tests that define done for this feature, written before implementation. What layers are covered and what is left to Phase 7 -->
<fill: purpose and scope>

## Risk Tier And Test Approver
<!-- guidance: Risk tier from the plan (Standard, High, Critical) and the approver it requires (see .ai/standards/review-and-approval.md) -->
<fill: risk tier and test approver>

## Criteria To Tests Map
<!-- guidance: Table: acceptance criterion ID (REQ S-N AC-n), test file path, test name, layer (database, backend, frontend, integration), what it asserts. Every criterion in FEAT-NNN-ACC has at least one row; include edge cases and error paths from the criteria -->
<fill: criteria to tests map>

## Test Files
<!-- guidance: Every test file path created for this feature. These files are locked once this artifact is Approved -->
<fill: test files>

## Stubs Created
<!-- guidance: Production files created only as empty signatures so tests compile (no logic), or 'Not applicable - reason' -->
<fill: stubs created>

## Red Run Evidence
<!-- guidance: Test command run, date, and result summary showing each new test fails because the behavior is missing (not because of syntax, import, or setup errors) -->
<fill: red run evidence>

## Test Commit
<!-- guidance: The commit SHA on the feature branch that contains exactly these tests. The checker diffs the test files against this SHA at PR time -->
<fill: test commit>

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every acceptance criterion maps to at least one test
- [ ] Tests assert behavior, not only that code runs
- [ ] Red run shows every new test failing for the missing behavior
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
