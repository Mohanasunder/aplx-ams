---
id: FEAT-010-TASKS
id_prefix: FEAT
title: "FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List â€” Tasks"
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
# FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List â€” Tasks

## Input References
- FEAT-010 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-24 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-010. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/sla/` app with `models.py` defining `HolidayEntry` (date, description) per DBD-001.
- [ ] T-2: Generate `sla/migrations/0001_initial.py`.
- [ ] T-3: Write `serializers.py` for `HolidayEntry`.
- [ ] T-4: Write `services.py` with `add_holiday`, `remove_holiday`, `is_holiday(date)` functions.
- [ ] T-5: Write `dal.py` with `get_holidays_in_range(start, end)` query.
- [ ] T-6: Write `views.py` with `HolidayEntryViewSet` (DM-only write; all authenticated users read).
- [ ] T-7: Write `urls.py` registering holiday endpoints.
- [ ] T-8: Register `sla.urls` in root `urls.py`.
- [ ] T-9: Write `src/frontend/src/pages/HolidayList.tsx` with MUI calendar/list; DM-only add/remove.
- [ ] T-10: Write `src/frontend/src/api/holidays.ts` with typed API calls.
- [ ] T-11: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-12: Verify `python3 scripts/check_feature_size.py size FEAT-010` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-010 plan.md; REQ-001 v0.3 Â§ S-24; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
