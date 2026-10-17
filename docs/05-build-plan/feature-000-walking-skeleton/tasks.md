---
id: FEAT-000-TASKS
id_prefix: FEAT
title: "FEAT-000: Walking Skeleton â€” Backend Scaffold and CI Pipeline â€” Tasks"
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

# FEAT-000: Walking Skeleton â€” Backend Scaffold and CI Pipeline â€” Tasks

## Input References
- FEAT-000 plan.md â€” implementation steps and file list
- STD-001 v0.1 Â§ Automated Gate Commands â€” gate commands to wire
- STD-001 v0.1 Â§ Backend file and folder structure â€” directory layout

## Purpose And Scope
Ordered task checklist for the builder of FEAT-000. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Run `django-admin startproject aplx_ams_django src/` to generate `manage.py`, `src/aplx_ams_django/__init__.py`, `src/aplx_ams_django/wsgi.py`, `src/aplx_ams_django/asgi.py`, `src/aplx_ams_django/settings.py` (rename to `settings/base.py`), `src/aplx_ams_django/urls.py`.
- [ ] T-2: Write `requirements.txt` with all packages listed in FEAT-000 plan.md New Packages at the specified version specs.
- [ ] T-3: Write `pyproject.toml` with `[tool.pytest.ini_options]` (testpaths, DJANGO_SETTINGS_MODULE), `[tool.ruff.lint]`, `[tool.mypy]` (strict=true), `[tool.coverage.run]` (omit migrations) â€” file: `pyproject.toml`.
- [ ] T-4: Write `src/aplx_ams_django/settings/base.py` with `read_secret()` helper, DATABASES config pointing to `db` service, Argon2id first in PASSWORD_HASHERS, `INSTALLED_APPS` for Django core (no story apps yet) â€” file: `src/aplx_ams_django/settings/base.py`.
- [ ] T-5: Write `src/aplx_ams_django/settings/production.py` importing base with `DEBUG = False` â€” file: `src/aplx_ams_django/settings/production.py`.
- [ ] T-6: Write `src/aplx_ams_django/health.py` with `health_check` view returning `JsonResponse({"status": "ok"})` with HTTP 200; update `src/aplx_ams_django/urls.py` to register `GET /api/health/` â€” files: `src/aplx_ams_django/health.py`, `src/aplx_ams_django/urls.py`.
- [ ] T-7: Write `src/aplx_ams_django/tests/test_health.py` with `test_health_returns_200` using APIClient.
- [ ] T-8: Write `Dockerfile` (Python 3.13 base, install requirements, copy src/, CMD gunicorn with `aplx_ams_django.wsgi:application`) â€” file: `Dockerfile`.
- [ ] T-9: Write `docker-compose.yml` with `app` service (build from Dockerfile, env DJANGO_SETTINGS_MODULE) and `db` service (PostgreSQL 18 image, health check) â€” file: `docker-compose.yml`.
- [ ] T-10: Run `detect-secrets scan > .secrets.baseline` and commit `.secrets.baseline`.
- [ ] T-11: Write `.github/workflows/ci.yml` with jobs: `lint` (ruff), `type-check` (mypy), `test` (pytest --cov with test db service), `sast` (bandit), `dep-scan` (pip-audit), `secrets-scan` (detect-secrets), `build` (docker compose build), `migration-check` (migrate + zero) â€” file: `.github/workflows/ci.yml`.
- [ ] T-12: Run all gate commands locally and confirm each exits 0; fix any failures before pushing.
- [ ] T-13: Verify `python3 scripts/check_feature_size.py size FEAT-000` exits 0.
- [ ] T-14: Verify `python3 scripts/check_feature_size.py task0` exits 0.

## Assumptions
- A-038 (Confirmed): Docker Compose file secrets at `/run/secrets/` for DB credentials; `read_secret()` reads those paths.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-000 plan.md; STD-001 v0.1; BED-001 v0.1; DBD-001 v0.1
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
