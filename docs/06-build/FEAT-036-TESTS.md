---
id: FEAT-036-TESTS
title: "FEAT-036: AppShell - Global Navigation Shell and Sign Out - Test Set"
phase: 6
version: 0.1
template: feature-test-set
template_version: 1.0
status: Approved
author_agent: documentation-writer
approver: Mohanasunder
date: 2026-10-21
validation: Pass
---
# FEAT-036: AppShell - Global Navigation Shell and Sign Out - Test Set

## Input References
- FEAT-036 plan.md v0.3 (Approved 2026-10-21, Mohanasunder) — docs/05-build-plan/feature-036-appshell-nav/plan.md
- FEAT-036-ACC v0.2 (Approved 2026-10-21, Mohanasunder) — docs/05-build-plan/feature-036-appshell-nav/acceptance.md
- UIS-001 v0.1 § AppShell — role-based nav link sets
- API-001 v0.2 § F-5 — GET /api/auth/me/, POST /api/auth/logout/
- PRM-001 v0.1 § Authentication F-5

## Purpose And Scope
Defines the tests that determine done for FEAT-036 (AppShell — Global Navigation Shell and Sign Out). Coverage: frontend layer only (9 Vitest unit tests). No database or backend tests — this feature makes no backend changes. Integration with AuthContext is tested by mocking API calls; AC-3 tests are co-located in AppShell.test.tsx because they verify AuthProvider's mount behavior which AppShell depends on. Phase 7 regression scope: AppShell.test.tsx (all 9 tests) remains in scope.

## Risk Tier And Test Approver
- Risk tier: High (from FEAT-036 plan.md — AuthContext.tsx is modified; an error here breaks authentication for every authenticated page)
- Test approver: Tech lead (Mohanasunder) — per `.ai/standards/review-and-approval.md` § Test set approval (High tier: tech lead)

## Criteria To Tests Map

| Criterion ID | Description | Test file | Test name | Layer | What it asserts | Mode A state |
|---|---|---|---|---|---|---|
| AC-1 | AppShell renders MuiTypography "APLX AMS", role chip, and "Sign out" button for an authenticated user | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-1: renders APLX AMS typography` | Frontend | `screen.getByText('APLX AMS')` finds the MuiTypography heading | Red — AppShell stub returns null; element not found |
| AC-1 | AppShell renders role chip with user's role label | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-1: renders role chip with role label` | Frontend | `screen.getByText('delivery_manager')` finds the MuiChip label | Red — AppShell stub returns null; element not found |
| AC-1 | AppShell renders "Sign out" button | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-1: renders Sign out button` | Frontend | `screen.getByRole('button', { name: /sign out/i })` finds the MuiButton | Red — AppShell stub returns null; no button in DOM |
| AC-2 | Clicking "Sign out" calls POST /api/auth/logout/, clears AuthContext user to null, and navigates to /login | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-2: sign out calls logout, clears user, and navigates to /login` | Frontend | `logout` mock called once; `setUser` called with null; `navigate` called with '/login' | Red — no "Sign out" button in DOM; logout/setUser/navigate never called |
| AC-3 (200) | AuthProvider calls GET /api/auth/me/ on mount; on 200 sets user in AuthContext and authenticated layout renders | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-3 (200): AuthProvider calls me() on mount; authenticated layout renders` | Frontend | `me` mock called once; `screen.getByText('APLX AMS')` visible after mount | Red — AuthProvider does not call me() on mount; layout never renders |
| AC-3 (401) | AuthProvider calls GET /api/auth/me/ on mount; on 401 navigates to /login | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-3 (401): AuthProvider calls me() on mount; on 401 navigates to /login` | Frontend | `navigate` called with '/login' after 401 error response | Red — AuthProvider does not call me() on mount; navigate never called |
| AC-4 (delivery_manager) | Nav drawer shows exactly 7 links for delivery_manager: Tickets, User accounts, Client organizations, Holiday list, Live dashboard, Monthly client report, Security events | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-4 (delivery_manager): shows all 7 DM nav links and only those` | Frontend | Each of the 7 link texts found; `queryAllByRole('link')` count is 7 | Red — AppShell stub returns null; no nav links in DOM |
| AC-4 (l2l3_support) | Nav drawer shows exactly 3 links for l2l3_support: Tickets, Live dashboard, Monthly client report; DM-only items absent | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-4 (l2l3_support): shows 3 nav links and only those` | Frontend | 3 allowed link texts found; DM-only items (User accounts, Client organizations, Holiday list, Security events) absent; count is 3 | Red — AppShell stub returns null; no nav links in DOM |
| AC-4 (client_user) | Nav drawer shows exactly 2 links for client_user: Tickets, Monthly client report; all others absent | `src/frontend/src/components/AppShell.test.tsx` | `FEAT-036 AC-4 (client_user): shows 2 nav links and only those` | Frontend | 2 allowed link texts found; 5 non-client-user items absent; count is 2 | Red — AppShell stub returns null; no nav links in DOM |

