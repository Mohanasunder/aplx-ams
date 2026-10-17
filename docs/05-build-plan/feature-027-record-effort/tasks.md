---
id: FEAT-027
id_prefix: FEAT
title: "FEAT-027: S-15: Support Engineer Records Effort on a Ticket — Tasks"
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
# FEAT-027: S-15: Support Engineer Records Effort on a Ticket — Tasks

## Input References
- FEAT-027 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-15 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-027. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/effort/` app with `models.py` defining `EffortEntry` (ticket FK, engineer FK, date, hours, is_deleted bool, created_at) per DBD-001 (soft-delete A-039).
- [ ] T-2: Generate `effort/migrations/0001_initial.py`.
- [ ] T-3: Write `effort/serializers.py` with `EffortEntryCreateSerializer`.
- [ ] T-4: Write `effort/services.py` with `record_effort(ticket_id, engineer, date, hours)`: validates hours > 0, validates engineer is assigned to ticket (A-024), checks active contract exists.
- [ ] T-5: Write `effort/dal.py` with `get_effort_for_ticket`, `get_effort_for_contract` queries.
- [ ] T-6: Write `effort/views.py` with POST `/api/effort/` (assigned engineer only).
- [ ] T-7: Write `effort/urls.py`; register in root `urls.py`.
- [ ] T-8: Update `TicketDetail.tsx` with effort entry form (assigned engineer only).
- [ ] T-9: Write `src/frontend/src/api/effort.ts` with typed API calls.
- [ ] T-10: Test: AC-3 creates an audit entry; stub audit write until FEAT-032 is merged.
- [ ] T-11: Run all gate commands locally; confirm each exits 0.
- [ ] T-12: Verify `python3 scripts/check_feature_size.py size FEAT-027` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-027 plan.md; REQ-001 v0.3 § S-15; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-027-TESTS (Phase 6 test set)

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
