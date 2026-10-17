---
id: VAL-020
title: Phase 4 Design — Validation Report Run 2
phase: 4
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-17
validation: Fail
---
> **One file per validation run per phase.** Each phase validation run produces one `phase-N-run-M.md` in `docs/validation/`. Use `--out docs/validation/phase-N-run-M.md` when calling `new_artifact.py`; never auto-name as `VAL-NNN.md`. M increments with each re-run of the same phase.

# Phase 4 Design — Validation Report Run 2

## Input References
- PIB-004 v0.1 — Phase 4 Input Brief (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (In review 2026-10-17)
- API-001 v0.1 — APLX AMS: API Specification (In review 2026-10-17)
- openapi.yaml — OpenAPI 3.1.0 definition (In review 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (In review 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (In review 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (In review 2026-10-17)
- STD-001 v0.1 — Coding Standards (In review 2026-10-17)
- TST-001 v0.1 — APLX AMS: Test Strategy (In review 2026-10-17)
- .ai/checker-rules/phase-4.md
- docs/validation/phase-4-run-1.md (Run 1 — 7 Majors, 6 Minors, all sent to producers)
- PRS-001 v0.3 — Product Requirement Specification (Approved 2026-10-17)

## Purpose And Scope
Verify that all 13 Run 1 findings are correctly resolved, and apply all validation layers across the 8 Phase 4 design deliverables and 2 standards artifacts. This report does not fix any artifact; it records findings for producer action or human override.

## Verdict
**FAIL** — 0 Blockers, 2 Majors, 6 Minors. The deterministic validator passed all 7 artifact files. The 2 Majors are new cross-artifact consistency issues discovered in this run.

## Scorecard

| Severity | Run 1 open | Resolved in Run 2 | Newly found | Still open |
|---|---|---|---|---|
| Blocker | 0 | 0 | 0 | 0 |
| Major | 7 | 7 | 2 | 2 |
| Minor | 6 | 4 | 4 | 6 |
| **Total** | **13** | **11** | **6** | **8** |

Deterministic validator: all 7 artifact files Pass (Blocker 0, Major 0, Minor 0 each).

## Findings

### MAJ-001 (new) — Security event type names inconsistent across DBD-001, BED-001, and openapi.yaml

**Severity:** Major
**Files:**
- `docs/04-design/database-design.md`: field_name values `successful_sign_in`, `failed_sign_in`, `account_lockout`, `temporary_password_set`, `own_password_changed`
- `docs/04-design/backend-design.md` constant table and sequence diagrams: `'SIGN_IN_OK'`, `'SIGN_IN_FAIL'`, `'ACCOUNT_LOCKOUT'`, `'TEMP_PASSWORD_SET'`, `'OWN_PASSWORD_CHANGED'`
- `docs/04-design/openapi.yaml` AuditEntry event_type: `sign_in_success`, `sign_in_failed`, `account_lockout`, `temp_password_set`, `own_password_changed`

Three of five names differ across all three contract artifacts. The `field_name` stored in `audit_auditentry` is the same value the API reads back as `event_type`; builders cannot determine which string to write.

**Suggested fix:** Adopt DBD-001 lowercase_snake_case as canonical (`successful_sign_in`, `failed_sign_in`, `account_lockout`, `temporary_password_set`, `own_password_changed`). Update BED-001 constants and sequence diagrams to use these values. Update openapi.yaml AuditEntry event_type enum to match.

---

### MAJ-002 (new) — TST-001 E2E journey table has systematically wrong feature codes, wrong persona, and wrong story reference

**Severity:** Major
**File:** `docs/04-design/test-strategy.md`, Level 3 E2E journey table

Five of eight journeys have wrong F-codes per PRS-001 v0.3; "Raise a ticket" assigns L1 engineer as persona but PRM-001 restricts `POST /api/tickets/` to client users only (P4); the live dashboard journey references S-24 (holiday management) instead of S-12.

**Correction table (from PRS-001 v0.3):**

| Journey | TST-001 code | Correct code |
|---|---|---|
| Sign in and sign out | F-1 | F-6 |
| Raise a ticket | F-2, persona: L1 engineer | F-1, persona: **client user** |
| View ticket list and open ticket | F-2 | F-2 (correct) |
| Acknowledge, assign, change priority, Resolve, Close | F-3 | F-2 |
| Record effort and view hours bank | F-4 | F-5 |
| View live dashboard | F-5, S-24 | F-4, **S-12** |
| View and download monthly client report | F-6 | F-4 |
| View audit trail entries | F-8 | F-8 (correct) |

**Suggested fix:** Correct 5 F-codes, change "L1 engineer" to "client user" for the raise-ticket journey, change S-24 to S-12 for the dashboard journey. Consider adding an F-3 (SLA timers) journey.

---

### MIN-001 (M-001 unresolved from Run 1) — PRM-001 BED-001 citation lacks status label

**Severity:** Minor
**File:** `docs/04-design/permission-matrix.md`, § Input References, BED-001 line
**Description:** All other citations in PRM-001 Input References include `(In review 2026-10-17)`; the BED-001 citation does not after the Run 2 fix stripped the label.
**Suggested fix:** Add `(In review 2026-10-17)` to the BED-001 citation to be consistent with all other Input References entries.

---

### MIN-002 (M-002 unresolved from Run 1) — TST-001 STD-001 citation lacks status label

**Severity:** Minor
**File:** `docs/04-design/test-strategy.md`, § Input References, STD-001 line
**Description:** Same issue as MIN-001 — the Run 2 fix stripped the status label; other citations in the file retain it.
**Suggested fix:** Add `(In review 2026-10-17)` to the STD-001 citation.

---

### MIN-003 (new) — Contract schema uses `organization_id`; DBD-001 uses `client_org_id`

**Severity:** Minor
**Files:** `docs/04-design/openapi.yaml` Contract schema (line ~305); `docs/04-design/database-design.md` `organizations_contract` table column `client_org_id`
**Description:** M-006 correctly renamed SAPApplication from `organization_id` to `client_org_id`. The Contract schema was not also renamed, leaving an inconsistency.
**Suggested fix:** Rename Contract schema field to `client_org_id` (matching the pattern applied to SAPApplication), or add an explicit mapping note.

---

### MIN-004 (new) — BED-001 Flow 6 response body lists fields absent from openapi.yaml UserAccount schema

**Severity:** Minor
**Files:** `docs/04-design/backend-design.md` Flow 6 response line; `docs/04-design/openapi.yaml` UserAccount schema
**Description:** BED-001 Flow 6 lists `username`, `failed_attempts`, `locked_until`, `date_joined`, `last_login`, and `client_org_id` — none of the first five exist in the UserAccount schema; the last should be `client_organization_id`.
**Suggested fix:** Change BED-001 Flow 6 response to `200 {UserAccount: id, name, email, role, is_active, client_organization_id, client_organization_name}`.

---

### MIN-005 (new) — BED-001 Flow 7 response body inconsistent with openapi.yaml UserMe schema

**Severity:** Minor
**Files:** `docs/04-design/backend-design.md` Flow 7 response line; `docs/04-design/openapi.yaml` UserMe schema
**Description:** BED-001 Flow 7 lists `username`, `last_login`, `client_org_id`, and omits `is_active` and `client_organization_name`. Same root cause as MIN-004.
**Suggested fix:** Change BED-001 Flow 7 response to `200 {UserMe: id, name, email, role, is_active, client_organization_id, client_organization_name}`.

---

### MIN-006 (new) — openapi.yaml ticket reference examples use "AMS-" prefix; all other artifacts use "TKT-"

**Severity:** Minor
**File:** `docs/04-design/openapi.yaml` Ticket schema (line ~480) and one other occurrence (line ~876)
**Description:** Two examples use `"AMS-0042"` and `"AMS-0012"`. BED-001 generation logic produces `TKT-{:05d}`, DBD-001 comments and UIS-001 wireframes all use "TKT-". Even the FinanceExportRow example in the same openapi.yaml uses "TKT-0001".
**Suggested fix:** Change both `"AMS-NNNN"` examples to `"TKT-NNNNN"` (5-digit, matching BED-001 format).

## Top Issues

1. **MAJ-001** — Security event type names have three incompatible naming conventions across DBD-001, BED-001, and openapi.yaml. Builders cannot determine which string to store in the audit trail.
2. **MAJ-002** — TST-001 E2E journey table is systematically wrong: 5 of 8 journeys have wrong feature codes, one journey assigns the wrong persona (only client users can raise tickets per PRM-001), and one journey references the wrong story.

## Unresolved From Earlier Runs

| Finding | Description | Status |
|---|---|---|
| M-001 | PRM-001 BED-001 citation status label | NOT RESOLVED — now MIN-001 |
| M-002 | TST-001 STD-001 citation status label | NOT RESOLVED — now MIN-002 |

## Run 1 Findings — Resolution Status

| Finding | Description | Run 2 Status |
|---|---|---|
| F-001 | RoleEnum in openapi.yaml → `[l1_support, l2l3_support, delivery_manager, client_user]` | RESOLVED |
| F-002 | TicketStatusEnum → `"Awaiting client"` (space) | RESOLVED |
| F-003 | Finance export columns aligned across openapi.yaml and BED-001 | RESOLVED |
| F-004 | set-temp-password → HTTP 200 + UserAccount body | RESOLVED |
| F-005 | change-own-password → HTTP 200 + UserMe body | RESOLVED |
| F-006 | DashboardOrgSummary extended with `sap_applications[]`; UIS-001 annotated | RESOLVED |
| F-007 | agent-charter.md rebuilt with no "not set yet" placeholders | RESOLVED |
| M-001 | PRM-001 BED-001 citation status label | NOT RESOLVED (MIN-001) |
| M-002 | TST-001 STD-001 citation status label | NOT RESOLVED (MIN-002) |
| M-003 | factory-boy and freezegun added to STD-001 | RESOLVED |
| M-005 | Comment field → `body` in openapi.yaml | RESOLVED |
| M-006 | SAPApplication FK → `client_org_id` in openapi.yaml | RESOLVED |

## Recommendation

Send back to producers. MAJ-001 requires a coordinated fix across DBD-001, BED-001, and openapi.yaml simultaneously (canonical event type names). MAJ-002 requires a fix to TST-001 only. All 6 Minors should be included in the same pass to avoid a Run 4. This is Run 2 of 3 allowed before escalation (project.md `loop_limit_failed_validations: 3`).

## Decision Record
<fill: to be completed when human decides>

## Assumptions
None raised in this check.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-004 v0.1 (Approved); REQ-001 v0.3, PRS-001 v0.3 (Approved)
- Artifacts checked: DBD-001, API-001, BED-001, UIS-001, PRM-001, STD-001, TST-001 (all In review)
- Downstream: Phase 5 cannot start until all artifacts Approved

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and included
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
