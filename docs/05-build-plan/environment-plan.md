---
id: ENV-001
title: APLX AMS Build Environment Plan
phase: 5
version: 0.1
template: environment-plan
template_version: 1.0
status: Approved
author_agent: environment-setup
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS Build Environment Plan

## Input References
- SUM-004 v0.1 — Phase 4 Solution Design Summary (Approved 2026-10-17); stack, constraints, and CI gate source
- STD-001 v0.1 — APLX AMS Coding Standards (Approved 2026-10-17); CI gate commands
- SUM-003 v0.2 — Phase 3 Solution Architecture Summary (Approved 2026-10-17); topology, ADRs A-5, A-13, A-17
- ADR-001 v0.3 — Architecture Decision Records (Approved 2026-10-17); ADR A-5 (Docker Compose), A-13 (CI rules, GitHub), A-17 (secrets)
- TOP-001 v0.2 — Deployment Topology (Approved 2026-10-17); environments and servers
- `.ai/standards/branching-standard.md` — branch naming, protection rules, merge rules
- `.ai/standards/automated-gates.md` — required CI gate commands
- `project.md` — approver names; `stale_branch_days: 5`, `max_open_feature_branches: 3`

## Purpose And Scope

Defines the repository layout, branching rules, branch protection configuration, required CI checks, environment descriptions, access controls, and CODEOWNERS entries for Phase 6 Build of APLX AMS. Humans apply branch protection and CODEOWNERS on the GitHub platform; this document specifies what to configure.

Out of scope: production deployment (Phase 8), infrastructure-as-code details, server OS configuration. Phase 6 builders do not access the test or production servers.

## Repositories And Branching

### Repository

Single public repository on GitHub: `https://github.com/Mohanasunder/aplx-ams` (ADR A-13; DEC-027).

### Top-level folder structure

```
aplx-ams/
├── src/
│   ├── aplx_ams_django/     Django project root: settings, urls, wsgi
│   ├── accounts/            Django app: user accounts, authentication, sessions
│   ├── organizations/       Django app: organizations and SAP contracts
│   ├── tickets/             Django app: ticket lifecycle
│   ├── sla/                 Django app: SLA computation and states
│   ├── effort/              Django app: effort entries
│   ├── reports/             Django app: report generation (Excel, CSV, PDF)
│   ├── audit/               Django app: audit trail and security events
│   └── frontend/            React 18 + TypeScript + MUI v6, Vite build
├── infra/                   Docker Compose files, Nginx config
├── tests/                   Integration and E2E tests (pytest-django, Playwright)
├── scripts/                 SDLC scripts — agents do not modify during build
└── docs/                    SDLC artifacts — agents do not modify during build
```

Source: BED-001 v0.1 (7 Django apps); UIS-001 v0.1 (React/Vite frontend); ADR-001 v0.3 A-5 (Docker Compose); ADR-001 v0.3 A-12 (XlsxWriter, csv, WeasyPrint).

### Branch naming

| Branch type | Pattern | Target | Notes |
| --- | --- | --- | --- |
| Feature (and Fix) | `feature/FEAT-NNN-slug` | `main` | One branch per feature; slug is 1–4 lowercase words |
| Hotfix | `hotfix/HOT-NNN-slug` | `main` (from release tag) | Urgent production fix only |
| Release stabilization | `release/x.y` | n/a | Short-lived; only if needed |
| Spike (throwaway) | `spike/spk-S-N-slug` | never merged | Deleted after ADR is approved |

Source: `.ai/standards/branching-standard.md`.

### Stale branch policy

Branches with no activity for 5 calendar days are flagged by `/sdlc-status` (`stale_branch_days: 5` in `project.md`). A maximum of 3 feature branches may be open simultaneously (`max_open_feature_branches: 3`).

### CODEOWNERS

Place the following content in `.github/CODEOWNERS` (human applies on the platform):

```
# All files — Mohanasunder is the sole named approver for all roles (project.md)
* @Mohanasunder
```

This enforces that every PR requires a review from @Mohanasunder. GitHub branch protection must reference CODEOWNERS for the reviewer requirement to apply automatically.

### Branch protection rules for `main` (human configures on GitHub)

| Rule | Setting |
| --- | --- |
| Require a pull request before merging | Enabled |
| Required approvals | 1 (Standard-tier features); CODEOWNERS enforces 2 for High, tech lead + release manager for Critical |
| Dismiss stale pull request approvals when new commits are pushed | Enabled |
| Require status checks to pass before merging | Enabled; all gates listed in CI Skeleton are required checks |
| Require branches to be up to date before merging | Enabled |
| Require linear history | Enabled |
| Allow force pushes | Disabled |
| Allow deletions | Disabled |
| Do not allow bypassing the above settings | Enabled |

