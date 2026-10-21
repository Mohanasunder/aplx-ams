---
id: FEAT-036
title: "FEAT-036: AppShell - Global Navigation Shell and Sign Out"
phase: 5
version: 0.3
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
date: 2026-10-19
validation: Pass
---
# FEAT-036: AppShell - Global Navigation Shell and Sign Out

## Input References
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17) § AppShell
- API-001 v0.3 — APLX AMS: API Specification (Approved 2026-10-17) § F-5
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17) § Authentication F-5
- FEAT-006 plan.md (Approved 2026-10-18) — AuthContext.tsx stub and auth API already built
- OQ-073 — AppShell gap identified in FEAT-006 live review; Mohanasunder approved creating FEAT-036 (2026-10-19)
- DEC-088 (2026-10-19, Mohanasunder) — UIS-001 v0.1 § AppShell sourcing accepted; Type reclassified to Enabling (OQ-074)

## Purpose And Scope
Delivers the global AppShell (MuiAppBar + MuiDrawer) that wraps every authenticated page. Fixes the two gaps identified in FEAT-006 AIR F-04: AuthContext.tsx must call GET /api/auth/me/ on mount to restore session, and must expose signOut() to clear AuthContext and redirect to /login after POST /api/auth/logout/. Covers UIS-001 v0.1 § AppShell (layout, role badge chip, sign-out button, role-based nav drawer) and API-001 v0.3 § F-5 (GET /api/auth/me/, POST /api/auth/logout/).

## Feature Type
Type: Enabling

## Objective
Implement the AppShell component (MuiAppBar, MuiDrawer, role badge chip, sign-out button, and role-based navigation links) and complete AuthContext.tsx so that authenticated sessions are restored on mount and users can sign out. Every authenticated page rendered after FEAT-036 will be wrapped by AppShell.

## Dependencies
- Depends on: FEAT-006

## Inputs And Contracts
- UIS-001 v0.1 § AppShell — layout, MUI component spec, role-based nav link sets, loading state (MuiCircularProgress), session expiry redirect
- API-001 v0.3 § F-5 — GET /api/auth/me/ (returns `{"role": ..., "org": ...}`; 401 if unauthenticated); POST /api/auth/logout/ (200 on success)
- PRM-001 v0.1 § Authentication F-5 — all authenticated roles can call /api/auth/me/ for their own record

## Context Pack
- UIS-001 v0.1 § AppShell
- API-001 v0.3 § Authentication (F-5)
- PRM-001 v0.1 § Authentication (F-5)
- src/frontend/src/context/AuthContext.tsx
- src/frontend/src/App.tsx

## Files To Create Or Modify

**Frontend (source files)**
- `src/frontend/src/components/AppShell.tsx` (new)
- `src/frontend/src/context/AuthContext.tsx` (update: add me() on mount, expose signOut())
- `src/frontend/src/App.tsx` (update: wrap authenticated routes in AppShell; keep /login outside AppShell)

**Tests**
- `src/frontend/src/components/AppShell.test.tsx` (new — Vitest unit tests for AC-1, AC-2, AC-3, AC-4)

## New Packages
None

## Out Of Scope
- Route-level permission guards for individual pages (each feature owns its own page guards)
- Profile page or account settings page
- Session timeout middleware (FEAT-001)
- Backend changes of any kind; no new Django views, models, or migrations
- Ticket placeholder page content (beyond the existing /tickets stub added in FEAT-006 commit 40b2e6c)
- React Query or SWR session caching layer (401 detection uses the Axios interceptor already configured in FEAT-006)

## Risk Tier
Tier: High
This feature touches AuthContext.tsx (session restore on mount and sign-out flow), which controls whether a user is authenticated in the UI; an error here bypasses or breaks authentication for every authenticated page.

