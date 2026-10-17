---
id: FEAT-019
id_prefix: FEAT
title: "FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA — Tasks"
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
# FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA — Tasks

## Input References
- FEAT-019 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-9 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-019. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Expand `sla/services.py` with `compute_elapsed_business_hours(start_dt, end_dt, holiday_dates)`: counts only IST business hours (09:00–18:00, Mon–Fri) excluding holiday dates.
- [ ] T-2: Add `get_holidays_as_set(start_date, end_date)` to `sla/dal.py` for fast lookup.
- [ ] T-3: Update `tickets/services.py` to call `compute_elapsed_business_hours` when computing response/resolution due times.
- [ ] T-4: Update `tickets/serializers.py` to include computed `response_elapsed_hours` and `resolution_elapsed_hours` (on-read, ADR A-10).
- [ ] T-5: Update `tickets/views.py` ticket detail endpoint to include SLA computed fields.
- [ ] T-6: Update `TicketDetail.tsx` to display response/resolution elapsed and due times.
- [ ] T-7: Update `tickets.ts` API types with new SLA fields.
- [ ] T-8: Write `sla/tests/test_sla_computation.py` with `freezegun` for AC-1 through AC-4.
- [ ] T-9: Run all gate commands locally; confirm each exits 0.
- [ ] T-10: Verify `python3 scripts/check_feature_size.py size FEAT-019` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-019 plan.md; REQ-001 v0.3 § S-9; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-019-TESTS (Phase 6 test set)

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
