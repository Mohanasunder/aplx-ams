---
id: FEAT-006-ACC
id_prefix: FEAT
title: "FEAT-006: S-21: User Signs In with a User Account â€” Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-006: S-21: User Signs In with a User Account â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-21
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-006 (REQ S-21). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-21.

## Acceptance Criteria
REQ-021 AC-1 REQ S-21 AC-1: Given an active user account with a correct password, when the user signs in, then they reach APLX AMS with the tasks of their role, and no second factor is asked for (NFR N-5).
REQ-021 AC-2 REQ S-21 AC-2: Given a wrong password, when the user signs in, then sign-in is refused without saying whether the account name or the password was wrong (A-019).
REQ-021 AC-3 REQ S-21 AC-3: Given a user setting a password, when it has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "abcdefg1" with no upper-case letter), then the password is refused; "Abcdefg1" is accepted (NFR N-5, OQ-044).
REQ-021 AC-4 REQ S-21 AC-4: Given 5 failed sign-ins on one user account, when a sixth sign-in is tried within 30 minutes of the fifth failure, then it is refused even with the correct password; after the 30 minutes the correct password is accepted (NFR N-5, OQ-044).

## Test Scenarios
REQ-021 AC-1 REQ S-21 AC-1: Given an active user account with a correct password... â€” verify Given/When/Then conditions as stated above.
REQ-021 AC-2 REQ S-21 AC-2: Given a wrong password... â€” verify Given/When/Then conditions as stated above.
REQ-021 AC-3 REQ S-21 AC-3: Given a user setting a password... â€” verify Given/When/Then conditions as stated above.
REQ-021 AC-4 REQ S-21 AC-4: Given 5 failed sign-ins on one user account... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-21; PIB-005 v0.1
- Downstream: FEAT-006-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | None |
| Timestamp | 2026-10-17 18:47 UTC |