Note on AC-4 role-total count assertion: tests use `screen.queryAllByRole('link')` to verify exactly the right number of nav items render. Mode B builder must render nav items as `<a>` elements (e.g., via `react-router-dom` `<Link>` component, which renders as `<a role="link">`) for the count assertions to pass. MUI `<ListItemButton>` alone does not have `role=link`; wrapping with `<Link>` gives the correct role.

## Test Files
- `src/frontend/src/components/AppShell.test.tsx` (new — locked once this artifact is Approved)
- `src/frontend/src/App.test.tsx` (updated — re-locked under FEAT-001-TESTS.md v0.2 once that artifact is Approved)

## Stubs Created
- `src/frontend/src/components/AppShell.tsx` (new — empty stub, exports `AppShell()` returning `null`; not locked)

## Red Run Evidence
Command: `cd src/frontend && npm run test -- --run`
Date: 2026-10-21
Branch: feature/FEAT-036-appshell-nav
Commit: aeb8323

```
❯ src/components/AppShell.test.tsx (9 tests | 9 failed) 2182ms
  × FEAT-036 AC-1: AppShell renders authenticated layout > FEAT-036 AC-1: renders APLX AMS typography
    → Unable to find an element with the text: APLX AMS.
  × FEAT-036 AC-1: AppShell renders authenticated layout > FEAT-036 AC-1: renders role chip with role label
    → Unable to find an element with the text: delivery_manager.
  × FEAT-036 AC-1: AppShell renders authenticated layout > FEAT-036 AC-1: renders Sign out button
    → Unable to find an accessible element with the role "button" and name `/sign out/i`
  × FEAT-036 AC-2: sign out flow > FEAT-036 AC-2: sign out calls logout, clears user, and navigates to /login
    → Unable to find an accessible element with the role "button" and name `/sign out/i`
  × FEAT-036 AC-3: me() called on mount > FEAT-036 AC-3 (200): AuthProvider calls me() on mount; authenticated layout renders
    → expected "spy" to be called 1 times, but got 0 times
  × FEAT-036 AC-3: me() called on mount > FEAT-036 AC-3 (401): AuthProvider calls me() on mount; on 401 navigates to /login
    → expected "spy" to be called with arguments: [ '/login' ] — Number of calls: 0
  × FEAT-036 AC-4: role-based navigation links > FEAT-036 AC-4 (delivery_manager): shows all 7 DM nav links and only those
    → Unable to find an element with the text: Tickets.
  × FEAT-036 AC-4: role-based navigation links > FEAT-036 AC-4 (l2l3_support): shows 3 nav links and only those
    → Unable to find an element with the text: Tickets.
  × FEAT-036 AC-4: role-based navigation links > FEAT-036 AC-4 (client_user): shows 2 nav links and only those
    → Unable to find an element with the text: Tickets.

 Test Files  1 failed | 5 passed (6)
       Tests  9 failed | 27 passed (36)
```

All 9 AppShell tests fail for behavioral reasons (missing implementation). App.test.tsx (TST-001 AC-1 updated) PASSES — acceptable per plan.md Mode A instructions; the test verifies unauthenticated default behavior which already works.

## Test Commit
`aeb8323` on branch `feature/FEAT-036-appshell-nav`

## Assumptions
- A-049: `loading: boolean` will be added to `AuthContextValue` in Mode B (implied by UIS-001 v0.1 § AppShell loading state; not named in AC-3 but required for MuiCircularProgress). Tests use `@ts-expect-error` on the `loading` prop until Mode B adds it to the type. Logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-036 plan.md v0.3; FEAT-036-ACC v0.2; UIS-001 v0.1 § AppShell; API-001 v0.2 § F-5; PRM-001 v0.1 § Authentication F-5
- Downstream: FEAT-036 Mode B implementation; FEAT-036 PR; Phase 7 regression suite

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every acceptance criterion maps to at least one test (AC-1: 3 tests; AC-2: 1 test; AC-3: 2 tests; AC-4: 3 tests)
- [x] Tests assert behavior, not only that code runs (getByText, getByRole, mock call count assertions)
- [x] Red run shows every new test failing for the missing behavior (AppShell stub returns null)
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
| Comments | All 9 tests correctly express AC-1 through AC-4. AC-4 link-count assertion noted; Mode B builder must use react-router-dom Link for nav items. |
| Timestamp | 2026-10-21 13:26 UTC |
