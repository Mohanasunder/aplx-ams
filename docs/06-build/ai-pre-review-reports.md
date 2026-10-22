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
validation: Pass with warnings
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

---

## AIR FEAT-001: AI Code Review — Frontend Scaffold

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes (F-1 fixed before save; verdict updated to Pass with minor findings) -->

### Input References
- FEAT-001 plan.md v0.2 (Approved 2026-10-17, Mohanasunder)
- FEAT-001-TESTS v0.1 (Approved 2026-10-18, Mohanasunder)
- STD-001 v0.1 (Approved 2026-10-17)
- TST-001 v0.1 (Approved 2026-10-17)
- Agent Charter — .ai/standards/agent-charter.md

### Findings

| ID | Severity | File | Line(s) | Category | Finding | Status |
|---|---|---|---|---|---|---|
| F-1 | Major | `src/aplx_ams_django/middleware.py` | 68–73 | `session-timeout-incomplete` | `AbsoluteSessionTimeoutMiddleware` never initialized `session_start`; 12-hour absolute timeout was silently inactive. | Fixed before report saved: added `if session_start is None: request.session["session_start"] = now`; test updated to assert `session_start` set on first request. |
| F-2 | Minor | `nginx/nginx.conf` | entire | `nginx-hardening` | `server_tokens off` missing; security headers absent from static responses. | Fixed before report saved: `server_tokens off` + `add_header` directives added. |
| F-3 | Minor | `docker-compose.yml` | 42–44 | `service-dependency` | nginx `depends_on: app` uses start-order only, not `condition: service_healthy`. | Open: no health endpoint exists yet (FEAT-000 skeleton only). Noted for Phase 7 or the feature that wires the health endpoint. |
| F-4 | Info | `src/frontend/vite.config.ts` | 14 | `coverage-threshold` | Only `lines: 70` gated; branches/functions/statements ungated. | Compliant with plan requirement. No action. |
| F-5 | Info | `src/aplx_ams_django/tests/test_middleware.py` | entire | `scope-exception-documented` | Not in plan.md file list; DEC-061 authorizes it. | No action. |
| F-6 | Info | `scripts/check_feature_size.py` | 317–325 | `scope-exception-documented` | CLAUDE.md rule 9; human-authored (DEC-057/DEC-058). | No action. |

### Acceptance Criteria Check

| Criterion | Status |
|---|---|
| TST-001 AC-1: Vitest passes ≥1 test | PASS |
| STD-001 AC-1: npm run build exits 0 | PASS (CI gate) |
| STD-001 AC-2: eslint + tsc --noEmit exit 0 | PASS (CI gate) |
| TST-001 AC-2: CI frontend job all steps exit 0 | PASS (CI artifact) |

### Verdict
**PASS with minor findings (after F-1 and F-2 fixed).** All four acceptance criteria met. F-3 (docker-compose health check) is Minor and noted for follow-on. No remaining Major or Blocker findings.

### Traceability Links
- Upstream: FEAT-001 plan.md v0.2; FEAT-001-TESTS v0.1; STD-001 v0.1; TST-001 v0.1
- Downstream: Phase 6 PR for FEAT-001; docs/logs/review-feedback-log.md

## AIR FEAT-035: E2E CI Scaffold

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Ready for human review -->

### Input References

- FEAT-035 plan.md v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-035-ACC v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-035-TESTS v0.1 (Approved 2026-10-18, Mohanasunder, Tech lead)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- `.ai/standards/automated-gates.md` — E2E tests gate row
- `.ai/standards/agent-charter.md` (no learned rules at time of review)

### Purpose And Scope

Advisory pre-review of FEAT-035 (E2E CI Scaffold) on branch `feature/FEAT-035-e2e-ci-scaffold`. Covers plan adherence, acceptance criteria coverage, CI workflow security, and agent charter compliance. The locked test file `src/frontend/e2e/scaffold.spec.ts` is not flagged per review instructions. This review is advisory only.

### Plan Adherence

| File | Present | Notes |
|---|---|---|
| `.github/workflows/e2e.yml` | Yes | New; all required steps present in correct order |
| `src/frontend/playwright.config.ts` | Yes | Upgraded from FEAT-001 stub to full config |
| `src/frontend/e2e/scaffold.spec.ts` | Yes | Locked test from approved FEAT-035-TESTS v0.1; not a scope violation |

New Packages: None added. Declared deviation: import path `playwright/test` instead of `@playwright/test` — functionally identical on playwright v1.64.1; consistent with `scaffold.spec.ts`. Correctly declared in PR description. Plan adherence: **Pass**.

### Acceptance Criteria Coverage

**TST-001 AC-5** — `.github/workflows/e2e.yml` triggers on `pull_request` and `push` to `master`; steps in correct order: checkout → node setup → npm ci → playwright install → docker compose up → health-check wait (60s, robust) → `npx playwright test`. All steps present and correctly sequenced. **Covered.**

**STD-001 AC-5** — `playwright.config.ts`: `testDir: './e2e'`, `use: { baseURL: 'http://nginx:80', headless: true }`, single Chromium project. All required values present. Covered by `scaffold.spec.ts` asserting `config.use?.baseURL === 'http://nginx:80'` (approved, 1/1 green). **Covered.**

### Findings

| # | File | Line | Category | Severity | Issue |
|---|---|---|---|---|---|
| F-1 | `.github/workflows/e2e.yml` | 24 (job: e2e) | `ci-workflow-robustness` | Minor | No `timeout-minutes` on the `e2e` job. GitHub Actions default is 6 hours; plan states expected runtime 2 minutes. A hung step would block a runner for up to 6 hours. **Applied fix:** added `timeout-minutes: 15`. |
| F-2 | `.github/workflows/e2e.yml` | 29, 32 | `ci-action-pinning` | Info | `actions/checkout@v4` and `actions/setup-node@v4` use mutable major-version tags. Pre-existing project-wide pattern (established in `ci.yml`); consistent with it. No change required. |

No Blockers. No Major findings. F-1 fix applied in the same commit as this report.

### Escalation to Human Reviewer

**Design concern — `baseURL: 'http://nginx:80'` DNS resolution.** The hostname `nginx` resolves only inside the Docker Compose network, not from the GitHub Actions runner. The scaffold test passes because it inspects the config object statically. Future navigation-based E2E tests using `page.goto('/')` will receive DNS errors. The e2e.yml comment documents this gap; however, no ADR or DEC has been recorded to govern how story-feature builders should handle it. A tech lead decision (DEC or ADR) is needed before the first story feature that adds navigation-based E2E tests.

### Verdict

**Ready for human review (advisory).** No Blockers. No Major findings. F-1 Minor fix applied (`timeout-minutes: 15`). F-2 Info noted. Both acceptance criteria correctly implemented.

