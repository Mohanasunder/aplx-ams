---
id: FEAT-036-TASKS
title: "FEAT-036: AppShell - Global Navigation Shell and Sign Out - Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: Approved
author_agent: build-planner
approver: Mohanasunder
date: 2026-10-19
validation: Pass
---
# FEAT-036: AppShell - Global Navigation Shell and Sign Out - Tasks

## Input References
- FEAT-036 plan.md — implementation steps and file list
- UIS-001 v0.1 § AppShell — component spec and role-based nav link sets
- API-001 v0.3 § F-5 — GET /api/auth/me/ and POST /api/auth/logout/ contracts
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-036. Each task names the file(s) it produces or modifies. Tasks must be completed in order; T-1 and T-2 must be done before T-3 because App.tsx imports AppShell.

## Task Checklist
- [x] T-1: Update `src/frontend/src/context/AuthContext.tsx` — add `useEffect` that calls GET /api/auth/me/ on mount; on 200 set user in state; on 401 navigate to /login; add `signOut()` function that calls POST /api/auth/logout/, clears user to null, navigates to /login; add `signOut` to the context type definition.
- [x] T-2: Create `src/frontend/src/components/AppShell.tsx` — render MuiAppBar + MuiToolbar with MuiTypography "APLX AMS", MuiChip with role label from AuthContext, MuiButton "Sign out" calling `signOut()`; render MuiDrawer (variant="permanent") with nav links filtered by role per UIS-001 v0.1 § AppShell; show MuiCircularProgress centered while loading state is true (while GET /api/auth/me/ is pending on mount).
- [x] T-3: Update `src/frontend/src/App.tsx` — wrap authenticated routes in `<AppShell>` as a layout route; keep the /login route outside AppShell; remove any duplicate inline nav elements.
- [x] T-4: Write `src/frontend/src/components/AppShell.test.tsx` — test AC-1 (render check for title, chip, button), AC-2 (sign-out flow: POST called, user cleared, navigate to /login), AC-3 (me() on mount: 200 path sets user; 401 path navigates to /login), AC-4 (role-based nav: assert exact link set for each of the three roles per UIS-001 v0.1 § AppShell).
- [ ] T-5: Run `npm run lint` and `npm run type-check` in `src/frontend/`; fix all errors before proceeding.
- [ ] T-6: Run `py -3 scripts/check_feature_size.py size FEAT-036`; confirm exit code 0.

## Assumptions
- A-048: Builder branches from master after FEAT-006 is merged. AuthContext.tsx starting point is the FEAT-006 stub. Logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-036 plan.md; UIS-001 v0.1 § AppShell; API-001 v0.3 § F-5; STD-001 v0.1
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
| Role | Tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Approved with plan.md at Phase 5 gate — build-planner task list for FEAT-036 AppShell |
| Timestamp | 2026-10-21 12:38 UTC |
