---
id: FEAT-003-TESTS
title: "FEAT-003: S-19 — Delivery Manager Sets Up a Client Organization Contract: Test Set"
phase: 6
version: 0.2
template: feature-test-set
template_version: 1.0
status: Approved
author_agent: documentation-writer
approver: Mohanasunder
date: 2026-10-18
validation: Pass
---
# FEAT-003: S-19 — Delivery Manager Sets Up a Client Organization Contract: Test Set

## Input References
- FEAT-003 v0.1 — Feature plan (Approved 2026-10-17)
- FEAT-003-ACC v0.1 — Acceptance criteria (Approved 2026-10-17)
- API-001 v0.2 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
This test set defines done for FEAT-003 (REQ S-19) at the database, backend API, and frontend layers. Tests were written before implementation (Mode A: tests-first). Every acceptance criterion in FEAT-003-ACC has at least one test at each relevant layer. Integration between layers and system-level NFR verification are left to Phase 7.

## Risk Tier And Test Approver
Tier: High. Contract data governs effort billing and hours bank balance; an incorrect constraint allowing two active contracts corrupts financial data. Requires approval by the tech lead (Mohanasunder) before implementation proceeds.

## Criteria To Tests Map

### Database layer — `src/aplx_ams_django/organizations/tests/test_contract_models.py`

| Criterion | Test function | Layer | What it asserts |
|---|---|---|---|
| REQ S-19 AC-1 | `test_create_hours_bank_contract_sets_contracted_hours` | Database | Creates hours_bank contract with contracted_hours=100; calls refresh_from_db; asserts value equals 100 |
| REQ S-19 AC-2 | `test_second_active_contract_same_org_raises_integrity_error` | Database | A second active contract for the same org raises IntegrityError (partial unique index BR B-15) |
| REQ S-19 AC-2 | `test_second_inactive_contract_same_org_succeeds` | Database | A second contract with is_active=False for the same org saves successfully |
| REQ S-19 AC-3 | `test_create_fixed_fee_contract_without_contracted_hours_succeeds` | Database | fixed_fee contract with contracted_hours=None saves; refresh_from_db returns None for contracted_hours |
| REQ S-19 AC-4 | `test_contract_has_client_org_fk` | Database | client_org is a ForeignKey to ClientOrg |
| REQ S-19 AC-4 | `test_contract_has_contract_type_field` | Database | contract_type is a CharField with hours_bank and fixed_fee choices |
| REQ S-19 AC-4 | `test_contract_has_contracted_hours_field_nullable` | Database | contracted_hours is a DecimalField with null=True |
| REQ S-19 AC-4 | `test_contract_has_is_active_field_with_default_true` | Database | is_active is a BooleanField with default=True |
| REQ S-19 AC-4 | `test_contract_has_started_at_field` | Database | started_at is a DateTimeField |
| REQ S-19 AC-4 | `test_contract_has_created_at_field` | Database | created_at is a DateTimeField with auto_now_add=True |
| REQ S-19 AC-4 | `test_hours_bank_without_contracted_hours_raises_integrity_error` | Database | hours_bank contract with contracted_hours=None raises IntegrityError (check constraint) |

### Backend API layer — `src/aplx_ams_django/organizations/tests/test_contract_api.py`

| Criterion | Test function | Layer | What it asserts |
|---|---|---|---|
| REQ S-19 AC-1 | `test_dm_can_create_hours_bank_contract` | Backend | POST by P3 (Delivery Manager) returns 201; response has contract_type=hours_bank and contracted_hours=100 |
| REQ S-19 AC-1 | `test_hours_bank_contract_balance_shows_100` | Backend | GET active contract after 100-hour creation returns hours_bank_balance=100 |
| REQ S-19 AC-2 | `test_second_active_contract_returns_409` | Backend | Second active contract POST by P3 returns 409 Conflict |
| REQ S-19 AC-3 | `test_fixed_fee_contract_has_no_contracted_hours` | Backend | POST fixed_fee contract returns 201; contracted_hours is null in the response |
| REQ S-19 AC-4 | `test_p1_cannot_create_contract` | Backend | POST by P1 returns 403 Forbidden |
| REQ S-19 AC-4 | `test_p2_cannot_create_contract` | Backend | POST by P2 returns 403 Forbidden |
| REQ S-19 AC-4 | `test_p4_cannot_create_contract` | Backend | POST by P4 returns 403 Forbidden |

### Frontend layer — `src/frontend/src/pages/ContractSetup.test.tsx`

