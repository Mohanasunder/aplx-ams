---
id: FEAT-001-TESTS
title: FEAT-001: Frontend Scaffold - Test Set
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Approved
author_agent: documentation-writer
approver: Mohanasunder
date: 2026-10-18
validation: Pass
---
# FEAT-001: Frontend Scaffold - Test Set

## Input References
- FEAT-001 plan.md v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-001-ACC v0.1 (Approved 2026-10-17, Mohanasunder)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels

## Purpose And Scope
Defines the tests that determine done for FEAT-001 (Enabling — React 18, Nginx, and Frontend CI Gates), written before implementation (Mode A). Coverage: frontend layer only (1 Vitest test). Three of the four acceptance criteria are CI-gate-only checks; they are verified by the `frontend` job in `.github/workflows/ci.yml`, which is a Mode B artifact (not yet written at test commit time). No database, backend, or integration tests for this feature. Phase 7 regression scope: the App render test in `App.test.tsx` remains in scope.

## Risk Tier And Test Approver
- Risk tier: Critical (from FEAT-001 plan.md — frontend CI infrastructure; a broken frontend build gate or Nginx misconfiguration blocks all subsequent frontend features)
- Test approver: Tech lead (Mohanasunder) — per `.ai/standards/review-and-approval.md` § Test set approval

## Criteria To Tests Map

| Criterion ID | Description | Test file | Test function | Layer | What it asserts | Mode A state |
|---|---|---|---|---|---|---|
| TST-001 AC-1 | Vitest runs ≥1 test, passes, exits 0 | `src/frontend/src/App.test.tsx` | `TST-001 AC-1: renders App and finds "APLX AMS" text` | Frontend | `screen.getByText('APLX AMS')` finds a DOM node, confirming the root component renders the expected heading | Red — stub `App()` returns `null`; `screen.getByText('APLX AMS')` throws `TestingLibraryElementError` |
| STD-001 AC-1 | `npm run build` exits 0; `dist/` written | N/A — CI gate | N/A — CI gate | Frontend CI gate | `npm run build` step in the `frontend` job of `.github/workflows/ci.yml` exits 0 and writes `src/frontend/dist/` | Pending Mode B — CI yml not yet written at test commit |
| STD-001 AC-2 | `eslint` + `tsc --noEmit` each exit 0 | N/A — CI gate | N/A — CI gate | Frontend CI gate | `npx eslint src/frontend/src/` and `npx tsc --noEmit` steps in the `frontend` CI job each exit 0 | Pending Mode B — CI yml not yet written at test commit |
| TST-001 AC-2 | CI `frontend` job all steps exit 0 | N/A — CI artefact | N/A — CI artefact | CI artefact | All steps in `.github/workflows/ci.yml` `frontend` job (`npm install`, `npm run build`, `npm run test -- --run`, eslint, tsc --noEmit) exit 0 | Pending Mode B — CI yml not yet written at test commit |

## Test Files
- `src/frontend/src/App.test.tsx` (locked once this artifact is Approved)

## Stubs Created
- `src/frontend/src/App.tsx` — `App()` function returns `null` (no render logic); imported by `App.test.tsx` so the test compiles and fails on missing behavior

## Red Run Evidence
Command: `npm run test -- --run` (in `src/frontend/`)
Date: 2026-10-18
Result: 1 collected, 1 FAILED. Output:
```
FAIL src/frontend/src/App.test.tsx > TST-001 AC-1: renders App and finds "APLX AMS" text
TestingLibraryElementError: Unable to find an element with the text: APLX AMS.
  at screen.getByText (...)
```
Failure is behavioral: `App()` returns `null`; the DOM contains no text node matching `'APLX AMS'`. Not a syntax, import, or setup error.

Note: STD-001 AC-1, STD-001 AC-2, and TST-001 AC-2 are CI-gate-only checks; their red run occurs when the `frontend` CI job runs against the stub implementation. That evidence will be captured in Mode B when `.github/workflows/ci.yml` is written.

## Test Commit
`670019bd4e3b2ba5a69b206880b69971efed6618` on branch `feature/FEAT-001-frontend-scaffold`

## Assumptions
- A-041 (Confirmed): FEAT-001's CI E2E job runs `playwright test --passWithNoTests`; no `playwright.config.ts` or e2e test file is added in this feature. Human decision: Mohanasunder, 2026-10-18 (DEC-056).

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-001 plan.md v0.1; FEAT-001-ACC v0.1; STD-001 v0.1; TST-001 v0.1
- Downstream: Phase 6 implementation (Mode B); `.github/workflows/ci.yml` (FEAT-001 frontend job); Phase 6 PR for FEAT-001

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test (TST-001 AC-1 has a Vitest test; STD-001 AC-1, STD-001 AC-2, TST-001 AC-2 are CI-gate-only checks per their acceptance criteria, pending Mode B)
- [x] Tests assert behavior, not only that code runs (getByText asserts rendered content)
- [x] Red run shows every new test failing for the missing behavior (TST-001 AC-1: TestingLibraryElementError; CI-gate criteria pending Mode B)
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | None |
| Timestamp | 2026-10-17 21:01 UTC |
