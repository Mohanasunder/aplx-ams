---
id: STD-001
title: APLX AMS: Coding Standards
phase: 4
version: 0.1
template: coding-standards
template_version: 2.0
status: Approved
author_agent: standards-author
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS: Coding Standards

> **Single file.** There is exactly one coding standards document per project. Always use `--id STD --out docs/04-design/coding-standards.md` when calling `new_artifact.py`; never auto-name as `STD-NNN.md`.

## Input References

- PIB-004 v0.1 — Phase 4 Input Brief (Approved 2026-10-17) § Interview Answers Q3, Q4, Q5, Q6; § Constraints; § Assumptions
- SUM-003 v0.2 — Phase 3 Summary (Approved 2026-10-17) § Decisions; § Constraints Set
- ADR-001 v0.3 — Architecture Decision Records (Approved 2026-10-17) § ADR A-2, A-6, A-8, A-11, A-13, A-17
- TEC-001 v0.3 — Technology Comparison (Approved 2026-10-17) § Recommendation
- THR-001 v0.2 — Threat Model (Approved 2026-10-17) § Mitigations
- NFR-001 v0.3 — Non-Functional Requirements (Approved 2026-10-17) § N-5, N-6, N-7, N-8, N-9
- BED-001 v0.1 — Backend Design (In review 2026-10-17) § Module Structure (structural reference)
- .ai/standards/branching-standard.md — Branching rules
- .ai/standards/automated-gates.md — Gate framework
- DEC-041 (Mohanasunder, chat, 2026-10-17) — Material UI v6, MIT licence, default theme
- DEC-042 (Mohanasunder, chat, 2026-10-17) — Sign-in rate limit: 10 req/min per IP, burst 5
- DEC-043 (Mohanasunder, chat, 2026-10-17) — Development tooling choices
- DEC-044 (Mohanasunder, chat, 2026-10-17) — Accessibility target: WCAG 2.1 Level A
- DEC-045 (Mohanasunder, chat, 2026-10-17) — Coverage gates: 80% backend, 70% frontend

## Purpose And Scope

Covers: the rules every builder agent must follow when writing Python, TypeScript, and configuration code for APLX AMS release 1. Rules govern language usage, naming conventions, file structure, error handling and logging, testing conventions, security controls, automated gate commands, the approved technology list, and branching rules.

Does not cover: the OpenAPI contract or database schema (DBD-001, API-001); UI layout rules (UIS-001); the permission matrix (PRM-001); infrastructure as code (Phase 8); or any production deployment command.

Production Configuration paths (no agent reads or writes these): server secret files under `/run/secrets/`, production Docker Compose files on either server, Nginx `ssl_certificate*` directives, and any file whose name matches the pattern `*.key` or `*.pem` on a server.

## Naming And Structure

### Python naming conventions

- Modules and packages: `snake_case` (e.g. `ticket_dal`, `sla_service`).
- Functions and variables: `snake_case`.
- Classes: `PascalCase` (e.g. `TicketSerializer`, `SLATimerService`).
- Constants: `UPPER_SNAKE_CASE` (e.g. `MAX_FAILED_SIGN_INS = 5`).
- Django model class names: `PascalCase`; database table names default to `<app>_<model_lower>` (do not set `db_table` unless a name clash requires it).
- Test functions: `test_<verb>_<condition>` (e.g. `test_sign_in_fails_after_five_attempts`).

### TypeScript naming conventions

- Components: `PascalCase`; one component per file; file name matches the component name exactly (e.g. `TicketList.tsx`).
- Functions and variables: `camelCase`.
- Types and interfaces: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Hooks: `use<PascalCase>` (e.g. `useTicketList`).

### REST endpoint naming

- All lowercase, words separated by hyphens, noun-plural segments (e.g. `/api/tickets/`, `/api/client-organizations/`).
- Path parameters use camelCase in OpenAPI but snake_case in Django URL patterns.

### Commit message format

- First line: `FEAT-NNN: <imperative present-tense summary>` (50 characters or fewer).
- Body (optional): explain why, not what.
- Never commit generated files (migrations excluded), compiled bundles, or secret values.