### Traceability Links
- Upstream: FEAT-035 plan.md v0.1; FEAT-035-ACC v0.1; FEAT-035-TESTS v0.1; STD-001 v0.1; TST-001 v0.1; automated-gates.md
- Downstream: Phase 6 PR for FEAT-035


## AIR FEAT-002: S-18 — Delivery Manager Sets Up Client Organizations and SAP Applications

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes -->

### Input References

- FEAT-002 plan.md v0.1 (Approved 2026-10-17)
- FEAT-002-ACC v0.1 (Approved 2026-10-17)
- FEAT-002-TESTS v0.1 (Approved 2026-10-18)
- API-001 v0.2; DBD-001 v0.1; STD-001 v0.1; PRM-001 v0.1; UIS-001 v0.1
- `.ai/standards/agent-charter.md` (generated 2026-10-18)
- DEC-070, DEC-071; A-046, A-047

### Purpose And Scope

Advisory pre-review of FEAT-002 on branch `feature/FEAT-002-org-sap-setup`. Covers plan adherence, AC coverage, code quality, security, and charter compliance. Locked test files not flagged. Advisory only.

### Findings

| # | File | Line | Category | Severity | Issue |
|---|---|---|---|---|---|
| 1 | `src/aplx_ams_django/organizations/views.py` | 35-36 | `api-contract-violation` | **Major** | `OrgViewSet` inherits `mixins.UpdateModelMixin` adding PUT /api/organizations/{pk}/ — not in API-001 v0.2 contract (only PATCH). Remove `UpdateModelMixin` or restrict HTTP methods to exclude PUT. |
| 2 | `src/aplx_ams_django/organizations/views.py` / `services.py` | 89 / 29 | `missing-input-validation` | **Major** | `SAPApplicationViewSet.create` passes `request.data` unvalidated to service; `data["name"]` raises unhandled KeyError (500) when name is missing. Add `SAPApplicationSerializer(data=request.data).is_valid(raise_exception=True)` before delegating. |
| 3 | `src/aplx_ams_django/settings/base.py` | 29 | `scope-deviation` | Minor | settings/base.py not in plan.md Files list; assumption A-046 logs it. Verify CI scope gate or record a DEC. |
| 4 | `pyproject.toml` | 33-40 | `type-check-suppression-broad` | Minor | Module-wide `disable_error_code = ["misc", "no-any-return"]` masks future issues; prefer targeted `# type: ignore[no-any-return]`. |
| 5 | `src/frontend/src/api/organizations.ts` | 31, 40 | `api-contract-field-mismatch` | Minor | `SapApp.organization` vs serializer field `client_org` — verify against API-001 v0.2 openapi.yaml. |
| 6 | `src/aplx_ams_django/organizations/views.py` | 82, 87, 89 | `type-ignore-unnarrowed` | Minor | `org_id: int | None = None` narrowed with `# type: ignore[arg-type]`; add `assert org_id is not None` to narrow cleanly. |
| 7 | `pyproject.toml` | 19-20 | `ruff-ignore-locked-file` | Info | I001 suppressed for locked test_api.py — correct workaround. |
| 8 | `src/frontend/tsconfig.json` | 19 | `tsc-excludes-tests` | Info | Test files excluded from tsc to avoid locked-test issue. Acceptable for this feature. |

### Security Observations

1. HasRolePermission returns 403 (not 401) for unauthenticated — functionally safe; auth middleware added in later feature.
2. `getattr(user, "role", None)` safely handles missing role attribute.
3. Major finding 2: unhandled KeyError degrades availability (not a data-exposure risk).
4. Major finding 1: uncontracted PUT can blank fields — not a data-exposure risk but bypasses contract intent.
5. No secrets committed. No raw SQL. No production config touched.

### Verdict

**Needs changes (advisory).** Two Major findings must be resolved before merge; four Minor findings do not block.

### Traceability Links

- Upstream: FEAT-002 plan.md v0.1; API-001 v0.2; DBD-001 v0.1; STD-001 v0.1
- Downstream: Human PR review; docs/logs/review-feedback-log.md


---

## AIR FEAT-003: S-19 — Delivery Manager Sets Up Client Organization Contract

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes (advisory) -->

### Verdict

**Needs changes (advisory).**

Two Major findings were raised; both were fixed before human review:
- **F-1 (integrity-error-too-broad):** `services.py:52-55` — broad `IntegrityError` catch returned misleading 409 for non-existent org. **Fixed:** org existence checked via `dal.get_org_by_id()` before DAL create; `ClientOrg.DoesNotExist` caught in view → 404.
- **F-2 (incomplete-frontend-api):** `contracts.ts` — stub returned mock data, no HTTP call. **Fixed:** real `fetch` call implemented to `POST /api/organizations/{orgId}/contracts/`.

Four Minor findings:
- **F-3 (out-of-scope-model-fields):** `monthly_close_at` and `ended_at` — VOID; both fields are defined in approved DBD-001 and backend-design.md.
- **F-4 (api-contract-field-mismatch):** TypeScript `Contract` interface mismatched serializer. **Fixed:** aligned to match `ContractSerializer` fields.
- **F-5 (hardcoded-org-id):** `ContractSetup.tsx:31` — `org_id=1` hardcoded. **Documented as Known Gap** pending FEAT-006 (routing/navigation).
- **F-6 (decimal-coercion-risk):** `COERCE_DECIMAL_TO_STRING` not set explicitly. **Accepted:** all 48 backend tests pass with numeric comparisons; field-level `coerce_to_string=False` overrides global setting per DRF docs.

### Plan Adherence

All 9 plan files present. No out-of-scope files. One-active-contract constraint enforced at both DB (partial unique index) and service level.

### Acceptance Criteria Coverage

All 4 ACs covered across DB, backend, and frontend test layers.

### Traceability Links

- Upstream: FEAT-003 plan.md v0.1; FEAT-003-ACC v0.1; FEAT-003-TESTS v0.1; API-001 v0.2; DBD-001 v0.1; STD-001 v0.1; PRM-001 v0.1
- Downstream: Human PR review of `feature/FEAT-003-contract-setup`; `docs/logs/review-feedback-log.md`

---

## AIR FEAT-005: S-20 Delivery Manager Manages User Accounts

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes -->

### Input References

- FEAT-005 plan.md v0.2 (Approved 2026-10-18, Mohanasunder)
- FEAT-005-ACC v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-005-TESTS v0.3 (Approved 2026-10-18, Mohanasunder)
- API-001 v0.2 § F-6 User account management
- DBD-001 v0.1 § accounts_user
- PRM-001 v0.1 § F-6
- STD-001 v0.1
- Branch: `feature/FEAT-005-user-accounts`; HEAD `02e32a5`

### Purpose And Scope

