---
id: FEAT-009-ACC
id_prefix: FEAT
title: "FEAT-009: S-31: User Changes Their Own Password â€” Acceptance Criteria"
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
# FEAT-009: S-31: User Changes Their Own Password â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-31
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-009 (REQ S-31). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-31.

## Acceptance Criteria
REQ-031 AC-1 REQ S-31 AC-1: Given signed-in user X (an internal user or a client user), when X enters their current password and changes their own password to "Cdefghi3", then X's next sign-in succeeds with "Cdefghi3" and X's previous password is refused (BR B-23).
REQ-031 AC-2 REQ S-31 AC-2: Given signed-in user X, when the new password has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "cdefghi3"), then the change is refused and X's previous password stays valid (NFR N-5, OQ-044).
REQ-031 AC-3 REQ S-31 AC-3: Given signed-in user X who is not a delivery manager, when X tries to change the password of another user's user account, then the change is refused (BR B-23).
REQ-031 AC-4 REQ S-31 AC-4: Given signed-in user X, when X enters a wrong current password while changing their own password, then the change is refused and X's previous password stays valid (BR B-23, OQ-053).

## Test Scenarios
REQ-031 AC-1 REQ S-31 AC-1: Given signed-in user X (an internal user or a client user)... â€” verify Given/When/Then conditions as stated above.
REQ-031 AC-2 REQ S-31 AC-2: Given signed-in user X... â€” verify Given/When/Then conditions as stated above.
REQ-031 AC-3 REQ S-31 AC-3: Given signed-in user X who is not a delivery manager... â€” verify Given/When/Then conditions as stated above.
REQ-031 AC-4 REQ S-31 AC-4: Given signed-in user X... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-31; PIB-005 v0.1
- Downstream: FEAT-009-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
