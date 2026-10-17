---
id: TST-001
title: APLX AMS: Test Strategy
phase: 4
version: 0.1
template: test-strategy
template_version: 2.0
status: Approved
author_agent: standards-author
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS: Test Strategy

> **Single file.** There is exactly one test strategy per project. Always use `--id TST --out docs/04-design/test-strategy.md` when calling `new_artifact.py`; never auto-name as `TST-NNN.md`.

## Input References

- PIB-004 v0.1 — Phase 4 Input Brief (Approved 2026-10-17) § Interview Answers Q4, Q5, Q6; § Constraints; § Assumptions
- SUM-003 v0.2 — Phase 3 Summary (Approved 2026-10-17) § Decisions; § Constraints Set
- ADR-001 v0.3 — Architecture Decision Records (Approved 2026-10-17) § ADR A-6, A-9, A-10, A-11, A-13
- NFR-001 v0.3 — Non-Functional Requirements (Approved 2026-10-17) § N-1 to N-9
- REQ-001 v0.3 — User Stories (Approved 2026-10-17) § S-1 to S-33
- PRS-001 v0.3 — Product Requirement Specification (Approved 2026-10-17) § Features F-1 to F-8
- TOP-001 v0.2 — Deployment Topology (Approved 2026-10-17) § Environments
- STD-001 v0.1 — Coding Standards § Automated Gate Commands; § Testing Rules (In review 2026-10-17)
- DEC-043 (Mohanasunder, chat, 2026-10-17) — Development tooling
- DEC-044 (Mohanasunder, chat, 2026-10-17) — Accessibility target: WCAG 2.1 Level A
- DEC-045 (Mohanasunder, chat, 2026-10-17) — Coverage gates: 80% backend, 70% frontend
- project.md § max_test_runtime_minutes (10 minutes)

## Purpose And Scope

Covers: how APLX AMS release 1 is tested at every level — unit, integration, end-to-end, load, accessibility, and security — including tools, coverage targets, test data rules, the environments where each level runs, and the key risk areas (SLA timer correctness, client data separation, security events in the audit trail) that require special test coverage.