The authoring agent never merges its own PR (branching-standard.md). Squash-merge or rebase-merge with a message referencing FEAT, REQ, and PR IDs.

## CI Skeleton

All gates run on GitHub Actions (ubuntu-latest runner) before a PR reaches a human. Failures on non-overridable gates block merge and cannot be overridden without a human decision recorded in `docs/logs/decision-log.md`. All commands are from `.ai/standards/automated-gates.md` and STD-001 v0.1.

FEAT-000 (Task 0, walking skeleton) makes every command run green in CI and corrects any that do not work; no gate may be left unset after FEAT-000 merges.

### Required status checks

| # | Gate | Command | Non-overridable |
| --- | --- | --- | --- |
| 1 | Build | `docker compose build app && npm --prefix src/frontend ci && npm --prefix src/frontend run build` | no |
| 2 | Health check | `docker compose up -d && curl --fail http://localhost/api/health/` | no |
| 3 | Python lint | `ruff check src/ && ruff format --check src/` | no |
| 4 | TypeScript lint | `eslint src/frontend/src/ --max-warnings=0` | no |
| 5 | Python type check | `mypy src/ --strict` | no |
| 6 | TypeScript type check | `tsc --noEmit --project src/frontend/tsconfig.json` | no |
| 7 | Python unit + integration tests (80% coverage gate) | `pytest src/ --cov=src --cov-fail-under=80 --timeout=600` | no |
| 8 | TypeScript unit tests (70% coverage gate) | `vitest run --coverage --coverage.threshold.lines=70` | no |
| 9 | E2E tests (separate CI job) | `playwright test` | no |
| 10 | SAST | `bandit -r src/ -ll` | yes |
| 11 | Dependency scan | `pip-audit` | yes |
| 12 | Secrets scan | `detect-secrets scan` | yes |
| 13 | Migration check | `python manage.py migrate --run-syncdb` then `python manage.py migrate <app> zero` (finalized in FEAT-000) | no |
| 14 | Locked tests unchanged | `python3 scripts/locked_tests.py check` | yes |
| 15 | Feature size | `python3 scripts/check_feature_size.py size` | yes |
| 16 | Wave plan collision-free | `python3 scripts/check_feature_size.py waves` | yes |
| 17 | Files in scope (Phase 6) | `python3 scripts/check_feature_size.py scope` | no |
| 18 | New packages approved (Phase 6) | `python3 scripts/check_feature_size.py packages` | yes |
| 19 | Spec change records | `python3 scripts/spec_impact.py records` | yes |
| 20 | Feature cites current approved specs (Phase 6) | `python3 scripts/spec_impact.py check` | yes |
| 21 | Context pack resolves within budget | `python3 scripts/context_pack.py check` | yes |
| 22 | Phase summary indexes the phase | `python3 scripts/context_pack.py summaries N` | no |
| 23 | Learned rules index matches approved rules | `python3 scripts/learned_rules.py check` | yes |
| 24 | Task 0 first; gates set after it merges | `python3 scripts/check_feature_size.py task0` | yes |
| 25 | Spikes never merged; time boxes; branches deleted | `python3 scripts/spike.py check` | yes |
| 26 | Change summary complete (Phase 6) | `python3 scripts/pr_summary.py check` | yes |
| 27 | Decision log well-formed and append-only | `python3 scripts/log_decision.py check --base origin/main` | yes |
| 28 | Agent charter matches its sources | `python3 scripts/build_charter.py check` | yes |
| 29 | Domain terms used consistently | `python3 scripts/glossary_check.py check` (add `--code` once `src/` exists) | yes |
| 30 | Artifact validation | `python3 scripts/validate_artifact.py docs --check-links` | no |
| 31 | Branch name | `scripts/check-branch-name.sh "$(git branch --show-current)"` | no |

Gates 17, 18, 20, 26 apply from Phase 6 onward; gates 15, 16, 21 apply from Phase 5 onward. Gates 27–31 (IaC validate, go recorded, feedback log) are Phase 8–9 and are left unset until those phases begin (permitted by automated-gates.md).

### GitHub Actions workflow structure (to be created in FEAT-000)

- `ci.yml` — lint, type checks, unit and integration tests, SAST, dependency scan, secrets scan, SDLC script checks
- `e2e.yml` — Playwright E2E job (separate, runs after `ci.yml`)
- Fork pull request restrictions: enabled (ADR A-13); workflow runs from forks require maintainer approval before secrets are exposed.

## Environments

### Local development

