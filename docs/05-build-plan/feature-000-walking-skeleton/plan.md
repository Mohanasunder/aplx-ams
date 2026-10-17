---
id: FEAT-000
id_prefix: FEAT
title: "FEAT-000: Walking Skeleton — Backend Scaffold and CI Pipeline"
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

# FEAT-000: Walking Skeleton — Backend Scaffold and CI Pipeline

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands, § Approved Technology List
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17) § Module Structure
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17) § Migration Approach
- .ai/standards/automated-gates.md — all 25 gate command definitions

## Purpose And Scope
Delivers the deployable Django 5.2 LTS project scaffold with a health check endpoint (`GET /api/health/` returning HTTP 200), Docker Compose setup (app + db containers), GitHub Actions CI pipeline wiring every gate listed in `.ai/standards/automated-gates.md`, pytest with 80% coverage gate, and all backend security scan gates passing on an otherwise empty codebase. This is the foundation every other feature depends on.

## Feature Type
Type: Enabling

## Objective
Provide a green CI pipeline with backend scaffold so every subsequent story feature can be built on a verified foundation. Covers: Django project skeleton, health endpoint, Docker Compose app+db services, pyproject.toml (pytest/ruff/mypy config), requirements.txt, and the complete GitHub Actions CI workflow file wiring all backend gate commands.

## Dependencies
- Depends on: none

## Inputs And Contracts
- STD-001 v0.1 § CI Gate Commands — exact commands the CI workflow must wire
- STD-001 v0.1 § Backend file and folder structure — directory layout to scaffold
- DBD-001 v0.1 § Migration Approach — Django migration framework and role setup
- .ai/standards/automated-gates.md — authoritative gate list

## Context Pack
- STD-001 v0.1 § Automated Gate Commands
- STD-001 v0.1 § Backend file and folder structure
- STD-001 v0.1 § Security Rules § Secrets and configuration
- STD-001 v0.1 § Python naming conventions
- STD-001 v0.1 § Approved Technology List
- BED-001 v0.1 § Module Structure
- DBD-001 v0.1 § Migration Approach
- .ai/standards/automated-gates.md

