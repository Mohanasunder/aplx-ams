---
id: AIR-001
id_prefix: AIR
title: Phase 6 AI Pre-Review Reports
phase: 6
version: 0.1
template: ai-pre-review-report
template_version: 2.0
status: Draft
author_agent: ai-code-reviewer
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: 2026-10-18
validation: Pending
---

# Phase 6 AI Pre-Review Reports

<!-- Collection file. All AI pre-review reports are appended as `## AIR FEAT-NNN: [title]` sections. Never create a separate file per feature. Per-report status stored as HTML comments within each section. Approve each section individually with `/approve docs/06-build/ai-pre-review-reports.md --sub-id FEAT-NNN`. -->

## AIR FEAT-000: Walking Skeleton — Backend Scaffold and CI Pipeline

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes -->

### Input References

- FEAT-000 plan.md v0.1 (Approved 2026-10-17) — `docs/05-build-plan/feature-000-walking-skeleton/plan.md`
- FEAT-000-ACC v0.1 (Approved 2026-10-17) — `docs/05-build-plan/feature-000-walking-skeleton/acceptance.md`
- FEAT-000-TESTS v0.1 (Approved 2026-10-17) — `docs/06-build/FEAT-000-TESTS.md`
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17)
- `.ai/standards/agent-charter.md` (generated 2026-10-18)
- `.ai/standards/automated-gates.md`
- `.ai/standards/learned-rules.md` (no learned rules at time of review)
- DEC-053 and DEC-054 (approved deviations): Django pinned to `>=5.2.18,<5.3`; pytest expanded to `>=9.0.3,<10`

### Purpose And Scope

Advisory pre-review of the FEAT-000 (Walking Skeleton — Backend Scaffold and CI Pipeline) implementation on branch `feature/FEAT-000-walking-skeleton`. Covers: plan adherence, acceptance criteria coverage, code quality, security, and agent charter compliance for the files listed in plan.md Files To Create Or Modify. Frontend gates are out of scope for this feature (no frontend scaffold in FEAT-000). This review is advisory only; the human developer reviewer decides.

### Plan Adherence

**Files from plan.md "Files To Create Or Modify":**

| File | Present | Notes |
|---|---|---|
| `manage.py` | Yes | Clean, standard Django management script with type hints |
| `pyproject.toml` | Yes | All required tool sections present |
| `requirements.txt` | Yes | All New Packages present (with approved deviations DEC-053, DEC-054) |
| `Dockerfile` | Yes | See Minor finding 3 |
| `docker-compose.yml` | Yes | Correctly uses Docker Compose file secrets per A-038 |
| `.github/workflows/ci.yml` | Yes | All backend methodology and code-quality gates wired |
| `src/aplx_ams_django/settings/base.py` | Yes | See Major finding 2 |
| `src/aplx_ams_django/settings/production.py` | Yes | See Major finding 2 |
| `src/aplx_ams_django/urls.py` | Yes | Correctly routes `GET /api/health/` |
| `src/aplx_ams_django/health.py` | Yes | Clean implementation, correctly typed |
| `.secrets.baseline` | Yes | Committed |

**Implicit files (plan.md Risks section):**

| File | Present | Notes |
|---|---|---|
| `src/aplx_ams_django/__init__.py` | Yes | Empty, correct |
| `src/aplx_ams_django/settings/__init__.py` | Yes | Present |
| `src/aplx_ams_django/tests/__init__.py` | Yes | Present and locked |
| `src/aplx_ams_django/wsgi.py` | **NO** | **See Major finding 1** |

**New Packages — version compliance (plan.md vs requirements.txt):**

All 16 packages from the New Packages section are present. Two approved deviations apply:
- Django: plan `==5.2` → actual `>=5.2.18,<5.3` (DEC-053, approved security patch)
- pytest: plan `>=8,<9` → actual `>=9.0.3,<10` (DEC-054, approved CVE fix)

No unapproved packages added.

### Acceptance Criteria Coverage

| Criterion | Test / Gate | Coverage |
|---|---|---|
| STD-001 AC-1: `docker compose build app` exits 0 | `build` job in `.github/workflows/ci.yml` | Covered by CI gate |
| TST-001 AC-2: `pytest src/ --cov=src --cov-fail-under=80` exits 0 with health test passing | `test_health_returns_200` in `src/aplx_ams_django/tests/test_health.py` | Covered by pytest test + CI gate |
| STD-001 AC-3: `ruff check src/ && ruff format --check src/ && mypy src/ --strict` each exit 0 | `lint` and `typecheck` CI jobs | Covered by CI gates |
| STD-001 AC-4: `bandit -r src/ -ll && pip-audit && detect-secrets scan` each exit 0 | `sast`, `deps`, and `secrets` CI jobs | Covered by CI gates |

All four acceptance criteria have corresponding automated tests or CI gates. The criterion-to-test mapping matches the Approved FEAT-000-TESTS.md.

### Findings

