---
id: FEAT-008
id_prefix: FEAT
title: "FEAT-008: S-30: Delivery Manager Sets a Temporary Password — Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-008: S-30: Delivery Manager Sets a Temporary Password — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-30
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-008 (REQ S-30). Criteria are copied verbatim from REQ-001 v0.3 § S-30.

## Acceptance Criteria
REQ-030 AC-1 REQ S-30 AC-1: Given the delivery manager creates a user account with temporary password "Abcdefg1", when the account is saved, then the user signs in with that user account and "Abcdefg1" and is not asked to change the password (BR B-23).
REQ-030 AC-2 REQ S-30 AC-2: Given the delivery manager sets a temporary password, when it has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "abcdefg1"), then the temporary password is refused (NFR N-5, OQ-044).
REQ-030 AC-3 REQ S-30 AC-3: Given user X told the delivery manager outside APLX AMS that they forgot their password, and X's user account is locked after 5 failed sign-ins, when the delivery manager sets new temporary password "Bcdefgh2" on X's user account, then the lock clears at once, X signs in immediately with "Bcdefgh2", X's previous password is refused, and X is not asked to change the password (BR B-23, OQ-054).
REQ-030 AC-4 REQ S-30 AC-4: Given a user who is not a delivery manager, when they try to set a temporary password on another user's user account, then the change is refused (BR B-21, BR B-23).

## Test Scenarios
REQ-030 AC-1 REQ S-30 AC-1: Given the delivery manager creates a user account with tempo... — verify Given/When/Then conditions as stated above.
REQ-030 AC-2 REQ S-30 AC-2: Given the delivery manager sets a temporary password... — verify Given/When/Then conditions as stated above.
REQ-030 AC-3 REQ S-30 AC-3: Given user X told the delivery manager outside APLX AMS that... — verify Given/When/Then conditions as stated above.
REQ-030 AC-4 REQ S-30 AC-4: Given a user who is not a delivery manager... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-30; PIB-005 v0.1
- Downstream: FEAT-008-TASKS (builder task list); Phase 6 test set FEAT-008-TESTS

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