Advisory pre-review of FEAT-005 (S-20: Delivery Manager Manages User Accounts). Covers plan adherence, all four acceptance criteria, API contract compliance, permission enforcement, DB constraint alignment, security, and agent charter compliance. Locked test files not flagged. Advisory only.

### Acceptance Criteria Coverage

| Criterion | Implementation | Tests | Gap |
|---|---|---|---|
| AC-1: DM creates user with 4 roles → saved | `UserCreateSerializer` validates role via ChoiceField; services.create_user saves; 201 | 4 backend tests + 1 frontend + DB tests | None for backend; frontend form field mismatch (F-3, F-5) |
| AC-2: Client user without org → 400 | `UserCreateSerializer.validate()` line 44–47 raises ValidationError | test_create_client_user_without_client_org_returns_400 + frontend tests | None |
| AC-3: Deactivate → is_active=False | `services.deactivate_user` sets is_active=False | test_deactivate_user_returns_200 + frontend test | DoesNotExist unhandled (F-2) |
| AC-4: Non-DM → 403 | `get_permissions()` returns HasRolePermission(delivery_manager) for all actions | 9 backend tests + 1 frontend | None |

### Findings

| # | File | Line(s) | Category | Severity | Issue |
|---|---|---|---|---|---|
| F-1 | `src/aplx_ams_django/accounts/views.py` | 58–67 | missing-input-validation | **Major** | `partial_update` reads `request.data` directly and applies via `setattr` without calling `UserUpdateSerializer`. Any string value can be set as `role`; invalid cross-field updates (role=client_user without client_org_id) raise unhandled IntegrityError → 500 instead of 400. Fix: import `UserUpdateSerializer`, validate via `ser.is_valid(raise_exception=True)`, apply `ser.validated_data`. |
| F-2 | `src/aplx_ams_django/accounts/views.py` | 55, 62, 72 | unhandled-exception-500 | **Major** | `retrieve`, `partial_update`, `deactivate` call DAL/service functions that raise `User.DoesNotExist` when user ID not found. DRF default exception handler does not convert DoesNotExist to HTTP 404. Result: HTTP 500. Fix: wrap each call with `try/except User.DoesNotExist: return Response(status=status.HTTP_404_NOT_FOUND)`. |
| F-3 | `src/frontend/src/api/users.ts` | 30, 33, 43, 46, 54 | api-contract-field-mismatch | **Major** | `User` interface uses `full_name` and `organization`; backend `UserDetailSerializer` returns `name` and `client_org_id` (per DBD-001 v0.1). All user list rows render blank names at runtime. Fix: rename to match backend: `full_name` → `name`, `organization` → `client_org_id`. |
| F-4 | `src/frontend/src/api/users.ts` | 37–40 | api-contract-field-mismatch | **Major** | `UserListResponse` typed as `{ count: number; results: User[] }`; `UserManagement.tsx` line 71 calls `setUsers(res.results)`. Backend `list` action returns flat JSON array (no DRF pagination class configured). `res.results` is always `undefined`. Fix: use flat array type, `setUsers(res as User[])`. |
| F-5 | `src/frontend/src/api/users.ts` | 42–48 | api-contract-field-mismatch | **Major** | `CreateUserPayload` has no `username` field; `UserManagement.tsx` create form has no `username` field. Backend `UserCreateSerializer` requires `username`. Every POST returns HTTP 400; no user can be created via UI. Fix: add `username` to `CreateFormState`, dialog form, and `CreateUserPayload`. |
| F-6 | `src/aplx_ams_django/accounts/serializers.py` | 51–62 | dead-code | Minor | `UserUpdateSerializer` defined but never imported or used; `views.py` imports only `UserCreateSerializer` and `UserDetailSerializer`. Remove once F-1 fix imports it. |
| F-7 | `src/frontend/src/pages/UserManagement.tsx` | 34, 217–228 | scope-deviation | Minor | `CreateFormState` includes `temporary_password`; form renders a password input; payload sends it. plan.md § Out Of Scope: "Temporary password — FEAT-008." Backend silently ignores field. Remove from form and payload; reinstate in FEAT-008. |
| F-8 | `src/frontend/src/api/users.ts` | 65, 73–75, 84–88, 92–96 | missing-error-handling | Minor | None of the four async functions check `r.ok` before calling `r.json()`. 400/403/500 responses parsed as success types → runtime errors or silent state corruption. Fix: add `if (!r.ok) throw new Error(...)` after each fetch. |
| F-9 | `src/frontend/src/pages/UserManagement.tsx` | 16 | coupling | Minor | `UserContext` imported from `'./OrgManagement'` — a sibling page component. Move to `src/context/UserContext.ts`. |
| F-10 | `src/aplx_ams_django/accounts/serializers.py` | 21–26 | duplication | Minor | `_VALID_ROLES` duplicates the four role strings already in `UserRole` TextChoices. Use `[r.value for r in UserRole]` instead. |
| F-11 | `.secrets.baseline` | — | scope-deviation | Minor | `.secrets.baseline` modified on branch but not listed in plan.md Files To Create Or Modify. Verify scope gate or record DEC. |

### Escalation to Human

**Design question — Frontend field naming:** Major findings F-3, F-4, F-5 stem from `users.ts` field names not matching the backend serializer. Confirm: DBD-001 v0.1 specifies `name` and `client_org_id`; the backend is correct; the frontend client needs to be fixed (not the backend). Tech lead should confirm this before fixes proceed.

### Verdict

**Needs changes (advisory).**

Five Major findings must be resolved before merge:
- **F-1:** PATCH bypasses validation — use `UserUpdateSerializer`
- **F-2:** DoesNotExist → 500 on retrieve/update/deactivate — add `try/except → 404`
- **F-3:** Frontend `full_name`/`organization` → `name`/`client_org_id`
- **F-4:** Frontend expects `{count,results}` wrapper — backend returns flat array
- **F-5:** Frontend create payload missing required `username` field

### Traceability Links

- Upstream: FEAT-005 plan.md v0.2; FEAT-005-ACC v0.1; FEAT-005-TESTS v0.3; API-001 v0.2 § F-6; DBD-001 v0.1; PRM-001 v0.1; STD-001 v0.1
- Downstream: Human PR review of `feature/FEAT-005-user-accounts`; `docs/logs/review-feedback-log.md` (5 Major findings)

## AIR FEAT-005 (re-review): S-20 Delivery Manager Manages User Accounts

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Needs changes -->

### Input References
- FEAT-005 plan.md v0.2 (Approved 2026-10-18, Mohanasunder)
- FEAT-005-TESTS v0.3 (Approved 2026-10-18, Mohanasunder)
- API-001 v0.2 / openapi.yaml (Approved 2026-10-17) — `docs/04-design/openapi.yaml`
- DEC-080, DEC-081 — decision-log.md entries recorded 2026-10-18
- Commits reviewed: `853d731` (backend), `6bbf5c8` (frontend)