### Backend file and folder structure

```
src/
  aplx_ams_django/           # Django project package
    settings/
      base.py                # Shared settings; reads secrets with read_secret() (A-038)
      production.py          # Imports base; DEBUG = False; no secrets in file
    urls.py
    middleware.py            # RLSContextMiddleware; AbsoluteSessionTimeoutMiddleware;
                             # SecurityHeadersMiddleware (CSP, X-Frame-Options)
    dal/                     # Shared DAL helpers: rls_context(), set_rls_session()
    permissions.py           # HasRolePermission DRF class; deny by default

  accounts/                  # User accounts, roles, sign-in, lockout, password management
    models.py
    serializers.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  organizations/             # Client organizations, SAP applications, contracts
    models.py
    serializers.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  tickets/                   # Tickets, comments, ticket lifecycle
    models.py
    serializers.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  sla/                       # Business calendar, holiday list, SLA timer computation
    models.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  effort/                    # Effort entries, hours bank
    models.py
    serializers.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  reports/                   # Dashboard, monthly client report, finance export
    models.py
    serializers.py
    services.py
    dal.py
    views.py
    urls.py
    tests/

  audit/                     # Append-only audit trail and security events
    models.py
    services.py
    dal.py
    tests/
```

### Frontend file and folder structure

```
src/frontend/
  src/
    components/
      <Feature>/
        <Component>.tsx      # PascalCase; one component per file
        <Component>.test.tsx # Vitest unit test alongside the component
    pages/                   # One file per route page (e.g. TicketsPage.tsx)
    hooks/                   # Custom React hooks
    api/                     # API client functions (one file per module)
    contexts/                # React context providers
  tsconfig.json
  vite.config.ts
```

## Error And Logging

### Python / Django logging

- Use the standard library `logging` module. Never use `print()` in production code.
- Logger names follow the module path (e.g. `logging.getLogger(__name__)`).
- Log level guide: `DEBUG` for development traces (disabled in production); `INFO` for normal lifecycle events (sign-in, ticket status change); `WARNING` for recoverable errors; `ERROR` for unhandled exceptions; `CRITICAL` for events that stop the service.
- Log format: `%(asctime)s %(levelname)s %(name)s %(message)s` with timestamps in UTC (Django `USE_TZ = True`).
- Never log: passwords, temporary passwords, password hashes, session identifiers, CSRF tokens, or the values of any secret file. A refused sign-in entry records the account name as typed (ADR A-11; BR B-24) but never a password value (NFR N-6).
- Never call the ORM directly inside a log message expression (avoids lazy evaluation database queries in log formatters).

### Django error responses

- DRF serializer validation errors return HTTP 400 with a JSON body listing field-level errors; never return a plain string.
- Authentication and permission failures return HTTP 401 or HTTP 403 with a generic JSON error body; the body never reveals whether an account name or password was wrong (ADR A-7; NFR N-5).
- Unhandled exceptions: Django's `PROPAGATE_EXCEPTIONS = False` (default in production); the framework logs the traceback and returns HTTP 500 with a generic JSON body.
- No stack traces, file paths, or system user names in any HTTP response body.

### TypeScript error handling

- API errors: catch the HTTP response, parse the JSON error body, and surface a user-visible message. Never display raw exception messages.
- Component render errors: wrap page-level components in React error boundaries.
- Unhandled promise rejections: log to the browser console using `console.error`; never silence with an empty `catch` block.

## Testing Rules

### General rules

- Write tests from the acceptance criteria before writing any implementation code (CLAUDE.md rule 3).
- Approved test sets are locked; only a human unlocks them via `/approve` (CLAUDE.md rule 3; CI gate `python3 scripts/locked_tests.py check`).
- Builders change only the files listed in `plan.md` for their feature.
- Mock only at system boundaries: external HTTP calls, the current time (use `freezegun` or `pytest-freezegun`), and outbound email. Never mock the database or the Django ORM in integration tests.

### Backend (Python)