Does not cover: writing individual test cases (those are in each feature's approved test set, FEAT-NNN-TESTS); defect management (Phase 7); UAT sign-off criteria (Phase 7 UAT-001); production monitoring (Phase 9).

## Test Levels

### Level 1: Unit tests

**Scope:** Individual pure functions, model methods, service functions, serializer validation, and React components tested in isolation. No database I/O, no HTTP calls, no file I/O.

**What to mock:** External HTTP calls, the current clock (use `freezegun` or `pytest-freezegun` for Python; `vi.useFakeTimers()` for TypeScript), and outbound email. Never mock the database or the Django ORM in unit tests of functions that are designed to query the database — use an integration test for those.

**Key unit test areas:**
- SLA timer calculation (`sla/services.py`): at-risk threshold (90%), breach at exactly 100%, pause accumulation across multiple pause/resume cycles, priority change recalculation from the raise time, holiday exclusion, business-hours boundary at 09:00 and 18:00 IST, and the 18:30 UTC / 00:00 IST day boundary (ADR A-9; BR B-1 to B-11).
- Password validator: 7-character password rejected; passwords without upper-case, lower-case, or digit each rejected; 8-character "Abcdefg1" accepted (NFR N-5).
- Export formula escaping: cell values starting with `=`, `+`, `-`, `@` are prefixed with a single quote before XlsxWriter or csv write (THR-001 § Mitigations).
- SLA denominator guard: when ticket count for a period is 0, percentage shows as "no tickets" and not 0% or 100% (A-021 confirmed, PIB-004 v0.1 Q2).
- React components: renders correct output for given props; user interaction events trigger the expected callbacks.

### Level 2: Integration tests

**Scope:** API endpoints tested against a real test PostgreSQL 18 database with the runtime role and row-level security policies active. Uses DRF `APIClient` or Django `TestClient`. Every integration test run includes data for at least two client organizations (organizations A and B) to exercise the RLS boundary (ADR A-6; NFR N-7).

**What to test per story:** Every user story S-1 to S-33 must have at least one integration test covering its Given/When/Then acceptance criteria. The test makes an HTTP request as the persona the story targets (P-1 L1, P-2 L2/L3, P-3 delivery manager, or P-4 client user, as specified in the story's acceptance criteria) and asserts the response body, HTTP status code, and any database side-effects including audit entries.

**Critical security integration tests (high-risk; must pass before the PR is merged):**
- S-30 (set temporary password): temporary password accepted, existing sessions ended, lockout cleared; no password value in the audit entry.
- S-31 (change own password): current password required; new password validates policy; no password value in the audit entry.
- S-32 (security events recorded): the 5 event types (successful sign-in, failed sign-in — wrong password, unknown account name, deactivated account, locked account — lockout, temporary password set, own password change) each produce exactly one audit entry with the correct fields and no password value; the refused sign-in with an account name matching no user account records the account name as typed (BR B-24; NFR N-6).
- S-33 (security events viewed): delivery manager sees all security events; an L1 engineer sees only their own; a client user sees none.
- NFR N-7 boundary: client user of organization A cannot list, open by reference, or raise a ticket against an SAP application of organization B; these assertions run in every CI integration test run.

**Audit completeness test (NFR N-6):** A single test makes one change of each audited type (status, priority, assignment, effort recorded, effort changed, effort deleted) plus each of the 5 security event types, then queries every audit entry produced during the test and checks that no entry contains any value that was supplied in a password field during the test run. The test expects 0 matches.

### Level 3: End-to-end tests (Playwright)

**Scope:** Key user journeys run against a fully running application stack (Nginx, Django, PostgreSQL) using real browser automation. Minimum 8 journeys, one per feature (F-1 to F-8).

| Journey | Feature | Story |
| --- | --- | --- |
| Sign in and sign out (L1 engineer) | F-6 | S-20, S-21 |
| Raise a ticket (client user) | F-1 | S-1, S-2 |
| View ticket list and open a ticket (L1 engineer) | F-2 | S-3, S-4 |
| Acknowledge, assign, change priority, set Resolved, Close (L2/L3) | F-2 | S-5, S-6, S-7, S-8, S-9 |
| View at-risk and breached tickets; SLA escalation flag visible (delivery manager) | F-3 | S-10, S-11 |
| Record effort and view hours bank (L2/L3) | F-5 | S-15, S-16 |
| View live dashboard (delivery manager) | F-4 | S-12 |
| View and download monthly client report (client user) | F-4 | S-14 |
| View audit trail entries for a ticket (L1 engineer) | F-8 | S-23 |

Each Playwright test also runs `@axe-core/playwright` against every page the journey visits and expects 0 WCAG 2.1 Level A violations (DEC-044).

### Level 4: Load tests

**Scope:** Simulate 30 concurrent users (10 engineer sessions, 20 client user sessions) running release 1 journeys for at least 30 minutes against the test server, and measure the p95 page response time per page (NFR N-2).

**Target:** p95 page response time under 2 seconds for every page at 30 concurrent users (NFR N-2).

**Journeys included in the load test:** raise ticket, view ticket list, acknowledge, change priority, assign, set Resolved, close, record effort, add comment, view live dashboard (with SLA timer computation per ticket), view monthly client report. The live dashboard journey is included because SLA timers are evaluated on read (ADR A-10) and the dashboard must stay within the p95 target.

**Tool:** [A-034] k6 or locust — decision deferred to Phase 7. The Phase 7 team selects the tool before the load test sprint begins and records the decision in `docs/logs/decision-log.md`.

**Run timing:** Load tests run in a separate CI job on the test server outside the 10-minute unit + integration suite. They do not block the feature-branch CI gate; they are a Phase 7 gate only.

### Level 5: Accessibility tests

**Scope:** Automated WCAG 2.1 Level A checks on every page visited by a Playwright E2E test (DEC-044).

**Tool:** `@axe-core/playwright` (MPL-2.0), integrated into every Playwright test.

**Rule:** Every page load in a Playwright test calls `checkA11y()` (axe-core) and expects 0 violations at the WCAG 2.1 Level A ruleset. Violations block the CI job.

**What automated checks do not cover:** color contrast at Level AA (MUI v6 default theme is Level AA, so Level A is satisfied, but the checker verifies this assumption for any custom color used); WCAG 2.1 Level AA criteria beyond Level A are out of scope for release 1 (DEC-044).

### Level 6: Security tests (SAST, dependency scan, secret scan)

**Scope:** Static analysis and dependency checking run on every pull request in CI.

**Tools and commands:**
- SAST: `bandit -r src/ -ll` (flags medium- and high-level findings; non-overridable gate).
- Dependency vulnerability: `pip-audit` (non-overridable gate).
- Secret scan: `detect-secrets scan` (non-overridable gate).

A finding that `bandit` rates as medium or high level blocks the PR. The builder fixes the finding or raises an OQ-NNN with an explanation before the PR goes to human review.

## Tools

| Level | Tool | Version | Licence | What it tests |
| --- | --- | --- | --- | --- |
| Unit (Python) | pytest | 8.x | MIT | Pure functions, service logic, model methods |
| Unit (Python) | pytest-django | latest stable | BSD-3-Clause | Django model and ORM integration |
| Unit (Python) | pytest-cov | latest stable | MIT | Line coverage reporting |
| Unit (Python) | pytest-timeout | latest stable | MIT | Enforces 10-minute suite limit |
| Unit (Python) | freezegun | latest stable | Apache-2.0 | Time mocking in SLA and session tests |
| Unit (TypeScript) | vitest | 2.x | MIT | React components, API client functions |
| Unit (TypeScript) | @vitest/coverage-v8 | 2.x | MIT | Line coverage reporting |
| Unit (TypeScript) | @testing-library/react | latest stable | MIT | Component render and interaction testing |
| Integration (Python) | pytest-django | latest stable | BSD-3-Clause | API endpoints against test PostgreSQL |
| Integration (Python) | factory_boy | latest stable | MIT | Test fixture factories for Django models |
| E2E | Playwright | 1.x | Apache-2.0 | Browser automation of user journeys |
| E2E | @axe-core/playwright | latest stable | MPL-2.0 | WCAG 2.1 Level A checks per page |
| Load [A-034] | k6 or locust (one chosen by QA lead at Phase 7 start; decision recorded in decision-log.md) | k6: AGPL-3.0; locust: MIT | NFR N-2 verification |
| SAST | bandit | latest stable | Apache-2.0 | Python security anti-patterns |
| Dependency scan | pip-audit | latest stable | Apache-2.0 | Known CVEs in Python dependencies |
| Secret scan | detect-secrets | latest stable | Apache-2.0 | Accidental secret commits |

All tools listed are free and open-source. No paid testing service is used (CST-001 v0.2; SUM-001 v0.3 § Constraints Set).

## Coverage Targets

Coverage targets were set by Mohanasunder (DEC-045). A change to either threshold requires a new human decision recorded in `docs/logs/decision-log.md`.

| Layer | Coverage type | Threshold | Enforced by |
| --- | --- | --- | --- |
| Backend Python | Line coverage | 80% | `pytest --cov-fail-under=80` |
| Frontend TypeScript | Line coverage | 70% | `vitest --coverage.threshold.lines=70` |
| E2E | Story happy path | 100% of F-1 to F-8 | Playwright test file review at each wave gate |

Migration files are excluded from backend coverage measurement (`[tool.coverage.run] omit = ["*/migrations/*"]` in `pyproject.toml`).

Every user story S-1 to S-33 must have at least one integration test covering its Given/When/Then acceptance criteria. Stories S-30, S-31 (password management) and S-32, S-33 (security events) are critical security tests; they are treated as high-risk and must pass before any PR that touches the `accounts` module is merged.

## Test Data Approach

### Rules

- Synthetic data only. No production data, no real personal data, and no real client organization records in any test fixture, factory, seed script, or Playwright test (NFR N-9; ADR A-13; THR-001 § Assets).
- Names and email addresses in test data follow the pattern: `testuser-N@example.com`, `Test User N`. No real person's name or email address is used.
- Client organizations in test data are named `OrgA` and `OrgB` (or similar clearly synthetic names).

### Factories and seed data

- Python model factories: use `factory_boy` (MIT) with `factory.django.DjangoModelFactory`. Each Django app's `tests/` directory contains a `factories.py` file that defines all model factories for that app.
- Every CI integration test run creates at least two client organizations (OrgA and OrgB) with distinct tickets, contracts, and user accounts to exercise the RLS boundary (ADR A-6; NFR N-7).
- Playwright seed scripts: a `playwright/fixtures/seed.py` script (run before the E2E suite) seeds the test database with enough synthetic data for all 8 journeys; it uses the Django management command `loaddata` or a custom management command.
- SLA timer tests use `freezegun` to set a fixed clock (IST business hours, e.g. 2026-11-10 10:00 IST = 2026-11-10 04:30 UTC) so that results are deterministic.

### What is prohibited in test data

- Real passwords, password hashes, or any value that was ever a production password.
- Real names, email addresses, phone numbers, or national identifiers.
- Production server addresses, host names, or IP addresses.
- The words `secret`, `password`, `token`, or `key` as the value of any string field in a fixture unless the test is specifically testing that the system rejects such values.

## Environments

| Test level | Environment | Database | Who runs it | Notes |
| --- | --- | --- | --- | --- |
| Unit (Python) | Developer workstation or GitHub Actions CI | In-memory or SQLite (pure-function unit tests); test PostgreSQL service container in CI (integration) | Builder agent, CI | pytest-django `--reuse-db` allowed locally to speed up reruns |
| Integration (Python) | GitHub Actions CI | PostgreSQL 18 service container; same schema as production | CI | Two client organizations in every run (A-6 requirement) |
| Unit (TypeScript) | Developer workstation or GitHub Actions CI | Not applicable — no database | Builder agent, CI | vitest --run for CI; --watch for local development |
| E2E (Playwright) | Test server (TOP-001 v0.2 § Environments) | PostgreSQL 18 (test stack) | CI (E2E job), QA lead | Seeded with synthetic data before each run; separate CI job from unit/integration |
| Load | Test server (TOP-001 v0.2 § Environments) | PostgreSQL 18 (test stack) | QA lead (Phase 7) | Scheduled separately; not a feature-branch gate |
| Accessibility | Test server (in-process with Playwright E2E) | PostgreSQL 18 (test stack) | CI (E2E job) | axe-core runs inside each Playwright test |
| Security (SAST, dep scan, secret scan) | GitHub Actions CI | Not applicable — static analysis | CI | Non-overridable; blocks PR merge |

No test touches any production configuration, server secret file, or production database connection string. The developer workstation runs Docker Engine inside WSL 2 (ADR A-5; OQ-060 answer).

## Key Risk: SLA Timer Correctness

SLA timer logic is complex (BR B-1 to B-11) and evaluated on read (ADR A-10). Incorrect SLA state affects all client-facing views and the monthly client report. The following test scenarios are mandatory in the `sla` module unit tests before any SLA-related feature PR is merged:

| Scenario | What it verifies |
| --- | --- |
| Ticket at 89%, 90%, 91% of target | At-risk starts exactly at 90% (BR B-5) |
| Ticket elapsed time equals target exactly | Breached state at 100% (BR B-6) |
| Ticket paused for N hours then resumed | Pause accumulation and business-hours exclusion (BR B-8) |
| Ticket priority changed from P2 to P1 while running | Recalculation from raise time with new target (BR B-9) |
| Ticket priority changed from P2 to P1 after breach | Stopped result (met or breached) kept; no recalculation (BR B-7) |
| Holiday added to the list after the ticket was raised | Business time after the addition excludes the new holiday; business time before is unchanged (BR B-2) |
| Ticket raised at 17:55 IST (09:25 UTC+5:30) | Business-hours boundary: only 5 minutes counted that day (BR B-2) |
| Ticket state evaluated at exactly 18:30 UTC | IST midnight boundary: 00:00:00 IST next calendar day; no double-counting (ADR A-9) |

## Assumptions

- A-034 (Open): peak load is 30 concurrent users at at most 15 API requests per second; one app container with 5 Gunicorn workers (ADR A-2; BED-001). This affects the load test scenario design. If the load test in Phase 7 finds the server under-provisioned, the Gunicorn worker count is reviewed first (TOP-001 v0.2). The load test tool selection (k6 or locust) is deferred to Phase 7 (labeled in § Tools).
- A-008 (Open): supported browsers are the current and previous major versions of Chrome and Edge on desktop (NFR N-8). The Playwright E2E suite must run on each of these 4 browser versions in Phase 7. The exact version numbers are determined at the start of Phase 7 by the QA lead.

## Open Questions

None. All Phase 4 entry interview questions and all earlier phase open questions are answered. No new open questions arose during writing of this artifact. If a builder identifies a gap in Phase 6, raise a new OQ-NNN in `docs/logs/open-questions-log.md` before proceeding.

## Traceability Links

- Upstream: PIB-004 v0.1; SUM-003 v0.2; ADR-001 v0.3 (ADR A-6, A-9, A-10, A-11, A-13); NFR-001 v0.3 (N-1 to N-9); REQ-001 v0.3 (S-1 to S-33); PRS-001 v0.3 (F-1 to F-8); TOP-001 v0.2; STD-001 v0.1; project.md.
- Decisions: Phase 4 entry interview decisions in docs/logs/decision-log.md (development tooling, accessibility target WCAG 2.1 Level A, coverage gates 80%/70%).
- Downstream: Phase 5 feature plans (FEAT-NNN); Phase 6 feature test sets (FEAT-NNN-TESTS); Phase 7 NFR test report; Phase 7 UAT sign-off.

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
