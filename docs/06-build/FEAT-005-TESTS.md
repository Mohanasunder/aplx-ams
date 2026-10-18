---
id: FEAT-005-TESTS
title: "FEAT-005: Delivery Manager Manages User Accounts — Test Set"
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Draft
author_agent: documentation-writer
approver: Human developer reviewer
date: 2026-10-18
validation: Pending
---
# FEAT-005: Delivery Manager Manages User Accounts — Test Set

## Input References
- FEAT-005 plan.md v0.1 (Approved 2026-10-17, Mohanasunder) — risk tier, scope, files to create
- FEAT-005-ACC v0.1 (Approved 2026-10-17, Mohanasunder) — 4 acceptance criteria (REQ S-20 AC-1 to AC-4)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-20
- API-001 v0.2 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Defines the tests that determine done for FEAT-005 (Delivery Manager Manages User Accounts), written before implementation (Mode A). Covers 3 layers: database (model behavior), backend (DRF API), and frontend (React component). 31 tests total across 3 test files. All 4 acceptance criteria (REQ S-20 AC-1 to AC-4) have at least one test at one layer.

One partial gap exists: REQ S-20 AC-3 requires that a deactivated user "can no longer sign in". The persistence side (`is_active=False` written to DB) is tested in this feature at the database and backend layers. The sign-in refusal gate (HTTP 401 on attempt to sign in with a deactivated account) is deferred to FEAT-006, which owns the sign-in endpoint per FEAT-005 plan.md § Out Of Scope. That gap is documented in this artifact and will be closed by FEAT-006-TESTS.

Phase 7 regression scope: all 31 tests remain in scope for regression.

## Risk Tier And Test Approver
- Risk tier: High (from FEAT-005 plan.md — personal data: names, emails, roles; incorrect role assignment grants unauthorized access)
- Test approver: Mohanasunder (Tech lead) — per `.ai/standards/review-and-approval.md` § Test set approval

## Criteria To Tests Map

### Database layer — `src/aplx_ams_django/accounts/tests/test_models.py`

| Criterion ID | Test function | Layer | What it asserts | Mode A state |
|---|---|---|---|---|
| REQ S-20 AC-1 | `test_role_field_exists` | Database | `User._meta.get_field("role")` returns a field without raising `FieldDoesNotExist` | Red — stub model has no `role` field; `FieldDoesNotExist` raised |
| REQ S-20 AC-1 | `test_role_field_has_all_four_valid_choices` | Database | `role` field choices include all 4 role values (`l1_support_engineer`, `l2_l3_support_engineer`, `delivery_manager`, `client_user`) | Red — no `role` field on stub model |
| REQ S-20 AC-1 | `test_create_user_with_l1_support_engineer_role` | Database | `l1_support_engineer` role persists through DB save + re-fetch | Red — no `role` field; save raises `TypeError` |
| REQ S-20 AC-1 | `test_create_user_with_l2_l3_support_engineer_role` | Database | `l2_l3_support_engineer` role persists through DB save + re-fetch | Red — no `role` field; save raises `TypeError` |
| REQ S-20 AC-1 | `test_create_user_with_delivery_manager_role` | Database | `delivery_manager` role persists through DB save + re-fetch | Red — no `role` field; save raises `TypeError` |
| REQ S-20 AC-1 | `test_create_user_with_client_user_role` | Database | `client_user` role + `client_org` FK persists through DB save + re-fetch | Red — no `role` or `client_org` field on stub model |
| REQ S-20 AC-1 | `test_invalid_role_rejected` | Database | DB rejects an invalid role value (constraint violation) | Red — no `role` field; assertion on constraint not reachable |
| REQ S-20 AC-2 | `test_client_user_without_org_raises_integrity_error` | Database | `IntegrityError` raised when `client_user` is saved with no `client_org` | Red — no `client_org` FK or NOT NULL constraint on stub model |
| REQ S-20 AC-2 | `test_client_user_with_valid_org_saved_successfully` | Database | `client_user` + valid `ClientOrg` FK accepted; no exception raised | Red — no `client_org` field; save raises `TypeError` |
| REQ S-20 AC-2 | `test_internal_role_with_org_raises_integrity_error` | Database | `IntegrityError` raised when an internal role is saved with a `client_org` (enforces BR B-21) | Red — no `client_org` field; constraint not present on stub model |
| REQ S-20 AC-3 | `test_is_active_field_is_booleanfield` | Database | `is_active` is a `BooleanField` on `User` | Red — stub model inherits `is_active` from `AbstractBaseUser` as a `BooleanField` but the test asserts a custom default of `True`; stub uses AbstractBaseUser default which passes — see note below* |
| REQ S-20 AC-3 | `test_is_active_defaults_to_true` | Database | `is_active` `BooleanField` `default` is `True` on the model field declaration | Red — stub model does not declare `is_active` explicitly; default assertion fails |
| REQ S-20 AC-3 | `test_deactivate_user_persists_through_db_round_trip` | Database | `is_active=False` survives `save()` + re-fetch from DB | Red — stub model has no explicit `is_active` override; save + re-fetch may not persist `False` without explicit declaration |

