---
id: FEAT-014
id_prefix: FEAT
title: "FEAT-014: S-4: L1 Support Engineer Changes a Ticket Priority — Tasks"
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
# FEAT-014: S-4: L1 Support Engineer Changes a Ticket Priority — Tasks

## Input References
- FEAT-014 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-4 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-014. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `change_priority(ticket_id, new_priority, reason, l1_user, action_time)` to `tickets/services.py`: validates reason not empty, ticket not Resolved; stops response clock if first L1 action; recalculates resolution_due from raise_time using new priority (BR B-7).
- [ ] T-2: Add PATCH `/api/tickets/{id}/change-priority/` to `tickets/views.py`; L1-only.
- [ ] T-3: Update `tickets/serializers.py` with `PriorityChangeSerializer` (new_priority, reason).
- [ ] T-4: Add `update_ticket_priority` to `tickets/dal.py`.
- [ ] T-5: Update `tickets/urls.py`.
- [ ] T-6: Update `TicketDetail.tsx` with Change Priority dialog (L1-only, requires reason).
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-014` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-014 plan.md; REQ-001 v0.3 § S-4; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-014-TESTS (Phase 6 test set)

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