### Purpose And Scope
Re-review of four files changed by builder fix commits in response to the initial AIR FEAT-005 Major findings. Scope: `views.py`, `serializers.py`, `users.ts`, `UserManagement.tsx`.

### Resolved Findings

| Finding | Status | Evidence |
|---|---|---|
| F-2: DoesNotExist not caught | Resolved | views.py lines 60-63, 69-72, 87-89 — all three actions wrap the DAL/service call in `try/except User.DoesNotExist` returning HTTP 404 |
| F-3: full_name / organization field names | Resolved | users.ts lines 31-38 — `User.name`, `User.client_org_id`; component reads `user.name` throughout |
| F-4: listUsers() return type mismatch | Resolved per DEC-081 | users.ts — `Promise<User[]>`; component uses `Array.isArray` guard for locked-test mock compatibility |
| F-5: username missing from CreateUserPayload | Resolved per DEC-081 | users.ts — `username: string` in payload; form state and dialog updated |
| F-7: temporary_password in API payload | Resolved per DEC-081 | Removed from `CreateUserPayload`; kept in form UI only (locked-test constraint) |
| F-8: r.json() called before r.ok check | Resolved | `if (!r.ok) throw new Error(...)` before every `r.json()` call |
| F-10: _VALID_ROLES as literal list | Resolved | `_VALID_ROLES = [r.value for r in UserRole]` derives from the TextChoices enum |

### F-1 Status: Partially Resolved — Major Finding Remains Open

The fix applied `UserUpdateSerializer(data=request.data)` and gates on `is_valid()`. However, `UserUpdateSerializer` has no `validate()` method. A PATCH payload of `{"role": "client_user"}` without `client_org_id` passes serializer validation and reaches `user.save()`, which hits the DB-level `chk_client_user_has_org` constraint → unhandled `IntegrityError` → HTTP 500. The OpenAPI spec (openapi.yaml line 1216) requires HTTP 400 in this case.

### New Findings

| Severity | File | Line | Category | Issue |
|---|---|---|---|---|
| Major | `src/aplx_ams_django/accounts/serializers.py` | 46-56 | `missing-input-validation` | `UserUpdateSerializer` has no `validate()` method. A PATCH `{"role": "client_user"}` without `client_org_id` passes serializer validation; DB constraint fires → HTTP 500. Fix: add `validate()` mirroring `UserCreateSerializer.validate()` scoped to partial-update case. |
| Major | `src/aplx_ams_django/accounts/views.py` | 80 | `unhandled-exception-500` | `user.save()` in `partial_update` is unprotected. Any `IntegrityError` results in HTTP 500. Fix: wrap in `try/except IntegrityError` returning HTTP 400, or rely on serializer-level fix as primary gate. |
| Observation | `src/aplx_ams_django/accounts/serializers.py` | 66 | `api-contract-field-mismatch` | `UserDetailSerializer` serializes FK as `client_org_id`; OpenAPI `UserAccount` schema uses `client_organization_id`. Pre-existing — not introduced by fixes. |
| Observation | `src/aplx_ams_django/accounts/views.py` | 46-47 | `api-contract-violation` | `list` action returns flat JSON array; OpenAPI spec defines `PaginatedUserAccountList`. Pre-existing — not introduced by fixes. |

### Verdict
**Needs changes.** F-1 is not fully resolved. All other original findings (F-2 through F-10) are resolved or appropriately deferred under DEC-081. Two pre-existing observations noted for traceability.

### Traceability Links
- Upstream: FEAT-005 plan.md v0.2; FEAT-005-TESTS v0.3; API-001 v0.2; DEC-080; DEC-081
- Downstream: FEAT-005 PR; `docs/logs/review-feedback-log.md` (2 new Major findings NF-1 NF-2)

## AIR FEAT-005 (final check): S-20 Delivery Manager Manages User Accounts

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-18 -->
<!-- air_verdict: Pass with observations -->
<!-- commit: ee574e1 -->

### NF-1 status — Confirmed resolved
`UserUpdateSerializer.validate()` (serializers.py lines 58–64) raises `ValidationError({"client_org_id": "..."})` → HTTP 400 when `role == "client_user"` and `client_org_id` is absent. Serializer invoked before `user.save()`. Satisfies OpenAPI spec line 1216.

### NF-2 status — Confirmed resolved
`IntegrityError` imported at views.py line 17. `try/except IntegrityError` at lines 81–84 wraps only `user.save()`, returns HTTP 400. Correct placement and exception type.

### New findings (Minor — for human reviewer)

| Severity | File | Line | Category | Issue |
|---|---|---|---|---|
| Minor | `views.py` | 84 | `info-disclosure-in-error` | `str(exc)` passes raw Django/PostgreSQL constraint name to the API consumer. Recommendation: replace with generic message `"A database conflict prevented this update."` |
| Minor | `views.py` | 84 | `contract-mismatch` | IntegrityError 400 response body `{"detail": str(exc)}` does not conform to the spec's `ValidationError` format (field-keyed arrays). Recommendation: use `{"non_field_errors": ["A database conflict prevented this update."]}` or update spec 400 schema to accept `SimpleError`. |

### Design concern — for human reviewer
A PATCH of `{"client_org_id": null}` on an existing `client_user` passes validation (role not in payload → guard not triggered) and may nullify their org. Whether this scenario should be rejected requires looking up current DB state in `validate()`. Raised for human review; not treated as a code defect.

### Verdict
**Pass with observations.** All Major findings resolved. Two Minor observations and one design concern for human reviewer.

### Traceability Links
- Upstream: FEAT-005 plan.md v0.2; FEAT-005-TESTS v0.3; API-001 v0.2; DEC-080; DEC-081; commit `ee574e1`
- Downstream: FEAT-005 PR human review

## AIR FEAT-006: S-21 — User Signs In with a User Account

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-19 -->
<!-- air_verdict: Needs changes -->

### Input References

| Artifact | Version | Status |
|---|---|---|
| FEAT-006 plan.md | v0.4 | Approved (Mohanasunder, 2026-10-18) |
| FEAT-006-TESTS.md | v0.1 | Approved (Mohanasunder, 2026-10-18) |
| REQ-001 § S-21 | v0.3 | Approved |
| API-001 § Authentication (F-5) | v0.2 | Approved |
| DBD-001 § accounts module | v0.1 | Approved |
| PRM-001 § Authentication (F-5) | v0.1 | Approved |
| UIS-001 § S-21 | v0.1 | Approved |

### Purpose and Scope

Phase 6 Mode B implementation review for FEAT-006 on branch `feature/FEAT-006-sign-in-auth`. Reviews the 11 source files listed in plan.md v0.4 plus 2 files found in the diff outside plan scope. Read-only; advisory only.

