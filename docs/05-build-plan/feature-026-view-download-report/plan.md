---
id: FEAT-026
id_prefix: FEAT
title: "FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report"
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
# FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-14
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-14: S-14: Client User Views and Downloads the Monthly Client Report. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-14 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-025

## Inputs And Contracts
- REQ-001 v0.3 § S-14 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-14
- API-001 v0.1 § Service reporting and dashboards (F-3)
- DBD-001 v0.1 § Module: reports
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Service reporting and dashboards (F-3)
- UIS-001 v0.1 § REQ S-14 — Client user views and downloads the monthly client report

## Files To Create Or Modify
- `src/aplx_ams_django/reports/views.py`
- `src/aplx_ams_django/reports/serializers.py`
- `src/aplx_ams_django/reports/urls.py`
- `src/aplx_ams_django/reports/services.py`
- `src/frontend/src/pages/ReportList.tsx`
- `src/frontend/src/pages/ReportDetail.tsx`
- `src/frontend/src/api/reports.ts`

## New Packages
- pypi: XlsxWriter >=3.2,<4 | BSD-2-Clause | Excel export for monthly client report and finance export (ADR A-12; A-029); alternatives: openpyxl (not approved)
- pypi: WeasyPrint >=62,<63 | BSD-3-Clause | PDF generation for monthly client report (ADR A-12; A-029); alternatives: reportlab (not approved)

## Out Of Scope
Report generation — FEAT-025. Finance export — FEAT-029.

## Risk Tier
Tier: Standard
Client report visibility; published flag prevents premature disclosure.

## Implementation Steps
1. Add `publish_report(report_id)` to `reports/services.py`; DM-only; sets published=True.
2. Add Excel export `export_report_excel(report)` using `XlsxWriter` to `reports/services.py`; prefix formula-starting values with `'` (STD-001 § Security Rules).
3. Add PDF export `export_report_pdf(report)` using `WeasyPrint` to `reports/services.py`.
4. Add GET `/api/reports/{id}/` (published reports only for client users), PATCH publish, GET download (Excel/PDF) to `reports/views.py`.
5. Update `reports/serializers.py`; update `reports/urls.py`.
6. Write `src/frontend/src/pages/ReportList.tsx` with list of published reports (client users); all reports (DM).
7. Write `src/frontend/src/pages/ReportDetail.tsx` showing report data; download buttons.
8. Update `src/frontend/src/api/reports.ts` with `getReport`, `downloadReport` calls.

## Test Plan
REQ-014 AC-1 REQ S-14 AC-1: Given the monthly client report for September 2026 is published for client organization A, when a cl...
REQ-014 AC-2 REQ S-14 AC-2: Given that report, when the client user downloads it as Excel and as PDF, then each file holds the s...
REQ-014 AC-3 REQ S-14 AC-3: Given a client user of client organization A, when they try to open client organization B's monthly ...
REQ-014 AC-4 REQ S-14 AC-4: Given the September 2026 report for organization A is generated but not yet published, when a client...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-026` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-026-ACC.

## Risks
- Export formula escaping must be applied per STD-001 § Security Rules: any cell value starting with `=`, `+`, `-`, `@` must be prefixed with `'`.
- WeasyPrint requires system fonts; the Docker image must install font packages in Dockerfile.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-14; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-026-TASKS; FEAT-026-ACC; FEAT-026-STATUS; Phase 6 PR

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
