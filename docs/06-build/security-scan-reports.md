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