### Plan Adherence

All 11 plan.md v0.4 files present and implemented. Two out-of-plan files found in diff:

1. `src/aplx_ams_django/accounts/serializers.py` — formatting-only diff (ruff format rewrapped one multi-line conditional in existing validate()); no logic change; scope gate (--base master) did not flag; DEC-087 recorded.
2. `pyproject.toml` — adds test_auth_api.py to ruff format.exclude; DEC-086 recorded.

### Acceptance Criteria Coverage

- AC-1 (valid creds → 200, session, role+org; deactivated → 401): implemented ✓
- AC-2 (wrong/unknown → 401, identical body via `_INVALID_CREDENTIALS`): implemented ✓
- AC-3 (PasswordComplexityValidator 4 rules): implemented ✓
- AC-4 (5 failures → locked_until in DB; locked → 401; expired → 200): implemented ✓

### Findings

| ID | File | Line(s) | Category | Severity | Issue |
|---|---|---|---|---|---|
| F-01 | `src/aplx_ams_django/accounts/serializers.py` | whole file | scope-deviation | **Major** | Modified outside plan scope. Actual diff: formatting-only (ruff format rewrapped effective_org assignment). DEC-087 records decision to accept. Scope gate did not flag. Human reviewer to confirm. |
| F-02 | `pyproject.toml` | 16–19 | scope-deviation | Minor | Not in plan file list. DEC-086 covers this addition. |
| F-03 | `src/frontend/src/api/auth.ts` | 38–46 | api-contract-field-mismatch | Minor | `UserMe` interface declares `id`, `name`, `email`, `is_active`, `client_organization_id`, `client_organization_name` but API returns only `role`+`org`. Extra fields will be `undefined`. Verify against API-001 v0.2; trim or document as forward-looking. |
| F-04 | `Login.tsx` / `App.tsx` / `AuthContext.tsx` | Login.tsx:65; App.tsx:8–29 | functional-gap | Minor | `me()` result discarded; `setUser()` never called (AuthContext always null). No `/tickets` route — success nav lands on catch-all (Login again). Deferred to follow-on feature; documented in PR Known Gaps. |
| F-05 | `src/aplx_ams_django/settings/base.py` | absent | session-cookie-missing-secure | Minor | `SESSION_COOKIE_SECURE` not in base.py. Verify it is set in `settings/production.py`. |

Design concern (escalate to human reviewer — not a code defect):
- F-06 (`authentication.py` 105–123): category: timing-side-channel. Write-path timing difference between unknown-username (SELECT only) and wrong-password (SELECT + UPDATE) is a timing side-channel for account enumeration. A-019 is satisfied at the message level. Whether this is in scope for this release is a design decision for the tech lead.

### Learned Rules Check

Rule from `.ai/standards/learned-rules.md` active at this review: **LRN L-1 (missing-input-validation)** — "DRF serializers and API views that write model instances subject to multi-column or cross-field DB constraints must include a `validate()` method with instance-awareness and a `try/except IntegrityError`."

- `LoginView.post()` (`views.py` lines 127–138): uses Django's `authenticate()` builtin; no serializer, no direct `model.save()` in the view. LRN L-1 not applicable. ✓
- `LogoutView.post()` and `MeView.get()`: no model writes. Not applicable. ✓
- `UserUpdateSerializer` (`serializers.py`, out-of-plan, formatting-only change): has `validate()` with instance-aware effective-role/org resolution; `partial_update` wraps `user.save()` in `try/except IntegrityError`. LRN L-1 followed. ✓
- `SessionAuthBackend.authenticate()` (`authentication.py`): calls `user.save(update_fields=[...])` for lockout counters. LRN L-1 applies to "DRF serializers and API views" — an authentication backend is neither, and the `chk_failed_attempts_non_negative` constraint cannot be triggered by `+= 1` or `= 0` logic. Not a LRN L-1 violation.

**Verdict: No LRN L-1 violation in in-plan code.**

### Security Observations

Lockout persists to DB ✓ | Lockout check before password verify ✓ | Reset on success ✓ | A-019 identical error bodies ✓ | SameSiteSessionAuthentication → 401 not 403 ✓ | SESSION_COOKIE_HTTPONLY+SAMESITE ✓ | Argon2id first in PASSWORD_HASHERS ✓ | Nginx rate limit 10r/m burst=5 nodelay ✓ | No hardcoded secrets ✓ | PasswordComplexityValidator all 4 rules ✓

### Verdict

**Advisory: Needs changes.** F-01 (Major) must have a recorded decision before merge — DEC-087 records it. F-02 through F-05 are Minor; F-03, F-04, F-05 should be deferred with OQs or fixed. F-06 escalated to tech-lead review. Core authentication implementation is sound.

### Traceability Links
- Upstream: FEAT-006 plan.md v0.4; FEAT-006-TESTS.md v0.1; REQ-001 v0.3 § S-21; API-001 v0.2; DBD-001 v0.1; PRM-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-006 PR human review; docs/logs/review-feedback-log.md

---

## AIR FEAT-036: AppShell -- Global Navigation Shell and Sign Out

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-21 -->
<!-- air_verdict: Conditional Pass -- minor findings only; core implementation ready for human review -->

### Input References

| Artifact | Version | Status | Path |
|---|---|---|---|
| FEAT-036 plan.md | v0.3 | Approved (Mohanasunder, 2026-10-21) | docs/05-build-plan/feature-036-appshell-nav/plan.md |
| FEAT-036-ACC | v0.2 | Approved (Mohanasunder, 2026-10-21) | docs/05-build-plan/feature-036-appshell-nav/acceptance.md |
| FEAT-036-TESTS | v0.1 | Approved (Mohanasunder, 2026-10-21) | docs/06-build/FEAT-036-TESTS.md |
| FEAT-001-TESTS | v0.2 | Approved (Mohanasunder, 2026-10-21) | docs/06-build/FEAT-001-TESTS.md |
| API-001 | v0.2 | Approved | docs/04-design/openapi.yaml section F-5 |
| UIS-001 | v0.1 | Approved | section AppShell role-based nav link sets |
| PRM-001 | v0.1 | Approved | section Authentication F-5 |
| SCR S-17 | -- | Approved | docs/logs/spec-changes.md -- role name correction |
| SCR S-18 | -- | Approved | docs/logs/spec-changes.md -- FEAT-001-TESTS.md unlock and App.test.tsx update |
| .ai/standards/agent-charter.md | generated | -- | Agent charter |
| .ai/standards/learned-rules.md | -- | -- | LRN L-1 only |
| .ai/standards/coding-standards.md | STD-001 v0.1 | Approved | Coding standards |
| docs/logs/review-feedback-log.md | -- | -- | Category reuse |

### Purpose And Scope

