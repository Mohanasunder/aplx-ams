---
id: FEAT-035-ACC
id_prefix: FEAT
title: "FEAT-035: E2E CI Scaffold â€” Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-035: E2E CI Scaffold â€” Acceptance Criteria

## Input References
- STD-001 v0.1 â€” APLX AMS: Coding Standards (Approved 2026-10-17) Â§ Automated Gate Commands
- TST-001 v0.1 â€” APLX AMS: Test Strategy (Approved 2026-10-17) Â§ Test Levels
- .ai/standards/automated-gates.md â€” E2E tests gate row

## Purpose And Scope
Covers the 2 acceptance criteria for FEAT-035 (Enabling). Both criteria cite TST-001 or STD-001 IDs as required for an Enabling feature.

## Acceptance Criteria
TST-001 AC-5: Given `.github/workflows/e2e.yml` is committed to the repository, when the GitHub Actions E2E job runs on the main branch, then each Playwright step exits 0 and the job reports success.
STD-001 AC-5: Given `src/frontend/playwright.config.ts` specifies `baseURL: 'http://nginx:80'` (the local-dev Docker Nginx service), when `npx playwright test` is invoked in CI against that URL, then the Playwright test runner loads the configuration without errors and exits 0 on the empty `e2e/` directory.

## Test Scenarios
- TST-001 AC-5: Given `.github/workflows/e2e.yml` committed... â€” verify the E2E job runs end-to-end in GitHub Actions and all steps exit 0.
- STD-001 AC-5: Given `src/frontend/playwright.config.ts` with `baseURL: 'http://nginx:80'`... â€” verify `npx playwright test` initializes and exits 0 on the empty test suite.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: STD-001 v0.1; TST-001 v0.1; .ai/standards/automated-gates.md; PIB-005 v0.1
- Downstream: FEAT-035-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
