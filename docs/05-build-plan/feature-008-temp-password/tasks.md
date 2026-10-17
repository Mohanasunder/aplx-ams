---
id: FEAT-008-TASKS
id_prefix: FEAT
title: "FEAT-008: S-30: Delivery Manager Sets a Temporary Password â€” Tasks"
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
# FEAT-008: S-30: Delivery Manager Sets a Temporary Password â€” Tasks

## Input References
- FEAT-008 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-30 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-008. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `set_temporary_password(user_id, password, acting_user)` to `accounts/services.py`: validates password policy, hashes with Argon2id, clears lockout counter, saves.
- [ ] T-2: Add PATCH `/api/users/{id}/set-temp-password/` action to `accounts/views.py` (DM-only).
- [ ] T-3: Add `TempPasswordSerializer` to `serializers.py` with password policy validation.
- [ ] T-4: Add `clear_lockout(user_id)` to `accounts/dal.py`.
- [ ] T-5: Register temp-password URL in `accounts/urls.py`.
- [ ] T-6: Update `UserManagement.tsx` with 'Set temporary password' dialog (DM-only).
- [ ] T-7: Update `users.ts` with `setTempPassword(id, password)` call.
- [ ] T-8: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-9: Verify `python3 scripts/check_feature_size.py size FEAT-008` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-008 plan.md; REQ-001 v0.3 Â§ S-30; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
