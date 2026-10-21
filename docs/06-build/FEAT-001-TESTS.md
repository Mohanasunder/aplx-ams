---
id: FEAT-001-TESTS
title: FEAT-001: Frontend Scaffold - Test Set
phase: 6
version: 0.2
template: feature-test-set
template_version: 1.0
status: Draft
author_agent: frontend-builder
approver: Mohanasunder
date: 2026-10-21
validation: Pass
---
# FEAT-001: Frontend Scaffold - Test Set

## Input References
- FEAT-001 plan.md v0.1 (Approved 2026-10-17, Mohanasunder)
- FEAT-001-ACC v0.1 (Approved 2026-10-17, Mohanasunder)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- SCR S-17 (2026-10-21): App.test.tsx update — FEAT-036 replaces `<nav>APLX AMS</nav>` with AppShell; TST-001 AC-1 must assert Login renders for unauthenticated users instead of asserting APLX AMS text on App root

## Purpose And Scope
Defines the tests that determine done for FEAT-001 (Enabling — React 18, Nginx, and Frontend CI Gates), updated in v0.2 per SCR S-17. Coverage: frontend layer only (1 Vitest test). Three of the four acceptance criteria are CI-gate-only checks; they are verified by the `frontend` job in `.github/workflows/ci.yml`. No database, backend, or integration tests for this feature. Phase 7 regression scope: the App render test in `App.test.tsx` remains in scope.

Note: Updated by FEAT-036 per SCR S-17 rejection of v0.1 (FEAT-001-TESTS rejected 2026-10-21 to allow App.test.tsx update). The FEAT-036 frontend-builder updated App.test.tsx in Mode A to assert Login renders for unauthenticated users, replacing the previous assertion on 'APLX AMS' text which FEAT-036 removes from App.tsx and replaces with AppShell.

## Risk Tier And Test Approver
- Risk tier: Critical (from FEAT-001 plan.md — frontend CI infrastructure; a broken frontend build gate or Nginx misconfiguration blocks all subsequent frontend features)
- Test approver: Tech lead (Mohanasunder) — per `.ai/standards/review-and-approval.md` § Test set approval

## Criteria To Tests Map

| Criterion ID | Description | Test file | Test function | Layer | What it asserts | Mode A state |
|---|---|---|---|---|---|---|
| TST-001 AC-1 | Vitest runs ≥1 test, passes, exits 0 | `src/frontend/src/App.test.tsx` | `TST-001 AC-1: unauthenticated app renders Login page` | Frontend | `screen.getByRole('heading', { level: 1, name: /sign in/i })` finds the Sign in h1, confirming the Login page renders for unauthenticated users at the default route. me() is mocked to reject with 401 so the test is correct in both Mode A (Login shown via `*` catch-all route) and Mode B (Login shown after AuthProvider 401 redirect). | Green in Mode A — Login renders at default `*` route; test passes |
| STD-001 AC-1 | `npm run build` exits 0; `dist/` written | N/A — CI gate | N/A — CI gate | Frontend CI gate | `npm run build` step in the `frontend` job of `.github/workflows/ci.yml` exits 0 and writes `src/frontend/dist/` | Pending Mode B — CI yml not yet written at test commit |
| STD-001 AC-2 | `eslint` + `tsc --noEmit` each exit 0 | N/A — CI gate | N/A — CI gate | Frontend CI gate | `npx eslint src/frontend/src/` and `npx tsc --noEmit` steps in the `frontend` CI job each exit 0 | Pending Mode B — CI yml not yet written at test commit |
| TST-001 AC-2 | CI `frontend` job all steps exit 0 | N/A — CI artefact | N/A — CI artefact | CI artefact | All steps in `.github/workflows/ci.yml` `frontend` job (`npm install`, `npm run build`, `npm run test -- --run`, eslint, tsc --noEmit) exit 0 | Pending Mode B — CI yml not yet written at test commit |

## Test Files
- `src/frontend/src/App.test.tsx` (locked once this artifact is Approved)

## Stubs Created
Not applicable - v0.2 update covers existing implementation. The App.tsx stub was created in FEAT-001 Mode A (v0.1). The TST-001 AC-1 test is now implementation-correct for both current state and post-FEAT-036 state.

## Red Run Evidence
Not applicable for v0.2 update — the updated TST-001 AC-1 test is GREEN in the current state (Login renders at default route) and GREEN in Mode B (Login renders after AuthProvider 401 redirect). The test is not red because its purpose is to verify the unauthenticated default behavior, which already works. Red/green status per criterion:
- TST-001 AC-1: Green (App.test.tsx passes in current state — Login shown via `*` catch-all route)
- STD-001 AC-1, STD-001 AC-2, TST-001 AC-2: CI-gate-only; red run evidence from FEAT-001 Mode B CI job.

## Test Commit
v0.2 commit: on branch `feature/FEAT-036-appshell-nav` (FEAT-036 Mode A commit)
v0.1 commit: `670019bd4e3b2ba5a69b206880b69971efed6618` on branch `feature/FEAT-001-frontend-scaffold`

## Assumptions
- A-041 (Confirmed): FEAT-001's CI E2E job runs `playwright test --passWithNoTests`; no `playwright.config.ts` or e2e test file is added in this feature. Human decision: Mohanasunder, 2026-10-18 (DEC-056).

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-001 plan.md v0.1; FEAT-001-ACC v0.1; STD-001 v0.1; TST-001 v0.1; SCR S-17 (2026-10-21)
- Downstream: Phase 6 implementation (Mode B); `.github/workflows/ci.yml` (FEAT-001 frontend job); Phase 6 PR for FEAT-001; FEAT-036 Mode B (AppShell implementation)

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test (TST-001 AC-1 has a Vitest test; STD-001 AC-1, STD-001 AC-2, TST-001 AC-2 are CI-gate-only checks per their acceptance criteria, pending Mode B)
- [x] Tests assert behavior, not only that code runs (getByRole asserts rendered heading with accessible name)
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | |
| Role | Tech lead |
| Version | 0.2 |
| Conditions | |
| Comments | v0.2 created by FEAT-036 Mode A per SCR S-17 to update TST-001 AC-1 (App.test.tsx) for FEAT-036 AppShell changes. |
| Timestamp | |