| # | File | Line | Category | Severity | Issue |
|---|---|---|---|---|---|
| 1 | `Dockerfile` line 13; `src/aplx_ams_django/` (directory) | — | missing-wsgi-module | **Major** | `src/aplx_ams_django/wsgi.py` is absent. The Dockerfile CMD `gunicorn aplx_ams_django.wsgi:application` will raise `ModuleNotFoundError` at container start. `docker compose build app` passes (build only), but the container cannot run. Suggested fix: create and commit `src/aplx_ams_django/wsgi.py` with the standard Django content. |
| 2 | `src/aplx_ams_django/settings/base.py` line 23; `src/aplx_ams_django/settings/production.py` | — | production-allowed-hosts-wildcard | **Major** | `ALLOWED_HOSTS: list[str] = ["*"]` is set in base.py and is not overridden in production.py. With `DEBUG = False` Django accepts any `Host:` header, enabling host header injection attacks. Requires human decision: fix in FEAT-000 or explicitly scope to FEAT-001. |
| 3 | `Dockerfile` line 10 | 10 | dockerfile-debug-mode-default | Minor | `ENV DJANGO_SETTINGS_MODULE=aplx_ams_django.settings.base` sets the default to base settings (`DEBUG = True`). Suggested fix: set to `aplx_ams_django.settings.production` in the Dockerfile default. |
| 4 | `.github/workflows/ci.yml` line 291 | 291 | ci-migration-reverse-missing | Minor | The `migrate` CI job runs `python manage.py migrate --run-syncdb` but omits the reverse migration step. Acceptable for FEAT-000 (no app migrations), but the job is incomplete for when app migrations land. |
| 5 | `docker-compose.yml` lines 39–42 | 39–42 | secrets-setup-not-documented | Minor | `docker-compose.yml` references secret files but no setup instructions exist for developers. Add a `# See README for secrets setup` comment. |
| 6 | `.github/workflows/ci.yml` lines 215, 276 | 215, 276 | ci-plaintext-test-password | Info | `POSTGRES_PASSWORD: postgres` hardcoded in CI for ephemeral test containers. Acceptable; no change required. |
| 7 | `src/aplx_ams_django/settings/base.py` line 19 | 19 | base-settings-insecure-secret-key-fallback | Info | `read_secret()` falls back to insecure literal. Operational risk noted for Phase 8 runbook; no code change required for FEAT-000. |
| 8 | `.github/workflows/ci.yml` | — | ci-no-runtime-health-check | Info | No CI job verifies the health endpoint at runtime. Noted for Phase 8 runbook. |
| 9 | `.github/workflows/ci.yml` | — | ci-gate-coverage-partial | Info | Frontend CI gates absent — correct for FEAT-000 (backend-only). Must be added when frontend scaffold lands. |

### Security Observations

1. **Host header injection (Major — finding 2):** `ALLOWED_HOSTS = ["*"]` inherited by production.py. This can be exploited for password-reset link poisoning and SSRF. Requires human scope decision.
2. **Secret key fallback (Info — finding 7):** Silent insecure fallback; production runbook should verify the secret is mounted.
3. **Docker Compose secrets correctly implemented:** per A-038 and ADR A-17.
4. **No hardcoded production secrets detected.** `.secrets.baseline` committed.
5. **PASSWORD_HASHERS:** Argon2 first. Correct.
6. **AUTH_PASSWORD_VALIDATORS:** All four present. Correct.
7. **MIDDLEWARE empty:** Intentional per plan.md Out Of Scope (security middleware in FEAT-001).

### Escalation to Human

Finding 2 (ALLOWED_HOSTS wildcard) is a scope boundary question: plan.md Out Of Scope says "security middleware — covered by FEAT-001," but ALLOWED_HOSTS is not middleware — it is active in production.py today. If FEAT-001 does not list `settings/production.py` in its files, this will persist through all build features. Human reviewer decides: require fix in FEAT-000, or explicitly scope to FEAT-001.

### Verdict

**Needs changes (advisory).**

Two Major findings must be resolved before merge:
- **Finding 1 (missing-wsgi-module):** Standard fix — create `src/aplx_ams_django/wsgi.py`.
- **Finding 2 (production-allowed-hosts-wildcard):** Requires human scope decision (FEAT-000 vs FEAT-001).

Once addressed, the implementation should be ready for human review. Minor findings noted for follow-up but do not block.

### Assumptions

Not applicable.

### Open Questions

Finding 2 is escalated to the human reviewer as a design question. No new open questions raised.

### Traceability Links

- Upstream: FEAT-000 plan.md v0.1; FEAT-000-ACC v0.1; FEAT-000-TESTS v0.1; STD-001 v0.1; TST-001 v0.1; `.ai/standards/automated-gates.md`
- Downstream: Human PR review of `feature/FEAT-000-walking-skeleton`; `docs/logs/review-feedback-log.md` (two Major findings appended)

### Quality Checklist

- [x] Every section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
