---
id: FEAT-035
id_prefix: FEAT
title: "FEAT-035: E2E CI Scaffold — Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-035: E2E CI Scaffold — Tasks

## Input References
- FEAT-035 plan.md — implementation steps and file list
- STD-001 v0.1 § Automated Gate Commands — E2E gate command
- .ai/standards/automated-gates.md — E2E tests row

## Purpose And Scope
Ordered task checklist for the builder of FEAT-035. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Write `.github/workflows/e2e.yml` with an `e2e` job: start Docker Compose services (`docker compose up -d`), wait for Nginx health, install Playwright browsers (`npx playwright install --with-deps chromium`), run `npx playwright test` from `src/frontend/`, and exit 0.
- [ ] T-2: Write `src/frontend/playwright.config.ts` configuring `baseURL: 'http://nginx:80'`, `testDir: './e2e'`, `use: { headless: true }`, and a single Chromium project.
- [ ] T-3: Verify the E2E workflow exits 0 on an empty `e2e/` directory (dry-run or local Docker Compose).
- [ ] T-4: Verify `python3 scripts/check_feature_size.py size FEAT-035` exits 0.
- [ ] T-5: Verify `python3 scripts/context_pack.py check FEAT-035` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-035 plan.md; STD-001 v0.1; TST-001 v0.1; .ai/standards/automated-gates.md
- Downstream: FEAT-035-TESTS (Phase 6 test set)

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
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