## Implementation Steps
1. Update `src/frontend/src/context/AuthContext.tsx`: add a `useEffect` that calls GET /api/auth/me/ on mount; on 200 set user in state; on 401 navigate to /login; expose `signOut()` that calls POST /api/auth/logout/, clears user state, and navigates to /login. Add `signOut` to the context value type.
2. Create `src/frontend/src/components/AppShell.tsx`: render MuiAppBar + MuiToolbar containing MuiTypography "APLX AMS", MuiChip showing the role label from AuthContext, and MuiButton "Sign out" calling `signOut()`. Render MuiDrawer (variant="permanent") with nav links filtered by role per UIS-001 v0.1 § AppShell (delivery_manager: Tickets / User accounts / Client organizations / Holiday list / Live dashboard / Monthly client report / Security events; l2l3_support: Tickets / Live dashboard / Monthly client report; client_user: Tickets / Monthly client report). Show MuiCircularProgress centered while GET /api/auth/me/ resolves on mount (loading state from AuthContext).
3. Update `src/frontend/src/App.tsx`: wrap authenticated routes in `<AppShell>` as a layout route; keep the /login route outside AppShell. Remove any inline nav elements that duplicate AppShell.
4. Write `src/frontend/src/components/AppShell.test.tsx`: one test per acceptance criterion (render check for AC-1, sign-out mock for AC-2, me() mount call and 401 redirect for AC-3, role-based link set for each role — delivery_manager, l2l3_support, client_user — for AC-4).

## Test Plan
- UIS-001 v0.1 § AppShell AC-1: Render AppShell in a test environment with an authenticated user; assert MuiTypography "APLX AMS", MuiChip with role label, and MuiButton "Sign out" are visible.
- UIS-001 v0.1 § AppShell AC-2: Mount AppShell with a mocked auth API; click "Sign out"; assert POST /api/auth/logout/ is called, AuthContext user is null, and the router navigates to /login.
- UIS-001 v0.1 § AppShell AC-3: Mount AuthProvider with GET /api/auth/me/ mocked to return 200 `{"role":"delivery_manager","org":"Applexus"}`; assert user is set and the authenticated layout renders. Then mount with me() returning 401; assert navigation to /login.
- UIS-001 v0.1 § AppShell AC-4: Mount AppShell for each of the three roles (delivery_manager, l2l3_support, client_user); assert exactly the nav links defined in UIS-001 v0.1 § AppShell are present and no others.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 3 | 30 |

Expected test runtime: 3 minutes
Open design decisions: None

## Definition Of Done
- [ ] All 4 acceptance criteria pass (verified by AppShell.test.tsx per the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `py -3 scripts/check_feature_size.py size FEAT-036` exits 0. (Known exception: script does not accept UIS- prefix for Enabling type; DEC-088 records Mohanasunder's override. Human to update check_feature_size.py to support UIS- sourcing when convenient.)
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in package.json at the stated version spec (None for this feature).
- [ ] PR description states `Tier: High` and references FEAT-036-ACC.

## Risks
- AuthContext.tsx is modified by FEAT-006 (currently in review, PR #17). The builder must branch FEAT-036 from master only after FEAT-006 is merged; branching from the FEAT-006 branch risks carrying unreviewed code (A-048).
- The three-role nav link set must match UIS-001 v0.1 § AppShell exactly; any mismatch is a spec deviation requiring an SCR.
- Vitest ARIA queries may require explicit MUI component labeling (aria-label on MuiButton, chip text) to make assertions reliable; builder must add ARIA labels consistent with STD-001 v0.1.

## Assumptions
- A-048: Builder branches FEAT-036 from master after FEAT-006 is merged, not from feature/FEAT-006-sign-in-auth. The AuthContext.tsx stub in FEAT-006 (user always null, no me() on mount, no signOut()) is the correct starting point for FEAT-036 modifications. Logged in docs/logs/assumptions-log.md.

## Open Questions
- OQ-073: Answered — Mohanasunder approved creating FEAT-036 (2026-10-19).
- OQ-074: Answered — DEC-088 (2026-10-19, Mohanasunder): UIS-001 v0.1 § AppShell sourcing accepted; Type reclassified to Enabling.

## Traceability Links
- Upstream: UIS-001 v0.1 § AppShell; API-001 v0.3 § F-5; PRM-001 v0.1 § Authentication F-5; FEAT-006 plan.md; docs/logs/open-questions-log.md; docs/logs/decision-log.md
- Downstream: FEAT-036-TASKS; FEAT-036-ACC; FEAT-036-STATUS; Phase 6 PR

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
| Version | 0.3 |
| Conditions | None |
| Comments | SCR S-16 + SCR S-17 applied; plan v0.3 approved for Mode A |
| Timestamp | 2026-10-21 13:05 UTC |
