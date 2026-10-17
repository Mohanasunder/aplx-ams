---
id: FEAT-009-TASKS
id_prefix: FEAT
title: "FEAT-009: S-31: User Changes Their Own Password â€” Tasks"
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
# FEAT-009: S-31: User Changes Their Own Password â€” Tasks

## Input References
- FEAT-009 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-31 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-009. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `change_own_password(user_id, current_password, new_password)` to `accounts/services.py`: verifies current password, validates new password policy, hashes and saves.
- [ ] T-2: Add POST `/api/auth/change-password/` to `accounts/views.py` (any authenticated user, own account only).
- [ ] T-3: Register in `accounts/urls.py`.
- [ ] T-4: Add `ChangePasswordSerializer` to `serializers.py` with `current_password` and `new_password` fields.
- [ ] T-5: Write `src/frontend/src/pages/ChangePassword.tsx` with MUI form; current + new + confirm password.
- [ ] T-6: Add `changePassword(current, newPwd)` to `src/frontend/src/api/auth.ts`.
- [ ] T-7: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-009` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-009 plan.md; REQ-001 v0.3 Â§ S-31; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
