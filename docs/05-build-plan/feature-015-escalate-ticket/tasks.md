---
id: FEAT-015
id_prefix: FEAT
title: "FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3 — Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3 — Tasks

## Input References
- FEAT-015 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-5 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-015. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `escalate_ticket(ticket_id, l2l3_user_id, l1_user, action_time)` to `tickets/services.py`: assigns ticket to L2/L3, removes escalation_flag, stops response clock if first L1 action, creates audit entry.
- [ ] T-2: Add PATCH `/api/tickets/{id}/assign/` to `tickets/views.py`; L1-only.
- [ ] T-3: Update `tickets/serializers.py` with `AssignSerializer` (assigned_to_id).
- [ ] T-4: Add `assign_ticket` to `tickets/dal.py`.
- [ ] T-5: Update `tickets/urls.py`.
- [ ] T-6: Update `TicketDetail.tsx` with Assign/Escalate dialog (L1-only, L2/L3 user picker).
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-015` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-015 plan.md; REQ-001 v0.3 § S-5; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-015-TESTS (Phase 6 test set)

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
