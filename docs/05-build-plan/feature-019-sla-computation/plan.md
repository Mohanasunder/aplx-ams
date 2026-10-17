---
id: FEAT-019
id_prefix: FEAT
title: "FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA"
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-9
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-9: S-9: SLA Timers Count Business Hours Against the Standard SLA. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-9 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-9 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-9
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: sla
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-10 — Support engineer sees SLA timer states

## Files To Create Or Modify
- `src/aplx_ams_django/sla/services.py`
- `src/aplx_ams_django/sla/dal.py`
- `src/aplx_ams_django/tickets/services.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/frontend/src/pages/TicketDetail.tsx`
- `src/frontend/src/api/tickets.ts`

## New Packages
- None

## Out Of Scope
SLA state (on track, at risk, breached, met) — FEAT-020. Escalation flag — FEAT-021. Awaiting client pause — FEAT-018 (already handled). Monthly report computation — FEAT-025.

## Risk Tier
Tier: Standard
Business-hours SLA computation is the core of IS-1; incorrect computation corrupts all SLA metrics.

## Implementation Steps
1. Expand `sla/services.py` with `compute_elapsed_business_hours(start_dt, end_dt, holiday_dates)`: counts only IST business hours (09:00–18:00, Mon–Fri) excluding holiday dates.
2. Add `get_holidays_as_set(start_date, end_date)` to `sla/dal.py` for fast lookup.
3. Update `tickets/services.py` to call `compute_elapsed_business_hours` when computing response/resolution due times.
4. Update `tickets/serializers.py` to include computed `response_elapsed_hours` and `resolution_elapsed_hours` (on-read, ADR A-10).
5. Update `tickets/views.py` ticket detail endpoint to include SLA computed fields.
6. Update `TicketDetail.tsx` to display response/resolution elapsed and due times.
7. Update `tickets.ts` API types with new SLA fields.
8. Write `sla/tests/test_sla_computation.py` with `freezegun` for AC-1 through AC-4.

## Test Plan
REQ-009 AC-1 REQ S-9 AC-1: Given a P1 ticket raised at 17:30 IST on Friday, when the next business day starts, then the respons...
REQ-009 AC-2 REQ S-9 AC-2: Given a P3 ticket raised at 10:00 IST on the business day before a date on the company holiday list,...
REQ-009 AC-3 REQ S-9 AC-3: Given tickets of P1, P2, P3 and P4, when they are raised, then their response and resolution targets...
REQ-009 AC-4 REQ S-9 AC-4: Given a ticket raised at 08:00 IST on a business day, when the clocks start, then elapsed business t...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 7 | 10 |

Expected test runtime: 6 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-019` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-019-ACC.

## Risks
- ADR A-10: SLA timers are computed on-read, not stored as running values; the serializer must not persist computed elapsed hours to the database.
- `freezegun` must set time in IST (UTC+5:30); use `pytz` or `zoneinfo` for timezone handling.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-9; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-019-TASKS; FEAT-019-ACC; FEAT-019-STATUS; Phase 6 PR

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
| Comments | Phase 5 validation passed (VAL-023). |
| Timestamp | 2026-10-17 16:50 UTC |
