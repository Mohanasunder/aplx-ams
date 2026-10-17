---
id: FEAT-008
id_prefix: FEAT
title: "FEAT-008: S-30: Delivery Manager Sets a Temporary Password — Tasks"
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
# FEAT-008: S-30: Delivery Manager Sets a Temporary Password — Tasks

## Input References
- FEAT-008 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-30 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

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
- Upstream: FEAT-008 plan.md; REQ-001 v0.3 § S-30; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-008-TESTS (Phase 6 test set)

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
