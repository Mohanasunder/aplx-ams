---
id: FEAT-001
id_prefix: FEAT
title: "FEAT-001: Frontend Scaffold — React 18, Nginx, and Frontend CI Gates"
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
# FEAT-001: Frontend Scaffold — React 18, Nginx, and Frontend CI Gates

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Approved Technology List, § Automated Gate Commands
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17) § Module Structure
- .ai/standards/automated-gates.md — gate command list

## Purpose And Scope
Delivers the frontend scaffold — react 18, nginx, and frontend ci gates as the enabling infrastructure for all subsequent story features.

## Feature Type
Type: Enabling

## Objective
Deliver the React 18 + TypeScript + Vite + MUI v6 frontend scaffold with an Nginx proxy container and wired frontend CI gates (ESLint, tsc --noEmit, Vitest with 70% coverage threshold), providing the baseline on which all subsequent story features build their UI.

## Dependencies
- Depends on: FEAT-000

## Inputs And Contracts
- STD-001 v0.1 § Automated Gate Commands — CI gate commands
- STD-001 v0.1 § Approved Technology List — packages allowed
- .ai/standards/automated-gates.md — full gate list

## Context Pack
- STD-001 v0.1 § Approved Technology List
- STD-001 v0.1 § Backend file and folder structure
- STD-001 v0.1 § Automated Gate Commands
- BED-001 v0.1 § Module Structure

## Files To Create Or Modify
- `docker-compose.yml`
- `nginx/nginx.conf`
- `src/aplx_ams_django/middleware.py`
- `.github/workflows/ci.yml`
- `src/frontend/package.json`
- `src/frontend/vite.config.ts`
- `src/frontend/tsconfig.json`
- `src/frontend/eslint.config.js`
- `src/frontend/src/App.tsx`
- `src/frontend/src/main.tsx`

## New Packages
- npm: react @^18.3 | MIT | React 18 UI framework (ADR A-3); alternatives: none approved
- npm: react-dom @^18.3 | MIT | React DOM renderer (ADR A-3); alternatives: none approved
- npm: typescript @^5.5 | Apache-2.0 | TypeScript 5 (ADR A-3); alternatives: none
- npm: vite @^5.4 | MIT | Vite build tool (ADR A-3); alternatives: none approved
- npm: @vitejs/plugin-react @^4.3 | MIT | Vite React plugin (ADR A-3); alternatives: none
- npm: @mui/material @^6.1 | MIT | Material UI v6 (DEC-041); alternatives: none approved
- npm: @mui/icons-material @^6.1 | MIT | MUI icon set (DEC-041); alternatives: none
- npm: @emotion/react @^11.13 | MIT | Required peer dep of @mui/material v6 (DEC-041); alternatives: none
- npm: @emotion/styled @^11.13 | MIT | Required peer dep of @mui/material v6 (DEC-041); alternatives: none
- npm: eslint @^9.9 | MIT | Linter (DEC-043); alternatives: none approved
- npm: @typescript-eslint/parser @^8.5 | MIT | TS ESLint parser (DEC-043); alternatives: none
- npm: @typescript-eslint/eslint-plugin @^8.5 | MIT | TS ESLint rules (DEC-043); alternatives: none
- npm: vitest @^2.0 | MIT | Frontend test runner (DEC-043); alternatives: none approved
- npm: @vitest/coverage-v8 @^2.0 | MIT | Coverage for Vitest (DEC-043); alternatives: none
- npm: @testing-library/react @^16.0 | MIT | React test utilities (DEC-043); alternatives: none
- npm: playwright @^1.47 | Apache-2.0 | E2E test runner (DEC-043); alternatives: none approved
- npm: @axe-core/playwright @^4.10 | MPL-2.0 | Accessibility scan (DEC-044); alternatives: none
- npm: package.json | N/A | Lockfile: src/frontend/package-lock.json

## Out Of Scope
All story-level React pages and API modules — each story feature adds its own pages. Backend Django apps (organizations, accounts, tickets, sla, effort, reports, audit) — FEAT-002 onward. Backend Python packages — installed in FEAT-000. Production Nginx SSL certificates and server configuration — Phase 8.

## Risk Tier
Tier: Critical
Frontend CI infrastructure; a broken frontend build gate or Nginx misconfiguration blocks all subsequent frontend features.

## Implementation Steps
1. Update `docker-compose.yml`: add `frontend` build service (Node 24 LTS) and `nginx` service proxying `/api/` to the `app` service and `/` to the Vite dist.
2. Write `nginx/nginx.conf` proxying `/api/` to `app:8000` and serving `src/frontend/dist/` for all other paths.
3. Write `src/aplx_ams_django/middleware.py` with `RLSContextMiddleware`, `AbsoluteSessionTimeoutMiddleware`, and `SecurityHeadersMiddleware` (CSP, X-Frame-Options) per STD-001 § Backend file and folder structure.
4. Update `.github/workflows/ci.yml` (created in FEAT-000): add `frontend` job with steps: `npm install`, `npm run build`, `npm run test -- --run`, eslint, tsc --noEmit.
5. Write `src/frontend/package.json` with all npm packages listed under New Packages at stated version specs.
6. Write `src/frontend/vite.config.ts` with `@vitejs/plugin-react` and `coverage` configured.
7. Write `src/frontend/tsconfig.json` with strict TypeScript settings (target ES2022, moduleResolution bundler).
8. Write `src/frontend/eslint.config.js` with `@typescript-eslint` rules.
9. Write `src/frontend/src/App.tsx` as a minimal root component rendering `<div>APLX AMS</div>`.
10. Write `src/frontend/src/main.tsx` as the Vite entry point mounting `<App />`.
11. Write `src/frontend/src/App.test.tsx` with one sample Vitest test asserting the root renders.
12. Run all gate commands locally; confirm each exits 0.

## Test Plan
- STD-001 AC-1: Given `npm install` runs in `src/frontend/`, when `npm run build` completes, the...
- TST-001 AC-1: Given a fresh clone, when `npm run test -- --run` runs in `src/frontend/`, then ...
- STD-001 AC-2: Given the frontend source in `src/frontend/src/`, when `npx eslint src/frontend/...
- TST-001 AC-2: Given the CI pipeline `.github/workflows/ci.yml`, when the `frontend` job runs (...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 8 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-001` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-001-ACC.

## Risks
- `@emotion/react` and `@emotion/styled` are required peer dependencies of `@mui/material v6`; they are listed under New Packages with a note citing DEC-041. If a checker flags them, raise OQ before Phase 6 starts.
- Nginx container in CI requires the `docker compose build nginx` step to complete; builder must ensure the nginx service is included in the CI build job.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; STD-001 v0.1; TST-001 v0.1; BED-001 v0.1; .ai/standards/automated-gates.md
- Downstream: FEAT-001-TASKS; FEAT-001-ACC; FEAT-001-STATUS; Phase 6 PR

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
