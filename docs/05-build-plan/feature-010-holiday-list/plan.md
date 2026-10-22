---
id: FEAT-010
id_prefix: FEAT
title: "FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List"
phase: 5
version: 0.5
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
# FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.4 — APLX AMS: User Stories (Approved 2026-10-17) § S-24
- API-001 v0.3 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)
- SCR S-22 (Approved 2026-10-21) — adds Django boilerplate files and test file to Files To Create Or Modify; corrects Size Check limit
- SCR S-23 (Approved 2026-10-21) — adds conftest.py to Tests file list
- SCR S-24 (Approved 2026-10-21) — adds test_holiday_api.py and HolidayList.test.tsx to Tests file list; closes OQ-076
- SCR S-25 (Approved 2026-10-22) — adds App.tsx to Frontend source files; Size Check 14→15

## Purpose And Scope
Implements REQ S-24: S-24: Delivery Manager Maintains the Company Holiday List. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-24 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-006

## Inputs And Contracts
- REQ-001 v0.4 § S-24 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.3 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.4 § S-24
- API-001 v0.3 § Company holiday list (SLA timers — F-2 support)
- DBD-001 v0.1 § Module: sla
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Company holiday list (F-2 support)
- UIS-001 v0.1 § REQ S-24 — Delivery manager maintains the company holiday list

## Files To Create Or Modify

**Django app boilerplate (create)**
- `src/aplx_ams_django/sla/__init__.py`
- `src/aplx_ams_django/sla/apps.py`
- `src/aplx_ams_django/sla/migrations/__init__.py`
- `src/aplx_ams_django/settings/base.py` (modify — add `'aplx_ams_django.sla'` to INSTALLED_APPS)

**Backend (source files)**
- `src/aplx_ams_django/sla/models.py`
- `src/aplx_ams_django/sla/migrations/0001_initial.py`
- `src/aplx_ams_django/sla/serializers.py`
- `src/aplx_ams_django/sla/services.py`
- `src/aplx_ams_django/sla/dal.py`
- `src/aplx_ams_django/sla/views.py`
- `src/aplx_ams_django/sla/urls.py`
- `src/aplx_ams_django/urls.py`

**Frontend (source files)**
- `src/frontend/src/pages/HolidayList.tsx`
- `src/frontend/src/api/holidays.ts`
- `src/frontend/src/App.tsx` (modify — add `/admin/holidays` route for HolidayList; protected by DM role guard)

**Tests**
- `src/aplx_ams_django/sla/tests/__init__.py`
- `src/aplx_ams_django/sla/tests/conftest.py` (new — pytest fixtures: SQLite switch + sla app registry injection)
- `src/aplx_ams_django/sla/tests/test_holiday_list.py` (new — pytest DB/DAL tests for AC-1, AC-2, AC-4)
- `src/aplx_ams_django/sla/tests/test_holiday_api.py` (new — pytest API tests for AC-1, AC-2, AC-3)
- `src/frontend/src/pages/HolidayList.test.tsx` (new — Vitest component tests for AC-3 permission guard and DM controls)

## New Packages
- None

## Out Of Scope
SLA timer computation — FEAT-019. SLA states — FEAT-020. Escalation flag — FEAT-021. The holiday change applies from the time of change onward; no recalculation of past elapsed time (OQ-050, confirmed).

## Risk Tier
Tier: Standard
Holiday list affects SLA timer computation; incorrect data causes wrong business hours, but the risk is limited to SLA reporting accuracy.

## Implementation Steps
1. Create `src/aplx_ams_django/sla/` app with `models.py` defining `HolidayEntry` (date, description) per DBD-001.
2. Generate `sla/migrations/0001_initial.py`.
3. Write `serializers.py` for `HolidayEntry`.
4. Write `services.py` with `add_holiday`, `remove_holiday`, `is_holiday(date)` functions.
5. Write `dal.py` with `get_holidays_in_range(start, end)` query.
6. Write `views.py` with `HolidayEntryViewSet` (DM-only write; all authenticated users read).
7. Write `urls.py` registering holiday endpoints.
8. Register `sla.urls` in root `urls.py`.
9. Write `src/frontend/src/pages/HolidayList.tsx` with MUI calendar/list; DM-only add/remove.
10. Write `src/frontend/src/api/holidays.ts` with typed API calls.

## Test Plan
REQ-024 AC-1 REQ S-24 AC-1: Given the delivery manager adds 2027-01-26 (a Tuesday) to the company holiday li...
REQ-024 AC-2 REQ S-24 AC-2: Given 2027-03-15 (a Monday) was on the company holiday list, when the delivery m...
REQ-024 AC-3 REQ S-24 AC-3: Given an L1 support engineer, an L2/L3 support engineer or a client user, when t...
REQ-024 AC-4 REQ S-24 AC-4: Given a P3 ticket raised at 09:00 IST on Monday 2027-02-01 whose resolution cloc...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 15 | 30 |
| Test files | 2 | — |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-010` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-010-ACC.

## Risks
- AC-4: holiday added mid-day; SLA service must check holiday status at query time, not cache it. Tests use `freezegun` to control time.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.4 § S-24; API-001 v0.3; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-010-TASKS; FEAT-010-ACC; FEAT-010-STATUS; Phase 6 PR

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
| Version | 0.5 |
| Conditions | None |
| Comments | SCR S-25 applied: added App.tsx to Frontend source files; Size Check 14->15. |
| Timestamp | 2026-10-21 18:51 UTC |