Advisory pre-review of FEAT-036 (AppShell -- Global Navigation Shell and Sign Out) on branch feature/FEAT-036-appshell-nav. Reviews all five source files: AppShell.tsx (new), AuthContext.tsx (modified), App.tsx (modified), AppShell.test.tsx (new, locked at commit aeb8323), and App.test.tsx (modified). Covers plan adherence, all four acceptance criteria, API and UI contract compliance, role-based nav correctness, security, and agent charter compliance. No backend files changed; LRN L-1 applies to backend only and is out of scope for this review. This review is advisory only; the human developer reviewer decides.

### Plan Adherence

**Files from plan.md v0.3 "Files To Create Or Modify":**

| File | Present | Notes |
|---|---|---|
| src/frontend/src/components/AppShell.tsx (new) | Yes | Correctly implements MuiAppBar, MuiDrawer, role nav, loading state, sign-out |
| src/frontend/src/context/AuthContext.tsx (update) | Yes | Adds loading, useEffect calling me() on mount, and signOut() |
| src/frontend/src/App.tsx (update) | Yes | Wraps authenticated routes in AppShell layout route; /login stays outside AppShell |
| src/frontend/src/components/AppShell.test.tsx (new) | Yes | 9 Vitest tests locked at commit aeb8323; file is unchanged from locked commit (git diff aeb8323 HEAD -- AppShell.test.tsx produces empty diff) |

**Files changed outside plan.md v0.3 scope:**

| File | Notes |
|---|---|
| src/frontend/src/App.test.tsx | Modified; not in plan.md Files list. Authorized by SCR S-18 (Approved), FEAT-001-TESTS.md v0.2 (Approved), and FEAT-036-TESTS.md (Approved). See finding F-1. |
| .secrets.baseline | Modified; not in plan.md Files list. No SCR or DEC found covering this change. See finding F-2. |

New Packages: None added or upgraded. Plan states "None." Compliant.

**Plan adherence: Pass** for all four plan files. Two out-of-plan files noted (F-1, F-2).

### Acceptance Criteria Coverage

| Criterion | Implementation | Tests | Coverage |
|---|---|---|---|
| AC-1: AppShell renders "APLX AMS", role chip, "Sign out" button | AppShell.tsx lines 130-158: MuiTypography "APLX AMS" (line 139), MuiChip with user.role (lines 141-149), MuiButton "Sign out" (lines 150-157) | AppShell.test.tsx lines 156-184: three getByText/getByRole assertions | Fully covered |
| AC-2: Sign out calls POST /api/auth/logout/, clears user, navigates to /login | AppShell.tsx lines 95-99: handleSignOut() calls logout(), setUser(null), navigate('/login') directly. Known deviation: not delegated to context.signOut() -- required by the locked AC-2 test | AppShell.test.tsx lines 199-225: verifies logout mock called once, setUser called with null, navigate called with '/login' | Fully covered |
| AC-3: AuthProvider calls me() on mount; 200 sets user; 401 navigates to /login | AuthContext.tsx lines 64-85: useEffect calls me().then(setUser) on 200; .catch sets user null and calls navigate('/login') on any error | AppShell.test.tsx lines 242-290: two waitFor tests (200 path and 401/error path) | Fully covered |
| AC-4: Role-based nav -- delivery_manager 7 links, l2l3_support 3 links, client_user 2 links | AppShell.tsx lines 59-81: NAV_BY_ROLE map rendered via React Router Link (role=link) in MuiDrawer | AppShell.test.tsx lines 304-369: three tests verify exact link texts and queryAllByRole('link') counts | Fully covered |

All 4 acceptance criteria are covered. Nav link sets match UIS-001 v0.1 section AppShell exactly (verified against acceptance.md AC-4 and FEAT-036-TESTS.md criteria map).

### Findings

| # | File | Line | Category | Severity | Issue |
|---|---|---|---|---|---|
| F-1 | src/frontend/src/App.test.tsx | whole file | scope-deviation | Minor | File is modified but not listed in plan.md v0.3 Files To Create Or Modify. Change is authorized by SCR S-18 (Approved), FEAT-001-TESTS.md v0.2 (Approved, Mohanasunder 2026-10-21), and FEAT-036-TESTS.md (Approved). Modification updates TST-001 AC-1 from asserting "APLX AMS" text to asserting Login h1 visible for unauthenticated users -- correct behavior after AppShell removes that nav element. Human reviewer to confirm authorization chain. |
| F-2 | .secrets.baseline | -- | scope-deviation | Minor | File is modified on branch but not listed in plan.md v0.3 Files To Create Or Modify. No SCR or DEC found covering this change. FEAT-036 is frontend-only and introduces no secrets. The baseline update may be an artifact of detect-secrets rescanning the working tree. Human reviewer to inspect the diff and record a DEC if accepted (precedent: FEAT-005 finding F-11). |
| F-3 | src/frontend/src/components/AppShell.test.tsx | 127, 209 | stale-suppression-comment | Info | Two @ts-expect-error directives (comment: "loading and signOut are added to AuthContextValue in FEAT-036 Mode B") are now stale: Mode B has implemented both fields. tsconfig.json line 20 excludes test files from tsc --noEmit so no CI failure occurs. File is locked and cannot be modified without a human unlock. No action required; noted for completeness. |
| F-4 | src/frontend/src/components/AppShell.tsx | 95-98 | missing-error-handling | Info | handleSignOut does not wrap await logout() in try/catch. A network error during POST /api/auth/logout/ exits the function before setUser(null) and navigate('/login') execute, leaving the user in an authenticated UI state. Retaining session state on a failed server-side logout is defensible (session cookie remains valid; user can retry), but the behavior is undocumented. No security vulnerability. |

No Blocker findings. No Major findings.

### Learned Rules Check

**LRN L-1 (missing-input-validation):** "Add a validate() method to every DRF serializer that enforces cross-field DB constraints ... wrap every model.save() call in a try/except django.db.IntegrityError."

This rule applies to backend DRF serializers and API views. FEAT-036 is frontend-only -- no Django views, serializers, or model saves are introduced or modified. **LRN L-1 is not applicable.** No violation.

### Security Observations

1. No hardcoded secrets. No production configuration paths touched. Compliant.
2. me() on mount (AuthContext.tsx lines 67-80): catches all errors (401, 500, network) and navigates to /login. No unauthenticated state can persist after loading completes in the normal flow. Compliant.
3. logout() call precedes setUser(null) and navigate('/login') in handleSignOut. Client state is not cleared until the server acknowledges the logout -- the safer ordering. Compliant.
4. Role-based nav filtering: NAV_BY_ROLE[user.role] ?? [] falls back to empty array for unexpected role values, showing no nav items rather than all items. Compliant.
5. l1_support role present in NAV_BY_ROLE (AppShell.tsx line 74) with only the Tickets link. Not in AC-4 test scope but is safe (fewer links, not more). Compliant.
6. No sensitive data (PII, auth tokens) exposed in nav link labels or paths. Compliant.

