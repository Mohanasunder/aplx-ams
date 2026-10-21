---
id: FEAT-036-ACC
title: "FEAT-036: AppShell - Global Navigation Shell and Sign Out - Acceptance Criteria"
phase: 5
version: 0.2
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
date: 2026-10-19
validation: Pass
---
# FEAT-036: AppShell - Global Navigation Shell and Sign Out - Acceptance Criteria

## Input References
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17) § AppShell
- API-001 v0.2 — APLX AMS: API Specification (Approved 2026-10-17) § F-5
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17) § Authentication F-5

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-036. Criteria are derived from UIS-001 v0.1 § AppShell and API-001 v0.2 § F-5 (the AppShell was not covered by any REQ story; the gap was identified as OQ-073 and resolved by creating this feature).

## Acceptance Criteria
UIS-001 v0.1 § AppShell AC-1: Given a user is authenticated, when any authenticated route renders, then the AppShell is visible with MuiTypography text "APLX AMS", a MuiChip showing the user's role label, and a MuiButton labelled "Sign out".
UIS-001 v0.1 § AppShell AC-2: Given a user is on an authenticated page, when the user clicks "Sign out", then the browser calls POST /api/auth/logout/, AuthContext user is cleared to null, and the browser navigates to /login.
UIS-001 v0.1 § AppShell AC-3: Given a user loads an authenticated route, when AuthProvider mounts, then it calls GET /api/auth/me/; if the response is 200 the user is set in AuthContext and the authenticated layout renders; if the response is 401 the browser navigates to /login.
UIS-001 v0.1 § AppShell AC-4: Given the user has role delivery_manager, l2l3_support, or client_user, when the MuiDrawer nav renders, then it shows exactly the links defined in UIS-001 v0.1 § AppShell for that role (delivery_manager: Tickets, User accounts, Client organizations, Holiday list, Live dashboard, Monthly client report, Security events; l2l3_support: Tickets, Live dashboard, Monthly client report; client_user: Tickets, Monthly client report) and no others.

## Test Scenarios
UIS-001 v0.1 § AppShell AC-1: Render AppShell with a mocked authenticated user; assert "APLX AMS" text, role chip text matching the user's role, and "Sign out" button are all present in the rendered output.
UIS-001 v0.1 § AppShell AC-2: Render AppShell with POST /api/auth/logout/ mocked to return 200; simulate click on "Sign out"; assert the logout endpoint was called once, AuthContext user is null, and useNavigate was called with "/login".
UIS-001 v0.1 § AppShell AC-3 (200 path): Mount AuthProvider with GET /api/auth/me/ returning `{"role":"delivery_manager","org":"Applexus"}`; assert AuthContext user is set and the authenticated layout renders. (401 path): Mount AuthProvider with GET /api/auth/me/ returning 401; assert useNavigate is called with "/login".
UIS-001 v0.1 § AppShell AC-4: For each role (delivery_manager, l2l3_support, client_user), mount AppShell with the role set in AuthContext; assert the nav drawer contains exactly the links specified in UIS-001 v0.1 § AppShell for that role, verified by link text.

## Assumptions
- A-048: These criteria are spec-derived from UIS-001 v0.1 § AppShell and API-001 v0.2 § F-5 because the AppShell was not assigned to any REQ story. Logged in docs/logs/assumptions-log.md.

## Open Questions
- OQ-073: Answered — Mohanasunder approved creating FEAT-036 (2026-10-19).
- OQ-074: Answered — DEC-088 (2026-10-19, Mohanasunder): UIS-001 v0.1 § AppShell sourcing accepted; plan.md reclassified to Type: Enabling.

## Traceability Links
- Upstream: UIS-001 v0.1 § AppShell; API-001 v0.2 § F-5; PRM-001 v0.1 § Authentication F-5; docs/logs/open-questions-log.md; docs/logs/decision-log.md
- Downstream: FEAT-036-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
| Version | 0.2 |
| Conditions | None |
| Comments | SCR S-17 role name correction applied |
| Timestamp | 2026-10-21 13:05 UTC |
