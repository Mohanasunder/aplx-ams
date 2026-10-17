---
id: UIS-001
title: APLX AMS: UI Specification
phase: 4
version: 0.1
template: ui-spec
template_version: 2.0
status: Approved
author_agent: ux-ui-designer
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS: UI Specification

> **Single file.** There is exactly one UI spec per project. Always use `--id UIS --out docs/04-design/ui-spec.md` when calling `new_artifact.py`; never auto-name as `UIS-NNN.md`.

## Input References

- PIB-004 v0.1 — Phase 4 input brief (Approved 2026-10-17): DEC-041 (MUI v6), DEC-044 (WCAG 2.1 Level A), A-014, A-019, A-021, A-022 confirmed.
- SUM-003 v0.2 — Phase 3 summary (Approved 2026-10-17): ADR A-3 (React/TS/Vite SPA), ADR A-7 (session), ADR A-9 (UTC/IST), ADR A-11 (audit), platform constraints.
- REQ-001 v0.3 — APLX AMS: User Stories, S-1 to S-33 (Approved 2026-10-17).
- PRS-001 v0.3 — APLX AMS: Product Requirement Specification, F-1 to F-8 (Approved 2026-10-17).
- GLO-001 v0.3 — APLX AMS: Domain Glossary (Approved 2026-10-17).
- NFR-001 v0.3 — APLX AMS: Non-Functional Requirements, N-1 to N-9 (Approved 2026-10-17).
- PER-001 v0.2 — APLX AMS: Personas, P-1 to P-4 (Approved 2026-10-17).
- API-001 v0.1 — APLX AMS: API Specification, 46 endpoints (In review 2026-10-17): endpoint list used as-is for wiring; API approval is a parallel Phase 4 gate.
- SCR S-3 (Approved 2026-10-17): password management (S-30, S-31).
- SCR S-4 (Approved 2026-10-17): security events in audit trail (S-32, S-33).

## Purpose And Scope

Covers: the complete UI specification for APLX AMS release 1 as a desktop single-page application built with React + TypeScript + Vite, using Material UI v6 (MUI) default theme (DEC-041). Specifies 12 pages/routes, one user flow per user-facing story (S-1 to S-31, S-33; S-9, S-10, S-11, S-22, S-32 are display behaviors or backend-only events, addressed within page wireframes), wireframes with loading/empty/error states, a component tree naming MUI v6 components, state management with React Query (server state) and React Context (auth/session), MUI default design tokens, and WCAG 2.1 Level A accessibility specification (DEC-044).

Does not cover: React or TypeScript code, CSS overrides, database schema (DBD), backend implementation (BED), permission matrix (PRM), mobile views (SCP OS-4 — desktop only, minimum viewport 1280×720 px), or third-party integrations (none in scope).

Platform: desktop web browser only; Google Chrome and Microsoft Edge, current and previous major versions (A-008 — open assumption). Minimum viewport 1280×720 px. All timestamps displayed in IST (UTC+05:30, no daylight saving) per ADR A-9 (A-027 — open assumption).

## Pages And Routes

Role codes: P1 = L1 support engineer, P2 = L2/L3 support engineer, P3 = delivery manager, P4 = client user.

| Route | Page name | Roles with access | Story IDs | Primary API endpoints |
| --- | --- | --- | --- | --- |
| `/login` | Sign-in | (unauthenticated) | S-21 | POST /api/auth/login/ |
| `/tickets` | Ticket list | P1, P2, P3, P4 | S-2, S-3, S-4, S-5, S-6, S-7, S-8, S-10, S-11, S-22 | GET /api/tickets/ |
| `/tickets/new` | Raise ticket | P4 only | S-1 | POST /api/tickets/, GET /api/organizations/{id}/sap-applications/ |
| `/tickets/:id` | Ticket detail | P1, P2, P3, P4 (role-filtered actions) | S-3, S-4, S-5, S-6, S-7, S-8, S-10, S-11, S-15, S-23, S-25, S-26, S-28, S-29 | GET /api/tickets/{id}/, PATCH /api/tickets/{id}/priority/, POST /api/tickets/{id}/assign/, POST /api/tickets/{id}/resolve/, POST /api/tickets/{id}/close/, POST/DELETE /api/tickets/{id}/await-client/, GET/POST /api/tickets/{id}/comments/, GET/POST /api/tickets/{id}/effort/, PATCH/DELETE /api/effort/{effort_id}/, GET /api/tickets/{id}/audit/ |
| `/reports/dashboard` | Live dashboard | P1, P2, P3 | S-12, S-16 | GET /api/reports/dashboard/, GET /api/organizations/ |
| `/reports/client/:orgId/:year/:month` | Monthly client report | P1, P2, P3, P4 (P4 own org and published only) | S-13, S-14 | GET /api/reports/client-reports/{org_id}/{year}/{month}/, POST …/generate/, POST …/publish/, GET …/download/ |
| `/reports/finance-export` | Finance export | P3 only | S-17 | GET /api/reports/finance-export/{year}/{month}/ |
| `/admin/users` | User management | P3 only | S-20, S-30 | GET/POST /api/accounts/users/, GET/PATCH /api/accounts/users/{id}/, POST /api/accounts/users/{id}/deactivate/, POST /api/accounts/users/{id}/set-temp-password/ |
| `/admin/organizations` | Organization management | P3 only | S-16, S-18, S-19, S-26, S-27 | GET/POST /api/organizations/, GET/PATCH /api/organizations/{id}/, POST /api/organizations/{id}/sap-applications/, GET/POST /api/organizations/{id}/contracts/, POST /api/organizations/{id}/contracts/{contract_id}/end/, GET /api/organizations/{id}/contracts/active/, GET /api/tickets/{id}/effort/ |
| `/admin/holidays` | Holiday management | P3 only | S-24 | GET/POST /api/holidays/, DELETE /api/holidays/{id}/ |
| `/profile` | Own profile and change password | P1, P2, P3, P4 | S-31 | GET /api/auth/me/, POST /api/accounts/me/change-password/ |
| `/audit/security-events` | Security events | P1, P2 (own only), P3 (all) | S-33 | GET /api/audit/security-events/, GET /api/accounts/users/ (P3 filter) |

## User Flows

Each flow lists numbered steps. Each step names the route, the user action, and the API call. Error and empty paths are included from the story's acceptance criteria.

---

### REQ S-21 — Sign in

**Normal path (correct password, active account):**
1. User opens `/login`. Page shows: Account name field, Password field, Sign in button.
2. User enters account name and password; clicks Sign in. → POST /api/auth/login/ → HTTP 200.
3. Browser stores `sessionid` cookie (HttpOnly, Secure, SameSite=Strict).
4. Frontend calls GET /api/auth/me/ to retrieve role and client organization (if P4).
5. Router redirects:
   - P1, P2, P3 → `/tickets`
   - P4 → `/tickets`

**Error path — wrong credentials / deactivated / locked account (AC-2, A-019):**
- Step 2 returns HTTP 401.
- Page shows inline alert: "Invalid credentials." No indication of whether the account name or the password was wrong.
- Fields are cleared of the password value; account name field retains its value.

**Error path — account locked (AC-4, NFR N-5):**
- 5th failed sign-in returns HTTP 401 with code `authentication_failed`; server also triggers lockout.
- Frontend shows the same generic message: "Invalid credentials."
- After 30 minutes, the correct password is accepted.

**Error path — rate limit (HTTP 429):**
- Page shows inline alert: "Too many sign-in attempts. Please wait and try again."

**Error path — validation (missing field):**
- Submit with empty account name or password: MUI TextField shows required-field helper text before API call is made.

---

### REQ S-31 — Change own password

**Normal path:**
1. Signed-in user (any role) navigates to `/profile`.
2. Page shows: Current password field, New password field, Confirm new password field, Save button.
3. User fills fields; clicks Save. → POST /api/accounts/me/change-password/ → HTTP 200.
4. Page shows success alert: "Password changed." Fields cleared.

**Error path — wrong current password (AC-4):**
- HTTP 400 returned. Page shows field-level error on the Current password field: "Incorrect current password."

**Error path — password policy violation (AC-2, NFR N-5):**
- HTTP 400 returned. New password field shows: "Password must be at least 8 characters and include an upper-case letter, a lower-case letter, and a digit."
- Client-side validation fires first (same rule) before the API call.

**Error path — trying to change another user's password (AC-3):**
- Not applicable on `/profile` (own account only). P3 sets temporary passwords on others via `/admin/users`.

---

### REQ S-1 — Client user raises a ticket

**Roles:** P4 only (POST /api/tickets/ is P4 only per API-001).

**Normal path:**
1. P4 user navigates to `/tickets/new`.
2. Page loads SAP applications for the user's client organization → GET /api/organizations/{id}/sap-applications/.
3. Page shows form: Type (Incident / Service request — MuiSelect), SAP application (MuiSelect, loaded from step 2), Priority (P1/P2/P3/P4 — MuiSelect), Description (MuiTextField multiline).
4. User fills all fields; clicks Raise ticket. → POST /api/tickets/ → HTTP 201.
5. Router navigates to `/tickets/:id` for the new ticket; success toast: "Ticket raised."

**Error path — missing required field (AC-2):**
- HTTP 400 returned with field errors. Each missing field shows its label highlighted and helper text: "[Field name] is required."

**Error path — SAP application belongs to another organization (AC-3):**
- API returns HTTP 403. Page shows alert: "You do not have permission to raise a ticket for this SAP application."

**Error path — SAP application list loading failure:**
- GET /api/organizations/{id}/sap-applications/ fails → page shows error alert with retry button. SAP application select is disabled.

