---
id: FEAT-027
id_prefix: FEAT
title: "FEAT-027: S-15: Support Engineer Records Effort on a Ticket"
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
# FEAT-027: S-15: Support Engineer Records Effort on a Ticket

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-15
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-15: S-15: Support Engineer Records Effort on a Ticket. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-15 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-003
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-15 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-15
- API-001 v0.1 § Effort tracking (F-4)
- DBD-001 v0.1 § Module: effort
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Effort tracking (F-4)
- UIS-001 v0.1 § REQ S-15 — Support engineer records effort on a ticket

## Files To Create Or Modify
- `src/aplx_ams_django/effort/models.py`
- `src/aplx_ams_django/effort/migrations/0001_initial.py`
- `src/aplx_ams_django/effort/serializers.py`
- `src/aplx_ams_django/effort/services.py`
- `src/aplx_ams_django/effort/dal.py`
- `src/aplx_ams_django/effort/views.py`
- `src/aplx_ams_django/effort/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`
- `src/frontend/src/api/effort.ts`

## New Packages
- None

## Out Of Scope
Engineer editing own effort — FEAT-030. DM correcting effort — FEAT-031. Effort review against contract — FEAT-028. Finance export — FEAT-029.

## Risk Tier
Tier: High
Effort entries directly affect hours bank balance and finance export; incorrect validation corrupts contract data.

## Implementation Steps
1. Create `src/aplx_ams_django/effort/` app with `models.py` defining `EffortEntry` (ticket FK, engineer FK, date, hours, is_deleted bool, created_at) per DBD-001 (soft-delete A-039).
2. Generate `effort/migrations/0001_initial.py`.
3. Write `effort/serializers.py` with `EffortEntryCreateSerializer`.
4. Write `effort/services.py` with `record_effort(ticket_id, engineer, date, hours)`: validates hours > 0, validates engineer is assigned to ticket (A-024), checks active contract exists.
5. Write `effort/dal.py` with `get_effort_for_ticket`, `get_effort_for_contract` queries.
6. Write `effort/views.py` with POST `/api/effort/` (assigned engineer only).
7. Write `effort/urls.py`; register in root `urls.py`.
8. Update `TicketDetail.tsx` with effort entry form (assigned engineer only).
9. Write `src/frontend/src/api/effort.ts` with typed API calls.
10. Test: AC-3 creates an audit entry; stub audit write until FEAT-032 is merged.

## Test Plan
REQ-015 AC-1 REQ S-15 AC-1: Given a ticket of client organization A with an active contract, assigned to a support engineer, whe...
REQ-015 AC-2 REQ S-15 AC-2: Given a support engineer recording effort, when the hours are 0 or negative, then the effort entry i...
REQ-015 AC-3 REQ S-15 AC-3: Given an effort entry is saved, when the audit trail of the ticket is viewed, then it holds the new ...
REQ-015 AC-4 REQ S-15 AC-4: Given a ticket assigned to an L2/L3 support engineer X, when a different support engineer or a clien...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-027` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-027-ACC.

## Risks
- A-039 (Confirmed): soft-delete is implemented with `is_deleted=True`; all effort queries must filter `is_deleted=False` by default.
- A-020 (Open): hours must be strictly > 0; zero and negative rejected.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-15; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-027-TASKS; FEAT-027-ACC; FEAT-027-STATUS; Phase 6 PR

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
