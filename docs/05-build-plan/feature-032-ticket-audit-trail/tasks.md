---
id: FEAT-032-TASKS
id_prefix: FEAT
title: "FEAT-032: S-23: Internal User Views a Ticket Audit Trail â€” Tasks"
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
# FEAT-032: S-23: Internal User Views a Ticket Audit Trail â€” Tasks

## Input References
- FEAT-032 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-23 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-032. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/audit/` app with `models.py` defining `AuditEntry` (ticket FK nullable, event_type, user FK nullable, old_value JSONB, new_value JSONB, occurred_at) per DBD-001.
- [ ] T-2: Generate `audit/migrations/0001_initial.py`.
- [ ] T-3: Write `audit/serializers.py` with read-only `AuditEntrySerializer`.
- [ ] T-4: Write `audit/services.py` with `write_audit_entry(ticket, event_type, user, old_value, new_value)` (append-only; no update or delete).
- [ ] T-5: Write `audit/dal.py` with `get_audit_entries_for_ticket` query (ordered by occurred_at).
- [ ] T-6: Write `audit/views.py` with GET `/api/tickets/{id}/audit/` (L1, L2/L3, DM only; read-only).
- [ ] T-7: Write `audit/urls.py`; register in root `urls.py`.
- [ ] T-8: Update `TicketDetail.tsx` with audit trail section (internal users only).
- [ ] T-9: Write `src/frontend/src/api/audit.ts` with typed `getAuditTrail(ticketId)` call.
- [ ] T-10: Update `tickets/services.py` in FEAT-014, FEAT-015, FEAT-027 services to call `write_audit_entry`.
- [ ] T-11: Run all gate commands locally; confirm each exits 0.
- [ ] T-12: Verify `python3 scripts/check_feature_size.py size FEAT-032` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-032 plan.md; REQ-001 v0.3 Â§ S-23; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
