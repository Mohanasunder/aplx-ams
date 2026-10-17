---
id: FEAT-001
id_prefix: FEAT
title: "FEAT-001: Frontend Scaffold — React 18, Nginx, and Frontend CI Gates — Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-001: Frontend Scaffold — React 18, Nginx, and Frontend CI Gates — Acceptance Criteria

## Input References
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- .ai/standards/automated-gates.md — gate command list

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-001 (Enabling). All criteria cite STD-001 or TST-001 IDs.

## Acceptance Criteria
STD-001 AC-1: Given `npm install` runs in `src/frontend/`, when `npm run build` completes, then the React 18 application is built to `src/frontend/dist/` and the command exits 0.
TST-001 AC-1: Given a fresh clone, when `npm run test -- --run` runs in `src/frontend/`, then Vitest runs at least one sample test, that test passes, and the command exits 0.
STD-001 AC-2: Given the frontend source in `src/frontend/src/`, when `npx eslint src/frontend/src/` and `npx tsc --noEmit` run in sequence, then each exits 0 on the skeleton codebase.
TST-001 AC-2: Given the CI pipeline `.github/workflows/ci.yml`, when the `frontend` job runs (`npm install`, `npm run build`, `npm run test -- --run`, eslint, tsc --noEmit), then each step exits 0.

## Test Scenarios
- STD-001 AC-1: Given `npm install` runs in `src/frontend/`... — verify Given/When/Then conditions as stated above.
- TST-001 AC-1: Given a fresh clone... — verify Given/When/Then conditions as stated above.
- STD-001 AC-2: Given the frontend source in `src/frontend/src/`... — verify Given/When/Then conditions as stated above.
- TST-001 AC-2: Given the CI pipeline `.github/workflows/ci.yml`... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: STD-001 v0.1; TST-001 v0.1; .ai/standards/automated-gates.md; PIB-005 v0.1
- Downstream: FEAT-001-TASKS (builder task list); Phase 6 test set FEAT-001-TESTS

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
