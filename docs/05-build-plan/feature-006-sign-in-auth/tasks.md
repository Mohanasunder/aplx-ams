---
id: FEAT-006
id_prefix: FEAT
title: "FEAT-006: S-21: User Signs In with a User Account — Tasks"
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
# FEAT-006: S-21: User Signs In with a User Account — Tasks

## Input References
- FEAT-006 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-21 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-006. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Write `accounts/authentication.py` with `SessionAuthBackend` that checks `is_active`, Argon2id password, and lockout (5 failures in 30 minutes per NFR N-5).
- [ ] T-2: Update `accounts/views.py`: add `LoginView` (POST /api/auth/login/), `LogoutView` (POST /api/auth/logout/), `MeView` (GET /api/auth/me/) returning role and org.
- [ ] T-3: Update `accounts/urls.py` with auth endpoints.
- [ ] T-4: Update `settings/base.py`: add `SESSION_COOKIE_HTTPONLY=True`, `SESSION_COOKIE_SAMESITE='Lax'`, session timeout, `AUTHENTICATION_BACKENDS`, password validators (length 8, upper, lower, digit).
- [ ] T-5: Register auth URLs in root `urls.py`.
- [ ] T-6: Write `src/frontend/src/pages/Login.tsx` with MUI form; calls POST /api/auth/login/.
- [ ] T-7: Write `src/frontend/src/api/auth.ts` with `login`, `logout`, `me` typed calls.
- [ ] T-8: Write `src/frontend/src/context/AuthContext.tsx` providing current user and role.
- [ ] T-9: Update `src/frontend/src/App.tsx` with React Router routes; guard by `AuthContext`.
- [ ] T-10: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-11: Verify `python3 scripts/check_feature_size.py size FEAT-006` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-006 plan.md; REQ-001 v0.3 § S-21; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-006-TESTS (Phase 6 test set)

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
