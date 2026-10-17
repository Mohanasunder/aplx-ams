---
id: FEAT-026-TASKS
id_prefix: FEAT
title: "FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report â€” Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report â€” Tasks

## Input References
- FEAT-026 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-14 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-026. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `publish_report(report_id)` to `reports/services.py`; DM-only; sets published=True.
- [ ] T-2: Add Excel export `export_report_excel(report)` using `XlsxWriter` to `reports/services.py`; prefix formula-starting values with `'` (STD-001 Â§ Security Rules).
- [ ] T-3: Add PDF export `export_report_pdf(report)` using `WeasyPrint` to `reports/services.py`.
- [ ] T-4: Add GET `/api/reports/{id}/` (published reports only for client users), PATCH publish, GET download (Excel/PDF) to `reports/views.py`.
- [ ] T-5: Update `reports/serializers.py`; update `reports/urls.py`.
- [ ] T-6: Write `src/frontend/src/pages/ReportList.tsx` with list of published reports (client users); all reports (DM).
- [ ] T-7: Write `src/frontend/src/pages/ReportDetail.tsx` showing report data; download buttons.
- [ ] T-8: Update `src/frontend/src/api/reports.ts` with `getReport`, `downloadReport` calls.
- [ ] T-9: Run all gate commands locally; confirm each exits 0.
- [ ] T-10: Verify `python3 scripts/check_feature_size.py size FEAT-026` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-026 plan.md; REQ-001 v0.3 Â§ S-14; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: Phase 6 test set (created in Phase 6)

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
| Comments | None |
| Timestamp | 2026-10-17 18:47 UTC |
