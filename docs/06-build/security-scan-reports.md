---
id: SSR-001
id_prefix: SSR
title: Security Scan Reports
phase: 6
version: 0.1
template: security-scan-report
template_version: 2.0
status: Draft
author_agent: security-scanner
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: 2026-10-18
validation: Pending
---

# Security Scan Reports

<!-- Collection file. All security scan reports are appended as `## SSR FEAT-NNN: [title]` sections. Never create a separate file per feature. Per-report status stored as HTML comments within each section. Approve each section individually with `/approve docs/06-build/security-scan-reports.md --sub-id FEAT-NNN`. -->

## SSR FEAT-000: Walking Skeleton — Security Scan

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Findings to fix -->

### Input References

- FEAT-000 plan: `docs/06-build/` (feature branch `feature/FEAT-000-walking-skeleton`, commit `0884c98`)
- `.secrets.baseline`: committed at `8eec279`
- `requirements.txt`: pinned at commit `b91e29f` (Django patched to 5.2.18, pytest to >=9.0.3)

### Purpose And Scope

This report covers the SAST, dependency, and secrets scans for FEAT-000 (Walking Skeleton) on branch `feature/FEAT-000-walking-skeleton`. It also includes a manual review of secrets handling in `settings/base.py`, `docker-compose.yml`, and `settings/production.py`. It does not cover frontend code (no frontend source exists in this feature), infrastructure-as-code (Phase 8), or runtime penetration testing.

### Scan Tools And Scope

| Tool | Version | Command | Exit Code | Scope |
| --- | --- | --- | --- | --- |
| bandit | 1.9.4 | `python -m bandit -r src/ -ll` | 0 | All Python source under `src/` (71 lines) |
| pip-audit | 2.10.1 | `python -m pip_audit -r requirements.txt` | 0 | All packages in `requirements.txt` |
| detect-secrets | 1.5.0 | `detect-secrets scan --baseline .secrets.baseline` | 0 | Repository-wide, against committed baseline |

Python runtime: 3.12.9

### Findings

#### Automated Scan Findings

| Tool | Rule / Finding | Severity | File | Line | Notes |
| --- | --- | --- | --- | --- | --- |
| bandit | No issues identified at or above MEDIUM (`-ll` threshold) | — | — | — | 2 LOW B101 (assert_used) exist in test file; below configured threshold |
| pip-audit | No known vulnerabilities found | — | — | — | All pinned packages clean |
| detect-secrets | No new secrets beyond baseline | — | — | — | Baseline acknowledged; see Secrets Check section |

#### Manual Review Findings

| Finding | Severity | File | Line | Detail |
| --- | --- | --- | --- | --- |
| `ALLOWED_HOSTS: ["*"]` not overridden in production settings | Medium | `src/aplx_ams_django/settings/base.py` | 23 | `production.py` imports `base.py` but does not override `ALLOWED_HOSTS`. The wildcard `["*"]` remains active in production, allowing requests with any HTTP Host header. |
| `SECRET_KEY` fallback is an insecure literal string | Medium | `src/aplx_ams_django/settings/base.py` | 19 | If `/run/secrets/django_secret_key` is absent and `DJANGO_SECRET_KEY` env var is unset, Django silently uses `"insecure-dev-key-replace-in-production"`. Production should raise `ImproperlyConfigured` instead of falling back. |

#### Low-Severity Informational Notes (below scan threshold — not blocking)

| Note | File | Lines |
| --- | --- | --- |
| B101 assert_used (Low, High-confidence): `assert` used in test code | `src/aplx_ams_django/tests/test_health.py` | 15–16 |
| CI test DB password `postgres` baselined in detect-secrets | `.github/workflows/ci.yml` | 215, 225 |

### Secrets Check

`detect-secrets scan --baseline .secrets.baseline` exited 0. No new secrets were detected beyond the committed baseline.

The `.secrets.baseline` file (generated 2026-10-17T19:59:03Z, committed at `8eec279`) contains three acknowledged findings:

1. **`.github/workflows/ci.yml` line 215** — `POSTGRES_PASSWORD: postgres` (Secret Keyword). This is an ephemeral test-service-container credential used only in GitHub Actions CI jobs. It is not a production secret. Baselined and acknowledged.
2. **`.github/workflows/ci.yml` line 225** — `DATABASE_URL: postgres://aplx_ams:postgres@localhost:5432/aplx_ams_test` (Basic Auth Credentials). Same CI test credential in connection-string form. Baselined and acknowledged.
3. **`docs/04-design/backend-design.md` line 632** — Secret Keyword match on documentation text describing a "temp password" reset flow. This is design documentation, not an actual credential value. Baselined and acknowledged.