| Property | Value |
| --- | --- |
| Provisioning | `docker compose up -d` from `infra/` |
| Containers | `proxy` (Nginx, publishes port 80), `app` (Django 5.2 / Gunicorn), `db` (PostgreSQL 18) |
| Host OS | Windows 11 with Docker Engine in WSL 2 (ADR A-5) |
| Database | PostgreSQL 18, single database, ephemeral in dev (seeded by fixtures) |
| Secrets | Root-only files on the developer's workstation, passed as Docker Compose file secrets; path references only in `compose.yml` (ADR A-17) |
| Agent access | Builder agents run `docker compose` commands on the developer workstation; no remote server access |

### CI (GitHub Actions)

| Property | Value |
| --- | --- |
| Runner | ubuntu-latest (GitHub-hosted) |
| Provisioning | Docker Compose in CI job; fresh container on every run |
| Secrets | GitHub Actions secrets, injected as environment variables; names are referenced in workflow files (no values in the repository) (ADR A-13, A-17) |
| Fork restriction | Enabled; workflow secrets not exposed to fork PRs without maintainer approval (ADR A-13) |
| Estimated usage | At most 1,500 runner-minutes per month on the public repository; free tier covers this (A-035) |

### Test server

| Property | Value |
| --- | --- |
| Hardware | Ubuntu LTS VM, 2 vCPU, 4 GB RAM, 40 GB free disk (TOP-001 v0.2; A-030) |
| Role | Deployment target for human-run deploys before production; holds weekly `pg_dump` copies |
| Deployment | Human only: checksum-verified bundle deployed outside business hours (ADR A-13) |
| Monitoring | Uptime Kuma, 60-second check, email alert to Release manager / DevOps (ADR A-16) |
| Agent access | None; builder agents do not access the test server during Phase 6 |
| Backup | Weekly `pg_dump`, encrypted at rest; 8 weekly dumps retained (ADR A-15) |

### Production

| Property | Value |
| --- | --- |
| Hardware | Ubuntu LTS VM, 2 vCPU, 4 GB RAM, 40 GB free disk (TOP-001 v0.2; A-030) |
| Scope | Out of scope for Phase 6; defined in Phase 8 |
| Agent access | None; no agent reads or writes production configuration |

## Access

### Repository write access

| Person / entity | Level | Source |
| --- | --- | --- |
| @Mohanasunder | Owner (admin, write, review, merge) | project.md — all approver roles |

No other person or entity has repository write access during Phase 6. Builder agents push to their feature branch only; they do not merge.

### Agent access model

Builder agents interact with the repository through the GitHub CLI and Git on the local workstation. They have no credentials for the test or production servers. CI runs under the GitHub Actions runner identity (ephemeral, scoped to the repository).

Agents never read secret values. Secrets are referenced by name only:
- `DJANGO_SECRET_KEY` — Django secret key (root-only file, Docker Compose file secret, ADR A-17)
- `DB_PASSWORD` — PostgreSQL password (root-only file, Docker Compose file secret, ADR A-17)
- `DB_NAME`, `DB_USER` — database credentials (root-only files, Docker Compose file secrets, ADR A-17)

In CI, these are GitHub Actions secrets injected as environment variables by the workflow. No secret value appears in any workflow file, Dockerfile, or source file.

### Platform admin actions (escalate to human)

The following require GitHub platform admin rights and must be performed by @Mohanasunder:
- Configuring branch protection rules on `main`
- Creating and committing `.github/CODEOWNERS`
- Configuring GitHub Actions secrets
- Enabling fork pull request restrictions on GitHub Actions workflows

## Assumptions

No new assumptions are introduced by this artifact. All inputs are from Approved artifacts at the versions cited. Relevant inherited assumptions:

- A-035 (Open, owner Mohanasunder): GitHub Actions usage for release 1 is at most 1,500 Linux runner-minutes per month, within the free tier for public repositories (DEC-027); logged in `docs/logs/assumptions-log.md`.
- A-038 (Open, owner Mohanasunder): Applexus provides no secret manager; secrets are held as root-only files on each server and passed to containers as Docker Compose file secrets (ADR A-17); logged in `docs/logs/assumptions-log.md`.

## Open Questions

None raised in this artifact. All relevant architecture and topology questions (OQ-052 to OQ-066) are Answered. All relevant design questions are Answered or Confirmed.

## Traceability Links

- Upstream: SUM-004 v0.1; STD-001 v0.1; SUM-003 v0.2; ADR-001 v0.3 (A-5, A-13, A-17); TOP-001 v0.2; BED-001 v0.1; UIS-001 v0.1; `project.md`; `.ai/standards/branching-standard.md`; `.ai/standards/automated-gates.md`
- Downstream: Phase 6 feature branches, GitHub Actions workflow files (`ci.yml`, `e2e.yml`), `.github/CODEOWNERS`; Phase 8 infrastructure plan (IaC validate gate set in Phase 8)

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
