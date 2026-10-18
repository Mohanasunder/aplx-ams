---
id: FEAT-006-TESTS
title: "FEAT-006: S-21: User Signs In with a User Account — Test Set"
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Draft
author_agent: documentation-writer
approver: Mohanasunder
date: 2026-10-19
validation: Pending
---
# FEAT-006: S-21: User Signs In with a User Account — Test Set

## Input References
- FEAT-006 plan.md v0.3 (Approved 2026-10-18, Mohanasunder) — risk tier, scope, files to create, new packages
- FEAT-006-ACC v0.1 (Approved 2026-10-17, Mohanasunder) — 4 acceptance criteria (REQ S-21 AC-1 to AC-4)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-21
- API-001 v0.2 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Defines the tests that determine done for FEAT-006 (User Signs In with a User Account), written before implementation (Mode A). Covers 2 layers: backend (Django/pytest) and frontend (React/Vitest). 30 tests total across 2 test files. All 4 acceptance criteria (REQ S-21 AC-1 to AC-4) have at least one test at each applicable layer.

Database layer: no new model fields are introduced in this feature; the `User` model (`is_active`, `locked_until`, `failed_login_count`) was established in FEAT-005. No new database-layer test file is added; behavior is verified via backend API tests that touch the DB through the ORM.

Contract tests (3 backend tests for `/api/auth/logout/` and `/api/auth/me/`) are included in the backend test file. They cover API contract surface not directly tied to a single AC; they are listed separately in the Criteria To Tests Map.

One intentionally green test exists in Mode A: `test_ac3_custom_validator_accepts_abcdefg1` passes because the positive-path assertion (valid password raises no exception) is satisfied by Django's default behavior even when the custom validator stub is absent. This is expected and documented in the Notes column.

Phase 7 regression scope: all 30 tests remain in scope for regression.

## Risk Tier And Test Approver
- Risk tier: Critical (from FEAT-006 plan.md — authentication and session management; account lockout protects against brute force; incorrect error messages expose account existence)
- Test approver: Mohanasunder (Architect / tech lead) — per `.ai/standards/review-and-approval.md` § Test set approval; Critical-tier features require tech-lead approval

## Criteria To Tests Map

### Backend layer — `src/aplx_ams_django/accounts/tests/test_auth_api.py`

| Criterion ID | Test function | Layer | What it asserts | Mode A state | Notes |
|---|---|---|---|---|---|
| REQ S-21 AC-1 | `test_ac1_active_user_correct_password_returns_200` | Backend | POST /api/auth/login/ with valid credentials → HTTP 200 | Red — LoginView stub not implemented; HTTP 501 or 404 returned | |
| REQ S-21 AC-1 | `test_ac1_login_response_contains_role_and_org` | Backend | Response body contains `role` and `org` fields | Red — stub returns no body or 501 | |
| REQ S-21 AC-1 | `test_ac1_deactivated_account_refused_on_login` | Backend | `is_active=False` → HTTP 401; closes FEAT-005-TESTS AC-3 sign-in gap | Red — stub returns no 401 for deactivated accounts | Closes documented gap in FEAT-005-TESTS |
| REQ S-21 AC-2 | `test_ac2_wrong_password_returns_401` | Backend | Wrong password → HTTP 401 | Red — stub not implemented | |
| REQ S-21 AC-2 | `test_ac2_unknown_username_returns_401` | Backend | Non-existent username → HTTP 401 | Red — stub not implemented | |
| REQ S-21 AC-2 | `test_ac2_wrong_password_and_unknown_username_have_same_error_body` | Backend | Both wrong-password and unknown-username return identical error body (no account-existence disclosure) | Red — stub not implemented | Exercises A-019 |
| REQ S-21 AC-3 | `test_ac3_custom_validator_rejects_fewer_than_8_chars` | Backend | `ValidationError` raised for password `"Short1"` (6 chars) | Red — custom `PasswordComplexityValidator` not wired into `AUTH_PASSWORD_VALIDATORS` | |
| REQ S-21 AC-3 | `test_ac3_custom_validator_rejects_no_uppercase` | Backend | `ValidationError` raised for `"abcdefg1"` (no upper-case letter) | Red — validator not installed | |
| REQ S-21 AC-3 | `test_ac3_custom_validator_rejects_no_lowercase` | Backend | `ValidationError` raised for `"ABCDEFG1"` (no lower-case letter) | Red — validator not installed | |
| REQ S-21 AC-3 | `test_ac3_custom_validator_rejects_no_digit` | Backend | `ValidationError` raised for `"Abcdefgh"` (no digit) | Red — validator not installed | |
| REQ S-21 AC-3 | `test_ac3_custom_validator_accepts_abcdefg1` | Backend | No exception raised for `"Abcdefg1"` (valid: upper, lower, digit, 8 chars) | **Intentionally green in Mode A** — positive-path assertion; Django's default behavior does not reject a valid password even when the custom validator stub is absent | Intentionally green in Mode A; see Purpose And Scope |
| REQ S-21 AC-4 | `test_ac4_five_wrong_attempts_set_locked_until` | Backend | After 5 failed sign-ins, `user.locked_until` is set in DB to a future datetime | Red — `SessionAuthBackend` lockout logic not implemented | |
| REQ S-21 AC-4 | `test_ac4_locked_account_refuses_correct_password_within_30_minutes` | Backend | Locked account (`locked_until` in future) → HTTP 401 even with correct password | Red — lockout check not present in stub | |
| REQ S-21 AC-4 | `test_ac4_lockout_clears_after_30_minutes` | Backend | `locked_until` 31 min in the past + correct password → HTTP 200 | Red — lockout expiry logic not implemented | |
| Contract | `test_logout_endpoint_invalidates_session` | Backend | Login → POST /api/auth/logout/ → HTTP 200 → GET /api/auth/me/ → HTTP 401 | Red — LogoutView and MeView stubs not implemented | |
| Contract | `test_me_endpoint_requires_authentication` | Backend | Unauthenticated GET /api/auth/me/ → HTTP 401 | Red — MeView stub not implemented | |
| Contract | `test_me_endpoint_returns_role_and_org_for_authenticated_user` | Backend | Authenticated GET /api/auth/me/ → HTTP 200 with `role` and `org` fields | Red — MeView stub not implemented | |

