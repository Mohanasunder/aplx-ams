---
id: FEAT-029
id_prefix: FEAT
title: "FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export — Tasks"
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
# FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export — Tasks

## Input References
- FEAT-029 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-17 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-029. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `generate_finance_export(year, month)` to `reports/services.py`: queries effort entries recorded in that month; computes per-org balance at month end (A-011); builds row list per BR B-18.
- [ ] T-2: Add Excel export variant using `XlsxWriter` with formula-escape rule (STD-001).
- [ ] T-3: Add CSV export variant using Python `csv` standard library.
- [ ] T-4: Add GET `/api/reports/finance-export/` with `month` and `format` query params to `reports/views.py`; DM-only.
- [ ] T-5: Update `reports/urls.py`.
- [ ] T-6: Write `src/frontend/src/pages/FinanceExport.tsx` with month picker and Excel/CSV download buttons.
- [ ] T-7: Update `src/frontend/src/api/reports.ts` with `downloadFinanceExport(month, format)` call.
- [ ] T-8: Run all gate commands locally; confirm each exits 0.
- [ ] T-9: Verify `python3 scripts/check_feature_size.py size FEAT-029` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-029 plan.md; REQ-001 v0.3 § S-17; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-029-TESTS (Phase 6 test set)

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
