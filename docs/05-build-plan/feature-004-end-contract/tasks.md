---
id: FEAT-004-TASKS
id_prefix: FEAT
title: "FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One â€” Tasks"
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
# FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One â€” Tasks

## Input References
- FEAT-004 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-27 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-004. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `end_contract(contract_id)` to `services.py`: sets `is_active=False`, preserves effort entries and balance.
- [ ] T-2: Add PATCH `/api/contracts/{id}/end/` action to `views.py`; DM-only.
- [ ] T-3: Add `get_effort_entries_for_contract` query to `dal.py`.
- [ ] T-4: Update `ContractSerializer` to expose `is_active`, `ended_at` fields in `serializers.py`.
- [ ] T-5: Register end-contract URL in `urls.py`.
- [ ] T-6: Update `src/frontend/src/pages/ContractSetup.tsx` with 'End contract' button (DM-only, confirmed dialog).
- [ ] T-7: Update `src/frontend/src/api/contracts.ts` with `endContract(id)` call.
- [ ] T-8: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-9: Verify `python3 scripts/check_feature_size.py size FEAT-004` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-004 plan.md; REQ-001 v0.3 Â§ S-27; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
