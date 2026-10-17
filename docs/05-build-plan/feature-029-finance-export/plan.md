---
id: FEAT-029
id_prefix: FEAT
title: "FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export"
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
# FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-17
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-17: S-17: Delivery Manager Produces the Monthly Finance Export. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-17 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-028

## Inputs And Contracts
- REQ-001 v0.3 § S-17 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-17
- API-001 v0.1 § Finance export (F-8)
- DBD-001 v0.1 § Module: effort
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Finance export (F-8)
- UIS-001 v0.1 § REQ S-17 — Delivery manager produces the monthly finance export

## Files To Create Or Modify
- `src/aplx_ams_django/reports/views.py`
- `src/aplx_ams_django/reports/services.py`
- `src/aplx_ams_django/reports/urls.py`
- `src/frontend/src/pages/FinanceExport.tsx`
- `src/frontend/src/api/reports.ts`

## New Packages
- pypi: XlsxWriter >=3.2,<4 | BSD-2-Clause | Excel export for finance export (ADR A-12; A-029); first used in FEAT-026

## Out Of Scope
Monthly client report download — FEAT-026. Emailing the export to finance — out of scope for release 1 (OQ-038).

## Risk Tier
Tier: High
Finance export is the source of billing data; incorrect rows, balances, or format cause financial errors.

## Implementation Steps
1. Add `generate_finance_export(year, month)` to `reports/services.py`: queries effort entries recorded in that month; computes per-org balance at month end (A-011); builds row list per BR B-18.
2. Add Excel export variant using `XlsxWriter` with formula-escape rule (STD-001).
3. Add CSV export variant using Python `csv` standard library.
4. Add GET `/api/reports/finance-export/` with `month` and `format` query params to `reports/views.py`; DM-only.
5. Update `reports/urls.py`.
6. Write `src/frontend/src/pages/FinanceExport.tsx` with month picker and Excel/CSV download buttons.
7. Update `src/frontend/src/api/reports.ts` with `downloadFinanceExport(month, format)` call.

## Test Plan
REQ-017 AC-1 REQ S-17 AC-1: Given effort entries recorded in October 2026, when the delivery manager produces the October 2026 f...
REQ-017 AC-2 REQ S-17 AC-2: Given an effort entry on a fixed fee contract, when it appears in the finance export, then its hours...
REQ-017 AC-3 REQ S-17 AC-3: Given client organization A's hours bank balance at the end of October 2026 is 70 hours, when the Oc...
REQ-017 AC-4 REQ S-17 AC-4: Given the finance export is produced, when the delivery manager downloads it as Excel or as CSV, the...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 5 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-029` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-029-ACC.

## Risks
- A-011 (Confirmed): balance at month end is `contracted_hours - sum(hours in and before that month)`.
- XlsxWriter is first introduced in FEAT-026; builder must ensure it is in requirements.txt before this feature's branch.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-17; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-029-TASKS; FEAT-029-ACC; FEAT-029-STATUS; Phase 6 PR

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
