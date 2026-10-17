---
id: FEAT-024
id_prefix: FEAT
title: "FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard"
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
# FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-12
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-12: S-12: Delivery Manager Monitors the Live Dashboard. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-12 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-021

## Inputs And Contracts
- REQ-001 v0.3 § S-12 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-12
- API-001 v0.1 § Service reporting and dashboards (F-3)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Service reporting and dashboards (F-3)
- UIS-001 v0.1 § REQ S-12 — Delivery manager monitors the live dashboard

## Files To Create Or Modify
- `src/aplx_ams_django/reports/migrations/0001_initial.py`
- `src/aplx_ams_django/reports/services.py`
- `src/aplx_ams_django/reports/views.py`
- `src/aplx_ams_django/reports/urls.py`
- `src/aplx_ams_django/settings/base.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/Dashboard.tsx`
- `src/frontend/src/api/reports.ts`

## New Packages
- None

## Out Of Scope
Monthly client report generation — FEAT-025. Finance export — FEAT-029. Report download — FEAT-026.

## Risk Tier
Tier: Standard
Read-only dashboard; incorrect count queries show wrong SLA data to the DM.

## Implementation Steps
1. Create `src/aplx_ams_django/reports/` app; write empty `migrations/0001_initial.py`; add 'reports' to INSTALLED_APPS in `settings/base.py`.
2. Write `reports/services.py` with `compute_dashboard()`: queries tickets (open counts, at-risk, breached, escalation flag per org per SAP app) and contracts (hours bank balance) — all computed on-read.
3. Write `reports/views.py` with `GET /api/reports/dashboard/` (DM, L1, L2/L3 only; client user refused).
4. Write `reports/urls.py`; register in root `urls.py`.
5. Write `src/frontend/src/pages/Dashboard.tsx` with MUI DataGrid showing per-org/per-app SLA counts and balance.
6. Write `src/frontend/src/api/reports.ts` with typed `getDashboard()` call.

## Test Plan
REQ-012 AC-1 REQ S-12 AC-1: Given open tickets in client organizations A and B, when the delivery manager views the live dashboa...
REQ-012 AC-2 REQ S-12 AC-2: Given a ticket's SLA timer changes from on track to at risk, when the delivery manager next views th...
REQ-012 AC-3 REQ S-12 AC-3: Given client organization A has an hours bank contract, when the delivery manager views the live das...
REQ-012 AC-4 REQ S-12 AC-4: Given a client user, when they try to view the live dashboard, then access is refused.
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 8 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-024` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-024-ACC.

## Risks
- Dashboard is computed on-read with no stored aggregate table; all counts query tickets directly. Performance is acceptable for release 1 (no > 1000 open tickets expected).

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-12; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-024-TASKS; FEAT-024-ACC; FEAT-024-STATUS; Phase 6 PR

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
