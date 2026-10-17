---
id: FEAT-035
id_prefix: FEAT
title: "FEAT-035: E2E CI Scaffold"
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

# FEAT-035: E2E CI Scaffold

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- .ai/standards/automated-gates.md — gate command list (E2E tests gate)

## Purpose And Scope
Delivers the Playwright E2E GitHub Actions CI workflow (`.github/workflows/e2e.yml`) and the Playwright configuration file (`src/frontend/playwright.config.ts`) that wire the E2E test gate required by `.ai/standards/automated-gates.md`. FEAT-001 installs the `playwright` npm package; this feature wires the E2E CI job and config so the gate is active.

Does not cover: writing application-level E2E test scenarios (those belong to story features); Playwright browser download commands (handled by the CI workflow itself via `npx playwright install`).

## Feature Type
Type: Enabling

## Objective
Deliver the Playwright E2E CI workflow and Playwright config targeting the local-dev Docker URL (`http://nginx:80`), providing the E2E CI gate on which all story features' E2E tests will run.

## Dependencies
- Depends on: FEAT-001

## Inputs And Contracts
- STD-001 v0.1 § Automated Gate Commands — E2E tests gate command: `playwright test`
- .ai/standards/automated-gates.md — E2E tests row requiring a separate CI job
- TST-001 v0.1 § Test Levels — E2E testing scope

## Context Pack
- STD-001 v0.1 § Automated Gate Commands
- .ai/standards/automated-gates.md

## Files To Create Or Modify
- `.github/workflows/e2e.yml`
- `src/frontend/playwright.config.ts`

## New Packages
- None

## Out Of Scope
No application features or React pages. No Playwright test scenario files (each story feature adds its own). Backend Django code — other features. Playwright npm package installation — FEAT-001. Production CI environment variables — Phase 8.

## Risk Tier
Tier: Critical
CI infrastructure gate; a missing or broken E2E workflow blocks the E2E gate for every subsequent story feature.

## Implementation Steps
1. Write `.github/workflows/e2e.yml` with an `e2e` job that: starts Docker Compose services (`docker compose up -d`), runs `npx playwright install --with-deps chromium`, runs `npx playwright test` from `src/frontend/`, and exits 0.
2. Write `src/frontend/playwright.config.ts` configuring `baseURL: 'http://nginx:80'`, `testDir: './e2e'`, `use: { headless: true }`, and a single Chromium project.
3. Run the E2E job locally (or dry-run) and confirm the workflow exits 0 on an empty `e2e/` directory.

## Test Plan
- TST-001 AC-5: Given `.github/workflows/e2e.yml` is committed to the repository, when the GitHub Actions E2E job runs on the main branch, then each Playwright step exits 0 and the job reports success.
- STD-001 AC-5: Given `src/frontend/playwright.config.ts` specifies `baseURL: 'http://nginx:80'`, when `npx playwright test` is invoked in CI against that URL, then the Playwright test runner loads the configuration without errors and exits 0 on the empty `e2e/` directory.
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 2 | 4 |
| Source files (non-test) | 2 | 10 |

Expected test runtime: 2 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-035` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-035-ACC.

## Risks
- The E2E workflow requires Docker Compose services to be healthy before Playwright tests run; the workflow must include a health-check wait step.
- `npx playwright install` downloads browser binaries; CI environment must allow network access or use a cached browser layer.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; STD-001 v0.1; TST-001 v0.1; .ai/standards/automated-gates.md; FEAT-001
- Downstream: FEAT-035-TASKS; FEAT-035-ACC; FEAT-035-STATUS; Phase 6 PR

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