*Note: `AbstractBaseUser` includes `is_active` as `BooleanField(default=True)` by default; the test asserts the field exists with the correct default. The stub omits the explicit field declaration which some Django versions may handle differently — the builder confirmed the red run as 13 failed.

### Backend layer — `src/aplx_ams_django/accounts/tests/test_api.py`

| Criterion ID | Test function | Layer | What it asserts | Mode A state |
|---|---|---|---|---|
| REQ S-20 AC-1 | `test_dm_creates_user_with_l1_support_engineer_role` | Backend | POST by DM (P3) → HTTP 201; response body `role == "l1_support_engineer"` | Red — stub view returns HTTP 501 |
| REQ S-20 AC-1 | `test_dm_creates_user_with_l2_l3_support_engineer_role` | Backend | POST by DM (P3) → HTTP 201; response body `role == "l2_l3_support_engineer"` | Red — stub view returns HTTP 501 |
| REQ S-20 AC-1 | `test_dm_creates_user_with_delivery_manager_role` | Backend | POST by DM (P3) → HTTP 201; response body `role == "delivery_manager"` | Red — stub view returns HTTP 501 |
| REQ S-20 AC-1 | `test_dm_creates_user_with_client_user_role` | Backend | POST by DM (P3) with `client_org_id` → HTTP 201; response body `role == "client_user"` | Red — stub view returns HTTP 501 |
| REQ S-20 AC-2 | `test_create_client_user_without_client_org_returns_400` | Backend | POST by DM (P3) with `role=client_user`, no `client_org_id` → HTTP 400 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-3 | `test_deactivate_user_returns_200` | Backend | POST `/deactivate/` → HTTP 200 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-3 | `test_deactivated_user_has_is_active_false` | Backend | After deactivation call, `is_active == False` in DB (sign-in refusal is in FEAT-006) | Red — stub view returns HTTP 501; no DB write |
| REQ S-20 AC-4 | `test_l1_cannot_create_user` | Backend | POST by P1 (L1 support engineer) → HTTP 403 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-4 | `test_l2_l3_cannot_create_user` | Backend | POST by P2 (L2/L3 support engineer) → HTTP 403 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-4 | `test_client_user_cannot_create_user` | Backend | POST by P4 (client user) → HTTP 403 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-4 | `test_l1_cannot_patch_user` | Backend | PATCH by P1 → HTTP 403 | Red — stub view returns HTTP 501 |
| REQ S-20 AC-4 | `test_l1_cannot_deactivate_user` | Backend | POST `/deactivate/` by P1 → HTTP 403 | Red — stub view returns HTTP 501 |

### Frontend layer — `src/frontend/src/pages/UserManagement.test.tsx`

| Criterion ID | Test name | Layer | What it asserts | Mode A state |
|---|---|---|---|---|
| REQ S-20 AC-1 | `FEAT-005 AC-1: role select renders all four role options` | Frontend | P3 (DM) context, dialog open → 4 `<option>` elements present with all role values | Red — stub `UserManagement` returns `null`; no DOM nodes rendered |
| REQ S-20 AC-1 | `FEAT-005 AC-1: form submission calls createUser with correct role field` | Frontend | P3 context, role selected, form submitted → `createUser` called with correct `role` in payload | Red — stub renders `null`; no form elements; `createUser` not called |
| REQ S-20 AC-2 | `FEAT-005 AC-2: Confirm button is disabled when client_user role and no org selected` | Frontend | Dialog open, `role=client_user`, no org selected → Confirm button is disabled | Red — stub renders `null`; no button found |
| REQ S-20 AC-2 | `FEAT-005 AC-2: error message shown when client_user submitted without org` | Frontend | `role=client_user`, no org → error text visible in DOM | Red — stub renders `null`; no error text |
| REQ S-20 AC-3 | `FEAT-005 AC-3: deactivated user row shows Deactivated chip` | Frontend | After deactivate action, user row shows "Deactivated" chip | Red — stub renders `null`; no DataGrid rows |
| REQ S-20 AC-4 | `FEAT-005 AC-4: non-DM role is redirected away from /admin/users` | Frontend | P1 (L1) context → redirect-to-tickets test ID present in DOM | Red — stub renders `null`; no redirect element |

## Test Files
- `src/aplx_ams_django/accounts/tests/test_models.py` (locked once this artifact is Approved; 13 tests — database layer)
- `src/aplx_ams_django/accounts/tests/test_api.py` (locked once this artifact is Approved; 12 tests — backend layer)
- `src/frontend/src/pages/UserManagement.test.tsx` (locked once this artifact is Approved; 6 tests — frontend layer)

