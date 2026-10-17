---
id: FEAT-017
id_prefix: FEAT
title: "FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket — Tasks"
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
# FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket — Tasks

## Input References
- FEAT-017 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-7 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-017. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `close_ticket(ticket_id, l1_user)` to `tickets/services.py`: validates status=Resolved; sets status=Closed; does NOT change resolution_stopped_at.
- [ ] T-2: Add POST `/api/tickets/{id}/close/` to `tickets/views.py`; L1-only.
- [ ] T-3: Update `tickets/serializers.py` (no new fields needed beyond status).
- [ ] T-4: Add `set_ticket_closed` to `tickets/dal.py`.
- [ ] T-5: Update `tickets/urls.py`.
- [ ] T-6: Update `TicketDetail.tsx` with Close button (L1-only, visible for Resolved tickets).
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-017` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-017 plan.md; REQ-001 v0.3 § S-7; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-017-TESTS (Phase 6 test set)

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
