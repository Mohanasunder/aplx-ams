---
id: FEAT-034-ACC
id_prefix: FEAT
title: "FEAT-034: S-33: Users View Security Events â€” Acceptance Criteria"
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
# FEAT-034: S-33: Users View Security Events â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-33
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-034 (REQ S-33). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-33.

## Acceptance Criteria
REQ-033 AC-1 REQ S-33 AC-1: Given security events recorded for user accounts X and Y and a failed sign-in with the account name "user.unknown", when the delivery manager views security events, then they see the security events of any user account they choose, X or Y, and the failed sign-in for "user.unknown", each with the event, the user, the user account or account name typed, and the date and time (BR B-24, OQ-064).
REQ-033 AC-2 REQ S-33 AC-2: Given an L1 support engineer, an L2/L3 support engineer or a delivery manager with user account W, when they view their own security events, then they see every security event of user account W (BR B-24, OQ-064).
REQ-033 AC-3 REQ S-33 AC-3: Given an L1 support engineer or an L2/L3 support engineer with user account W, when they try to view the security events of another user account, then access is refused (BR B-24, OQ-064).
REQ-033 AC-4 REQ S-33 AC-4: Given a client user, when they try to view any security event, their own included, then access is refused; and given any user, when they try to edit or delete a security event entry, then the change is refused (BR B-22, BR B-24, OQ-064).

## Test Scenarios
REQ-033 AC-1 REQ S-33 AC-1: Given security events recorded for user accounts X and Y and a failed sign-in wi... â€” verify Given/When/Then conditions as stated above.
REQ-033 AC-2 REQ S-33 AC-2: Given an L1 support engineer, an L2/L3 support engineer or a delivery manager wi... â€” verify Given/When/Then conditions as stated above.
REQ-033 AC-3 REQ S-33 AC-3: Given an L1 support engineer or an L2/L3 support engineer with user account W, w... â€” verify Given/When/Then conditions as stated above.
REQ-033 AC-4 REQ S-33 AC-4: Given a client user, when they try to view any security event, their own include... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-33; PIB-005 v0.1
- Downstream: FEAT-034-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
