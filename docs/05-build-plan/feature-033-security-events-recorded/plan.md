---
id: FEAT-033
id_prefix: FEAT
title: "FEAT-033: S-32: Security Events Are Recorded in the Audit Trail"
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
# FEAT-033: S-32: Security Events Are Recorded in the Audit Trail

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-32
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-32: S-32: Security Events Are Recorded in the Audit Trail. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-32 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-032

## Inputs And Contracts
- REQ-001 v0.3 § S-32 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-32
- API-001 v0.1 § Audit trail (F-7)
- DBD-001 v0.1 § Module: audit
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Audit trail (F-7)
- UIS-001 v0.1 § REQ S-33 — Users view security events

## Files To Create Or Modify
- `src/aplx_ams_django/accounts/authentication.py`
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/audit/services.py`
- `src/aplx_ams_django/audit/models.py`
- `src/aplx_ams_django/audit/migrations/0002_security_event_type.py`

## New Packages
- None

## Out Of Scope
Viewing security events — FEAT-034. RLS on audit table — FEAT-007. Alerting on security events — out of scope for release 1 (OQ-062).

## Risk Tier
Tier: Critical
Security events must be immutable and must never contain password values; failure enables forensic blind spots.

## Implementation Steps
1. Add security event types (sign_in_success, sign_in_failure, account_lockout, temp_password_set, own_password_change) to `AuditEntry.event_type` choices in `audit/models.py`.
2. Generate `audit/migrations/0002_security_event_type.py`.
3. Update `audit/services.py` with `write_security_event(event_type, account_name_or_user, occurred_at)`: append-only; assert no password value in new_value or old_value fields.
4. Update `accounts/authentication.py` to call `write_security_event` on every sign-in success, failure, and lockout (AC-1, AC-2, AC-3); record account name as typed for unknown accounts (OQ-065).
5. Update `accounts/services.py` `set_temporary_password` and `change_own_password` to call `write_security_event` (AC-4); assert no password values written.

## Test Plan
REQ-032 AC-1 REQ S-32 AC-1: Given active, unlocked user account X, when X signs in with the correct password at 10:00:05 IST and...
REQ-032 AC-2 REQ S-32 AC-2: Given user account X with 4 failed sign-ins, when a fifth sign-in with a wrong password is refused a...
REQ-032 AC-3 REQ S-32 AC-3: Given deactivated user account Y and the account name "user.unknown", which matches no user account,...
REQ-032 AC-4 REQ S-32 AC-4: Given delivery manager D sets temporary password "Bcdefgh2" on user account X, and signed-in user Z ...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 5 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-033` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-033-ACC.

## Risks
- AC-4: the password-value search test is a critical security control; builder must scan all audit entries for any password string and assert 0 matches.
- Timestamps must be recorded to the second (BR B-24); use `datetime.now(tz=UTC)` without truncation.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-32; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-033-TASKS; FEAT-033-ACC; FEAT-033-STATUS; Phase 6 PR

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
