---
id: FEAT-025-TASKS
id_prefix: FEAT
title: "FEAT-025: S-13: Delivery Manager Generates the Monthly Client Report â€” Tasks"
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
# FEAT-025: S-13: Delivery Manager Generates the Monthly Client Report â€” Tasks

## Input References
- FEAT-025 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-13 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-025. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `MonthlyClientReport` model to `reports/models.py` (org FK, year, month, data JSONB, published bool, generated_at) per DBD-001.
- [ ] T-2: Generate `reports/migrations/0002_monthlyclientreport.py`.
- [ ] T-3: Write `reports/serializers.py` with `MonthlyClientReportSerializer`.
- [ ] T-4: Add `generate_report(org_id, year, month)` to `reports/services.py`: queries tickets resolved in given month, computes response %, resolution %, MTTR (BR B-12, B-13), breached list (BR B-14); A-015 counts by resolution month not raise month.
- [ ] T-5: Write `reports/dal.py` with `get_tickets_resolved_in_month`, `get_tickets_raised_in_month`.
- [ ] T-6: Add POST `/api/reports/generate/` and GET `/api/reports/` to `reports/views.py`; DM-only generate.
- [ ] T-7: Update `reports/urls.py`.
- [ ] T-8: Write `src/frontend/src/pages/GenerateReport.tsx` with org picker, month/year picker, Generate button.
- [ ] T-9: Run all gate commands locally; confirm each exits 0.
- [ ] T-10: Verify `python3 scripts/check_feature_size.py size FEAT-025` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-025 plan.md; REQ-001 v0.3 Â§ S-13; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