| Criterion | Test name | Layer | What it asserts |
|---|---|---|---|
| REQ S-19 AC-1 | `FEAT-003 AC-1: renders Create Contract button for DM role` | Frontend | P3 (DM) context renders the Create Contract button in the DOM |
| REQ S-19 AC-2 | `FEAT-003 AC-2: shows error on 409 conflict` | Frontend | P3 context with 409 mock response; error message is visible in the DOM |
| REQ S-19 AC-3 | `FEAT-003 AC-3: does not show contracted hours field for fixed fee` | Frontend | P3 context with Fixed fee selected; contracted hours input is absent from the DOM |
| REQ S-19 AC-4 | `FEAT-003 AC-4: does not show create controls for non-DM role` | Frontend | P1 context; no Create Contract button; access-denied sentinel is visible |

## Test Files
- `src/aplx_ams_django/organizations/tests/test_contract_models.py` — locked once this artifact is Approved
- `src/aplx_ams_django/organizations/tests/test_contract_api.py` — locked once this artifact is Approved
- `src/frontend/src/pages/ContractSetup.test.tsx` — locked once this artifact is Approved

## Stubs Created
The following production files were created as empty signatures so tests compile and resolve imports. They contain no business logic:

- `src/aplx_ams_django/organizations/models.py` — `Contract` class stub with no fields (added to existing file; commit 5ef96df)
- `src/aplx_ams_django/organizations/migrations/0002_contract.py` — minimal migration skeleton creating an empty Contract table so `serialize_db_to_string` does not error (commit 5ef96df)
- `src/aplx_ams_django/organizations/dal.py` — empty DAL stub functions for contract queries (commit 8b8914d)
- `src/aplx_ams_django/organizations/serializers.py` — empty `ContractSerializer` stub (commit 8b8914d)
- `src/aplx_ams_django/organizations/services.py` — empty `create_contract` and `get_active_contract` stub functions (commit 8b8914d)
- `src/aplx_ams_django/organizations/views.py` — empty `ContractViewSet` stub returning HTTP 501 (commit 8b8914d)
- `src/aplx_ams_django/organizations/urls.py` — URL registration stubs for contract endpoints (commit 8b8914d)
- `src/frontend/src/api/contracts.ts` — empty typed API call stubs (commit 6824848)
- `src/frontend/src/pages/ContractSetup.tsx` — stub component returning null (commit 6824848)

## Red Run Evidence
Date: 2026-10-18. Branch: `feature/FEAT-003-contract-setup`.

**Database layer** (`pytest src/aplx_ams_django/organizations/tests/test_contract_models.py`):
- Result: 11 FAILED
- Failure cause: `FieldDoesNotExist` / unexpected kwargs — the stub `Contract` model has no fields, so field introspection and model instantiation fail as expected; behavior is missing, not the test setup.

**Backend API layer** (`pytest src/aplx_ams_django/organizations/tests/test_contract_api.py`):
- Result: 7 FAILED
- Failure cause: All stub views return HTTP 501 Not Implemented; tests expect 201, 409, and 403 responses; the difference confirms behavior is absent, not a syntax or import error.

**Frontend layer** (`npx vitest run src/frontend/src/pages/ContractSetup.test.tsx`):
- Result: 4 FAILED
- Failure cause: `TestingLibraryElementError` — the stub `ContractSetup.tsx` component returns null, so all DOM queries for buttons, inputs, and sentinels fail; behavior is absent, not a test configuration error.

**Existing tests**: All FEAT-002 tests remained green across all three commits, confirming no regression.

## Test Commit
Last builder test commit: `b4b18a1` (FEAT-003: fix ruff formatting in test files, 2026-10-18). This commit updated `8b8914d` (the original test set commit) with a formatting-only fix: removed one extra blank line after imports in `test_contract_api.py` (ruff I001) and applied `ruff format` to `test_api.py` (pre-existing FEAT-002 formatting problem). Authorized by Mohanasunder (DEC-073). No test logic was changed.

## Assumptions
None beyond those logged in `docs/logs/assumptions-log.md`.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-003 v0.1; FEAT-003-ACC v0.1; API-001 v0.2; DBD-001 v0.1; UIS-001 v0.1; PRM-001 v0.1; REQ-001 v0.3 § S-19; BR B-15
- Downstream: FEAT-003 Phase 6 PR; PRD FEAT-003 (pr-descriptions.md)

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
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Tests cover all 4 ACs including constraint edge cases and role-based refusal. |
| Timestamp | 2026-10-18 12:58 UTC |

## SCR S-28 Record
Version 0.2 (2026-10-22): SCR S-28 — glossary compliance fix; line 105 replaced avoided term with 'formatting problem' (GLO-001). No test logic changed.
