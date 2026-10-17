---
id: FEAT-017-ACC
id_prefix: FEAT
title: "FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket â€” Acceptance Criteria"
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
# FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-7
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-017 (REQ S-7). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-7.

## Acceptance Criteria
REQ-007 AC-1 REQ S-7 AC-1: Given a Resolved ticket in the L1 queue, when an L1 support engineer closes it, then its status is Closed, it leaves the L1 queue, and the client user of its client organization sees it as Closed.
REQ-007 AC-2 REQ S-7 AC-2: Given a ticket that is not Resolved, when an L1 support engineer tries to close it, then the close is refused and the status does not change.
REQ-007 AC-3 REQ S-7 AC-3: Given a Resolved ticket, when it is closed, then the resolution clock stop time does not change (the clock stopped at Resolved, BR B-5).
REQ-007 AC-4 REQ S-7 AC-4: Given a Resolved ticket of client organization A, when an L1 support engineer closes it, then APLX AMS sends no email or other message about the closure to the client user; the Closed status on the ticket is the only notice (BR B-11, OQ-037).

## Test Scenarios
REQ-007 AC-1 REQ S-7 AC-1: Given a Resolved ticket in the L1 queue, when an L1 support engineer closes it, ... â€” verify Given/When/Then conditions as stated above.
REQ-007 AC-2 REQ S-7 AC-2: Given a ticket that is not Resolved, when an L1 support engineer tries to close ... â€” verify Given/When/Then conditions as stated above.
REQ-007 AC-3 REQ S-7 AC-3: Given a Resolved ticket, when it is closed, then the resolution clock stop time ... â€” verify Given/When/Then conditions as stated above.
REQ-007 AC-4 REQ S-7 AC-4: Given a Resolved ticket of client organization A, when an L1 support engineer cl... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-7; PIB-005 v0.1
- Downstream: FEAT-017-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
