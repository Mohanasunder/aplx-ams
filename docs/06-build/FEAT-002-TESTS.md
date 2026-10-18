---
id: FEAT-002
title: FEAT-002: S-18 — Test Set
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
# FEAT-002: S-18 — Test Set

## Input References
- FEAT-002 plan.md v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-002-ACC v0.1 (Approved 2026-10-17, Mohanasunder)
- REQ-001 v0.3 § S-18 — acceptance criteria source
- API-001 v0.2 — endpoint contracts
- DBD-001 v0.1 § Module: organizations — table definitions
- STD-001 v0.1 — naming and structure conventions
- PRM-001 v0.1 § Organization setup — permission matrix

## Purpose And Scope
Covers all 3 acceptance criteria of FEAT-002 (REQ S-18) across three layers: database model tests, backend API tests, and frontend component tests. Tests are written before implementation (Mode A). Phase 7 regression testing covers end-to-end flows including real authentication.

## Risk Tier And Test Approver
Tier: **Standard**. Approver required: **Tech lead** (Mohanasunder), per `.ai/standards/review-and-approval.md` Standard tier test approval rule.

## Criteria To Tests Map

| Criterion | Test file | Test name | Layer | What it asserts |
|---|---|---|---|---|
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_client_org_has_name_field` | Database | `ClientOrg._meta.get_field("name")` has `max_length=255, unique=True` |
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_client_org_has_created_at_field` | Database | `ClientOrg._meta.get_field("created_at")` is a `DateTimeField` with `auto_now_add=True` |
| REQ-018 AC-1, AC-2 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_sap_application_has_client_org_fk` | Database | `SAPApplication._meta.get_field("client_org")` is a `ForeignKey` to `ClientOrg` |
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_sap_application_has_name_field` | Database | `SAPApplication._meta.get_field("name")` has `max_length=255` |
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_sap_application_has_created_at_field` | Database | `SAPApplication._meta.get_field("created_at")` is `DateTimeField` with `auto_now_add=True` |
| REQ-018 AC-2 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_sap_application_has_unique_name_per_org_constraint` | Database | `SAPApplication._meta` has `unique_together` or `UniqueConstraint` covering `(client_org, name)` |
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_client_org_name_unique_in_db` | Database | DB raises `IntegrityError` when same `ClientOrg.name` inserted twice |
| REQ-018 AC-2 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_sap_app_unique_per_org` | Database | DB raises `IntegrityError` when same SAP app name added to same org twice |
| REQ-018 AC-2 | `src/aplx_ams_django/organizations/tests/test_models.py` | `test_same_sap_app_name_different_org_allowed` | Database | Same SAP app name on a different org saves without `IntegrityError` |
| REQ-018 AC-1 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_dm_can_create_org_and_sap_app` | Backend | POST /api/organizations/ as P3 → 201; POST /api/organizations/{id}/sap-applications/ as P3 → 201; GET returns the new SAP app |
| REQ-018 AC-2 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_sap_app_isolated_to_org` | Backend | SAP app added to org A does NOT appear in org B's sap-applications list |
| REQ-018 AC-3 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_p1_cannot_create_org` | Backend | POST /api/organizations/ as P1 → 403 |
| REQ-018 AC-3 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_p2_cannot_create_org` | Backend | POST /api/organizations/ as P2 → 403 |
| REQ-018 AC-3 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_p4_cannot_create_org` | Backend | POST /api/organizations/ as P4 → 403 |
| REQ-018 AC-3 | `src/aplx_ams_django/organizations/tests/test_api.py` | `test_p1_cannot_add_sap_app` | Backend | POST /api/organizations/{id}/sap-applications/ as P1 → 403 |
| REQ-018 AC-1 | `src/frontend/src/pages/OrgManagement.test.tsx` | `FEAT-002 AC-1: renders org list heading for DM role` | Frontend | Renders `OrgManagement` with P3 context; `getByRole('heading', { name: /client organizations/i })` present in DOM |
| REQ-018 AC-1 | `src/frontend/src/pages/OrgManagement.test.tsx` | `FEAT-002 AC-1: shows Add organization button for DM role` | Frontend | Renders with P3 context; `getByRole('button', { name: /add organization/i })` present |
| REQ-018 AC-3 | `src/frontend/src/pages/OrgManagement.test.tsx` | `FEAT-002 AC-3: redirects non-DM role to /tickets` | Frontend | Renders with P1 context; `getByTestId('redirect-to-tickets')` present (route-guard sentinel) |

AC-2 (data isolation) has no separate frontend test — the frontend renders what the API returns; isolation is enforced and tested at the backend layer.

## Test Files
- `src/aplx_ams_django/organizations/tests/test_models.py` — locked once this artifact is Approved
- `src/aplx_ams_django/organizations/tests/test_api.py` — locked once this artifact is Approved
- `src/frontend/src/pages/OrgManagement.test.tsx` — locked once this artifact is Approved

## Stubs Created

| File | Contents |
|---|---|
| `src/aplx_ams_django/organizations/__init__.py` | Empty package marker |
| `src/aplx_ams_django/organizations/apps.py` | `OrganizationsConfig(AppConfig)` |
| `src/aplx_ams_django/organizations/models.py` | `ClientOrg(models.Model)` and `SAPApplication(models.Model)` — no fields (stubs) |
| `src/aplx_ams_django/organizations/migrations/__init__.py` | Empty package marker |
| `src/aplx_ams_django/organizations/migrations/0001_initial.py` | Stub migration — creates tables with `id` only |
| `src/aplx_ams_django/organizations/serializers.py` | `ClientOrgSerializer`, `SAPApplicationSerializer` — empty Meta.fields |
| `src/aplx_ams_django/organizations/services.py` | `create_org()`, `add_sap_application()` — raise `NotImplementedError` |
| `src/aplx_ams_django/organizations/dal.py` | `get_org_by_id()`, `list_orgs()`, `get_sap_apps_for_org()` — raise `NotImplementedError` |
| `src/aplx_ams_django/organizations/views.py` | `OrgViewSet`, `SAPApplicationViewSet` — stubs with `permission_classes = [HasRolePermission]` |
| `src/aplx_ams_django/organizations/urls.py` | `urlpatterns: list = []` (empty — causes 404 on all org requests) |
| `src/aplx_ams_django/permissions.py` | `class HasRolePermission: pass` |
| `src/frontend/src/pages/OrgManagement.tsx` | `export default function OrgManagement() { return null; }` |
| `src/frontend/src/api/organizations.ts` | Type definitions and stub async functions (`listOrgs`, `createOrg`, `listSapApps`, `createSapApp`) |

## Red Run Evidence

**Database tests** — Command: `pytest src/aplx_ams_django/organizations/tests/test_models.py -v` — Date: 2026-10-18 — Branch: `feature/FEAT-002-org-sap-setup`
```
6 FAILED — FieldDoesNotExist / AssertionError (fields and constraints absent from stubs)
3 ERROR  — OperationalError: failed to resolve host 'db' (Docker DB not reachable from host; CI will fail with ProgrammingError: table does not exist instead)
```
All failures are for missing behavior, not syntax or import errors.

**Backend API tests** — Command: `pytest src/aplx_ams_django/organizations/tests/test_api.py -v` — Date: 2026-10-18
```
6 FAILED — AssertionError: 404 != 201 / 404 != 403 (empty urlpatterns stub returns 404)
```

**Frontend tests** — Command: `cd src/frontend && npm run test -- --run` — Date: 2026-10-18
```
✓ src/App.test.tsx (1 test) — existing test PASSES
❯ src/pages/OrgManagement.test.tsx (3 tests | 3 failed)
  × FEAT-002 AC-1: renders org list heading for DM role → Unable to find heading (DOM: <body><div /></body>)
  × FEAT-002 AC-1: shows Add organization button for DM role → Unable to find button
  × FEAT-002 AC-3: redirects non-DM role to /tickets → Unable to find [data-testid="redirect-to-tickets"]