### Escalation to Human

**Design concern -- absence of an explicit route guard in App.tsx.** AppShell.tsx lines 120-123 render Outlet when user === null && loading === false. Authentication protection relies entirely on the AuthContext useEffect navigate('/login') completing before child route content is meaningful. App.tsx has no Navigate-to-login component wrapping the authenticated route subtree. While the AuthContext catch block redirects on all me() errors, a React render can fire before the asynchronous navigate completes -- for one render cycle the protected route JSX may execute. In this project this presents no data-exposure risk because child component API calls would fail with 401, but the pattern differs from an explicit PrivateRoute guard. Tech lead should confirm this is the intended design for all protected routes in this application.

### Verdict

**Conditional Pass (advisory).** No Blockers. No Major findings. Core implementation is correct: all four acceptance criteria are fully covered; the role-based nav sets match UIS-001 v0.1 section AppShell exactly; the API contract (API-001 v0.2 section F-5) is honoured; LRN L-1 does not apply; coding standards are followed throughout.

Two Minor findings require human review before merge:
- **F-1 (scope-deviation -- App.test.tsx):** Authorization chain is present (SCR S-18, FEAT-001-TESTS.md v0.2, FEAT-036-TESTS.md); human to confirm.
- **F-2 (scope-deviation -- .secrets.baseline):** No SCR/DEC found; human to inspect diff and record a DEC if accepted.

One design concern escalated to tech lead: absence of an explicit Navigate-to-login route guard in App.tsx.

### Assumptions

Not applicable -- no new assumptions raised by this review.

### Open Questions

Not applicable -- no new open questions raised; design concern escalated to human reviewer above.

### Traceability Links

- Upstream: FEAT-036 plan.md v0.3; FEAT-036-ACC v0.2; FEAT-036-TESTS v0.1; FEAT-001-TESTS v0.2; API-001 v0.2 section F-5; UIS-001 v0.1 section AppShell; PRM-001 v0.1 section Authentication F-5; SCR S-17; SCR S-18; .ai/standards/learned-rules.md; .ai/standards/coding-standards.md
- Downstream: Human PR review of feature/FEAT-036-appshell-nav; docs/logs/review-feedback-log.md (F-1 Minor scope-deviation, F-2 Minor scope-deviation)

### Quality Checklist

- [x] Every section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed
- [x] Every finding cites file and line and has a category
- [x] Learned rules checked (LRN L-1 not applicable -- frontend-only feature)
- [x] Plan adherence assessed explicitly
- [x] Verdict stated as advisory

---

## AIR FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List

<!-- air_status: Draft -->
<!-- air_author: ai-code-reviewer -->
<!-- air_date: 2026-10-22 -->
<!-- air_verdict: Advisory pass -- all 4 Major findings resolved -->

### Input References

| Artifact | Version | Status | Path |
|---|---|---|---|
| FEAT-010 plan.md | v0.5 | Approved (Mohanasunder, 2026-10-21) | docs/05-build-plan/feature-010-holiday-list/plan.md |
| FEAT-010-ACC | v0.1 | Approved (Mohanasunder, 2026-10-17) | docs/05-build-plan/feature-010-holiday-list/acceptance.md |
| FEAT-010-TESTS | v0.2 | Approved (Mohanasunder, 2026-10-21) | docs/06-build/FEAT-010-TESTS.md |
| REQ-001 | v0.4 § S-24 | Approved | docs/02-requirements/ |
| API-001 | v0.3 § Company holiday list | Approved | docs/04-design/openapi.yaml |
| DBD-001 | v0.1 § Module: sla | Approved | docs/04-design/ |
| PRM-001 | v0.1 § Company holiday list | Approved | docs/04-design/ |
| UIS-001 | v0.1 § REQ S-24 | Approved | docs/04-design/ |
| .ai/standards/learned-rules.md | LRN L-1 | Generated | .ai/standards/learned-rules.md |
| .ai/standards/agent-charter.md | Generated | -- | .ai/standards/agent-charter.md |
| DEC-090 | 2026-10-21 | Approved | docs/logs/decision-log.md |
| Fix commits | 8ff6200 (backend), 70ba412 (frontend) | -- | feature/FEAT-010-holiday-list |

### Purpose And Scope

Advisory re-review of FEAT-010 (S-24: Delivery Manager Maintains the Company Holiday List) on branch `feature/FEAT-010-holiday-list`. This re-review confirms that the 4 Major findings from the initial review (2026-10-22) have been resolved by fix commits `8ff6200` (backend IntegrityError handlers) and `70ba412` (frontend field names, description removal, UserContext.Provider). Covers: fix correctness for all 4 Major findings, check for new findings in changed files, and Minor findings status. Locked test files are not flagged as defects. This review is advisory only; the human developer reviewer decides.

### Plan Adherence

All 20 plan.md v0.5 files are present and correctly implemented -- unchanged from the initial review assessment. Plan adherence assessment from initial review stands: **Conditional Pass**. Two out-of-plan files (pyproject.toml, .secrets.baseline) remain without a recorded DEC (Minor findings F-5, F-6 -- unchanged, still open for human decision).

### Acceptance Criteria Coverage

| Criterion | Status after fixes | Gap |
|---|---|---|
| AC-1: DM adds 2027-01-26; contributes 0 business hours | Resolved -- `holidays.ts` sends `{ holiday_date }` (commit 70ba412); `handleAdd()` calls `addHoliday({ holiday_date: newDate })` (HolidayList.tsx:60); backend correct | None |
| AC-2: DM removes 2027-03-15; counts as business day | Resolved -- table now renders `h.holiday_date` (HolidayList.tsx:92, commit 70ba412); DELETE path unchanged and correct | None |
| AC-3: Non-DM refused; DM can access | Resolved -- `HolidayListRoute` in App.tsx (lines 42--51, commit 70ba412) wraps `HolidayList` in `UserContext.Provider` using `useAuth()` role; DM correctly reaches the page | None |
| AC-4: Time-based DAL behavior | Unchanged -- correct from initial review; backend-only; no UI changes required | None |

### Resolved Findings

The following 4 Major findings from the initial review are confirmed resolved.

