---
id: FEAT-011
id_prefix: FEAT
title: "FEAT-011: S-1: Client User Raises a Ticket in the Portal — Tasks"
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
# FEAT-011: S-1: Client User Raises a Ticket in the Portal — Tasks

## Input References
- FEAT-011 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-1 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-011. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/tickets/` app with `models.py` defining `Ticket` model (org FK, sap_app FK, type, priority, description, raise_time, status, response_due, resolution_due, response_stopped_at, resolution_stopped_at, assigned_to FK nullable, awaiting_client bool) per DBD-001.
- [ ] T-2: Generate `tickets/migrations/0001_initial.py`.
- [ ] T-3: Write `serializers.py` with `TicketCreateSerializer` (client user write) and `TicketDetailSerializer`.
- [ ] T-4: Write `services.py` with `raise_ticket(user, org, sap_app, type, priority, description)`: validates org membership, computes response/resolution targets from BR B-1 (per priority), records raise_time.
- [ ] T-5: Write `dal.py` with `get_tickets_for_org`, `get_l1_queue`, `get_ticket_by_id` queries.
- [ ] T-6: Write `views.py` with `TicketViewSet`; POST restricted to client users of the correct org.
- [ ] T-7: Write `urls.py`; register in root `urls.py`.
- [ ] T-8: Write `src/frontend/src/pages/RaiseTicket.tsx` with MUI form (type, SAP app, priority, description).
- [ ] T-9: Write `src/frontend/src/api/tickets.ts` with typed API calls.
- [ ] T-10: Write test with `freezegun` for AC-4: raise at 18:30 IST; assert SLA elapsed = 0 until next 09:00.
- [ ] T-11: Run all gate commands locally; confirm each exits 0.
- [ ] T-12: Verify `python3 scripts/check_feature_size.py size FEAT-011` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-011 plan.md; REQ-001 v0.3 § S-1; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-011-TESTS (Phase 6 test set)

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
