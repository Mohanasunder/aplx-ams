---
id: FEAT-031
id_prefix: FEAT
title: "FEAT-031: S-26: Delivery Manager Corrects an Effort Entry"
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
# FEAT-031: S-26: Delivery Manager Corrects an Effort Entry

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-26
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-26: S-26: Delivery Manager Corrects an Effort Entry. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-26 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-027

## Inputs And Contracts
- REQ-001 v0.3 § S-26 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-26
- API-001 v0.1 § Effort tracking (F-4)
- DBD-001 v0.1 § Module: effort
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Effort tracking (F-4)
- UIS-001 v0.1 § REQ S-26 — Delivery manager corrects an effort entry

## Files To Create Or Modify
- `src/aplx_ams_django/effort/services.py`
- `src/aplx_ams_django/effort/views.py`
- `src/aplx_ams_django/effort/serializers.py`
- `src/aplx_ams_django/effort/dal.py`
- `src/aplx_ams_django/effort/urls.py`
- `src/frontend/src/pages/EffortReview.tsx`
- `src/frontend/src/api/effort.ts`

## New Packages
- None

## Out Of Scope
Engineer editing own effort — FEAT-030. Audit trail display — FEAT-032.

## Risk Tier
Tier: High
DM can correct any effort entry including after month end; incorrect logic corrupts historical data.

## Implementation Steps
1. Add `dm_correct_effort(entry_id, dm_user, new_hours)` to `effort/services.py`: DM-only, no month-end restriction, validates new_hours > 0, DM cannot delete (AC-4).
2. Add PATCH `/api/effort/{id}/dm-correct/` to `effort/views.py` (DM-only).
3. Update `effort/serializers.py` with `DMCorrectSerializer`.
4. Update `effort/dal.py` with update query.
5. Update `effort/urls.py`.
6. Update `EffortReview.tsx` with DM edit control (no delete button for DM).
7. Update `src/frontend/src/api/effort.ts` with `dmCorrectEffort(id, hours)` call.

## Test Plan
REQ-026 AC-1 REQ S-26 AC-1: Given support engineer X recorded an effort entry of 2 hours dated 2026-10-15 on an hours bank contr...
REQ-026 AC-2 REQ S-26 AC-2: Given the delivery manager correcting an effort entry, when the hours are 0 or negative, then the ch...
REQ-026 AC-3 REQ S-26 AC-3: Given a client user, when they try to change any effort entry, then the change is refused (BR B-15).
REQ-026 AC-4 REQ S-26 AC-4: Given an effort entry recorded by support engineer X, when the delivery manager tries to delete it, ...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-031` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-031-ACC.

## Risks
- AC-4: DM cannot delete effort entries (confirmed, Phase 2 review answers, 2026-10-17); the view must return 405 for DELETE requests by DM.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-26; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-031-TASKS; FEAT-031-ACC; FEAT-031-STATUS; Phase 6 PR

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