- Framework: `pytest` 8.x with `pytest-django`; configuration in `pyproject.toml` under `[tool.pytest.ini_options]`.
- Test location: `tests/` subdirectory within each Django app (e.g. `accounts/tests/test_sign_in.py`).
- Database: integration tests use a real test PostgreSQL database with the runtime role and RLS policies active; unit tests for pure functions (e.g. SLA calculation) use no database.
- Client data boundary: every integration test run includes test data for at least two client organizations (A and B) and asserts that a client user of organization A cannot see any record of organization B (NFR N-7; ADR A-6).
- Coverage: 80% line coverage; CI enforces with `--cov-fail-under=80`. Excluding generated migration files from coverage is allowed (`[tool.coverage.run] omit = ["*/migrations/*"]`).
- Timeout: the full unit + integration suite must complete in 10 minutes (`project.md`; `pytest --timeout=600`).
- SLA timer tests must cover: at-risk threshold (90%), breach at exactly 100%, pause accumulation, priority change recalculation, holiday exclusion, business-hours boundary (IST), and the 18:30 UTC / 00:00 IST day boundary (ADR A-9; ADR A-10).
- Security tests: NFR N-5 verification (wrong password, 7-character password, no upper-case, no digit, correct 6th attempt within lock window, post-30-minutes attempt, temporary password clearing lock). NFR N-6 verification: 0 audit entries contain a password value.

### Frontend (TypeScript)

- Framework: `vitest` 2.x with `@vitest/coverage-v8`.
- Test location: alongside the component (`<Component>.test.tsx`) or in a `__tests__/` folder within the feature directory.
- Coverage: 70% line coverage; CI enforces with `--coverage.threshold.lines=70`.
- Component tests use `@testing-library/react`; assert on rendered output and user interactions, not on internal state.
- API client functions are tested with mocked `fetch` responses; never call the real API from a unit test.

### End-to-end (Playwright)

- Framework: Playwright 1.x.
- At least one Playwright test covering the happy path for each of the 8 features (F-1 to F-8, PRS-001 v0.3).
- Tests run against a running application instance, not mocked endpoints.
- Accessibility: run `@axe-core/playwright` against each page loaded in an E2E test and expect 0 violations at WCAG 2.1 Level A (DEC-044).

## Security Rules

### Input validation and output encoding

- Every API endpoint validates all input through a DRF serializer before reaching a service function.
- Export formula escaping: any cell value starting with `=`, `+`, `-`, or `@` must be prefixed with a single quote (`'`) before writing to an Excel (XlsxWriter) or CSV file. This rule applies in the reports and finance export services (THR-001 § Mitigations).
- SQL: use the Django ORM or parameterized queries only. No string interpolation in raw SQL.

### Authentication and sessions

- Sessions: server-side Django sessions with HttpOnly, Secure, SameSite=Strict cookie. New session identifier issued at sign-in. Session expires after 60 minutes idle (rolling) and 12 hours from sign-in (ADR A-7).
- CSRF: X-CSRFToken header required on every POST, PUT, PATCH, and DELETE request. DRF `SessionAuthentication` enforces this when `SessionAuthentication` is the authentication class.
- Sign-in rate limit: Nginx `limit_req_zone` configuration — 10 requests per minute per IP address, burst of 5 — applied to `POST /api/auth/login/` (DEC-042; ADR A-14). The Nginx configuration snippet is:
  ```nginx
  limit_req_zone $binary_remote_addr zone=signin:10m rate=10r/m;

  location /api/auth/login/ {
      limit_req zone=signin burst=5 nodelay;
      proxy_pass http://app;
  }
  ```
  This snippet is included in the Phase 8 Nginx configuration template; the exact file path is set in the deployment runbook.
- Password lockout: lock user account for 30 minutes after 5 failed sign-in attempts; the delivery manager's `set_temp_password()` call clears the lock at once (NFR N-5; ADR A-7).
- Argon2id password storage (assumption A-028): Django's `Argon2PasswordHasher` is first in `PASSWORD_HASHERS`; `argon2-cffi` (MIT) is in the approved package list. PBKDF2-SHA256 is kept second only to verify hashes created before the switch. Passwords, temporary passwords, and hashes are never logged, printed, or returned in any API response (NFR N-6; ADR A-8).

