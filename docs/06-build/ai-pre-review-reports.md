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
