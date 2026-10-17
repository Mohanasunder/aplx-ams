---
id: FEAT-032
id_prefix: FEAT
title: "FEAT-032: S-23: Internal User Views a Ticket Audit Trail"
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
# FEAT-032: S-23: Internal User Views a Ticket Audit Trail

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-23
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-23: S-23: Internal User Views a Ticket Audit Trail. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-23 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-027

## Inputs And Contracts
- REQ-001 v0.3 § S-23 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-23
- API-001 v0.1 § Audit trail (F-7)
- DBD-001 v0.1 § Module: audit
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Audit trail (F-7)
- UIS-001 v0.1 § REQ S-23 — Internal user views a ticket's audit trail

## Files To Create Or Modify
- `src/aplx_ams_django/audit/models.py`
- `src/aplx_ams_django/audit/migrations/0001_initial.py`
- `src/aplx_ams_django/audit/serializers.py`
- `src/aplx_ams_django/audit/services.py`
- `src/aplx_ams_django/audit/dal.py`
- `src/aplx_ams_django/audit/views.py`
- `src/aplx_ams_django/audit/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`
- `src/frontend/src/api/audit.ts`

## New Packages
- None

## Out Of Scope
Security event recording — FEAT-033. RLS policies on audit table — FEAT-007. Audit entries for prior features (priority change FEAT-014, escalation FEAT-015, effort FEAT-027) — those services will call the audit write after FEAT-032 is merged.

## Risk Tier
Tier: High
Audit trail is append-only; incorrect write guard allows tampering with audit entries.

## Implementation Steps
1. Create `src/aplx_ams_django/audit/` app with `models.py` defining `AuditEntry` (ticket FK nullable, event_type, user FK nullable, old_value JSONB, new_value JSONB, occurred_at) per DBD-001.
2. Generate `audit/migrations/0001_initial.py`.
3. Write `audit/serializers.py` with read-only `AuditEntrySerializer`.
4. Write `audit/services.py` with `write_audit_entry(ticket, event_type, user, old_value, new_value)` (append-only; no update or delete).
5. Write `audit/dal.py` with `get_audit_entries_for_ticket` query (ordered by occurred_at).
6. Write `audit/views.py` with GET `/api/tickets/{id}/audit/` (L1, L2/L3, DM only; read-only).
7. Write `audit/urls.py`; register in root `urls.py`.
8. Update `TicketDetail.tsx` with audit trail section (internal users only).
9. Write `src/frontend/src/api/audit.ts` with typed `getAuditTrail(ticketId)` call.
10. Update `tickets/services.py` in FEAT-014, FEAT-015, FEAT-027 services to call `write_audit_entry`.

## Test Plan
REQ-023 AC-1 REQ S-23 AC-1: Given a ticket whose priority, status, assignment and effort were each changed once, when the delive...
REQ-023 AC-2 REQ S-23 AC-2: Given an L1 support engineer or an L2/L3 support engineer, when they view the audit trail of a ticke...
REQ-023 AC-3 REQ S-23 AC-3: Given a client user, when they try to view the audit trail of their organization's ticket, then acce...
REQ-023 AC-4 REQ S-23 AC-4: Given any user, when they try to edit or delete an audit entry, then the change is refused (A-016).
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-032` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-032-ACC.

## Risks
- A-016 (Open): audit entries are read-only; the view must return 405 for PUT, PATCH, DELETE.
- The audit write in FEAT-014, FEAT-015, FEAT-027 was stubbed; this feature activates it.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-23; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-032-TASKS; FEAT-032-ACC; FEAT-032-STATUS; Phase 6 PR

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