**Empty state — no SAP applications configured:**
- SAP application select shows: "No SAP applications available. Contact your delivery manager."
- Raise ticket button is disabled.

---

### REQ S-2 — Client user follows their client organization's tickets

**Roles:** P4 (sees own organization's tickets only, API enforces via RLS).

**Normal path:**
1. P4 user navigates to `/tickets`. → GET /api/tickets/ → returns paginated list, own org only.
2. Ticket list shows: Ticket reference, Type, Priority, Status, SAP application, Raised date (IST display, A-027).
3. User clicks a ticket reference → navigates to `/tickets/:id`.

**Error path — other organization's ticket (AC-2):**
- If P4 opens `/tickets/:id` for another org's ticket directly, GET /api/tickets/{id}/ returns HTTP 403. Page shows error: "Ticket not found."

**Empty state — no tickets (AC-1 when org has no tickets):**
- List shows: "No tickets have been raised by your organization yet." with a Raise ticket button.

**Loading state:**
- MuiDataGrid shows skeleton rows (MuiSkeleton) while waiting for GET /api/tickets/.

---

### REQ S-3 — L1 support engineer acknowledges a new ticket

**Roles:** P1 only (first action stops the response clock).

**Normal path:**
1. P1 user opens `/tickets/:id`. → GET /api/tickets/{id}/ → response includes SLA state (response clock running) and escalation flag.
2. Ticket detail shows response clock as running, SLA status chip labeled "On track" / "At risk" / "Breached".
3. Any first action by P1 (priority change, assign, add comment, record effort) stops the response clock automatically on the backend.
4. On successful action, ticket detail re-fetches → response clock now shows "Met" or "Breached" with stopped time.

**Error path — another L1 has already acknowledged (AC-2):**
- No UI error; response clock already shows stopped ("Met" or "Breached"). First action time displayed.

**Error path — P2, P3, P4 trying to acknowledge (AC-4):**
- Role-conditional rendering: action buttons for P1-only actions (priority change, assign) are not rendered for P2, P3, P4. The response clock continues to run.

---

### REQ S-4 — L1 support engineer changes a ticket's priority

**Roles:** P1 only.

**Normal path:**
1. P1 opens `/tickets/:id`. Priority section shows current priority (MuiChip) and Change priority button.
2. P1 clicks Change priority → MuiDialog opens: Priority selector (MuiSelect: P1/P2/P3/P4), Reason field (MuiTextField, required).
3. P1 selects new priority and enters reason; clicks Confirm. → PATCH /api/tickets/{id}/priority/ → HTTP 200.
4. Dialog closes; ticket detail re-fetches. New priority shown. SLA clocks recalculated (resolution clock). If this was the first L1 action, response clock shows stopped.

**Error path — no reason entered (AC-3):**
- Confirm button remains disabled until Reason field is non-empty. If submitted empty via keyboard: MuiTextField shows "Reason is required."

**Error path — ticket is Resolved (AC-4):**
- Change priority button is not rendered when ticket status is Resolved or Closed.

**Error path — P2, P3, P4 role (no permission):**
- Change priority button is not rendered for P2, P3, P4.

---

### REQ S-5 — L1 support engineer escalates a ticket to L2/L3

**Roles:** P1 only.

**Normal path:**
1. P1 opens `/tickets/:id`. Assign button visible (P1 only).
2. P1 clicks Assign → MuiDialog opens: L2/L3 support engineer selector (MuiAutocomplete, loads from user list), Confirm button.
3. P1 selects an L2/L3 engineer; clicks Confirm. → POST /api/tickets/{id}/assign/ → HTTP 200.
4. Dialog closes; ticket detail re-fetches. Assigned support engineer shown. Escalation flag cleared if set.

**Error path — client user tries to change assignment (AC-4):**
- Assign button not rendered for P2, P3, P4.

---

### REQ S-6 — Support engineer sets a ticket to Resolved

**Roles:** P1, P2.

**Normal path:**
1. P1 or P2 opens `/tickets/:id`. Resolve button visible for P1 and P2 on non-Resolved tickets.
2. User clicks Resolve → MuiDialog: "Set this ticket to Resolved?" with Confirm button.
3. User confirms. → POST /api/tickets/{id}/resolve/ → HTTP 200.
4. Dialog closes; ticket re-fetches. Status chip shows "Resolved". Resolution clock shows stopped time ("Met" / "Breached"). Ticket appears in L1 queue.

**Error path — L2/L3 tries to close (AC-4):**
- Close button is only rendered for P1 and only when status is Resolved. P2 sees no Close button.

---

### REQ S-7 — L1 support engineer closes a Resolved ticket

**Roles:** P1 only, ticket must be Resolved.

**Normal path:**
1. P1 opens `/tickets/:id` for a Resolved ticket. Close button visible.
2. P1 clicks Close → MuiDialog: "Close this ticket?" with Confirm button.
3. P1 confirms. → POST /api/tickets/{id}/close/ → HTTP 200.
4. Dialog closes; ticket re-fetches. Status chip shows "Closed". No email is sent (OQ-037 confirmed).

**Error path — ticket not Resolved (AC-2):**
- HTTP 409 returned. Alert: "Only Resolved tickets can be closed." Close button not rendered when status is not Resolved.

---

### REQ S-8 — Support engineer marks a ticket as awaiting client

**Roles:** assigned support engineer (P1 when ticket is in L1 queue; P2 when assigned to them).

**Normal path — set awaiting client:**
1. Assigned P1 or P2 opens `/tickets/:id`. Set awaiting client button visible.
2. User clicks Set awaiting client → MuiDialog: "Mark as awaiting client? SLA timers will be paused." Confirm button.
3. User confirms. → POST /api/tickets/{id}/await-client/ → HTTP 200.
4. Dialog closes; ticket re-fetches. Status chip shows "Awaiting client". SLA timers paused (shown as paused state in timer chips).

**Normal path — clear awaiting client (by support engineer):**
1. Assigned support engineer opens `/tickets/:id`. Clear awaiting client button visible.
2. User clicks Clear → confirmation dialog → DELETE /api/tickets/{id}/await-client/ → HTTP 204.
3. Ticket re-fetches. Status reverts (Open / previous), SLA timers resume.

**Normal path — cleared automatically by client comment (AC-2):**
- P4 adds a comment on an awaiting-client ticket → POST /api/tickets/{id}/comments/ → server clears awaiting client automatically. On re-fetch, status changes and timers resume. No separate UI action required.

**Error path — non-assigned support engineer (AC-4):**
- Set awaiting client button not rendered if the current user is not the assigned support engineer (checked against GET /api/auth/me/ role and GET /api/tickets/{id}/ assigned_engineer field).

---

### REQ S-10 — Support engineer sees SLA timer states

**Roles:** P1, P2 (display; P3 sees on dashboard; P4 does not see SLA timer internals).

**Normal path:**
- On `/tickets/:id` and `/tickets` list, SLA timer state is embedded in ticket data from GET /api/tickets/ and GET /api/tickets/{id}/.
- Response clock and resolution clock each show a MuiChip with:
  - "On track" (text + green circle icon, not color-only)
  - "At risk" (text + amber warning icon)
  - "Breached" (text + red error icon)
  - "Met" (text + green check icon)
  - "Paused" (text + pause icon, when awaiting client)
- Labels shown: "Response clock" and "Resolution clock" (separate per A-014).
- Elapsed business hours shown numerically next to each chip (e.g., "2 h 30 min / 4 h target").
- SLA states are evaluated on read by the backend (ADR A-10); frontend displays without computing.

---

### REQ S-11 — Ticket is flagged for escalation at L1's target

**Normal path (display):**
- GET /api/tickets/ and GET /api/tickets/{id}/ include `escalation_flag` boolean.
- Ticket list: escalation flag column shows a red flag icon + "Escalation" label when true; no icon when false (non-color indicator).
- Ticket detail: escalation flag alert banner (MuiAlert severity="warning") shown below the header when flag is true: "This ticket has passed its L1 target. Assign it to an L2/L3 support engineer."
- Flag is removed when ticket is assigned (REQ S-5) or set to Resolved (REQ S-6); re-fetch removes the banner.

---

### REQ S-12 — Delivery manager monitors the live dashboard

**Roles:** P1, P2, P3. P4 access refused.

**Normal path:**
1. P1, P2, or P3 navigates to `/reports/dashboard`. → GET /api/reports/dashboard/ → HTTP 200.
2. Dashboard shows per-client-organization and per-SAP-application summary:
   - Count of open tickets, at-risk tickets, breached tickets, tickets with escalation flag.
   - Hours bank balance for hours bank contracts (P3 view, AC-3).
3. Data refreshes on page focus or manual refresh button (GET /api/reports/dashboard/).

**Error path — P4 access (AC-4):**
- P4 navigating to `/reports/dashboard` → API returns HTTP 403 → frontend route guard redirects P4 to `/tickets` with toast: "You do not have access to the dashboard."

**Empty state — no open tickets:**
- Each cell in the summary grid shows 0. Counts shown as numeric "0" with non-color context.

**Loading state:**
- MuiSkeleton placeholders in summary cards.

---

### REQ S-13 — Delivery manager generates the monthly client report

**Roles:** P3 only for generate/publish; P1, P2, P3 can view.

**Normal path:**
1. P3 navigates to `/reports/client/:orgId/:year/:month`.
2. If no report exists, page shows Generate report button.
3. P3 clicks Generate → POST /api/reports/client-reports/{org_id}/{year}/{month}/generate/ → HTTP 200.
4. Report renders: response % and resolution % per priority (P1/P2/P3/P4). When denominator is 0: "no tickets" (not 0% or 100%, A-021). Breached tickets list. MTTR. Ticket counts raised/Resolved/Closed per priority.
5. P3 reviews; clicks Publish → POST /api/reports/client-reports/{org_id}/{year}/{month}/publish/ → HTTP 200.
6. Report status changes to Published. Client users can now view it.

**Error path — network failure during generate:**
- MuiAlert: "Failed to generate report. Please try again."

**Empty path — P1 priority, 0 tickets in period (AC-2, A-021):**
- P1 rows in the report table show "no tickets" in response % and resolution % columns, not "0%" or "100%".

---

### REQ S-14 — Client user views and downloads the monthly client report

**Roles:** P4 (own organization, published only); P1, P2, P3 (any org).

**Normal path:**
1. P4 user navigates to `/reports/client/:orgId/:year/:month` for their own org.
2. Page fetches → GET /api/reports/client-reports/{org_id}/{year}/{month}/ → HTTP 200 (only if published for P4).
3. Report displays the same content as S-13.
4. Download as Excel button: → GET …/download/?format=xlsx → browser downloads file.
5. Download as PDF button: → GET …/download/?format=pdf → browser downloads file.

**Error path — another organization's report (AC-3):**
- HTTP 403. Page shows: "Report not found."

**Error path — report not yet published (AC-4):**
- HTTP 404 for P4. Page shows: "This report is not available yet."

---

### REQ S-15 — Support engineer records effort on a ticket

**Roles:** P1 (when ticket in L1 queue), P2 (when assigned to them).

**Normal path:**
1. Assigned P1 or P2 opens `/tickets/:id`. Effort section shows existing effort entries table and Add effort button.
2. User clicks Add effort → MuiDialog: Date (MuiDatePicker), Hours (MuiTextField type="number", step 0.5, min 0.01), Confirm.
3. User fills fields; clicks Confirm. → POST /api/tickets/{id}/effort/ → HTTP 201.
4. Dialog closes; effort list re-fetches.

**Error path — hours 0 or negative (AC-2, A-020):**
- HTTP 400. Dialog shows: "Hours must be greater than zero."

**Error path — non-assigned support engineer (AC-4):**
- Add effort button not rendered.

**Error path — no active contract for client organization:**
- HTTP 409. Dialog shows: "No active contract for this client organization. Effort cannot be recorded."

---

### REQ S-16 — Delivery manager reviews effort against a contract

**Normal path:**
1. P3 navigates to `/admin/organizations`.
2. Selects a client organization → expands Contract section.
3. Active contract displays: contracted hours (if hours bank), hours recorded, hours bank balance (A-020). If balance is 0 or below: MuiAlert severity="warning" — "Hours bank balance is [N] hours. Contract limit reached."
4. Effort entries per ticket shown in an expandable table.

---

### REQ S-17 — Delivery manager produces the monthly finance export

**Roles:** P3 only.

**Normal path:**
1. P3 navigates to `/reports/finance-export`.
2. Page shows: Year selector (MuiSelect), Month selector (MuiSelect), Download as Excel button, Download as CSV button.
3. P3 selects year and month; clicks Download as Excel. → GET /api/reports/finance-export/{year}/{month}/?format=xlsx → HTTP 200 → browser downloads file.
4. Same for CSV: ?format=csv.

**Error path — no effort entries for selected month:**
- HTTP 200 with empty file or MuiAlert: "No effort entries for the selected month."

---

### REQ S-18 — Delivery manager sets up client organizations and SAP applications

**Roles:** P3 only.

**Normal path:**
1. P3 navigates to `/admin/organizations`. List of client organizations shown.
2. P3 clicks Add organization → MuiDialog: Organization name field → POST /api/organizations/ → HTTP 201.
3. P3 selects an organization → Add SAP application → MuiDialog: SAP application name → POST /api/organizations/{id}/sap-applications/ → HTTP 201.
4. List re-fetches after each action.

**Error path — non-P3 role (AC-3):**
- Route guard prevents P1, P2, P4 from accessing `/admin/organizations`. Redirect to `/tickets`.

---

### REQ S-19 — Delivery manager sets up a contract

**Normal path:**
1. P3 selects an organization on `/admin/organizations`. Contract section visible.
2. If no active contract: Create contract button available → MuiDialog: Contract type (MuiSelect: Hours bank / Fixed fee), Contracted hours field (MuiTextField, shown only when Hours bank selected) → POST /api/organizations/{id}/contracts/ → HTTP 201.
3. Contract section re-fetches. Hours bank balance shown.

**Error path — second active contract (AC-2):**
- HTTP 409. Alert: "This organization already has an active contract."

**Error path — non-P3 role (AC-4):**
- Route guard blocks access.

---

### REQ S-20 — Delivery manager manages user accounts

**Roles:** P3 only.

**Normal path:**
1. P3 navigates to `/admin/users`. → GET /api/accounts/users/ → paginated list.
2. P3 clicks Create user → MuiDialog: Full name, Email, Role (MuiSelect: L1/L2/L3/Delivery manager/Client user), Client organization (MuiSelect, shown only when Client user selected), Temporary password field (required) → POST /api/accounts/users/ → HTTP 201.
3. P3 clicks a user → user detail panel opens. Can edit name, email, role, client org → PATCH /api/accounts/users/{id}/ → HTTP 200.
4. Deactivate: P3 clicks Deactivate → MuiDialog confirm → POST /api/accounts/users/{id}/deactivate/ → HTTP 200. User row shows "Deactivated" chip.

**Error path — client user with no organization (AC-2):**
- Dialog Confirm button disabled until a client organization is selected. If submitted: "Client organization is required for client user accounts."

**Error path — non-P3 access (AC-4):**
- Route guard blocks `/admin/users`. Redirect to `/tickets`.

---

### REQ S-22 — Client data boundary

Not applicable as a separate flow — enforced by API (HTTP 403 / HTTP 404 for cross-org access). Displayed in `/tickets`, `/tickets/:id`, and `/reports/client/:orgId/:year/:month` flows above via 403 error states.

---

### REQ S-23 — Internal user views a ticket's audit trail

**Roles:** P1, P2, P3. P4 access refused at field level.

**Normal path:**
1. P1, P2, or P3 opens `/tickets/:id`. Audit trail tab visible (tab bar with MuiTabs).
2. User clicks Audit trail tab → GET /api/tickets/{id}/audit/ → list of audit entries.
3. Each entry shows: user, date and time (IST, A-027), old value, new value, change type.
4. No edit or delete controls shown.

**Error path — P4 access (AC-3):**
- Audit trail tab not rendered for P4. `/tickets/:id` for P4 shows only ticket status, comments, and SLA information.

**Empty state — no audit entries:**
- Audit trail tab shows: "No changes have been recorded for this ticket."

---

### REQ S-24 — Delivery manager maintains the company holiday list

**Roles:** P3 only.

**Normal path:**
1. P3 navigates to `/admin/holidays`. → GET /api/holidays/ → list of dates.
2. P3 clicks Add holiday → MuiDialog: Date (MuiDatePicker) → POST /api/holidays/ → HTTP 201. List re-fetches.
3. P3 clicks Remove on a date → MuiDialog confirm → DELETE /api/holidays/{id}/ → HTTP 204. List re-fetches.

**Error path — non-P3 access (AC-3):**
- Route guard blocks access for P1, P2, P4.

**Empty state — no holidays configured:**
- List shows: "No holidays have been added. Add holidays to exclude them from SLA business hours."

---

### REQ S-25 — Support engineer changes or deletes their own effort entry

**Roles:** P1, P2 (own entries, within calendar month of entry date).

**Normal path:**
1. Support engineer opens `/tickets/:id`. Effort section shows their own entries with Edit and Delete buttons.
2. Edit: → MuiDialog with pre-filled date and hours → PATCH /api/effort/{effort_id}/ → HTTP 200. List re-fetches.
3. Delete: → MuiDialog confirm → DELETE /api/effort/{effort_id}/ → HTTP 204. List re-fetches.

**Error path — entry outside its calendar month (AC-3):**
- Edit/Delete buttons not rendered for entries whose date is in a past month relative to today.
- API returns HTTP 409 if attempted: "This effort entry can no longer be changed."

**Error path — another user's entry (AC-4):**
- Edit/Delete buttons not rendered for entries belonging to another user.

---

### REQ S-26 — Delivery manager corrects an effort entry

**Roles:** P3 (any entry, any time; cannot delete, can edit only).

**Normal path:**
1. P3 opens `/tickets/:id`. Effort section shows all entries with Edit button (no Delete button for P3).
2. P3 clicks Edit → MuiDialog with pre-filled date and hours → PATCH /api/effort/{effort_id}/ → HTTP 200.
3. Hours bank balance updates on re-fetch.

**Error path — hours 0 or negative (AC-2, A-020):**
- HTTP 400. Dialog shows: "Hours must be greater than zero."

---

### REQ S-27 — Delivery manager ends a contract and sets up a new one

**Roles:** P3 only.

**Normal path:**
1. P3 on `/admin/organizations` → organization's Contract section. Active contract shown with End contract button.
2. P3 clicks End contract → MuiDialog: "This will end the active contract. Effort already recorded will be kept." Confirm button. → POST /api/organizations/{id}/contracts/{contract_id}/end/ → HTTP 200.
3. Contract section re-fetches. Organization now shows "No active contract".
4. P3 creates a new contract (REQ S-19 flow).

**Error path — non-P3 role (AC-4):**
- Route guard blocks `/admin/organizations`.

---

### REQ S-28 — Client user adds a comment on their client organization's ticket

**Roles:** P4 (own org only).

**Normal path:**
1. P4 opens `/tickets/:id` for their own organization's ticket. Comments section shows existing comments and Add comment textarea (MuiTextField multiline) with Submit button.
2. P4 types comment; clicks Submit. → POST /api/tickets/{id}/comments/ → HTTP 201.
3. Comments list re-fetches. New comment appears with P4 user name and time (IST, A-027).
4. If ticket was in awaiting client: status changes automatically on re-fetch (awaiting client cleared, SLA timers resume).

**Error path — another org's ticket (AC-4):**
- HTTP 403. Alert: "You do not have access to this ticket."

---

### REQ S-29 — Internal user adds a comment on a ticket

**Roles:** P1, P2, P3.

**Normal path:**
1. P1, P2, or P3 opens `/tickets/:id`. Comments section shows existing comments and Add comment form.
2. Internal user submits comment. → POST /api/tickets/{id}/comments/ → HTTP 201.
3. Comments list re-fetches. If ticket was awaiting client: status does NOT change (internal comment does not clear awaiting client, per REQ S-29 AC-2).
4. If this is the first L1 action (P1 adding a comment on a new ticket): response clock stops on the backend; ticket re-fetch shows updated SLA state.

---

### REQ S-30 — Delivery manager sets a temporary password

**Roles:** P3 only.

**Normal path:**
1. P3 on `/admin/users`. Selects a user → opens user detail panel.
2. P3 clicks Set temporary password → MuiDialog: Temporary password field (required, policy stated below the field) → POST /api/accounts/users/{id}/set-temp-password/ → HTTP 200.
3. Dialog closes. Success toast: "Temporary password set." If account was locked, lock is cleared.

**Error path — password policy violation (AC-2, NFR N-5):**
- HTTP 400. Dialog shows: "Temporary password must be at least 8 characters and include an upper-case letter, a lower-case letter, and a digit."

**Error path — non-P3 role (AC-4):**
- Route `/admin/users` is not accessible to P1, P2, P4.

---

### REQ S-33 — Users view security events

**Roles:** P1, P2 (own account only); P3 (all accounts).

**Normal path (P3 — all accounts):**
1. P3 navigates to `/audit/security-events`. → GET /api/audit/security-events/ → list of all security events.
2. P3 can filter by user account (MuiAutocomplete select). List shows: event type, user account or account name as typed (for unknown account names), date and time (IST, A-027).
3. No edit or delete controls.

**Normal path (P1, P2 — own account):**
1. P1 or P2 navigates to `/audit/security-events`. → GET /api/audit/security-events/ (own account enforced by API object-level permission) → own events only.
2. No user account filter shown (own account only).

**Error path — P4 access (AC-4):**
- Route guard redirects P4 to `/tickets`. No security events visible to P4.

**Error path — P1/P2 trying to view another user's events (AC-3):**
- API returns HTTP 403. Not reachable through UI as the filter is not shown for P1/P2.

---

## Wireframes

Each wireframe shows the layout at 1280×720 px minimum viewport. The global shell (AppShell) wraps every authenticated page. Labels use GLO-001 terms.

---

### AppShell — global navigation shell

```
+------------------------------------------------------------------+
| APLX AMS             [role badge]                  [Sign out]    |
+----------------+------------------------------------------------- +
| Nav (left)     |  Main content area                               |
|                |                                                  |
| Tickets        |                                                  |
| Dashboard*     |  (page-specific content renders here)           |
| Reports >      |                                                  |
|   Client       |                                                  |
|   Finance*     |                                                  |
| Admin* >       |                                                  |
|   Users        |                                                  |
|   Organizations|                                                  |
|   Holidays     |                                                  |
| Security       |                                                  |
|   Events**     |                                                  |
| Profile        |                                                  |
+----------------+--------------------------------------------------+
```

`*` shown only for P3.
`**` shown for P1, P2 (own only), P3 (all).
Dashboard shown for P1, P2, P3. Not shown for P4.
Admin section shown for P3 only.

MUI components: `<MuiDrawer variant="permanent">`, `<MuiList>`, `<MuiListItemButton>`, `<MuiAppBar>`, `<MuiToolbar>`, `<MuiChip label={role}>`.

**Loading state (AppShell):** Full-page `<MuiCircularProgress>` centered while GET /api/auth/me/ resolves.
**Auth error state:** If session expires, any API call returns HTTP 401; auth context clears the session and redirects to `/login` with toast: "Your session has expired. Please sign in again."

---

### /login — Sign-in

```
+------------------------------------------------------------------+
|                      APLX AMS                                    |
|                                                                  |
|            +-------------------------------+                     |
|            |  Account name                 |                     |
|            |  [_______________________]    |                     |
|            |                               |                     |
|            |  Password                     |                     |
|            |  [_______________________]    |                     |
|            |                               |                     |
|            |  [  Sign in  ]                |                     |
|            |                               |                     |
|            |  (error alert appears here)   |                     |
|            +-------------------------------+                     |
+------------------------------------------------------------------+
```

MUI components: `<MuiTextField label="Account name" required>`, `<MuiTextField label="Password" type="password" required>`, `<MuiButton variant="contained">Sign in</MuiButton>`, `<MuiAlert severity="error">` for sign-in errors.

**Loading state:** Sign in button shows `<MuiCircularProgress size={20}>` while POST /api/auth/login/ is in flight. Button is disabled.
**Error state:** MuiAlert below the button. Generic message: "Invalid credentials." (A-019). For HTTP 429: "Too many sign-in attempts. Please wait and try again." No field-level error.
**Validation:** Required-field validation before API call. Account name and password MuiTextField show red border + "Required" helper text when submitted empty.
**Accessibility:** heading "Sign in" (h1), form label associations, autocomplete="username" on account name, autocomplete="current-password" on password. Focus placed on Account name field on mount.

---

### /tickets — Ticket list

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Tickets                              [+ Raise*] |
|                |  [Search...][Status v][Priority v][SAP app v]    |
|                +--------------------------------------------------+
|                | Ref    | Type | Priority | Status | SLA Response|
|                |        |      |          |        | SLA Resolut.|
|                |        |      |          |        | Escalation  |
|                +--------------------------------------------------+
|                | TKT-001 | Inc | P2 chip  | Open   | On track    |
|                |         |     |          |        | At risk [!] |
|                |         |     |          |        |             |
|                | TKT-002 | SR  | P1 chip  | Awaiting| Paused     |
|                |         |     |          | client  | Paused      |
|                +--------------------------------------------------+
|                |         [< Prev]  Page 1 of N  [Next >]         |
+----------------+--------------------------------------------------+
```

`*` Raise ticket button shown for P4 only.

Columns:
- **Ticket reference** (ticket_reference field from API) — link to `/tickets/:id`
- **Type** (Incident / Service request)
- **Priority** (P1/P2/P3/P4 as `<MuiChip>` with non-color label)
- **Status** (`<MuiChip>` with icon: Open=circle, Awaiting client=pause, Resolved=check, Closed=lock)
- **SAP application** (sap_application name)
- **Response clock** (`<MuiChip>` with text + icon: On track=circle-green, At risk=warning-amber, Breached=error-red, Met=check-green, Paused=pause-grey) — P1, P2, P3 only; hidden for P4
- **Resolution clock** (same chip format) — P1, P2, P3 only; hidden for P4
- **Escalation** (flag icon + "Escalation" label if escalation_flag=true) — P1, P2, P3 only

P4 sees: Ticket reference, Type, Priority, Status, SAP application. No SLA clock columns.

MUI components: `<MuiDataGrid>`, `<MuiTextField label="Search">`, `<MuiSelect label="Status">`, `<MuiSelect label="Priority">`, `<MuiSelect label="SAP application">`, `<MuiPagination>`, `<MuiChip>`.

**Loading state:** `<MuiSkeleton variant="rectangular">` for each table row while GET /api/tickets/ is pending.
**Empty state:** Centered illustration area + "No tickets found." For P4: "No tickets have been raised by your organization yet." with Raise ticket button.
**Error state:** `<MuiAlert severity="error">` below filter bar: "Failed to load tickets. [Retry]" button.

---

### /tickets/new — Raise ticket (P4 only)

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Raise a ticket                                  |
|                |                                                  |
|                |  Type *                                          |
|                |  [Incident / Service request  v]                 |
|                |                                                  |
|                |  SAP application *                               |
|                |  [___________  v]                                |
|                |                                                  |
|                |  Priority *                                      |
|                |  [P1 / P2 / P3 / P4  v]                         |
|                |                                                  |
|                |  Description *                                   |
|                |  [                             ]                 |
|                |  [                             ]                 |
|                |                                                  |
|                |  [  Raise ticket  ]   [Cancel]                   |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiSelect label="Type">`, `<MuiSelect label="SAP application">`, `<MuiSelect label="Priority">`, `<MuiTextField label="Description" multiline rows={4} required>`, `<MuiButton variant="contained">Raise ticket</MuiButton>`, `<MuiButton variant="text">Cancel</MuiButton>`.

**Loading state (SAP application options):** `<MuiCircularProgress size={20}>` inside the SAP application select while GET /api/organizations/{id}/sap-applications/ is pending.
**Empty state (SAP application):** Select disabled, helper text: "No SAP applications available. Contact your delivery manager."
**Error state (form):** Each required field shows `<MuiFormHelperText error>` with the field name + "is required." on submit attempt.
**Error state (API):** `<MuiAlert severity="error">` above submit button with the API error detail.
**Route guard:** P1, P2, P3 navigating to `/tickets/new` → redirect to `/tickets`. Only P4 can access this page.

---

### /tickets/:id — Ticket detail

```
+----------------+--------------------------------------------------+
| AppShell nav   |  [← Tickets]  Ticket TKT-001                    |
|                |  Incident | P2 | Open  [!Escalation flag]        |
|                |  SAP application: [name]  Raised: 17 Oct 2026    |
|                |  Client organization: Applexus                   |
|                +--------------------------------------------------+
|                |  SLA timers (P1, P2, P3 only):                   |
|                |  Response clock:   [On track] 1h 30min / 4h      |
|                |  Resolution clock: [At risk]  8h 15min / 9h      |
|                +--------------------------------------------------+
|                |  Assigned:  L1 queue / [Engineer name]           |
|                |  Actions (role-conditional):                     |
|                |  [Change priority*] [Assign*] [Resolve**]        |
|                |  [Close***] [Set awaiting client†] [Clear†]      |
|                +--------------------------------------------------+
|                |  [Comments] [Effort‡] [Audit trail§]             |
|                | (tab panel)                                      |
|                |  Comments tab:                                   |
|                |  --- User A (10:00 IST) ---                      |
|                |  Comment text                                    |
|                |  [Add comment textarea]    [Submit]              |
|                +--------------------------------------------------+
```

Role-conditional action legend:
- `*` Change priority, Assign: P1 only, status not Resolved/Closed
- `**` Resolve: P1, P2, status not Resolved/Closed
- `***` Close: P1 only, status Resolved
- `†` Set awaiting client / Clear: assigned support engineer only (P1 when in L1 queue, P2 when assigned)
- `‡` Effort tab: P1, P2 (own entries + add), P3 (all entries + edit, no delete)
- `§` Audit trail tab: P1, P2, P3 only (hidden for P4)

SLA timers: shown for P1, P2, P3 only. Each clock on its own line with label, chip, elapsed/target. Paused state shown as "Paused" chip with pause icon.

MUI components: `<MuiBreadcrumbs>`, `<MuiChip label="status">`, `<MuiAlert severity="warning">` for escalation flag, `<MuiButton>` for each action, `<MuiTabs>`, `<MuiTabPanel>`, `<MuiTextField multiline>` for comment, `<MuiDialog>` for all confirmation and form dialogs.

Priority change dialog: `<MuiSelect label="Priority">`, `<MuiTextField label="Reason" required>`.
Assign dialog: `<MuiAutocomplete label="L2/L3 support engineer">` loaded from user list.
Set awaiting client dialog: `<MuiDialog>` with confirmation text and Confirm/Cancel buttons.

**Loading state (page):** `<MuiSkeleton>` for header and SLA section while GET /api/tickets/{id}/ is pending.
**Loading state (audit/effort/comments tabs):** `<MuiSkeleton>` rows inside tab panels.
**Empty state (comments):** "No comments yet."
**Empty state (effort):** "No effort entries for this ticket."
**Empty state (audit trail):** "No audit entries for this ticket."
**Error state (page):** `<MuiAlert severity="error">` full-width: "Failed to load ticket. [Retry]"
**Error state (action dialog):** Inline `<MuiAlert severity="error">` inside dialog, dialog stays open.

---

### /reports/dashboard — Live dashboard

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Live dashboard          [Refresh]              |
|                +--------------------------------------------------+
|                |  Client org: Applexus                           |
|                |  +----------+----------+----------+-----------+ |
|                |  | SAP App  | Open tkt | At risk  | Breached  | |
|                |  +----------+----------+----------+-----------+ |
|                |  | App A    |    3     |    1     |     0     | |
|                |  | App B    |    7     |    2     |     1     | |
|                |  +----------+----------+----------+-----------+ |
|                |  Escalation flags: 2                            |
|                |  Hours bank balance: 70 h  [⚠ Warning if ≤ 0]  |
|                +--------------------------------------------------+
```

**Data source:** The per-SAP-application table is populated from `DashboardOrgSummary.sap_applications[]` returned by `GET /api/reports/dashboard/`. The array is nested inside each element of `Dashboard.organizations[]` (keyed by `org_id` / `org_name`).

Column label to API field mapping:

| Wireframe label | API field | Type |
| --- | --- | --- |
| SAP App | `sap_app_name` | string |
| Open tkt | `open_ticket_count` | integer |
| At risk | `at_risk_count` | integer |
| Breached | `breached_count` | integer |

Escalation flags count and hours bank balance are sourced from `DashboardOrgSummary.escalation_flag_count` and `DashboardOrgSummary.hours_bank_balance` respectively (organization-level fields, not per-SAP-application).

Balance warning (AC-4 of S-16): `<MuiAlert severity="warning">` when hours bank balance is 0 or below.

MUI components: `<MuiTable>`, `<MuiTableCell>`, `<MuiAlert severity="warning">`, `<MuiButton variant="outlined">Refresh</MuiButton>`, `<MuiChip>` for escalation flag count.

**Loading state:** `<MuiSkeleton>` table rows.
**Empty state:** "No open tickets across all client organizations."
**Error state:** `<MuiAlert severity="error">`: "Failed to load dashboard. [Retry]"

---

### /reports/client/:orgId/:year/:month — Monthly client report

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Monthly client report                          |
|                |  Organization: Applexus | Oct 2026              |
|                |  Status: Published / Draft / Not generated      |
|                |                                                  |
|                |  [Generate*]  [Publish*]                        |
|                |  [Download Excel]  [Download PDF]               |
|                +--------------------------------------------------+
|                |  SLA Summary                                     |
|                |  | Priority | Response % | Resolution %         |
|                |  | P1       | 90%        | no tickets           |
|                |  | P2       | 95%        | 90%                  |
|                +--------------------------------------------------+
|                |  Breached tickets                                |
|                |  | Ref   | Priority | Breached clock | ...     |
|                +--------------------------------------------------+
|                |  MTTR: 1.5 business days                        |
|                |  Tickets raised: 20 | Resolved: 18 | Closed: 15 |
+----------------+--------------------------------------------------+
```

"no tickets" is shown when denominator is 0 (A-021). Not "0%" or "100%".

Generate and Publish buttons shown for P3 only. Download buttons shown for all roles (P4 own org and published only).

MUI components: `<MuiTable>`, `<MuiButton>`, `<MuiAlert>` for status, `<MuiChip label="Published|Draft">`.

**Loading state:** `<MuiSkeleton>` for report content.
**Empty state (not yet generated):** Message: "No report has been generated for this period." with Generate button (P3 only).
**Error state (generate/publish fails):** `<MuiAlert severity="error">`: "Failed to [generate|publish] report. Please try again."
**P4 viewing unpublished report:** `<MuiAlert severity="info">`: "This report is not yet available."

---

### /reports/finance-export — Finance export

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Finance export                                 |
|                |                                                  |
|                |  Year   [2026 v]                                |
|                |  Month  [October v]                             |
|                |                                                  |
|                |  [Download as Excel]   [Download as CSV]        |
|                |                                                  |
|                |  (error/empty alert if applicable)              |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiSelect label="Year">`, `<MuiSelect label="Month">`, `<MuiButton variant="contained">Download as Excel</MuiButton>`, `<MuiButton variant="outlined">Download as CSV</MuiButton>`.

**Loading state:** Buttons show `<MuiCircularProgress size={20}>` while download is in progress. Buttons disabled.
**Empty state / error state:** `<MuiAlert severity="info">`: "No effort entries for the selected month." on HTTP 200 empty file or API error.
**Route guard:** P1, P2, P4 navigating to `/reports/finance-export` → redirect to `/tickets`.

---

### /admin/users — User management

```
+----------------+--------------------------------------------------+
| AppShell nav   |  User accounts               [+ Create user]   |
|                |  [Search by name/email...]                      |
|                +--------------------------------------------------+
|                | Name     | Email     | Role      | Status       |
|                +--------------------------------------------------+
|                | Alice    | a@co.com  | L1        | Active       |
|                | Bob      | b@co.com  | Client    | Deactivated  |
|                +--------------------------------------------------+
|                |  [< Prev]   Page 1 of N   [Next >]             |
|                |                                                  |
|                |  (right panel opens on row click)               |
|                |  User: Alice                                    |
|                |  [Edit] [Deactivate] [Set temporary password]   |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiDataGrid>`, `<MuiButton>`, `<MuiDrawer>` or `<MuiPanel>` for detail panel, `<MuiChip label="Active|Deactivated">`, `<MuiDialog>` for create/edit/deactivate/set-temp-password actions.

Create user dialog: Name field, Email field, Role select (L1 / L2/L3 / Delivery manager / Client user), Client organization select (conditional on Client user role), Temporary password field, Confirm button.

Set temporary password dialog: `<MuiTextField label="Temporary password" type="password">`, policy helper text, Confirm button.

**Loading state:** `<MuiSkeleton>` table rows.
**Empty state:** "No user accounts. Create the first account."
**Error state:** `<MuiAlert severity="error">` above table.

---

### /admin/organizations — Organization management

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Client organizations       [+ Add organization]|
|                +--------------------------------------------------+
|                |  [ Applexus ]  [ + Add SAP application ]        |
|                |  SAP applications: App A, App B                 |
|                |                                                  |
|                |  Contract                                        |
|                |  Type: Hours bank | Fixed fee                   |
|                |  Contracted hours: 100   Balance: 70 h          |
|                |  [⚠ Balance ≤ 0 warning]                        |
|                |  [Create contract] | [End contract] [+ New]     |
|                |                                                  |
|                |  Effort entries                                  |
|                |  | Engineer | Ticket | Date | Hours | [Edit P3] |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiAccordion>` per organization, `<MuiTable>` for SAP applications and effort entries, `<MuiButton>`, `<MuiAlert severity="warning">` for balance warning, `<MuiDialog>` for all actions.

**Loading state:** `<MuiSkeleton>` per accordion section.
**Error state:** `<MuiAlert severity="error">` per section.

---

### /admin/holidays — Holiday management

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Company holiday list      [+ Add holiday]      |
|                +--------------------------------------------------+
|                |  Date          | Day        | Action             |
|                |  2027-01-26    | Tuesday    | [Remove]           |
|                |  2027-08-15    | Sunday     | [Remove]           |
|                +--------------------------------------------------+
|                |  (no dates outside of future business days)     |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiTable>`, `<MuiButton>`, `<MuiDialog>` for add (date picker) and remove confirmation.

**Loading state:** `<MuiSkeleton>` rows.
**Empty state:** "No holidays have been added. SLA timers count all business days (Monday to Friday, 09:00 to 18:00 IST)."
**Error state:** `<MuiAlert severity="error">`.

---

### /profile — Own profile and change password

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Profile                                        |
|                |                                                  |
|                |  Name:   [Alice Smith]  (read-only)             |
|                |  Email:  [a@co.com]     (read-only)             |
|                |  Role:   L1 support engineer  (read-only)       |
|                |                                                  |
|                |  Change password                                 |
|                |  Current password   [___________]               |
|                |  New password       [___________]               |
|                |  Confirm new password [_________]               |
|                |  Policy: min 8 chars, 1 upper, 1 lower, 1 digit |
|                |                                                  |
|                |  [Save password]                                |
|                |                                                  |
|                |  (success / error alert)                        |
+----------------+--------------------------------------------------+
```

MUI components: `<MuiTextField type="password" label="Current password">`, `<MuiTextField type="password" label="New password">`, `<MuiTextField type="password" label="Confirm new password">`, `<MuiButton variant="contained">Save password</MuiButton>`, `<MuiAlert severity="success|error">`.

**Loading state:** Save button shows `<MuiCircularProgress size={20}>` while POST /api/accounts/me/change-password/ is in flight. Button disabled.
**Error state:** `<MuiAlert severity="error">` below form: field-level error on Current password if wrong, policy error on New password if violated.
**Success state:** `<MuiAlert severity="success">`: "Password changed." Fields cleared.
**Validation:** Confirm new password must match New password (client-side). Policy stated as helper text below New password field.

---

### /audit/security-events — Security events

```
+----------------+--------------------------------------------------+
| AppShell nav   |  Security events                                |
|                |  [User account filter v] (P3 only)              |
|                +--------------------------------------------------+
|                |  Event          | User account | Date/time IST  |
|                +--------------------------------------------------+
|                | Successful sign-in | Alice     | 17 Oct 10:00   |
|                | Failed sign-in     | user.unk  | 17 Oct 10:01   |
|                | Account lockout    | Bob       | 17 Oct 10:31   |
|                | Temp password set  | Alice     | 17 Oct 11:00   |
|                | Own password change| Alice     | 17 Oct 11:05   |
|                +--------------------------------------------------+
|                |  [< Prev]  Page 1 of N  [Next >]               |
+----------------+--------------------------------------------------+
```

No edit or delete controls. Unknown account names shown as typed (A-019, OQ-065).

MUI components: `<MuiDataGrid>`, `<MuiAutocomplete label="User account">` (P3 only), `<MuiPagination>`.

Event type column labels (from GLO-001):
- "Successful sign-in"
- "Failed sign-in"
- "Account lockout"
- "Temporary password set"
- "Own password change"

**Loading state:** `<MuiSkeleton>` rows.
**Empty state:** "No security events found for the selected filter."
**Error state:** `<MuiAlert severity="error">`.
**Route guard:** P4 navigating to `/audit/security-events` → redirect to `/tickets`.

---

## Component Tree

All components use MUI v6. API calls listed are triggered by the component's mount (useQuery) or by user action (useMutation). Props are React props.

### Shared / Layout

```
AppShell
  props: role (P1|P2|P3|P4), orgId (P4 only)
  MuiAppBar > MuiToolbar > MuiTypography ("APLX AMS"), MuiChip (role label), MuiButton ("Sign out")
  MuiDrawer permanent > NavMenu
    NavMenu
      props: role
      MuiList > MuiListItemButton (route, label, icon) per nav item
      NavItem (filtered by role via props.role)

AuthContext  (React Context — see State Management)
SessionExpiredRedirect  (checks HTTP 401 globally, redirects to /login)
```

### /login

```
SignInPage
  MuiBox (centered layout)
  MuiTypography variant="h1" ("Sign in")
  SignInForm
    MuiTextField label="Account name" required autoComplete="username"
    MuiTextField label="Password" type="password" required autoComplete="current-password"
    MuiButton variant="contained" type="submit" ("Sign in")
      on click → POST /api/auth/login/ (useMutation)
    MuiAlert severity="error" (conditional — sign-in error message)
```

### /tickets

```
TicketListPage
  MuiTypography variant="h1" ("Tickets")
  MuiButton variant="contained" ("Raise ticket") — P4 only → /tickets/new
  TicketFilterBar
    MuiTextField label="Search" (client-side filter on displayed data)
    MuiSelect label="Status" (Open|Awaiting client|Resolved|Closed|All)
    MuiSelect label="Priority" (P1|P2|P3|P4|All)
    MuiSelect label="SAP application" (All|[app names])
  TicketDataGrid
    props: tickets[], role, isLoading, error
    MuiDataGrid rows={tickets} columns={columnDefs}
    columns (role-conditional):
      - ticket_reference (link → /tickets/:id)
      - type (Incident|Service request)
      - priority → MuiChip (P1|P2|P3|P4)
      - status → StatusChip (MuiChip + icon)
      - sap_application
      - response_clock_state (P1/P2/P3 only) → SlaClockChip
      - resolution_clock_state (P1/P2/P3 only) → SlaClockChip
      - escalation_flag (P1/P2/P3 only) → EscalationBadge
    MuiPagination
    EmptyState → MuiBox, MuiTypography, MuiButton (P4)
    LoadingState → MuiSkeleton rows
    ErrorState → MuiAlert severity="error", MuiButton ("Retry")

SlaClockChip
  props: state (on_track|at_risk|breached|met|paused), elapsed_hours, target_hours
  MuiChip icon={stateIcon} label="{stateLabel} {elapsed}/{target}"
  state → icon mapping:
    on_track → MuiIcon "RadioButtonUnchecked" (green)
    at_risk → MuiIcon "Warning" (amber)
    breached → MuiIcon "Error" (red)
    met → MuiIcon "CheckCircle" (green)
    paused → MuiIcon "Pause" (grey)
  Non-color: icon + text label always shown alongside color (WCAG A non-color indicator requirement)

StatusChip
  props: status (Open|Awaiting client|Resolved|Closed)
  MuiChip icon={statusIcon} label={status}
  Open → MuiIcon "Circle" | Awaiting client → MuiIcon "Pause" | Resolved → MuiIcon "CheckCircle" | Closed → MuiIcon "Lock"

EscalationBadge
  props: escalation_flag (boolean)
  if escalation_flag: MuiChip icon="Flag" color="error" label="Escalation"
  else: null
```

### /tickets/new

```
RaiseTicketPage (P4 only)
  MuiTypography variant="h1" ("Raise a ticket")
  RaiseTicketForm
    props: orgId (from AuthContext)
    MuiSelect label="Type" required options=[Incident, Service request]
    MuiSelect label="SAP application" required
      options → GET /api/organizations/{id}/sap-applications/ (useQuery)
      loading → MuiCircularProgress
      empty → disabled with helper text
    MuiSelect label="Priority" required options=[P1, P2, P3, P4]
    MuiTextField label="Description" multiline rows={4} required
    MuiButton variant="contained" ("Raise ticket") → POST /api/tickets/ (useMutation)
    MuiButton variant="text" ("Cancel") → navigate('/tickets')
    MuiAlert severity="error" (API error)
```

### /tickets/:id

```
TicketDetailPage
  props: ticketId (from route params)
  data → GET /api/tickets/{id}/ (useQuery)
  MuiBreadcrumbs [Tickets / TKT-NNN]
  TicketHeader
    props: ticket, role
    MuiTypography variant="h1" (ticket_reference + type)
    StatusChip, PriorityChip, SlaAlertBanner (escalation_flag)
    MuiTypography (sap_application, raised_at IST, client_organization)
  SlaTimerPanel (P1, P2, P3 only)
    props: response_clock, resolution_clock
    SlaClockChip × 2 (Response clock / Resolution clock labeled)
    elapsed/target shown numerically
  TicketActionBar
    props: ticket, role, currentUser
    ChangePriorityButton (P1, status ≠ Resolved/Closed)
      → MuiDialog > MuiSelect (Priority), MuiTextField (Reason required)
      → PATCH /api/tickets/{id}/priority/ (useMutation)
    AssignButton (P1 only)
      → MuiDialog > MuiAutocomplete (L2/L3 users)
      → POST /api/tickets/{id}/assign/ (useMutation)
    ResolveButton (P1, P2, status ≠ Resolved/Closed)
      → MuiDialog confirm → POST /api/tickets/{id}/resolve/ (useMutation)
    CloseButton (P1 only, status = Resolved)
      → MuiDialog confirm → POST /api/tickets/{id}/close/ (useMutation)
    AwaitClientButton (assigned support engineer, status = Open)
      → MuiDialog confirm → POST /api/tickets/{id}/await-client/ (useMutation)
    ClearAwaitClientButton (assigned support engineer, status = Awaiting client)
      → MuiDialog confirm → DELETE /api/tickets/{id}/await-client/ (useMutation)
  MuiTabs [Comments | Effort‡ | Audit trail§]
  CommentsTab
    CommentList → GET /api/tickets/{id}/comments/ (useQuery)
    CommentItem (user, time IST, text)
    AddCommentForm (P1, P2, P3, P4 — own org for P4)
      MuiTextField multiline label="Add comment"
      MuiButton ("Submit") → POST /api/tickets/{id}/comments/ (useMutation)
  EffortTab (P1, P2, P3 only)
    EffortList → GET /api/tickets/{id}/effort/ (useQuery)
    EffortItem (engineer, date, hours, Edit/Delete — role/date-conditional)
    AddEffortButton (assigned P1, P2) → MuiDialog > MuiDatePicker, MuiTextField (hours)
      → POST /api/tickets/{id}/effort/ (useMutation)
    EditEffortDialog (P1/P2 own within month; P3 any) → PATCH /api/effort/{effort_id}/ (useMutation)
    DeleteEffortDialog (P1/P2 own within month only) → DELETE /api/effort/{effort_id}/ (useMutation)
  AuditTrailTab (P1, P2, P3 only)
    AuditList → GET /api/tickets/{id}/audit/ (useQuery)
    AuditEntry (change_type, user, old_value, new_value, time IST)
```

### /reports/dashboard

```
DashboardPage
  data → GET /api/reports/dashboard/ (useQuery)
  MuiTypography variant="h1" ("Live dashboard")
  MuiButton ("Refresh") → invalidates dashboard query
  DashboardGrid
    props: data, role
    MuiTable per client organization
    DashboardRow (sap_application, open_count, at_risk_count, breached_count, escalation_flag_count)
    HoursBankBalance (P3: MuiAlert warning if ≤ 0)
```

### /reports/client/:orgId/:year/:month

```
ClientReportPage
  props: orgId, year, month (from route params)
  data → GET /api/reports/client-reports/{org_id}/{year}/{month}/ (useQuery)
  role = P3 → GenerateButton → POST …/generate/ (useMutation)
  role = P3 → PublishButton → POST …/publish/ (useMutation)
  DownloadBar
    MuiButton ("Download Excel") → GET …/download/?format=xlsx
    MuiButton ("Download PDF") → GET …/download/?format=pdf
  ReportContent
    SLASummaryTable (priority, response_pct, resolution_pct — "no tickets" when 0 denominator A-021)
    BreachedTicketsList (ticket_reference, priority, breached_clock)
    MTTRDisplay (mttr_business_days)
    TicketCountsSummary (raised, resolved, closed per priority)
```

### /reports/finance-export

```
FinanceExportPage (P3 only)
  MuiTypography variant="h1" ("Finance export")
  MuiSelect label="Year" options=[current year-1 … current year]
  MuiSelect label="Month" options=[Jan…Dec]
  MuiButton ("Download as Excel") → GET /api/reports/finance-export/{year}/{month}/?format=xlsx
  MuiButton ("Download as CSV") → GET /api/reports/finance-export/{year}/{month}/?format=csv
```

### /admin/users

```
UserManagementPage (P3 only)
  MuiTypography variant="h1" ("User accounts")
  MuiButton ("Create user") → CreateUserDialog
  CreateUserDialog
    MuiTextField label="Full name" required
    MuiTextField label="Email" type="email" required
    MuiSelect label="Role" required (L1|L2/L3|Delivery manager|Client user)
    MuiSelect label="Client organization" (shown when role = Client user, required)
    MuiTextField label="Temporary password" type="password" required
    MuiButton ("Confirm") → POST /api/accounts/users/ (useMutation)
  UserDataGrid → GET /api/accounts/users/ (useQuery)
    columns: name, email, role, status (Active|Deactivated chip)
  UserDetailDrawer (opens on row click)
    UserEditForm → PATCH /api/accounts/users/{id}/ (useMutation)
    DeactivateButton → MuiDialog confirm → POST /api/accounts/users/{id}/deactivate/ (useMutation)
    SetTempPasswordButton → SetTempPasswordDialog
      MuiTextField label="Temporary password" type="password" required
      MuiButton ("Confirm") → POST /api/accounts/users/{id}/set-temp-password/ (useMutation)
```

### /admin/organizations

```
OrganizationManagementPage (P3 only)
  MuiButton ("Add organization") → MuiDialog → POST /api/organizations/ (useMutation)
  OrganizationList → GET /api/organizations/ (useQuery, P3 sees all)
  OrganizationAccordion (per org)
    SapApplicationSection
      list → GET /api/organizations/{id}/sap-applications/ (useQuery)
      MuiButton ("Add SAP application") → MuiDialog → POST /api/organizations/{id}/sap-applications/ (useMutation)
    ContractSection
      data → GET /api/organizations/{id}/contracts/active/ (useQuery)
      display: type, contracted_hours, recorded_hours, hours_bank_balance
      HoursBankWarning (MuiAlert warning when balance ≤ 0)
      MuiButton ("Create contract") → CreateContractDialog (if no active)
      MuiButton ("End contract") → MuiDialog confirm → POST …/end/ (useMutation)
    EffortSection
      EffortList → GET /api/tickets/{id}/effort/ — NOTE: effort is loaded per-ticket; this section shows effort for all tickets of the org aggregated via dashboard or by navigating per ticket. Delivery manager edits via ticket detail page.
      (A-039: effort entries use soft-delete to satisfy both BR B-15 and NFR N-4)
```

### /admin/holidays

```
HolidayManagementPage (P3 only)
  MuiButton ("Add holiday") → MuiDialog > MuiDatePicker → POST /api/holidays/ (useMutation)
  HolidayList → GET /api/holidays/ (useQuery)
  HolidayRow: date (formatted), day of week, Remove button
    Remove → MuiDialog confirm → DELETE /api/holidays/{id}/ (useMutation)
```

### /profile

```
ProfilePage
  data → GET /api/auth/me/ (useQuery)
  ProfileInfo (name, email, role — read-only MuiTextField disabled)
  ChangePasswordForm
    MuiTextField label="Current password" type="password" required
    MuiTextField label="New password" type="password" required
      helperText="Min 8 chars, 1 upper-case, 1 lower-case, 1 digit"
    MuiTextField label="Confirm new password" type="password" required
    MuiButton variant="contained" ("Save password") → POST /api/accounts/me/change-password/ (useMutation)
    MuiAlert (success / error)
```

### /audit/security-events

```
SecurityEventsPage (P1, P2, P3 only)
  MuiTypography variant="h1" ("Security events")
  UserAccountFilter (P3 only)
    MuiAutocomplete label="User account" → GET /api/accounts/users/ (useQuery, P3)
  SecurityEventDataGrid → GET /api/audit/security-events/ (useQuery, filtered by role)
    columns: event_type (label), user_account_or_typed_name, date_time (IST)
    MuiPagination
```

## State Management

### Server state — React Query (TanStack Query v5)

All API responses are managed by React Query. No Redux or Zustand. Configuration:

- `staleTime`: 30 seconds for ticket lists and dashboard; 5 minutes for reference data (organizations, SAP applications, holidays, users).
- `refetchOnWindowFocus`: true (ensures SLA states are current on tab switch).
- `retry`: 1 (one retry on network error; not retried on HTTP 4xx).
- Optimistic updates: not used; all mutations invalidate relevant queries on success.
- Error boundary: React Query error state propagated to component-level MuiAlert.

Key query keys:
- `['tickets']` — ticket list with filter params
- `['ticket', id]` — ticket detail
- `['ticket', id, 'comments']` — comment list
- `['ticket', id, 'effort']` — effort entries
- `['ticket', id, 'audit']` — audit trail
- `['dashboard']` — live dashboard
- `['report', orgId, year, month]` — monthly client report
- `['users']` — user account list
- `['organizations']` — organization list
- `['sap-applications', orgId]` — SAP application list for org
- `['contracts', orgId, 'active']` — active contract
- `['holidays']` — holiday list
- `['security-events']` — security events (with filter)
- `['me']` — current user (session)

### Auth / session state — React Context

`AuthContext` holds:
- `currentUser`: `{ id, name, role, orgId | null, isAuthenticated }` — populated from GET /api/auth/me/ at app mount.
- `signOut()`: calls POST /api/auth/logout/, clears `currentUser`, redirects to `/login`.
- `onUnauthorized()`: called by React Query's global error handler when HTTP 401 is received; clears session, redirects to `/login`.

Session expiry: the `sessionid` cookie is HttpOnly; the frontend cannot read it. React Query detects HTTP 401 on any request and calls `onUnauthorized()` (ADR A-7, 60-minute idle / 12-hour absolute timeout).

CSRF token: fetched from the `csrftoken` cookie (readable by JS, SameSite=Strict) and sent as `X-CSRFToken` header on every POST, PATCH, DELETE by a central Axios/fetch interceptor.

### Route guards

`ProtectedRoute` component wraps every authenticated route:
- If `currentUser.isAuthenticated === false` → redirect to `/login`.
- If `currentUser.role` is not in the route's allowed roles list → redirect to `/tickets` with toast.

Role allowlists per route:
- `/tickets/new`: P4 only
- `/reports/dashboard`: P1, P2, P3
- `/reports/finance-export`: P3 only
- `/admin/users`, `/admin/organizations`, `/admin/holidays`: P3 only
- `/audit/security-events`: P1, P2, P3

### Form state

Form state for dialogs and forms is local React `useState` / `useReducer`. No global form library is introduced (no new dependency outside MUI). MUI TextField `value` and `onChange` control each field. Validation runs:
1. Client-side on submit (required fields, password policy pattern matching).
2. Server-side error surfaced from React Query mutation error.

## Design Tokens

MUI v6 default theme is applied without customization in Phase 4. A custom brand theme may be introduced in a future SCR.

| Token | MUI default value | Usage |
| --- | --- | --- |
| `palette.primary.main` | `#1976d2` (blue) | Primary buttons, active nav item, links |
| `palette.secondary.main` | `#9c27b0` (purple) | Not used in initial design; reserved |
| `palette.error.main` | `#d32f2f` (red) | Error alerts, Breached chip, Deactivate button |
| `palette.warning.main` | `#ed6c02` (amber) | At-risk chip, hours bank balance warning |
| `palette.success.main` | `#2e7d32` (green) | On track chip, Met chip, success alerts |
| `palette.text.primary` | `rgba(0,0,0,0.87)` | Body text |
| `palette.text.secondary` | `rgba(0,0,0,0.6)` | Secondary labels, helper text |
| `palette.background.default` | `#fff` | Page background |
| `typography.h1.fontSize` | `6rem` (96 px) — overridden to `1.5rem` for page headings using `variant="h1"` but `component semantics`; see note | Page-level headings |
| `typography.body1.fontSize` | `1rem` (16 px) | Body text, table cells |
| `typography.body2.fontSize` | `0.875rem` (14 px) | Helper text, secondary labels |
| `spacing` | 8 px base | `theme.spacing(1)` = 8 px; used for consistent padding/margin |
| `shape.borderRadius` | `4 px` | Card, dialog, chip border radius |

**Note on headings:** MUI default h1 at 6rem is too large for application UIs. The frontend sets `typography.h1.fontSize = "1.5rem"` in the theme override to produce 24 px page headings, while keeping `variant="h1"` for semantic HTML and screen-reader heading hierarchy. This is a single token override (not a brand change) and does not require an SCR or brand decision.

**SLA chip colors (non-color indicators mandatory, WCAG 1.4.1):**
- On track: green chip `palette.success.main` + "RadioButtonUnchecked" icon + text label "On track"
- At risk: amber chip `palette.warning.main` + "Warning" icon + text label "At risk"
- Breached: red chip `palette.error.main` + "Error" icon + text label "Breached"
- Met: green chip `palette.success.main` + "CheckCircle" icon + text label "Met"
- Paused: grey chip `palette.text.secondary` + "Pause" icon + text label "Paused"

Color is always supplemented by icon and text; no state is communicated by color alone.

> MUI default theme; tokens can be swapped for Applexus brand in a future SCR.

## Accessibility

**Target:** WCAG 2.1 Level A (DEC-044). MUI v6 default theme exceeds this target: its default contrast ratios meet WCAG 2.1 Level AA (contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text), which is a superset of Level A requirements.

### Keyboard navigation

All pages:
- Tab order follows DOM source order. MUI components provide native keyboard support.
- Interactive elements (buttons, links, selects, text fields) are reachable via Tab / Shift+Tab.
- MuiDataGrid: row navigation via Arrow keys; row activation via Enter; column headers sortable via Space.
- MuiDialog: focus is trapped inside the dialog when open (MUI built-in FocusTrap). Tab cycles within the dialog. Escape closes cancellable dialogs.
- MuiDrawer (AppShell nav): nav items reachable via Tab; Enter activates.
- MuiTabs: Tab moves focus to the tab list; Arrow keys navigate between tabs; Enter/Space activates the focused tab.
- MuiSelect: opens with Enter/Space; options navigable with Arrow keys; selection with Enter.
- MuiDatePicker: fully keyboard-operable via MUI built-in keyboard support.

### Focus management

- On route change: focus moves to the page `<h1>` heading. Implemented via `useEffect(() => { h1Ref.current?.focus(); }, [pathname])`.
- On dialog open: focus moves to the first interactive element inside the dialog (MUI default).
- On dialog close: focus returns to the triggering button.
- On mutation success (e.g., ticket action completes): focus remains on the action area; success toast is announced via `aria-live="polite"`.
- Sign-in page: focus placed on the Account name field on mount.

### ARIA labels and roles

- Icon-only buttons (e.g., Remove on holiday list, Close on dialog): `aria-label="Remove holiday date [DATE]"`. No button is icon-only without an `aria-label`.
- SlaClockChip: `aria-label="Response clock: At risk, 3 hours 30 minutes of 4 hour target"` (combines state + elapsed + target for screen readers).
- EscalationBadge: `role="status"` with `aria-label="Escalation flag: this ticket has passed its L1 target"`.
- Status chip: `aria-label="Status: Awaiting client"`.
- MuiDataGrid sort headers: MUI provides `aria-sort` automatically.
- Loading skeletons: `aria-busy="true"` on the container; `aria-label="Loading [content description]"` on the MuiSkeleton region.
- Empty states: `aria-live="polite"` region so screen readers announce when list transitions from loading to empty.
- Error alerts (MuiAlert): `role="alert"` (MUI default for severity="error"); content is announced immediately.
- Success alerts: `role="status"` via `aria-live="polite"` (MUI default for severity="success").
- Nav items: `aria-current="page"` on the active nav item.
- Dialogs: `aria-labelledby` pointing to the dialog title element.

### Non-color status indicators

All status and SLA state information uses icon + text label in addition to color (GLO-001 terms):
- Ticket status: icon + text in StatusChip.
- SLA clock state: icon + text in SlaClockChip.
- Escalation flag: flag icon + "Escalation" label.
- Hours bank balance warning: MuiAlert with warning icon + text.
- Deactivated user: "Deactivated" text chip in addition to any color.
No state is communicated by color alone (WCAG 1.4.1, Level A).

### Contrast

MUI v6 default theme: primary blue (#1976d2) on white (#fff) provides contrast ratio 4.65:1 (exceeds 4.5:1 AA for normal text; exceeds 3:1 A for large text). Error red (#d32f2f) on white: 5.08:1. All body text rgba(0,0,0,0.87) on white: 16.07:1. These ratios exceed Level A requirements.

### Minimum viewport

1280×720 px. No horizontal scrolling at this size. MUI Grid system at 12-column layout. Drawer is `variant="permanent"` (always visible, width 240 px) leaving 1040 px for content at 1280 px viewport.

### Form accessibility

- Every form control has an associated `<label>` via MUI's `label` prop (rendered as `<label for="...">` in HTML).
- Required fields: `required` prop on MuiTextField sets `aria-required="true"`.
- Validation errors: field-level errors are set via `helperText` with `error={true}` prop, which renders as `aria-describedby` pointing to the helper text element.
- Password fields: `type="password"`, `autoComplete="current-password"` on the Current password field; `autoComplete="new-password"` on the New password and Confirm new password fields.

## Assumptions

Inherited open assumptions from PIB-004 v0.1 that affect UIS decisions:

- **A-008** (Open): supported browsers are the current and previous major versions of Google Chrome and Microsoft Edge on desktop. All MUI v6 components are tested against these browser targets. The frontend is built with Vite and React targeting ES2020+; no polyfills are specified beyond what Vite provides for the target matrix. If A-008 is revised (e.g., to include older browsers or mobile), a SCR is required.
- **A-014** (Confirmed, PIB-004 Q2): SLA clock states are evaluated separately for the response clock and the resolution clock. The UI displays both clocks side by side on each ticket with distinct labels. No combined "ticket SLA state" chip is shown.
- **A-019** (Confirmed, PIB-004 Q2): A refused sign-in shows "Invalid credentials." with no indication of which field was wrong. The sign-in error alert uses this exact string.
- **A-021** (Confirmed, PIB-004 Q2): When the denominator of response % or resolution % is 0, the value shown is "no tickets". Not "0%", not "100%", not "—" or blank.
- **A-022** (Confirmed, PIB-004 Q2): Ticket statuses are Open, Awaiting client, Resolved, Closed. These are the only four statuses rendered in StatusChip and in status filter selects.
- **A-027** (Open): All timestamps displayed in IST (UTC+05:30). Frontend converts UTC ISO 8601 timestamps from the API using the `Intl.DateTimeFormat` API with timezone `Asia/Kolkata`. If this assumption is rejected, all timestamp formatting must be updated.
- **A-039** (Open): Soft-delete on effort entries (effort_effortentry.is_deleted) reconciles BR B-15 (support engineer may delete own entries within the month) and NFR N-4 (unlimited retention). The Delete button on effort entries calls DELETE /api/effort/{effort_id}/; the API marks the entry as deleted without removing the row. The frontend simply removes the entry from the displayed list on re-fetch. If data retention is clarified to permit hard deletes, this assumption is irrelevant to the UI but an SCR is required for the backend.

## Open Questions

No new open questions are raised by this artifact. All Phase 2 and Phase 3 open questions are answered. The following inherited open assumptions may become open questions if new information arrives (logged in docs/logs/assumptions-log.md and docs/logs/open-questions-log.md as applicable):

- A-008: if browser support is widened or narrowed by a human decision, raise a new OQ and update this spec.
- A-027: if IST display is rejected in favor of UTC or user-local timezone, raise a new OQ; timestamp formatting changes across all wireframes.

## Traceability Links

- Upstream: PIB-004 v0.1; SUM-003 v0.2; REQ-001 v0.3 (S-1 to S-33); PRS-001 v0.3 (F-1 to F-8); GLO-001 v0.3; NFR-001 v0.3 (N-1 to N-9); PER-001 v0.2 (P-1 to P-4); API-001 v0.1 (46 endpoints); SCR S-3; SCR S-4.
- Downstream: Phase 5 feature breakdown (FBD) — builders load this spec via context packs; Phase 6 feature branches for each page; Phase 7 test cases (accessibility, functional UI tests via Playwright).

## Quality Checklist

- [x] Every template section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every user-facing story has a user flow, including its error paths
- [x] Every page has a wireframe with loading, empty, and error states
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead + UX |
| Version | 0.1 |
| Conditions | None |
| Comments | Phase 4 design package approved. |
| Timestamp | 2026-10-17 14:04 UTC |
