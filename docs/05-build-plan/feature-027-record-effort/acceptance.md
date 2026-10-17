---
id: FEAT-027-ACC
id_prefix: FEAT
title: "FEAT-027: S-15: Support Engineer Records Effort on a Ticket â€” Acceptance Criteria"
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
# FEAT-027: S-15: Support Engineer Records Effort on a Ticket â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-15
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-027 (REQ S-15). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-15.

## Acceptance Criteria
REQ-015 AC-1 REQ S-15 AC-1: Given a ticket of client organization A with an active contract, assigned to a support engineer, when that support engineer records 1.5 hours on 2026-11-02, then an effort entry with that support engineer as the engineer, the date, 1.5 hours and the ticket is saved and counts against organization A's active contract (BR B-15; each engineer records their own effort, OQ-015).
REQ-015 AC-2 REQ S-15 AC-2: Given a support engineer recording effort, when the hours are 0 or negative, then the effort entry is not saved (A-020).
REQ-015 AC-3 REQ S-15 AC-3: Given an effort entry is saved, when the audit trail of the ticket is viewed, then it holds the new effort entry, the user and the time (BR B-22).
REQ-015 AC-4 REQ S-15 AC-4: Given a ticket assigned to an L2/L3 support engineer X, when a different support engineer or a client user tries to record effort on it, then no effort entry is saved (BR B-15, OQ-048).

## Test Scenarios
REQ-015 AC-1 REQ S-15 AC-1: Given a ticket of client organization A with an active contract, assigned to a s... â€” verify Given/When/Then conditions as stated above.
REQ-015 AC-2 REQ S-15 AC-2: Given a support engineer recording effort, when the hours are 0 or negative, the... â€” verify Given/When/Then conditions as stated above.
REQ-015 AC-3 REQ S-15 AC-3: Given an effort entry is saved, when the audit trail of the ticket is viewed, th... â€” verify Given/When/Then conditions as stated above.
REQ-015 AC-4 REQ S-15 AC-4: Given a ticket assigned to an L2/L3 support engineer X, when a different support... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-15; PIB-005 v0.1
- Downstream: FEAT-027-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