Docker secrets configuration review:
- `docker-compose.yml` uses Docker file secrets for both `django_secret_key` (via `./secrets/django_secret_key.txt`) and `db_password` (via `./secrets/db_password.txt`). No plaintext passwords appear in the compose file.
- The PostgreSQL service uses `POSTGRES_PASSWORD_FILE` pointing to the mounted secret, not `POSTGRES_PASSWORD`.
- `settings/base.py` uses `read_secret()` for `SECRET_KEY` (line 19) and database `PASSWORD` (line 40). Both resolve `/run/secrets/<name>` before environment variables.

### Verdict

**Findings to fix**

All automated scans passed (exit code 0). No secrets detected. No High or Critical SAST findings.

Two Medium-severity manual observations require remediation before production deployment (not blocking this FEAT-000 PR, but must be resolved before any production-bound feature goes live):

1. `ALLOWED_HOSTS` must be restricted in `settings/production.py`.
2. `SECRET_KEY` must raise `ImproperlyConfigured` (or equivalent) when no secret is available rather than falling back to a literal insecure value.

Neither finding constitutes a non-overridable Blocker under the automated-gates policy (no secret value found, no scan returned non-zero exit code). Both are advisory findings requiring human decision on remediation timing.

### Assumptions

- A-SEC-001: The `secrets/` directory (referenced by `docker-compose.yml`) is gitignored and not committed. Verified: `secrets/` appears in `.gitignore` line 5. Confirmed safe.

### Open Questions

- OQ-SEC-001: Should `SECRET_KEY` raise `ImproperlyConfigured` immediately when no secret source is available, or is the insecure fallback acceptable for local development (with CI enforcing a real secret in non-dev environments)? Assign to tech lead.
- OQ-SEC-002: Is there a plan to populate `ALLOWED_HOSTS` in `settings/production.py` once the production hostname is known, or should it be set via environment variable?

### Traceability Links

- Upstream: FEAT-000 plan (docs/06-build/), ADR A-17 (secrets pattern), automated-gates.md
- Downstream: Not applicable — this is a scan report; findings feed into developer review and remediation tasks

### Quality Checklist

- [x] Every configured scan was run
- [x] Failures reported, not hidden
- [x] Every section is filled, or marked "Not applicable — reason"
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream

---

## SSR FEAT-001: Security Scan — Frontend Scaffold

<!-- ssr_status: Pass (with decisions) -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->

### Input References
- FEAT-001 plan.md v0.2 (Approved 2026-10-17)
- .ai/standards/automated-gates.md
- .secrets.baseline (committed)

### Gate Results

| Gate | Command | Exit Code | Result |
| --- | --- | --- | --- |
| SAST | `bandit -r src/ -ll` | 0 | PASS — no MEDIUM or HIGH issues; 21 LOW below threshold |
| Dependency scan (project) | `pip-audit -r requirements.txt` | 0 | PASS — no known vulnerabilities in APLX AMS packages |
| Dependency scan (env) | `pip-audit` (bare) | 1 | ENVIRONMENTAL NOISE — flags Claude Code infrastructure packages (langchain-core, pyjwt, etc.) not in requirements.txt; accepted per DEC-065 |
| Secrets scan | `detect-secrets scan` | 0 | PASS — all findings previously acknowledged in .secrets.baseline |

### Manual Review — nginx/nginx.conf
Fixed during scan cycle (Medium findings resolved):
- `server_tokens off` added
- Security headers (`X-Frame-Options`, `X-Content-Type-Options`, `Content-Security-Policy`, `Referrer-Policy`) added to server block for static-file responses
- HSTS discrepancy resolved: middleware.py comment updated to clarify HSTS is a Phase 8 production Nginx concern

### Manual Review — middleware.py

| Finding | Status |
| --- | --- |
| `unsafe-inline` in `style-src` | Accepted per DEC-066 — MUI v6 Emotion requires inline styles; no unsafe-eval present |
| session_start uninitialized (F-1) | Fixed per AIR FEAT-001 F-1 before this report saved |
| Session timeouts | Correct (after F-1 fix) |

