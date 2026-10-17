---
id: FEAT-034
id_prefix: FEAT
title: "FEAT-034: S-33: Users View Security Events"
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
# FEAT-034: S-33: Users View Security Events

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-33
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-33: S-33: Users View Security Events. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-33 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-033

## Inputs And Contracts
- REQ-001 v0.3 § S-33 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-33
- API-001 v0.1 § Audit trail (F-7)
- DBD-001 v0.1 § Module: audit
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Audit trail (F-7)
- UIS-001 v0.1 § REQ S-33 — Users view security events

## Files To Create Or Modify
- `src/aplx_ams_django/audit/views.py`
- `src/aplx_ams_django/audit/serializers.py`
- `src/aplx_ams_django/audit/dal.py`
- `src/aplx_ams_django/audit/urls.py`
- `src/frontend/src/pages/SecurityEvents.tsx`
- `src/frontend/src/api/audit.ts`

## New Packages
- None

## Out Of Scope
Security event recording — FEAT-033. Alerting — out of scope for release 1.

## Risk Tier
Tier: High
Security event visibility; incorrect access control exposes another user's security history.

## Implementation Steps
1. Add `get_security_events_for_user(user_id)` and `get_all_security_events()` to `audit/dal.py` filtering on security event_types.
2. Add `SecurityEventSerializer` to `audit/serializers.py` (read-only; event, account_name, occurred_at).
3. Add GET `/api/audit/security-events/` to `audit/views.py`: DM: sees all security events with optional `account_name` filter; L1/L2/L3: sees own security events only; client user: 403.
4. Update `audit/urls.py`.
5. Write `src/frontend/src/pages/SecurityEvents.tsx` with MUI DataGrid; DM shows account filter; L1/L2/L3 shows own events only.
6. Update `src/frontend/src/api/audit.ts` with `getSecurityEvents(accountName?)` call.

## Test Plan
REQ-033 AC-1 REQ S-33 AC-1: Given security events recorded for user accounts X and Y and a failed sign-in with the account name ...
REQ-033 AC-2 REQ S-33 AC-2: Given an L1 support engineer, an L2/L3 support engineer or a delivery manager with user account W, w...
REQ-033 AC-3 REQ S-33 AC-3: Given an L1 support engineer or an L2/L3 support engineer with user account W, when they try to view...
REQ-033 AC-4 REQ S-33 AC-4: Given a client user, when they try to view any security event, their own included, then access is re...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 6 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-034` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-034-ACC.

## Risks
- AC-4: any edit or delete attempt must return 405; the view must not implement write endpoints.
- Client users must receive 403, not 404, to avoid information disclosure.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-33; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-034-TASKS; FEAT-034-ACC; FEAT-034-STATUS; Phase 6 PR

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
