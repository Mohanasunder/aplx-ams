---
id: FEAT-005
id_prefix: FEAT
title: "FEAT-005: S-20: Delivery Manager Manages User Accounts — Acceptance Criteria"
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
# FEAT-005: S-20: Delivery Manager Manages User Accounts — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-20
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-005 (REQ S-20). Criteria are copied verbatim from REQ-001 v0.3 § S-20.

## Acceptance Criteria
REQ-020 AC-1 REQ S-20 AC-1: Given the delivery manager, when they create a user account with role L1 support engineer, L2/L3 support engineer, delivery manager or client user, then the account is saved with that role.
REQ-020 AC-2 REQ S-20 AC-2: Given the delivery manager creates a client user account, when no client organization is chosen, then the account is not saved.
REQ-020 AC-3 REQ S-20 AC-3: Given an active user account, when the delivery manager deactivates it, then that user can no longer sign in.
REQ-020 AC-4 REQ S-20 AC-4: Given a user who is not a delivery manager, when they try to create, change or deactivate a user account, then the change is refused.

## Test Scenarios
REQ-020 AC-1 REQ S-20 AC-1: Given the delivery manager... — verify Given/When/Then conditions as stated above.
REQ-020 AC-2 REQ S-20 AC-2: Given the delivery manager creates a client user account... — verify Given/When/Then conditions as stated above.
REQ-020 AC-3 REQ S-20 AC-3: Given an active user account... — verify Given/When/Then conditions as stated above.
REQ-020 AC-4 REQ S-20 AC-4: Given a user who is not a delivery manager... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-20; PIB-005 v0.1
- Downstream: FEAT-005-TASKS (builder task list); Phase 6 test set FEAT-005-TESTS

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
