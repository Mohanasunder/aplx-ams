---
id: FEAT-030
id_prefix: FEAT
title: "FEAT-030: S-25: Support Engineer Changes or Deletes Their Own Effort Entry"
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
# FEAT-030: S-25: Support Engineer Changes or Deletes Their Own Effort Entry

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-25
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-25: S-25: Support Engineer Changes or Deletes Their Own Effort Entry. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-25 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-027

## Inputs And Contracts
- REQ-001 v0.3 § S-25 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-25
- API-001 v0.1 § Effort tracking (F-4)
- DBD-001 v0.1 § Module: effort
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Effort tracking (F-4)
- UIS-001 v0.1 § REQ S-25 — Support engineer changes or deletes their own effort entry

## Files To Create Or Modify
- `src/aplx_ams_django/effort/services.py`
- `src/aplx_ams_django/effort/views.py`
- `src/aplx_ams_django/effort/serializers.py`
- `src/aplx_ams_django/effort/dal.py`
- `src/aplx_ams_django/effort/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`
- `src/frontend/src/api/effort.ts`

## New Packages
- None

## Out Of Scope
DM correcting effort (cross-month) — FEAT-031. Audit trail display — FEAT-032.

## Risk Tier
Tier: High
Effort entry modification affects hours bank balance; incorrect month-end lock corrupts financial data.

## Implementation Steps
1. Add `update_own_effort(entry_id, engineer, new_hours)` and `delete_own_effort(entry_id, engineer)` to `effort/services.py`: validate same engineer, validate effort date is in current calendar month (A-025), validate new_hours > 0; soft-delete sets is_deleted=True.
2. Add PATCH and DELETE `/api/effort/{id}/` to `effort/views.py` (assigned engineer, own entry only).
3. Update `effort/serializers.py` with `EffortUpdateSerializer`.
4. Add `get_effort_by_id` to `effort/dal.py`.
5. Update `effort/urls.py`.
6. Update `TicketDetail.tsx` with edit/delete buttons on own effort entries (same month only).
7. Update `src/frontend/src/api/effort.ts` with `updateEffort`, `deleteEffort` calls.

## Test Plan
REQ-025 AC-1 REQ S-25 AC-1: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X changes it t...
REQ-025 AC-2 REQ S-25 AC-2: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X deletes it o...
REQ-025 AC-3 REQ S-25 AC-3: Given an effort entry of X dated 2026-11-02, when X tries to change or delete it on 2026-12-01, then...
REQ-025 AC-4 REQ S-25 AC-4: Given an effort entry recorded by support engineer X, when support engineer Y tries to change or del...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 7 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-030` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-030-ACC.

## Risks
- A-025 (Confirmed): 'end of that month' is end of the calendar month of the effort entry date, NOT the current month. Use `freezegun` to simulate cross-month access.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-25; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-030-TASKS; FEAT-030-ACC; FEAT-030-STATUS; Phase 6 PR

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
