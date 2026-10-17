---
id: FEAT-025
id_prefix: FEAT
title: "FEAT-025: S-13: Delivery Manager Generates the Monthly Client Report"
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
# FEAT-025: S-13: Delivery Manager Generates the Monthly Client Report

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-13
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-13: S-13: Delivery Manager Generates the Monthly Client Report. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-13 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-024

## Inputs And Contracts
- REQ-001 v0.3 § S-13 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-13
- API-001 v0.1 § Service reporting and dashboards (F-3)
- DBD-001 v0.1 § Module: reports
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Service reporting and dashboards (F-3)
- UIS-001 v0.1 § REQ S-13 — Delivery manager generates the monthly client report

## Files To Create Or Modify
- `src/aplx_ams_django/reports/models.py`
- `src/aplx_ams_django/reports/migrations/0002_monthlyclientreport.py`
- `src/aplx_ams_django/reports/serializers.py`
- `src/aplx_ams_django/reports/services.py`
- `src/aplx_ams_django/reports/dal.py`
- `src/aplx_ams_django/reports/views.py`
- `src/aplx_ams_django/reports/urls.py`
- `src/frontend/src/pages/GenerateReport.tsx`

## New Packages
- None

## Out Of Scope
Client report viewing and download — FEAT-026. Finance export — FEAT-029. Dashboard — FEAT-024.

## Risk Tier
Tier: High
Monthly client report is the primary SLA deliverable; incorrect % or MTTR calculation is a contractual risk.

## Implementation Steps
1. Add `MonthlyClientReport` model to `reports/models.py` (org FK, year, month, data JSONB, published bool, generated_at) per DBD-001.
2. Generate `reports/migrations/0002_monthlyclientreport.py`.
3. Write `reports/serializers.py` with `MonthlyClientReportSerializer`.
4. Add `generate_report(org_id, year, month)` to `reports/services.py`: queries tickets resolved in given month, computes response %, resolution %, MTTR (BR B-12, B-13), breached list (BR B-14); A-015 counts by resolution month not raise month.
5. Write `reports/dal.py` with `get_tickets_resolved_in_month`, `get_tickets_raised_in_month`.
6. Add POST `/api/reports/generate/` and GET `/api/reports/` to `reports/views.py`; DM-only generate.
7. Update `reports/urls.py`.
8. Write `src/frontend/src/pages/GenerateReport.tsx` with org picker, month/year picker, Generate button.

## Test Plan
REQ-013 AC-1 REQ S-13 AC-1: Given in September 2026 client organization A had 20 P2 tickets whose resolution clock stopped, 18 w...
REQ-013 AC-2 REQ S-13 AC-2: Given in September 2026 client organization A had no P1 tickets whose clocks stopped, when the deliv...
REQ-013 AC-3 REQ S-13 AC-3: Given the generated September 2026 report for organization A, in which exactly 2 tickets were set to...
REQ-013 AC-4 REQ S-13 AC-4: Given a ticket raised in September 2026 and set to Resolved in October 2026, when the delivery manag...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 8 | 10 |

Expected test runtime: 6 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-025` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-025-ACC.

## Risks
- A-015 (Open): counts by month of resolution_stopped_at, not raise_time; builder must use `resolution_stopped_at` as the month filter.
- A-021 (Open): zero denominator shows 'no tickets'; builder must handle division-by-zero in service.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-13; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-025-TASKS; FEAT-025-ACC; FEAT-025-STATUS; Phase 6 PR

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
