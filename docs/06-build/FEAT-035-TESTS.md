---
id: FEAT-035
title: FEAT-035: E2E CI Scaffold — Test Set
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Draft
author_agent: documentation-writer
approver: Human developer reviewer
date: 2026-10-18
validation: Pending
---
# FEAT-035: E2E CI Scaffold — Test Set

## Input References
- FEAT-035 plan.md v0.1 (Approved 2026-10-17)
- FEAT-035-ACC v0.1 (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- .ai/standards/automated-gates.md — E2E tests gate row

## Purpose And Scope
Covers the 2 acceptance criteria for FEAT-035 (Enabling — E2E CI Scaffold). Tests are written before implementation. Only the frontend layer is covered here. TST-001 AC-5 is a CI-level criterion (the GitHub Actions e2e.yml workflow run); it cannot be exercised by a local unit test — its red state is the absence of the workflow file. STD-001 AC-5 is covered by `src/frontend/e2e/scaffold.spec.ts`, which imports the Playwright config and asserts `use.baseURL` equals `'http://nginx:80'`. Phase 7 regression testing covers the full E2E job.

## Risk Tier And Test Approver
Tier: **Critical**. Approver required: **Tech lead** (Mohanasunder), per `.ai/standards/review-and-approval.md` Critical tier test approval rule.

## Criteria To Tests Map

| Criterion | Test file | Test name | Layer | What it asserts |
|---|---|---|---|---|
| TST-001 AC-5 | CI-level only (no unit test possible) | n/a — CI workflow run | CI | Red state = `.github/workflows/e2e.yml` does not exist; workflow cannot run until Mode B creates it. Green state = e2e.yml committed and every Playwright step exits 0 in GitHub Actions. |
| STD-001 AC-5 | `src/frontend/e2e/scaffold.spec.ts` | `playwright initialises with baseURL http://nginx:80` | Frontend | Imports `playwright.config.ts` default export and asserts `config.use?.baseURL === 'http://nginx:80'`. Fails with `Expected: "http://nginx:80", Received: undefined` until Mode B upgrades the config. |

## Test Files
- `src/frontend/e2e/scaffold.spec.ts` — locked once this artifact is Approved

## Stubs Created
Not applicable — the test imports the existing `playwright.config.ts` stub (no logic stubs required for this feature type).

## Red Run Evidence
Command: `cd src/frontend && npx playwright test --reporter=list`
Date: 2026-10-18
Branch: `feature/FEAT-035-e2e-ci-scaffold`

```
Running 1 test using 1 worker

  x  1 e2e\scaffold.spec.ts:14:1 › playwright initialises with baseURL http://nginx:80 (7ms)

  1) e2e\scaffold.spec.ts:14:1 › playwright initialises with baseURL http://nginx:80

    Error: expect(received).toBe(expected) // Object.is equality

    Expected: "http://nginx:80"
    Received: undefined

      15 |   // The config must specify baseURL so the E2E runner targets the correct Docker Nginx service.
      16 |   // Until playwright.config.ts is upgraded (Mode B), config.use?.baseURL is undefined → test is red.
    > 17 |   expect((config as { use?: { baseURL?: string } }).use?.baseURL).toBe('http://nginx:80');
         |                                                                   ^
      18 | });

  1 failed
    e2e\scaffold.spec.ts:14:1 › playwright initialises with baseURL http://nginx:80
```

Failure is `Expected: "http://nginx:80", Received: undefined` — the behavior is missing (no `use.baseURL` in the current stub config), not a syntax, import, or setup error.

TST-001 AC-5 red state: `.github/workflows/e2e.yml` does not exist on the branch as of test commit `13a976b`; the CI E2E job cannot run.

## Test Commit
`13a976b` — `FEAT-035: tests (frontend)` — branch `feature/FEAT-035-e2e-ci-scaffold` — 2026-10-18

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-035 plan.md v0.1; FEAT-035-ACC v0.1; STD-001 v0.1; TST-001 v0.1; .ai/standards/automated-gates.md
- Downstream: Phase 6 Mode B implementation (`.github/workflows/e2e.yml`, `src/frontend/playwright.config.ts`); Phase 6 PR for FEAT-035

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test
- [x] Tests assert behavior, not only that code runs
- [x] Red run shows every new test failing for the missing behavior
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