### Manual Review — docker-compose.yml
No plaintext secrets; Docker file secrets used. secrets/*.txt gitignored. Verified.

### Overall Verdict
**PASS with decisions.** All non-overridable gate commands pass against APLX AMS project packages. nginx.conf medium findings fixed. middleware.py CSP unsafe-inline accepted per DEC-066. session_start fix applied per AIR FEAT-001 F-1.

### Traceability Links
- Upstream: FEAT-001 plan.md v0.2; STD-001 v0.1; automated-gates.md; DEC-065; DEC-066
- Downstream: PR FEAT-001 human review

## SSR FEAT-035: E2E CI Scaffold — Security Scan

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Clean -->

### Input References

- FEAT-035 plan: `docs/06-build/` (feature branch `feature/FEAT-035-e2e-ci-scaffold`, HEAD `fde38e1`)
- `.ai/standards/automated-gates.md`
- `.secrets.baseline` (committed at `4d29043`, `generated_at: 2026-10-17T21:50:38Z`)
- `requirements.txt` (unchanged from FEAT-001 merge)

### Purpose And Scope

Covers the SAST, dependency, secrets, and CI workflow security scans for FEAT-035 (E2E CI Scaffold). Files in scope:
- `.github/workflows/e2e.yml` — new GitHub Actions E2E workflow
- `src/frontend/playwright.config.ts` — upgraded from stub
- `src/frontend/e2e/scaffold.spec.ts` — new locked Playwright test file

Does not cover: infrastructure-as-code (Phase 8), runtime penetration testing, or artifacts outside the feature scope.

### Scan Tools And Scope

| Tool | Version | Command | Exit Code | Scope |
| --- | --- | --- | --- | --- |
| bandit | 1.9.4 | `python -m bandit -r src/ -ll` | 0 | All Python source under `src/` (12 files, 380 lines) |
| pip-audit | (installed) | `python -m pip_audit -r requirements.txt` | 0 | All packages in `requirements.txt` |
| detect-secrets | 1.5.0 | `python -m detect_secrets scan --baseline .secrets.baseline` | 0 | Repository-wide, against committed baseline |
| Manual review | — | Inspection of `.github/workflows/e2e.yml` | — | Script injection, permissions, credential exposure |

### Findings

#### Automated Scan Findings

| Tool | Rule / Finding | Severity | File | Line | Notes |
| --- | --- | --- | --- | --- | --- |
| bandit | No issues at or above MEDIUM (`-ll` threshold) | — | — | — | 22 LOW B101 (assert_used) in test files; pre-existing, unchanged; none in changed files (TypeScript / YAML not scanned by bandit) |
| pip-audit | No known vulnerabilities found | — | — | — | All pinned packages clean |
| detect-secrets | No new secrets beyond committed baseline | — | — | — | Baseline diff limited to `generated_at` timestamp update; results section unchanged |

#### CI Workflow Manual Review — `.github/workflows/e2e.yml`

| Finding | Severity | File | Line | Detail |
| --- | --- | --- | --- | --- |
| No explicit `permissions:` block | Low | `.github/workflows/e2e.yml` | (global) | **Resolved.** `permissions: contents: read` added at workflow level (commit after AIR/SSR). `ci.yml` retains the same omission (on master; out of FEAT-035 scope; tracked via OQ-070). |
| `docker compose logs` on failure may expose container stdout | Informational | `.github/workflows/e2e.yml` | 53 | On health-check timeout the step runs `docker compose logs` and prints to the CI log. Docker file secrets are used rather than environment-variable credentials, so actual secret values are not expected in container stdout. Advisory only. |

No script-injection risk: the workflow contains no `${{ github.event.* }}` or other user-controlled context interpolated into `run:` steps.

No action-SHA pinning: `actions/checkout@v4` and `actions/setup-node@v4` are referenced by major-version tag (consistent with `ci.yml`; informational, not blocking under current project gates).

### Secrets Check

`detect-secrets scan --baseline .secrets.baseline` exited 0. No new secrets detected. The committed baseline contains four acknowledged findings across three pre-existing files (`ci.yml`, `backend-design.md`, `security-scan-reports.md`) — all assessed in prior scan reports (SSR FEAT-000, SSR FEAT-001). None of the three FEAT-035 files appear in baseline results.

### Verdict

**Clean**

All automated scan gates passed with exit code 0. No secrets detected. No MEDIUM or HIGH SAST findings. No script-injection vectors in the new CI workflow. One Low-severity advisory (missing `permissions:` block, pre-existing pattern). No Blockers.

### Assumptions

- A-SEC-035-01: The `generated_at` timestamp difference in `.secrets.baseline` (local scan ran 2026-10-18 vs committed 2026-10-17) is expected behavior of detect-secrets; the `results` object is unchanged.

### Open Questions

- OQ-070: Should all GitHub Actions workflows add `permissions: contents: read` to enforce least-privilege GITHUB_TOKEN access? Applies to both `ci.yml` and `e2e.yml`. Assigned to Mohanasunder (tech lead).

### Traceability Links

- Upstream: FEAT-035 plan; STD-001 AC-5; automated-gates.md; `.secrets.baseline` commit `4d29043`
- Downstream: PR FEAT-035 human review


## SSR FEAT-002: Org and SAP Setup — Security Scan

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Clean -->

### Scan Results

| Tool | Command | Exit Code | Findings |
|---|---|---|---|
| bandit | `python -m bandit -r src/aplx_ams_django/ -ll -q` | 0 | No MEDIUM/HIGH findings; 47 LOW (B101 assert_used in tests, below threshold) |
| bandit (focused) | `python -m bandit -r src/aplx_ams_django/organizations/ -ll` | 0 | 0 MEDIUM/HIGH in new organizations app |
| pip-audit | `pip-audit -r requirements.txt` | 0 | No known vulnerabilities in project dependencies |
| detect-secrets | `detect-secrets scan --baseline .secrets.baseline` | 0 | No new secrets; baseline unchanged in results |

### Verdict

**Clean.** All four gate commands exited 0. No MEDIUM or HIGH SAST findings. No new secrets detected. No new dependency vulnerabilities. 4 pre-existing baselined secrets (CI credentials, design doc examples) unchanged from prior features.

### Traceability Links

- Upstream: FEAT-002-TESTS v0.1; automated-gates.md; DEC-071
- Downstream: PR FEAT-002 human review


---

## SSR FEAT-003: S-19 — Delivery Manager Sets Up Client Organization Contract

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Pass with findings -->

### Input References

- FEAT-003 plan.md v0.1
- FEAT-003-TESTS v0.1 (Approved, SHA b4b18a1)
- `.ai/standards/automated-gates.md`
- `requirements.txt`

### Scan Results

| Tool | Command | Exit Code | Findings |
|---|---|---|---|
| bandit | `python -m bandit -r src/aplx_ams_django/ -ll -q` | 0 | No MEDIUM/HIGH findings; B101 assert_used (tests, expected) |
| pip-audit | `pip-audit -r requirements.txt` | 0 | No known vulnerabilities in project dependencies |
| detect-secrets | `detect-secrets scan --baseline .secrets.baseline` | 0 | No new secrets detected |
| ESLint | `npx eslint src/ --max-warnings=0` | 0 | No warnings |
| tsc | `npx tsc --noEmit` | 0 | No type errors |

### Findings Detail

**M-1 (Minor) — assert used for control flow:** `views.py` uses `assert org_id is not None` at lines 133 and 155. In production Python (with `-O`), `assert` statements are stripped. If Django URL conf ever passes `None`, the view silently proceeds. **Accepted:** `org_id` is always provided by Django's URL router for nested routes; `-O` is not used in this project's deployment (Gunicorn standard invocation); no real risk in current deployment context.

**M-2 (Minor) — COERCE_DECIMAL_TO_STRING not set:** DRF default coerces `DecimalField` to string in JSON. `contracted_hours` and `hours_bank_balance` are serialized as strings unless `coerce_to_string=False`. **Accepted:** All backend tests pass numeric comparisons through the serializer layer; TypeScript client `Contract` interface types these as `number | null`; DRF docs confirm field-level `coerce_to_string=False` overrides the global default per field.

**Pre-existing:** 4 baselined secrets (CI credentials, design doc examples) — unchanged from prior features.

### Verdict

**Pass with findings.** All gate commands exited 0. Two Minor findings accepted. No MEDIUM or HIGH SAST findings. No new secrets. No dependency vulnerabilities.

### Traceability Links

- Upstream: FEAT-003-TESTS v0.1; automated-gates.md; DEC-071; DEC-072; DEC-073
- Downstream: PR FEAT-003 human review

---

## SSR FEAT-005: S-20 Delivery Manager Manages User Accounts — Security Scan

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Pass with observations -->

### Input References

- FEAT-005 plan: `docs/06-build/` (branch `feature/FEAT-005-user-accounts`, HEAD `02e32a5`)
- FEAT-005-TESTS v0.1 (Approved)
- `.ai/standards/automated-gates.md`
- `.secrets.baseline` (committed)
- `requirements.txt` (unchanged from FEAT-003 merge)
- DEC-079 (pre-existing pip-audit environment overrides for pyjwt, python-dotenv, python-jose, urllib3)
- DEC-065 (bare pip-audit environmental noise from Claude Code infrastructure packages)

### Purpose And Scope

This report covers the SAST, dependency, and secrets scans for FEAT-005 (S-20: Delivery Manager Manages User Accounts) on branch `feature/FEAT-005-user-accounts`. Files in scope:

- `src/aplx_ams_django/accounts/` — all Python source files (views.py, models.py, serializers.py, services.py, dal.py, urls.py, admin.py, apps.py, migrations/0001_initial.py, tests/)
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`

Does not cover: infrastructure-as-code (Phase 8), runtime penetration testing, or artifacts outside the feature scope.

### Scan Tools And Scope

| Tool | Version | Command | Exit Code | Scope |
| --- | --- | --- | --- | --- |
| bandit | 1.9.4 | `python -m bandit -r src/aplx_ams_django/accounts/ -ll -q` | 0 | All Python source under `accounts/` (1,080 lines) |
| pip-audit | 2.10.1 | `python -m pip_audit -r requirements.txt` | 0 | All packages in `requirements.txt` |
| pip-audit (env) | 2.10.1 | `python -m pip_audit` | 1 | Full Python environment (Claude Code tool infrastructure — environmental noise per DEC-065) |
| detect-secrets | 1.5.0 | `python -m detect_secrets scan --baseline .secrets.baseline` | 0 | Repository-wide, against committed baseline |
| Manual review | — | Source inspection | — | views.py, models.py, serializers.py, services.py, dal.py, UserManagement.tsx, users.ts |

Python runtime: 3.12.9

### Findings

#### Automated Scan Findings

| Tool | Rule / Finding | Severity | File | Line | Notes |
| --- | --- | --- | --- | --- | --- |
| bandit (-ll) | No issues identified at or above MEDIUM threshold | — | — | — | 50 Low-severity findings exist (B101 assert_used in test files; B110 try_except_pass in conftest.py); all below configured -ll threshold |
| pip-audit (-r requirements.txt) | No known vulnerabilities found | — | — | — | All pinned project packages clean |
| pip-audit (env bare) | 48 findings across 12 packages | Environmental noise | Various | — | All in Claude Code infrastructure packages or pre-existing overrides (pyjwt, python-dotenv, python-jose, urllib3 per DEC-079); none in requirements.txt |
| detect-secrets | No new secrets beyond committed baseline | — | — | — | Baseline unchanged in results section |

#### Low-Severity Bandit Findings in Production Source (below -ll gate threshold — informational only)

| Rule | Severity | File | Lines | Notes |
| --- | --- | --- | --- | --- |
| B101 assert_used | Low | `src/aplx_ams_django/accounts/views.py` | 54, 60, 71 | `assert pk is not None` in retrieve, partial_update, and deactivate actions. `pk` is typed `<int:pk>` in the URL pattern and cannot be None at runtime. Same pattern accepted in FEAT-003 M-1. Below -ll gate threshold. |

#### Manual Review Findings

| Finding | Severity | File | Line(s) | Detail |
| --- | --- | --- | --- | --- |
| M-1: `partial_update` bypasses `UserUpdateSerializer` | Minor | `src/aplx_ams_django/accounts/views.py` | 62–67 | The PATCH handler whitelists four field names and applies values from `request.data` directly via `setattr` without routing through `UserUpdateSerializer`. DB constraints backstop integrity, but API contract compliance (returning 400 for invalid input) is not enforced consistently for PATCH. No SQL injection risk; ORM is used throughout. |
| M-2: No `password` field exposure | Info | `src/aplx_ams_django/accounts/serializers.py` | 74–84 | `UserDetailSerializer` does not include `password` or `last_login`. Confirmed safe. |
| M-3: `services.create_user` uses `set_unusable_password()` | Info | `src/aplx_ams_django/accounts/services.py` | 40 | No plaintext password stored at account creation. Password flow deferred to FEAT-006 per plan. Confirmed safe. |
| M-4: Frontend `temporary_password` field | Info | `src/frontend/src/pages/UserManagement.tsx` | 217–229 | Input uses `type="password"` (masked). Form state reset on dialog close. No credential leak risk. |
| M-5: Frontend fetch uses `credentials: 'include'` | Info | `src/frontend/src/api/users.ts` | 64, 74, 87, 93 | Session cookie credentials. No hardcoded tokens or API keys. Confirmed correct. |
| M-6: `HasRolePermission` checks `is_authenticated` first | Info | `src/aplx_ams_django/permissions.py` | 27–29 | Unauthenticated requests return False (403) before any role check. All `UserViewSet` actions invoke this via `get_permissions()` before any DB access. |

#### Pre-existing Environmental pip-audit Findings (not FEAT-005 findings)

| Package | IDs | Status |
| --- | --- | --- |
| pyjwt 2.13.0 | PYSEC-2026-4140 through PYSEC-2026-4183 (12 entries) | Pre-existing; overridden per DEC-079 |
| python-dotenv 1.0.1 | PYSEC-2026-2270 (2 entries) | Pre-existing; overridden per DEC-079 |
| python-jose 3.5.0 | PYSEC-2026-4298 | Pre-existing; overridden per DEC-079 |
| urllib3 2.7.0 | PYSEC-2026-4175, PYSEC-2026-4176, PYSEC-2026-4177 | Pre-existing; overridden per DEC-079 |
| langchain-core, langchain-openai, langgraph-sdk, ecdsa, multidict, oauthlib, pdfminer-six, pip | Multiple | Claude Code tool infrastructure; not in requirements.txt; environmental noise per DEC-065 |

### Secrets Check

`python -m detect_secrets scan --baseline .secrets.baseline` exited 0. No new secrets detected beyond the committed baseline. No credentials, tokens, or API keys appear in any FEAT-005 source file.

### Verdict

**Pass with observations**

All non-overridable gate commands passed with exit code 0:
- bandit -ll: PASS (exit 0, no MEDIUM or HIGH findings)
- pip-audit -r requirements.txt: PASS (exit 0, no vulnerabilities in project packages)
- detect-secrets: PASS (exit 0, no new secrets)

One Minor finding (M-1) is raised as an advisory observation: the `partial_update` view handler applies PATCH field values via `setattr` without routing through `UserUpdateSerializer`, meaning application-layer validation is not enforced for that endpoint. DB constraints backstop integrity. No Blockers.

### Assumptions

- A-SEC-005-01: The bare `pip-audit` findings for langchain-core, ecdsa, multidict, oauthlib, pdfminer-six, and pip are Claude Code host environment packages, not APLX AMS project dependencies. Verified by cross-checking all 48 flagged packages against `requirements.txt`.

### Open Questions

None.

### Traceability Links

- Upstream: FEAT-005 plan; FEAT-005-TESTS v0.1; automated-gates.md; DEC-079; DEC-065; PRM-001 v0.1
- Downstream: PR FEAT-005 human review

## SSR FEAT-005 (re-scan): S-20 Delivery Manager Manages User Accounts — Post-Fix Security Scan

<!-- ssr_status: Draft -->
<!-- ssr_author: security-scanner -->
<!-- ssr_date: 2026-10-18 -->
<!-- ssr_verdict: Pass -->

### Scan Tools And Results

| Tool | Command | Exit Code |
| --- | --- | --- |
| bandit | `python -m bandit -r src/ -ll` | 0 — No MEDIUM or HIGH findings |
| pip-audit | `python -m pip_audit -r requirements.txt` | 0 — No known vulnerabilities in project packages |
| detect-secrets | `python -m detect_secrets scan --baseline .secrets.baseline` | 0 — No new secrets beyond committed baseline |

### Key Changes Reviewed
- F-1 (M-1 resolved): `partial_update` now routes through `UserUpdateSerializer`; `validated_data` applied instead of raw `request.data`
- F-2: All three pk-based actions wrap DAL/service calls in `try/except User.DoesNotExist` → 404
- F-8: `r.ok` check before every `r.json()` — prevents UI treating error payloads as valid data
- `temporary_password` excluded from API payload (form state only for locked-test compat)

### Verdict
**Pass.** All three non-overridable gate commands exited 0. The sole Minor advisory M-1 from the initial SSR FEAT-005 (partial_update bypassing UserUpdateSerializer) is resolved by commit `853d731`. No security regressions introduced by builder fixes. No Blockers.

### Traceability Links
- Upstream: FEAT-005 plan; FEAT-005-TESTS v0.3; automated-gates.md; DEC-079; DEC-081; prior SSR FEAT-005 (initial, HEAD `02e32a5`)
- Downstream: PR FEAT-005 human review