### Frontend layer — `src/frontend/src/pages/Login.test.tsx`

| Criterion ID | Test name | Layer | What it asserts | Mode A state | Notes |
|---|---|---|---|---|---|
| REQ S-21 AC-1 | `REQ-021 AC-1: heading "Sign in" rendered as h1` | Frontend | `getByRole('heading', {level:1, name:/sign in/i})` present in DOM | Red — Login stub returns `null`; no DOM nodes rendered | |
| REQ S-21 AC-1 | `REQ-021 AC-1: account name field has autocomplete='username'` | Frontend | `input[autocomplete="username"]` present in DOM | Red — stub returns `null` | |
| REQ S-21 AC-1 | `REQ-021 AC-1: password field has autocomplete='current-password'` | Frontend | `input[autocomplete="current-password"]` present in DOM | Red — stub returns `null` | |
| REQ S-21 AC-1 | `REQ-021 AC-1: renders Sign in button` | Frontend | `getByRole('button', {name:/sign in/i})` present | Red — stub returns `null` | |
| REQ S-21 AC-1 | `REQ-021 AC-1: successful login calls login() then me() then navigates to /tickets` | Frontend | `login` mock called; `me` called once; navigation to `/tickets` triggered | Red — stub returns `null`; no form interactions possible | |
| REQ S-21 AC-1 | `REQ-021 AC-1: Sign in button disabled and loading indicator shown while submitting` | Frontend | Button disabled during in-flight `login()` promise | Red — stub returns `null` | |
| REQ S-21 AC-2 | `REQ-021 AC-2: HTTP 401 shows generic 'Invalid credentials.' alert` | Frontend | `getByRole('alert')` + `getByText('Invalid credentials.')` after 401 response | Red — stub returns `null`; no alert rendered | |
| REQ S-21 AC-2 | `REQ-021 AC-2: password cleared and account name retained after 401` | Frontend | Username input retains value; password input is cleared after 401 | Red — stub returns `null` | |
| REQ S-21 AC-3 | `REQ-021 AC-3: empty account name shows Required before API call` | Frontend | `getByText('Required')` visible in DOM; `login` not called | Red — stub returns `null` | |
| REQ S-21 AC-3 | `REQ-021 AC-3: empty password shows Required before API call` | Frontend | `getByText('Required')` visible in DOM; `login` not called | Red — stub returns `null` | |
| REQ S-21 AC-3 | `REQ-021 AC-3: API error message from server is displayed` | Frontend | Server-returned error detail string visible in DOM | Red — stub returns `null` | |
| REQ S-21 AC-4 | `REQ-021 AC-4: HTTP 401 for locked account shows 'Invalid credentials.' (generic message)` | Frontend | Alert shows `'Invalid credentials.'`; no text matching `/locked/i` present (no account-existence disclosure) | Red — stub returns `null` | Exercises A-019 at the UI layer |
| REQ S-21 AC-4 | `REQ-021 AC-4: HTTP 429 shows rate-limit message` | Frontend | Alert shows `'Too many sign-in attempts. Please wait and try again.'` | Red — stub returns `null` | |

