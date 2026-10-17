---
id: FEAT-024
id_prefix: FEAT
title: "FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard — Tasks"
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
# FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard — Tasks

## Input References
- FEAT-024 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-12 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-024. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/reports/` app; write empty `migrations/0001_initial.py`; add 'reports' to INSTALLED_APPS in `settings/base.py`.
- [ ] T-2: Write `reports/services.py` with `compute_dashboard()`: queries tickets (open counts, at-risk, breached, escalation flag per org per SAP app) and contracts (hours bank balance) — all computed on-read.
- [ ] T-3: Write `reports/views.py` with `GET /api/reports/dashboard/` (DM, L1, L2/L3 only; client user refused).
- [ ] T-4: Write `reports/urls.py`; register in root `urls.py`.
- [ ] T-5: Write `src/frontend/src/pages/Dashboard.tsx` with MUI DataGrid showing per-org/per-app SLA counts and balance.
- [ ] T-6: Write `src/frontend/src/api/reports.ts` with typed `getDashboard()` call.
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-024` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-024 plan.md; REQ-001 v0.3 § S-12; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-024-TESTS (Phase 6 test set)

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