### HTTP security headers (middleware)

The `SecurityHeadersMiddleware` in `src/aplx_ams_django/middleware.py` adds the following headers to every response:

| Header | Value |
| --- | --- |
| Content-Security-Policy | `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'` |
| X-Frame-Options | `DENY` |
| X-Content-Type-Options | `nosniff` |
| Referrer-Policy | `no-referrer` |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains` (set by Nginx; do not duplicate in Django) |

### Secrets and configuration

- [A-038] No secret manager is available; secrets are root-only Docker Compose file secrets mounted at `/run/secrets/<name>` (ADR A-17). Builders never read or write secret values; they use only the `read_secret(name: str) -> str` helper from `aplx_ams_django.settings.base`, which reads `/run/secrets/<name>`.
- Never place a secret, server address, host name, server username, or production data in any file committed to the repository (ADR A-13; THR-001 T-31, T-32). This includes `.env` files, Django settings files, CI workflow files, comments, and documentation.
- Secret file names go in `.gitignore`; their values are never in the repository history. If a secret is ever committed, rotate it immediately; do not only remove it from history.
- Environment variables may hold non-secret configuration (e.g. `DJANGO_SETTINGS_MODULE`). The values `DEBUG`, `SECRET_KEY`, and any database password must come from secret files, not environment variables.

### Client data separation (RLS)

- Every view or service that accesses a client-owned table must go through the DAL. The DAL calls `set_rls_session()` at the start of each request transaction, setting the user kind and, for a client user, the client organization ID (ADR A-6).
- Direct ORM queries on client-owned models outside the DAL are prohibited. The `ai-code-reviewer` flags this as a Major finding.
- Every integration test run includes data for at least two client organizations and asserts 0 cross-organization records visible to a client user (NFR N-7).

### Audit trail

- Every state change to a ticket's status, priority, assignment, or effort entry must call the audit function from the `audit` module in the same database transaction (ADR A-11; NFR N-6). No change path may skip the audit call.
- Every security event (sign-in, failed sign-in, lockout, temporary password set, own password change) must call the audit function in its own transaction even if the sign-in is refused.
- The audit function has no parameter that accepts a password value; no password, temporary password, or hash may reach an audit entry through any code path.

### Dependency policy

- Add only packages on the approved technology list (§ Approved Technology List). Any other package requires a new ADR before it may appear in `requirements.txt` or `package.json` in Phase 6.
- CI runs `pip-audit` (dependency vulnerability scan) and the licence scan; a known Critical or High CVE or an unapproved licence is a non-overridable gate failure.

## Automated Gate Commands

All commands below are run by GitHub Actions CI on every pull request. Each command must exit 0 for the PR to be mergeable. These commands also define what builders run locally before pushing.

### Linting and formatting

```
# Python: lint and format check
ruff check src/
ruff format --check src/

# TypeScript: lint
eslint src/frontend/src/ --max-warnings=0
```

### Type checking

```
# Python: strict type check
mypy src/ --strict

# TypeScript: type check (no emit)
tsc --noEmit --project src/frontend/tsconfig.json
```

### Unit and integration tests with coverage

```
# Backend: unit + integration tests, 80% line coverage gate, 10-minute timeout
pytest src/ --cov=src --cov-fail-under=80 --timeout=600

# Frontend: unit tests, 70% line coverage gate
vitest run --coverage --coverage.threshold.lines=70
```

### End-to-end tests

```
playwright test
```

End-to-end tests run in a separate CI job against a running application instance; they do not count against the 10-minute unit + integration timeout.

### Security and dependency scanning

```
# SAST (non-overridable)
bandit -r src/ -ll

# Dependency vulnerability scan (non-overridable)
pip-audit

# Secret scan (non-overridable)
detect-secrets scan
```

### Migration check

```
# Apply then reverse the latest migration on a scratch database
python manage.py migrate --run-syncdb
python manage.py migrate <app> zero
```

The exact migration check command is finalized in FEAT-000 (Task 0) when the database container and test credentials are configured.

### Build

```
# Backend image (CI uses docker compose build)
docker compose build app