## Test Files
- `src/aplx_ams_django/accounts/tests/test_auth_api.py` (locked once this artifact is Approved; 17 tests — backend layer; commit 9ececb7)
- `src/frontend/src/pages/Login.test.tsx` (locked once this artifact is Approved; 13 tests — frontend layer; commit 8bd2f25)

## Stubs Created

**Backend builder (commit 9ececb7):**
- `src/aplx_ams_django/accounts/authentication.py` — stub `SessionAuthBackend`; no logic; `authenticate()` returns `None` unconditionally
- `src/aplx_ams_django/accounts/views.py` — stubs added for `LoginView`, `LogoutView`, `MeView`; each returns HTTP 501 Not Implemented
- `src/aplx_ams_django/accounts/urls.py` — stub URL patterns registering `/api/auth/login/`, `/api/auth/logout/`, `/api/auth/me/` pointing at stub views

**Frontend builder (commit 8bd2f25):**
- `src/frontend/src/pages/Login.tsx` — stub component: `export default function Login() { return null; }`
- `src/frontend/src/api/auth.ts` — 3 async stub functions: `login`, `logout`, `me`; each returns `Promise<never>` or throws `NotImplementedError`
- `src/frontend/src/context/AuthContext.tsx` — stub context providing `null` user and no-op methods

## Red Run Evidence

**Backend layer**
Command: `python -m pytest src/aplx_ams_django/accounts/tests/test_auth_api.py -v`
Date: 2026-10-19
Result: 17 collected, 16 FAILED, 1 PASSED (`test_ac3_custom_validator_accepts_abcdefg1` — intentionally green; see Purpose And Scope)
Failure reason: `LoginView`, `LogoutView`, and `MeView` stubs return HTTP 501; `SessionAuthBackend` returns `None`; password validators not wired; lockout fields not written. Failures are behavioral, not syntax, import, or setup errors.

**Frontend layer**
Command: `npm --prefix src/frontend run test -- --run Login.test`
Date: 2026-10-19
Result: 13 collected, 13 FAILED, 0 PASSED
Failure reason: stub `Login` component returns `null`; no DOM elements are rendered; all `getBy*` queries throw `TestingLibraryElementError`. Failures are behavioral, not syntax, import, or setup errors.

## Test Commit
- Backend Mode A commit (test_auth_api.py): `9ececb7` (branch `feature/FEAT-006-sign-in-auth`, 2026-10-19)
- Frontend Mode A commit (Login.test.tsx): `8bd2f25` (branch `feature/FEAT-006-sign-in-auth`, 2026-10-19)
- Final test commit (HEAD of Mode A; both test files at approved state): `8bd2f25`

## Assumptions
- A-019: A refused sign-in does not say whether the account name or the password was wrong. Tests `test_ac2_wrong_password_and_unknown_username_have_same_error_body` (backend) and `REQ-021 AC-4: HTTP 401 for locked account shows 'Invalid credentials.' (generic message)` (frontend) exercise this assumption. Logged in `docs/logs/assumptions-log.md`. Confirmed by Mohanasunder, 2026-10-17 (DEC-041).

## Open Questions
- OQ-071 (Answered): FEAT-006 plan.md § Implementation Steps step 9 references React Router routes but `react-router-dom` was absent from New Packages in plan v0.2. Resolved via SCR S-13 (plan.md v0.3); Mode B uses `useNavigate` from `react-router-dom` (DEC-084, 2026-10-19). Logged in `docs/logs/open-questions-log.md`.

## Traceability Links
- Upstream: FEAT-006 plan.md v0.3; FEAT-006-ACC v0.1; REQ-001 v0.3 § S-21; API-001 v0.2; DBD-001 v0.1; UIS-001 v0.1; PRM-001 v0.1; FEAT-005-TESTS (AC-3 sign-in gap closed by `test_ac1_deactivated_account_refused_on_login`)
- Downstream: FEAT-006 Phase 6 implementation (Mode B); Phase 6 PR for FEAT-006

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test (AC-1: 9 tests across 2 layers; AC-2: 5 tests across 2 layers; AC-3: 9 tests across 2 layers; AC-4: 5 tests across 2 layers)
- [x] Tests assert behavior, not only that code runs (HTTP status codes, response body fields, DOM element presence, DB state, error message text, button state)
- [x] Red run shows every new test failing for the missing behavior (16 backend + 13 frontend = 29 failures; 1 intentionally green in Mode A documented; all behavioral, not syntax or setup)
- [x] Assumptions and open questions are logged and linked (A-019; OQ-071 answered)
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
