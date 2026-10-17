---
id: FEAT-001-TASKS
id_prefix: FEAT
title: "FEAT-001: Frontend Scaffold â€” React 18, Nginx, and Frontend CI Gates â€” Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-001: Frontend Scaffold â€” React 18, Nginx, and Frontend CI Gates â€” Tasks

## Input References
- FEAT-001 plan.md â€” implementation steps and file list
- STD-001 v0.1 Â§ Automated Gate Commands â€” gate commands to wire
- STD-001 v0.1 Â§ Approved Technology List â€” packages

## Purpose And Scope
Ordered task checklist for the builder of FEAT-001. Each task names the file(s) it produces.

## Task Checklist
- [x] T-1: Update `docker-compose.yml`: add `frontend` build service (Node 24 LTS) and `nginx` service proxying `/api/` to the `app` service and `/` to the Vite dist.
- [x] T-2: Write `nginx/nginx.conf` proxying `/api/` to `app:8000` and serving `src/frontend/dist/` for all other paths.
- [x] T-3: Write `src/aplx_ams_django/middleware.py` with `RLSContextMiddleware`, `AbsoluteSessionTimeoutMiddleware`, and `SecurityHeadersMiddleware` (CSP, X-Frame-Options) per STD-001 Â§ Backend file and folder structure.
- [x] T-4: Update `.github/workflows/ci.yml` (created in FEAT-000): add `frontend` job with steps: `npm install`, `npm run build`, `npm run test -- --run`, eslint, tsc --noEmit.
- [x] T-5: Write `src/frontend/package.json` with all npm packages listed under New Packages at stated version specs.
- [x] T-6: Write `src/frontend/vite.config.ts` with `@vitejs/plugin-react` and `coverage` configured.
- [x] T-7: Write `src/frontend/tsconfig.json` with strict TypeScript settings (target ES2022, moduleResolution bundler).
- [x] T-8: Write `src/frontend/eslint.config.js` with `@typescript-eslint` rules.
- [x] T-9: Write `src/frontend/src/App.tsx` as a minimal root component rendering `<div>APLX AMS</div>`.
- [x] T-10: Write `src/frontend/src/main.tsx` as the Vite entry point mounting `<App />`.
- [x] T-11: Write `src/frontend/src/App.test.tsx` with one sample Vitest test asserting the root renders.
- [x] T-12: Run frontend gate commands: `npx eslint src/frontend/src/`, `npx tsc --noEmit`, `npm run test -- --run --coverage`; assert each exits 0.
- [x] T-13: Run backend gate commands: ruff, mypy, pytest --cov, bandit, pip-audit, detect-secrets; assert each exits 0.
- [x] T-14: Verify `python3 scripts/check_feature_size.py size FEAT-001` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-001 plan.md; STD-001 v0.1; TST-001 v0.1
- Downstream: Phase 6 test set (created in Phase 6)

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