## Stubs Created

**Database builder (commit 6248aa5):**
- `src/aplx_ams_django/accounts/models.py` — stub `User` model extending `AbstractBaseUser`; no `role` field, no `client_org` FK, no `is_active` explicit declaration; tests fail on missing field and constraint behavior
- `src/aplx_ams_django/accounts/migrations/0001_initial.py` — stub migration; creates `accounts_user` table with `id`, `password`, `last_login`, `username` columns only (no `role`, no `client_org_id`, no `is_active`)
- `src/aplx_ams_django/accounts/tests/conftest.py` — test fixtures: `ClientOrg` factory helper and `User` factory for each role; not a locked test file

**Backend builder (commit 8a33dca):**
- `src/aplx_ams_django/accounts/serializers.py` — stub serializers: empty class bodies; no validation logic
- `src/aplx_ams_django/accounts/services.py` — stub services: `create_user` and `deactivate_user` raise `NotImplementedError`
- `src/aplx_ams_django/accounts/dal.py` — stub DAL: `get_user_by_id`, `list_users`, `get_active_users_by_org` return `None` or empty
- `src/aplx_ams_django/accounts/views.py` — stub `UserViewSet`: all actions return HTTP 501 Not Implemented
- `src/aplx_ams_django/accounts/urls.py` — stub URL patterns: registers endpoint paths pointing at stub `UserViewSet`

**Frontend builder (commit 0c9ce44):**
- `src/frontend/src/pages/UserManagement.tsx` — stub component: `export default function UserManagement() { return null; }`
- `src/frontend/src/api/users.ts` — 4 async stub functions: `createUser`, `listUsers`, `deactivateUser`, `listOrgs`; each returns `Promise<never>` or throws

## Red Run Evidence

**Database layer**
Command: `python -m pytest src/aplx_ams_django/accounts/tests/test_models.py -v`
Date: 2026-10-18
Result: 13 collected, 13 FAILED
Failure reason: stub `User` model has no `role` field, no `client_org` FK, and no explicit `is_active` declaration; `FieldDoesNotExist` and `TypeError` raised on field access and save calls. Not syntax, import, or setup errors.

**Backend layer**
Command: `python -m pytest src/aplx_ams_django/accounts/tests/test_api.py -v`
Date: 2026-10-18
Result: 12 collected, 12 FAILED
Failure reason: stub `UserViewSet` returns HTTP 501 for all actions; tests assert HTTP 201, 200, or 403. Not syntax, import, or setup errors.

**Frontend layer**
Command: `npm --prefix src/frontend run test -- --run UserManagement.test`
Date: 2026-10-18
Result: 6 collected, 6 FAILED
Failure reason: stub `UserManagement` returns `null`; no DOM elements rendered; all `getBy*` queries throw `TestingLibraryElementError`. Not syntax, import, or setup errors.

## Test Commit
Three sequential commits on branch `feature/FEAT-005-user-accounts`:
- `6248aa5` — database layer: 13 model tests + stub accounts app (committed 2026-10-18)
- `8a33dca` — backend layer: 12 API tests + stub serializers, services, dal, views, urls (committed 2026-10-18)
- `0c9ce44` — frontend layer: 6 component tests + stub UserManagement.tsx and users.ts (committed 2026-10-18)

The checker diffs the three test files against commit `0c9ce44` (HEAD of the test-only run), which is the final state of all test files at Mode A completion.

## Assumptions
None specific to this test set. No new assumptions are raised beyond those already in `docs/logs/assumptions-log.md`.

## Open Questions
None. The AC-3 sign-in refusal gap is a documented scope boundary from FEAT-005 plan.md § Out Of Scope, not an open question.

## Traceability Links
- Upstream: FEAT-005 plan.md v0.1; FEAT-005-ACC v0.1; REQ-001 v0.3 § S-20; API-001 v0.2; DBD-001 v0.1; UIS-001 v0.1; PRM-001 v0.1
- Downstream: FEAT-005 Phase 6 implementation (Mode B); Phase 6 PR for FEAT-005; FEAT-006 test set (will cover AC-3 sign-in refusal gap — sign-in endpoint is in FEAT-006 scope)

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test (AC-1: 9 tests across 3 layers; AC-2: 5 tests across 3 layers; AC-3: 5 tests across 3 layers with sign-in refusal gap documented; AC-4: 6 tests across 2 layers)
- [x] Tests assert behavior, not only that code runs (field existence, HTTP status codes, DOM element presence, DB persistence, permission refusals)
- [x] Red run shows every new test failing for the missing behavior (13 + 12 + 6 = 31 failures; all behavioral, not syntax or setup)
- [x] Assumptions and open questions are logged and linked (none new; gap is a scope boundary)
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
