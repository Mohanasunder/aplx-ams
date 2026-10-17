---
id: FEAT-032
id_prefix: FEAT
title: "FEAT-032: S-23: Internal User Views a Ticket Audit Trail — Acceptance Criteria"
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
# FEAT-032: S-23: Internal User Views a Ticket Audit Trail — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-23
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-032 (REQ S-23). Criteria are copied verbatim from REQ-001 v0.3 § S-23.

## Acceptance Criteria
REQ-023 AC-1 REQ S-23 AC-1: Given a ticket whose priority, status, assignment and effort were each changed once, when the delivery manager views its audit trail, then it shows 4 entries, each with the user, date and time, old value and new value.
REQ-023 AC-2 REQ S-23 AC-2: Given an L1 support engineer or an L2/L3 support engineer, when they view the audit trail of a ticket, then they see the same entries.
REQ-023 AC-3 REQ S-23 AC-3: Given a client user, when they try to view the audit trail of their organization's ticket, then access is refused.
REQ-023 AC-4 REQ S-23 AC-4: Given any user, when they try to edit or delete an audit entry, then the change is refused (A-016).

## Test Scenarios
REQ-023 AC-1 REQ S-23 AC-1: Given a ticket whose priority, status, assignment and effort were each changed o... — verify Given/When/Then conditions as stated above.
REQ-023 AC-2 REQ S-23 AC-2: Given an L1 support engineer or an L2/L3 support engineer, when they view the au... — verify Given/When/Then conditions as stated above.
REQ-023 AC-3 REQ S-23 AC-3: Given a client user, when they try to view the audit trail of their organization... — verify Given/When/Then conditions as stated above.
REQ-023 AC-4 REQ S-23 AC-4: Given any user, when they try to edit or delete an audit entry, then the change ... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-23; PIB-005 v0.1
- Downstream: FEAT-032-TASKS (builder task list); Phase 6 test set FEAT-032-TESTS

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