# Frontend bundle
npm --prefix src/frontend ci
npm --prefix src/frontend run build
```

### Health check (local)

```
docker compose up -d
curl --fail http://localhost/api/health/
```

### Coverage gates summary

| Layer | Coverage type | Threshold | Enforced by |
| --- | --- | --- | --- |
| Backend Python | Line coverage | 80% | `pytest --cov-fail-under=80` |
| Frontend TypeScript | Line coverage | 70% | `vitest --coverage.threshold.lines=70` |

Thresholds were set by Mohanasunder (DEC-045). A change to either threshold requires a new human decision recorded in `docs/logs/decision-log.md`.

## Accessibility

- All new pages and UI components must meet WCAG 2.1 Level A (DEC-044; PIB-004 v0.1 Q5).
- Material UI v6 (MIT) default theme is used throughout; no custom theme in Phase 4 (DEC-041). MUI v6's default theme meets WCAG 2.1 Level AA, which satisfies Level A for color contrast and focus indicators.
- Every new interactive component must be keyboard-navigable and have a visible focus indicator.
- Form inputs must have associated `<label>` elements or `aria-label` attributes.
- Images that carry meaning must have non-empty `alt` text; decorative images use `alt=""`.
- Automated WCAG 2.1 Level A checks run via `@axe-core/playwright` in the Playwright E2E test suite (see § Testing Rules § End-to-end).

## Branching and PR Rules

Branching rules are defined in `.ai/standards/branching-standard.md`. The following rules apply to every builder:

- Work only on a `feature/FEAT-NNN-slug` branch created by `scripts/create-feature-branch.sh FEAT-NNN`.
- Never commit directly to `main` or push `main`.
- One feature per branch; one PR per branch.
- Open a draft PR immediately after branch creation: `gh pr create --draft`.
- Sync `main` into the feature branch with `git merge main` before opening the PR and before merge; never rebase a pushed branch.
- All CI gates must pass (exit 0) before the PR is ready for human review.
- Approved test sets are locked; approved tests may not be modified on the feature branch. The `python3 scripts/locked_tests.py check` gate is non-overridable.
- Builders change only the files listed in their feature's `plan.md`; the `python3 scripts/check_feature_size.py scope` gate enforces this.
- Only packages named in the feature's `plan.md` New Packages section may be added; the `python3 scripts/check_feature_size.py packages` gate is non-overridable.
- A branch with no activity for 5 days (`stale_branch_days` in `project.md`) is flagged by `/sdlc-status`.

## Approved Technology List

The table below is the complete approved list derived from TEC-001 v0.3 § Recommendation (Approved 2026-10-17) and ADR-001 v0.3 (Approved 2026-10-17), plus DEC-041 (MUI v6, Mohanasunder, chat, 2026-10-17). Any package not on this list requires a new ADR before it may be added in Phase 6.

| Component | Version | Licence | ADR or decision |
| --- | --- | --- | --- |
| Python | 3.13 | PSF-2.0 | ADR A-2 |
| Django | 5.2 LTS | BSD-3-Clause | ADR A-2 |
| Django REST framework | 3.x | BSD-3-Clause | ADR A-2 |
| Gunicorn | latest stable | MIT | ADR A-2 |
| psycopg 3 | latest stable | LGPL-3.0 (unmodified library use) | ADR A-4 |
| argon2-cffi | latest stable | MIT | ADR A-8; A-028 |
| XlsxWriter | latest stable | BSD-2-Clause | ADR A-12; A-029 |
| Python csv (standard library) | included in Python 3.13 | PSF-2.0 | ADR A-12; A-029 |
| WeasyPrint | latest stable | BSD-3-Clause | ADR A-12; A-029 |
| React | 18.x or later | MIT | ADR A-3 |
| TypeScript | 5.x | Apache-2.0 | ADR A-3 |
| Vite | 5.x | MIT | ADR A-3 |
| Node.js 24 LTS | 24.x (CI build only) | MIT | ADR A-3 |
| Material UI (MUI) | 6.x | MIT | DEC-041 |
| PostgreSQL | 18 | PostgreSQL License | ADR A-4 |
| Nginx | stable | BSD-2-Clause | ADR A-14 |
| Docker Engine | latest stable | Apache-2.0 | ADR A-5 |
| Docker Compose | latest stable | Apache-2.0 | ADR A-5 |
| Uptime Kuma | 2.x | MIT | ADR A-16 |
| age or GnuPG (backup encryption, one chosen in Phase 8) | latest stable | age: BSD-3-Clause; GnuPG: GPL-3.0 (tool, not library) | ADR A-15 |

Development-only tools (not deployed to production servers):

| Tool | Version | Licence | Decision |
| --- | --- | --- | --- |
| ruff | latest stable | MIT | DEC-043 |
| mypy | latest stable | MIT | DEC-043 |
| pytest | 8.x | MIT | DEC-043 |
| pytest-django | latest stable | BSD-3-Clause | DEC-043 |
| pytest-cov | latest stable | MIT | DEC-043 |
| pytest-timeout | latest stable | MIT | DEC-043 |
| factory-boy | latest stable | MIT | DEC-043; test fixture factories |
| freezegun | latest stable | Apache-2.0 | DEC-043; time-travel in tests |
| bandit | latest stable | Apache-2.0 | DEC-043 |
| pip-audit | latest stable | Apache-2.0 | DEC-043 |
| detect-secrets | latest stable | Apache-2.0 | DEC-043 |
| ESLint | 9.x | MIT | DEC-043 |
| @typescript-eslint/parser and plugin | latest stable | MIT | DEC-043 |
| vitest | 2.x | MIT | DEC-043 |
| @vitest/coverage-v8 | 2.x | MIT | DEC-043 |
| @testing-library/react | latest stable | MIT | DEC-043 |
| Playwright | 1.x | Apache-2.0 | DEC-043 |
| @axe-core/playwright | latest stable | MPL-2.0 | DEC-044 |

## Assumptions

- A-028 (Open): passwords are stored using Argon2id via `argon2-cffi` (ADR A-8; ADR A-2). This assumption affects § Security Rules § Authentication and sessions. If Argon2id is unavailable, an approved alternative (bcrypt) must be chosen via an ADR before Phase 6 starts.
- A-035 (Open): GitHub Actions usage stays within the free-tier quota for a public repository (ADR A-13). This affects the number and duration of CI jobs. If usage exceeds the free tier, a paid plan or self-hosted runners require a new ADR.
- A-038 (Open): no secret manager is available on the servers; secrets are root-only Docker Compose file secrets mounted at `/run/secrets/` (ADR A-17). This affects § Security Rules § Secrets and configuration and the `read_secret()` helper design. If a secret manager becomes available, a new ADR is required.

## Open Questions

None. All Phase 4 entry interview questions (Q3, Q4, Q5, Q6) and all Phase 2 and Phase 3 open questions are answered. No new open questions were raised during writing of this artifact. If a builder identifies a gap in Phase 6, raise a new OQ-NNN in `docs/logs/open-questions-log.md` before proceeding.

## Traceability Links

- Upstream: PIB-004 v0.1; SUM-003 v0.2; ADR-001 v0.3 (ADR A-2, A-6, A-8, A-11, A-13, A-17); TEC-001 v0.3; THR-001 v0.2; NFR-001 v0.3 (N-5, N-6, N-7, N-8, N-9); BED-001 v0.1; .ai/standards/branching-standard.md; .ai/standards/automated-gates.md.
- Decisions: Phase 4 entry interview decisions in docs/logs/decision-log.md (MUI v6 licence, sign-in rate limit, development tooling, accessibility target WCAG 2.1 Level A, coverage gates 80%/70%).
- Downstream: .ai/standards/gate-commands.md; .ai/standards/agent-charter.md (rebuilt from this file); Phase 5 feature plans; Phase 6 feature branches; TST-001 v0.1.

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
| Role | Architect / tech lead + UX |
| Version | 0.1 |
| Conditions | None |
| Comments | Phase 4 design package approved. |
| Timestamp | 2026-10-17 14:04 UTC |
