---
id: FEAT-006
id_prefix: FEAT
title: "FEAT-006: S-21: User Signs In with a User Account"
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-006: S-21: User Signs In with a User Account

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-21
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-21: S-21: User Signs In with a User Account. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-21 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-005

## Inputs And Contracts
- REQ-001 v0.3 § S-21 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-21
- API-001 v0.1 § Authentication (F-5)
- DBD-001 v0.1 § Module: accounts
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Authentication (F-5)
- UIS-001 v0.1 § REQ S-21 — Sign in

## Files To Create Or Modify
- `src/aplx_ams_django/accounts/authentication.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/aplx_ams_django/settings/base.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/Login.tsx`
- `src/frontend/src/api/auth.ts`
- `src/frontend/src/context/AuthContext.tsx`
- `src/frontend/src/App.tsx`

## New Packages
- None

## Out Of Scope
Temporary password — FEAT-008. Change own password — FEAT-009. Security event recording of sign-in events — FEAT-033. Session timeout in middleware — already stubbed in FEAT-001 middleware.py; session settings are added to base.py in this feature.

## Risk Tier
Tier: Critical
Authentication and session management; account lockout protects against brute force; incorrect error messages expose account existence.

## Implementation Steps
1. Write `accounts/authentication.py` with `SessionAuthBackend` that checks `is_active`, Argon2id password, and lockout (5 failures in 30 minutes per NFR N-5).
2. Update `accounts/views.py`: add `LoginView` (POST /api/auth/login/), `LogoutView` (POST /api/auth/logout/), `MeView` (GET /api/auth/me/) returning role and org.
3. Update `accounts/urls.py` with auth endpoints.
4. Update `settings/base.py`: add `SESSION_COOKIE_HTTPONLY=True`, `SESSION_COOKIE_SAMESITE='Lax'`, session timeout, `AUTHENTICATION_BACKENDS`, password validators (length 8, upper, lower, digit).
5. Register auth URLs in root `urls.py`.
6. Write `src/frontend/src/pages/Login.tsx` with MUI form; calls POST /api/auth/login/.
7. Write `src/frontend/src/api/auth.ts` with `login`, `logout`, `me` typed calls.
8. Write `src/frontend/src/context/AuthContext.tsx` providing current user and role.
9. Update `src/frontend/src/App.tsx` with React Router routes; guard by `AuthContext`.

## Test Plan
REQ-021 AC-1 REQ S-21 AC-1: Given an active user account with a correct password, when the user signs in, th...
REQ-021 AC-2 REQ S-21 AC-2: Given a wrong password, when the user signs in, then sign-in is refused without ...
REQ-021 AC-3 REQ S-21 AC-3: Given a user setting a password, when it has fewer than 8 characters or lacks an...
REQ-021 AC-4 REQ S-21 AC-4: Given 5 failed sign-ins on one user account, when a sixth sign-in is tried withi...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 9 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-006` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-006-ACC.

## Risks
- Lockout state must persist in the database (not only in memory) so that container restarts do not reset it.
- DEC-042: rate limit 10 req/min per IP, burst 5, enforced at Nginx; builder must add rate_limit to nginx.conf.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-21; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-006-TASKS; FEAT-006-ACC; FEAT-006-STATUS; Phase 6 PR

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
| Comments | Phase 5 validation passed (VAL-023). |
| Timestamp | 2026-10-17 16:50 UTC |
