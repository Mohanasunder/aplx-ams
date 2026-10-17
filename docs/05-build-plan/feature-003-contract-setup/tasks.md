---
id: FEAT-003-TASKS
id_prefix: FEAT
title: "FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract â€” Tasks"
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
# FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract â€” Tasks

## Input References
- FEAT-003 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-19 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-003. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `Contract` model to `organizations/models.py` (type: hours_bank or fixed_fee, contracted_hours nullable, is_active flag, org FK) per DBD-001.
- [ ] T-2: Generate `organizations/migrations/0002_contract.py`.
- [ ] T-3: Add `ContractSerializer` to `serializers.py` with validation: only one active contract per org.
- [ ] T-4: Add `create_contract`, `get_active_contract` to `services.py`.
- [ ] T-5: Add contract DAL queries to `dal.py`.
- [ ] T-6: Add `ContractViewSet` (DM-only write) to `views.py`.
- [ ] T-7: Register contract endpoints in `urls.py`.
- [ ] T-8: Write `src/frontend/src/pages/ContractSetup.tsx` with MUI form for contract type, contracted hours, activate.
- [ ] T-9: Write `src/frontend/src/api/contracts.ts` with typed API calls.
- [ ] T-10: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-11: Verify `python3 scripts/check_feature_size.py size FEAT-003` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-003 plan.md; REQ-001 v0.3 Â§ S-19; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