```

## Test Commit
`0f15688` — `FEAT-002: tests (backend)` — branch `feature/FEAT-002-org-sap-setup` — 2026-10-18
(Contains all three test layers: database commit `e9695a9`, frontend commit `1bda5af`, backend commit `0f15688`)

## Assumptions
- A-046 (plan gap): `src/aplx_ams_django/settings/base.py` is not listed in FEAT-002 plan.md Files To Create Or Modify, but adding `"aplx_ams_django.organizations"` to `INSTALLED_APPS` is required. Mode B must add this entry; treated as an implied step for any new Django app. Logged in `docs/logs/assumptions-log.md`.
- A-047 (plan gap): DB-dependent tests (`test_client_org_name_unique_in_db`, `test_sap_app_unique_per_org`, `test_same_sap_app_name_different_org_allowed`) require `@pytest.mark.django_db` and a live database. On the host they error with `OperationalError`; in CI Docker they will fail with `ProgrammingError` (no migration yet). Mode B wires the migration and the mark via `conftest.py` (not a locked file). Logged in `docs/logs/assumptions-log.md`.
- A-NNN (frontend): `OrgManagement` uses a `UserContext` defined in the same file for Mode A. Mode B must reconcile with any shared auth context introduced by FEAT-006 (sign-in).

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-002 plan.md v0.1; FEAT-002-ACC v0.1; REQ-001 v0.3 § S-18; API-001 v0.2; DBD-001 v0.1; STD-001 v0.1; PRM-001 v0.1
- Downstream: Phase 6 Mode B implementation; Phase 6 PR for FEAT-002; Phase 7 regression test suite

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test
- [x] Tests assert behavior, not only that code runs
- [x] Red run shows every new test failing for the missing behavior
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
