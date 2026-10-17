---
id: FEAT-000-TESTS
title: FEAT-000: Walking Skeleton — Test Set
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Approved
author_agent: documentation-writer
approver: Mohanasunder
date: 2026-10-18
validation: Pass with warnings
---
# FEAT-000: Walking Skeleton — Test Set

## Input References
- FEAT-000 plan.md v0.1 (Approved 2026-10-17)
- FEAT-000-ACC v0.1 (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17)

## Purpose And Scope
Defines the tests for FEAT-000 (Walking Skeleton — Backend Scaffold and CI Pipeline, Enabling type). Only TST-001 AC-2 maps to a pytest test; the other three criteria (AC-1, AC-3, AC-4) are CI-gate-only checks verified by the GitHub Actions workflow, as stated explicitly in FEAT-000-ACC. Coverage: backend layer only. No database, frontend, or integration tests for this feature. Phase 7 regression scope: the health endpoint remains covered by this test set.

## Risk Tier And Test Approver
- Risk tier: Critical
- Test approver: Tech lead (Mohanasunder) — per `.ai/standards/review-and-approval.md` § Test set approval

## Criteria To Tests Map

| Criterion ID | Test file | Test function | Layer | What it asserts |
|---|---|---|---|---|
| TST-001 AC-2 | `src/aplx_ams_django/tests/test_health.py` | `test_health_returns_200` | Backend | GET `/api/health/` returns HTTP 200 and JSON body `{"status": "ok"}` |
| STD-001 AC-1 | N/A — CI gate | N/A | CI | `docker compose build app` exits 0; verified by `build` job in `.github/workflows/ci.yml` |
| STD-001 AC-3 | N/A — CI gate | N/A | CI | `ruff check src/ && ruff format --check src/ && mypy src/ --strict` each exit 0; verified by `lint` and `typecheck` jobs |
| STD-001 AC-4 | N/A — CI gate | N/A | CI | `bandit -r src/ -ll && pip-audit && detect-secrets scan --baseline .secrets.baseline` each exit 0; verified by `sast`, `deps`, and `secrets` jobs |

## Test Files
- `src/aplx_ams_django/tests/__init__.py` (package init, locked)
- `src/aplx_ams_django/tests/test_health.py` (locked)

## Stubs Created
- `src/aplx_ams_django/__init__.py` — empty package init (implied by plan.md Risks: "implicitly created by django-admin startproject")
- `src/aplx_ams_django/health.py` — `health_check(request)` raises `NotImplementedError`
- `src/aplx_ams_django/urls.py` — `urlpatterns: list = []`

## Red Run Evidence
Command: `python -m pytest src/aplx_ams_django/tests/test_health.py -v`
Date: 2026-10-18
Result: 1 collected, 1 FAILED. Output:
```
FAILED src/aplx_ams_django/tests/test_health.py::test_health_returns_200
AssertionError: assert 404 == 200
 +  where 404 = <HttpResponseNotFound status_code=404, ...>.status_code
WARNING django.request: Not Found: /api/health/
```
Failure is behavioral: `urlpatterns = []` means `/api/health/` is not routed; Django returns 404. Not a syntax, import, or setup error.

Note: `@pytest.mark.django_db` was removed from the test (no database access needed for a pure view) and the test re-committed at `6586f38`. The behavioral failure mode is unchanged.

## Test Commit
`6586f38` on branch `feature/FEAT-000-walking-skeleton`

## Assumptions
- A-038 (Confirmed): Docker Compose file secrets at `/run/secrets/` for DB credentials; test database uses `DATABASE_URL` env var injected by CI service container.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-000 plan.md v0.1; FEAT-000-ACC v0.1; STD-001 v0.1; TST-001 v0.1
- Downstream: Phase 6 implementation (Mode B); `.github/workflows/ci.yml` (commit `ad647ae`)

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
| Role | Tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Test set approved for FEAT-000 walking skeleton. Mode B may begin. |
| Timestamp | 2026-10-17 19:43 UTC |
