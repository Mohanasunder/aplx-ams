---
id: FEAT-028-ACC
id_prefix: FEAT
title: "FEAT-028: S-16: Delivery Manager Reviews Effort Against a Contract â€” Acceptance Criteria"
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
# FEAT-028: S-16: Delivery Manager Reviews Effort Against a Contract â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-16
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-028 (REQ S-16). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-16.

## Acceptance Criteria
REQ-016 AC-1 REQ S-16 AC-1: Given client organization A has an hours bank contract of 100 contracted hours and 30 hours recorded, when the delivery manager reviews it, then it shows 30 hours recorded and an hours bank balance of 70 hours (BR B-16).
REQ-016 AC-2 REQ S-16 AC-2: Given client organization B has a fixed fee contract and 12 hours recorded, when the delivery manager reviews it, then it shows 12 hours recorded and no hours bank balance (BR B-17).
REQ-016 AC-3 REQ S-16 AC-3: Given a client user, when they try to review effort against a contract, then access is refused.
REQ-016 AC-4 REQ S-16 AC-4: Given client organization A's hours bank balance is 1 hour, when a support engineer records 3 hours on a ticket of organization A assigned to them, then the effort entry is saved, the hours bank balance is -2 hours, and the delivery manager reviewing the contract sees a warning with the balance (BR B-16, OQ-042).

## Test Scenarios
REQ-016 AC-1 REQ S-16 AC-1: Given client organization A has an hours bank contract of 100 contracted hours a... â€” verify Given/When/Then conditions as stated above.
REQ-016 AC-2 REQ S-16 AC-2: Given client organization B has a fixed fee contract and 12 hours recorded, when... â€” verify Given/When/Then conditions as stated above.
REQ-016 AC-3 REQ S-16 AC-3: Given a client user, when they try to review effort against a contract, then acc... â€” verify Given/When/Then conditions as stated above.
REQ-016 AC-4 REQ S-16 AC-4: Given client organization A's hours bank balance is 1 hour, when a support engin... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-16; PIB-005 v0.1
- Downstream: FEAT-028-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