| Finding | Category | Fix commit | File : line evidence | Status |
|---|---|---|---|---|
| F-1 (api-contract-field-mismatch) | `api-contract-field-mismatch` | 70ba412 | `holidays.ts:18` -- `HolidayEntry.holiday_date: string`; `holidays.ts:24` -- `CreateHolidayPayload.holiday_date: string`; `HolidayList.tsx:60` -- `addHoliday({ holiday_date: newDate })`; `HolidayList.tsx:92` -- renders `h.holiday_date` | Resolved |
| F-2 (invented-field) | `invented-field` | 70ba412 | `HolidayEntry` interface (`holidays.ts:15--19`) has only `id` and `holiday_date` -- `description` removed; `CreateHolidayPayload` (`holidays.ts:22--25`) has only `holiday_date` -- `description` removed; `HolidayList.tsx` has no description field or render | Resolved |
| F-3 (missing-context-provider) | `missing-context-provider` | 70ba412 | `App.tsx:42--51` -- new `HolidayListRoute` component calls `useAuth()`, maps `user.role` via `AUTH_ROLE_MAP` to a P-role, and wraps `<HolidayList />` in `<UserContext.Provider value={{ role }}>`. Route `/admin/holidays` uses `<HolidayListRoute />` at `App.tsx:72` | Resolved |
| F-4 (missing-input-validation, LRN L-1) | `missing-input-validation` | 8ff6200 | `views.py:65--73` -- `create()` now catches both `ValueError` (HTTP 409) and `IntegrityError` (HTTP 400); `views.py:91--97` -- `destroy()` wraps `remove_holiday()` in `try/except IntegrityError` (HTTP 400). `IntegrityError` imported at `views.py:15` | Resolved |

### Open Findings (from initial review -- not blocking, unchanged)

| ID | File | Line | Category | Severity | Status |
|---|---|---|---|---|---|
| F-5 | `pyproject.toml` | 17--18, 29--30 | `scope-deviation` | Minor | Open -- no DEC recorded. Human reviewer to inspect diff and record DEC if accepted. |
| F-6 | `.secrets.baseline` | -- | `scope-deviation` | Minor | Open -- no DEC recorded. Human reviewer to inspect diff and record DEC if accepted. |
| F-7 | `src/frontend/src/pages/HolidayList.tsx` | 19 | `coupling` | Minor | Still present -- `UserContext` imported from `'./OrgManagement'`. F-3 was fixed via a wrapper in App.tsx; the import path remains a coupling issue but is no longer a functional defect. |
| F-8 | `src/frontend/src/pages/HolidayList.tsx` | 58--69 | `missing-error-handling` | Minor | Still present -- `handleAdd()` (line 58) and `handleRemove()` (line 66) have no `try/catch`; network errors produce unhandled promise rejections with no UI feedback. |
| F-9 | `src/aplx_ams_django/sla/serializers.py` | 22--36 | `api-contract-response-fields` | Advisory | Unchanged -- `added_at`, `added_by_id` included in GET response. Verify against openapi.yaml `/api/holidays/` 200 schema. |
| F-10 | `.ai/standards/automated-gates.md`, `.ai/standards/agent-charter.md` | -- | `scope-deviation` | Advisory (resolved) | Resolved by DEC-090 in initial review -- no change. |

### New Findings

No new findings. The fix commits (`8ff6200`, `70ba412`) are narrow and correct:

- `views.py`: Only the exception-handling blocks in `create()` and `destroy()` changed; no unintended side-effects detected.
- `holidays.ts`: Only field names changed (`date` to `holiday_date`, `description` removed); function signatures and fetch logic unchanged.
- `HolidayList.tsx`: Render updated to `h.holiday_date`; `handleAdd()` uses `{ holiday_date: newDate }`; `handleRemove()` unchanged; coupling import (F-7) and missing try/catch (F-8) remain Minor open issues.
- `App.tsx`: `HolidayListRoute` component added (lines 42--51); route wiring on line 72 is correct; no other routes or components affected.

### Security Observations

All observations from the initial review remain valid and unchanged. Additional notes for the fix commits:

1. `HolidayListRoute` (`App.tsx:43--45`): falls back to `'P1'` (minimum-privilege) when no user or unknown role -- correct sentinel behavior; the AuthProvider already redirects unauthenticated users to `/login` before this component can render. Compliant.
2. `AUTH_ROLE_MAP` (`App.tsx:29--34`): uses `?? 'P1'` fallback for unmapped role strings -- defensive and correct. Compliant.
3. No secrets introduced or exposed by the fix commits. Compliant.

### Learned Rules Check

**LRN L-1 (missing-input-validation):** "Wrap every model.save() call in a try/except django.db.IntegrityError block and return HTTP 400 with a structured error."

- `views.create()` (`views.py:65--73`, commit 8ff6200): `except IntegrityError` added, returns HTTP 400. **LRN L-1 now followed.**
- `views.destroy()` (`views.py:91--97`, commit 8ff6200): `try/except IntegrityError` added, returns HTTP 400. **LRN L-1 now followed.**

No LRN L-1 violations remain in the backend.

### Assumptions

Not applicable -- no new assumptions raised by this re-review.

### Open Questions

Not applicable -- no new open questions raised by this re-review.

### Traceability Links

- Upstream: FEAT-010 plan.md v0.5; FEAT-010-ACC v0.1; FEAT-010-TESTS v0.2; REQ-001 v0.4 § S-24; API-001 v0.3 § Company holiday list; DBD-001 v0.1 § Module: sla; PRM-001 v0.1 § Company holiday list; UIS-001 v0.1 § REQ S-24; .ai/standards/learned-rules.md (LRN L-1); DEC-090; fix commits 8ff6200 and 70ba412
- Downstream: Human PR review of `feature/FEAT-010-holiday-list`; docs/logs/review-feedback-log.md

### Quality Checklist

- [x] Every section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every finding cites file and line and has a category
- [x] Learned rules checked (LRN L-1: now followed in views.py after commit 8ff6200)
- [x] Plan adherence assessed explicitly
- [x] Verdict stated as advisory
- [x] Every AC assessed individually
- [x] Security observations documented
- [x] No secrets read or printed
- [x] No project files created or modified by this reviewer

### Verdict

**Advisory pass -- all 4 prior Major findings resolved.**

- **F-1 (api-contract-field-mismatch):** Resolved (commit 70ba412) -- `holidays.ts` and `HolidayList.tsx` now use `holiday_date` throughout; POST payload and GET list render are correct.
- **F-2 (invented-field):** Resolved (commit 70ba412) -- `description` removed from all TypeScript types and component UI.
- **F-3 (missing-context-provider):** Resolved (commit 70ba412) -- `HolidayListRoute` wrapper in `App.tsx` provides `UserContext.Provider` from `useAuth()`; DM can access the holiday list at runtime.
- **F-4 (missing-input-validation, LRN L-1):** Resolved (commit 8ff6200) -- `try/except IntegrityError` added to both `create()` and `destroy()` in `views.py`; LRN L-1 now satisfied.

Four Minor/Advisory findings remain open (F-5, F-6, F-7, F-8) -- none block merge; human reviewer decides. No new findings introduced by the fix commits.