## Files To Create Or Modify
- `manage.py`
- `pyproject.toml`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`
- `.github/workflows/ci.yml`
- `src/aplx_ams_django/settings/base.py`
- `src/aplx_ams_django/settings/production.py`
- `src/aplx_ams_django/urls.py`
- `src/aplx_ams_django/health.py`
- `.secrets.baseline`

## New Packages
- pypi: Django ==5.2 | BSD-3-Clause | Core web framework; alternatives: Flask (rejected, ADR A-2)
- pypi: djangorestframework >=3.15,<4 | BSD-3-Clause | REST API serialization and views; alternatives: none (ADR A-2)
- pypi: gunicorn >=22,<23 | MIT | WSGI production server; alternatives: uvicorn (rejected ADR A-2)
- pypi: psycopg[binary] >=3.1,<4 | LGPL-3.0 | PostgreSQL 18 adapter; alternatives: psycopg2 (rejected ADR A-4)
- pypi: argon2-cffi >=23,<24 | MIT | Argon2id password hashing; alternatives: bcrypt (lower security, ADR A-8)
- pypi: pytest >=8,<9 | MIT | Test framework; alternatives: unittest (less powerful, DEC-043)
- pypi: pytest-django >=4.9,<5 | BSD-3-Clause | Django pytest integration; alternatives: none (DEC-043)
- pypi: pytest-cov >=5,<6 | MIT | Coverage measurement; alternatives: coverage.py alone (DEC-043)
- pypi: pytest-timeout >=2,<3 | MIT | Per-test timeout enforcement; alternatives: none (DEC-043)
- pypi: factory-boy >=3.3,<4 | MIT | Test fixture factories; alternatives: model-bakery (DEC-043)
- pypi: freezegun >=1.5,<2 | Apache-2.0 | Time-travel in tests; alternatives: none (DEC-043)
- pypi: ruff >=0.6,<1 | MIT | Python linter and formatter; alternatives: flake8+black (DEC-043)
- pypi: mypy >=1.11,<2 | MIT | Strict static type checker; alternatives: pyright (DEC-043)
- pypi: bandit >=1.7,<2 | Apache-2.0 | Python SAST scanner; alternatives: semgrep (DEC-043)
- pypi: pip-audit >=2.7,<3 | Apache-2.0 | Dependency vulnerability scan; alternatives: safety (DEC-043)
- pypi: detect-secrets >=1.5,<2 | Apache-2.0 | Secret scan baseline; alternatives: trufflehog (DEC-043)

## Out Of Scope
- Frontend scaffold, Nginx configuration, and security middleware — covered by FEAT-001.
- All app-level Django models (organizations, accounts, sla, tickets, effort, reports, audit) — each app is created by its own story feature.
- Any endpoint beyond `GET /api/health/`.
- RLS policies, database roles, and grants — added by FEAT-007 after all app migrations are in place.
- Production configuration files (server secrets, production Docker Compose overrides, SSL certificates) — Phase 8.

## Risk Tier
Tier: Critical
FEAT-000 is the CI infrastructure and the repository scaffold; every subsequent feature depends on it. A broken gate or wrong directory structure blocks the entire build phase.

## Implementation Steps
1. Initialize Django 5.2 LTS project with `django-admin startproject aplx_ams_django src/`.
2. Create `requirements.txt` with all Python packages listed under New Packages.
3. Configure `pyproject.toml` with `[tool.pytest.ini_options]`, `[tool.ruff]`, `[tool.mypy]`, `[tool.coverage.run]` sections per STD-001.
4. Write `src/aplx_ams_django/settings/base.py` with `read_secret()` helper, `DATABASES` pointing to docker-compose db service, `INSTALLED_APPS` for Django core only (no app apps yet), `AUTH_PASSWORD_VALIDATORS`, `PASSWORD_HASHERS` with Argon2id first.
5. Write `src/aplx_ams_django/settings/production.py` importing base with `DEBUG = False`.
6. Add `GET /api/health/` in `src/aplx_ams_django/health.py` returning `{"status": "ok"}` with HTTP 200; register in `src/aplx_ams_django/urls.py`.
7. Write `Dockerfile` (Python 3.13, install requirements, copy src/, CMD gunicorn).
8. Write `docker-compose.yml` with `app` (Django+Gunicorn) and `db` (PostgreSQL 18) services; environment variables from Docker Compose secrets for DB credentials.
9. Write `.github/workflows/ci.yml` with jobs for: lint (ruff), type-check (mypy), test (pytest --cov), SAST (bandit), dependency scan (pip-audit), secrets scan (detect-secrets), build (docker compose build), migration check.
10. Create `src/aplx_ams_django/tests/test_health.py` with a single passing test hitting `GET /api/health/`.
11. Run all gate commands locally; confirm each exits 0.

## Test Plan
- STD-001 AC-1: `docker compose build app` exits 0 (Docker image builds).
- STD-001 AC-2: `ruff check src/ && ruff format --check src/ && mypy src/ --strict` each exit 0.
- TST-001 AC-3: `pytest src/ --cov=src --cov-fail-under=80 --timeout=600` exits 0 with health test passing; coverage ≥ 80%.
- STD-001 AC-4: `bandit -r src/ -ll && pip-audit && detect-secrets scan` each exit 0.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-000` exits 0.
- [ ] `python3 scripts/check_feature_size.py task0` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-000-ACC.

## Risks
- Django 5.2 LTS and psycopg 3 may have configuration nuances not covered by boilerplate; builder must follow DBD-001 § Migration Approach for database role setup.
- The `detect-secrets` baseline must be committed before the scan gate can pass; builder creates `.secrets.baseline` with `detect-secrets scan > .secrets.baseline`.
- `manage.py`, `src/aplx_ams_django/__init__.py`, `src/aplx_ams_django/settings/__init__.py`, and `src/aplx_ams_django/wsgi.py` are created by `django-admin startproject` and are not individually listed above but are implicitly created; builder must ensure they are committed.

## Assumptions
- A-038 (Confirmed): no secret manager available; Docker Compose file secrets at `/run/secrets/` are used for database credentials (ADR A-17).

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; STD-001 v0.1; TST-001 v0.1; BED-001 v0.1; DBD-001 v0.1; .ai/standards/automated-gates.md
- Downstream: FEAT-001 through FEAT-035 (all depend on this feature)

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
