---
id: FEAT-031-TASKS
id_prefix: FEAT
title: "FEAT-031: S-26: Delivery Manager Corrects an Effort Entry â€” Tasks"
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
# FEAT-031: S-26: Delivery Manager Corrects an Effort Entry â€” Tasks

## Input References
- FEAT-031 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-26 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-031. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `dm_correct_effort(entry_id, dm_user, new_hours)` to `effort/services.py`: DM-only, no month-end restriction, validates new_hours > 0, DM cannot delete (AC-4).
- [ ] T-2: Add PATCH `/api/effort/{id}/dm-correct/` to `effort/views.py` (DM-only).
- [ ] T-3: Update `effort/serializers.py` with `DMCorrectSerializer`.
- [ ] T-4: Update `effort/dal.py` with update query.
- [ ] T-5: Update `effort/urls.py`.
- [ ] T-6: Update `EffortReview.tsx` with DM edit control (no delete button for DM).
- [ ] T-7: Update `src/frontend/src/api/effort.ts` with `dmCorrectEffort(id, hours)` call.
- [ ] T-8: Run all gate commands locally; confirm each exits 0.
- [ ] T-9: Verify `python3 scripts/check_feature_size.py size FEAT-031` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-031 plan.md; REQ-001 v0.3 Â§ S-26; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
