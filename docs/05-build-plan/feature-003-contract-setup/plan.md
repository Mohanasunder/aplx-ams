---
id: FEAT-003
id_prefix: FEAT
title: "FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract"
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
# FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-19
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-19: S-19: Delivery Manager Sets Up a Client Organization Contract. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-19 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-002

## Inputs And Contracts
- REQ-001 v0.3 § S-19 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-19
- API-001 v0.1 § Contract management (F-4, F-5)
- DBD-001 v0.1 § Module: organizations
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Contract management (F-4, F-5)
- UIS-001 v0.1 § REQ S-19 — Delivery manager sets up a contract

## Files To Create Or Modify
- `src/aplx_ams_django/organizations/models.py`
- `src/aplx_ams_django/organizations/migrations/0002_contract.py`
- `src/aplx_ams_django/organizations/serializers.py`
- `src/aplx_ams_django/organizations/services.py`
- `src/aplx_ams_django/organizations/dal.py`
- `src/aplx_ams_django/organizations/views.py`
- `src/aplx_ams_django/organizations/urls.py`
- `src/frontend/src/pages/ContractSetup.tsx`
- `src/frontend/src/api/contracts.ts`

## New Packages
- None

## Out Of Scope
Ending a contract and creating a replacement — FEAT-004. Effort recording against a contract — FEAT-027. Hours bank balance review — FEAT-028. Finance export — FEAT-029.

## Risk Tier
Tier: High
Contract data governs effort billing and hours bank balance; an incorrect constraint allowing two active contracts corrupts financial data.

## Implementation Steps
1. Add `Contract` model to `organizations/models.py` (type: hours_bank or fixed_fee, contracted_hours nullable, is_active flag, org FK) per DBD-001.
2. Generate `organizations/migrations/0002_contract.py`.
3. Add `ContractSerializer` to `serializers.py` with validation: only one active contract per org.
4. Add `create_contract`, `get_active_contract` to `services.py`.
5. Add contract DAL queries to `dal.py`.
6. Add `ContractViewSet` (DM-only write) to `views.py`.
7. Register contract endpoints in `urls.py`.
8. Write `src/frontend/src/pages/ContractSetup.tsx` with MUI form for contract type, contracted hours, activate.
9. Write `src/frontend/src/api/contracts.ts` with typed API calls.

## Test Plan
REQ-019 AC-1 REQ S-19 AC-1: Given client organization A with no active contract, when the delivery manager c...
REQ-019 AC-2 REQ S-19 AC-2: Given client organization A already has an active contract, when the delivery ma...
REQ-019 AC-3 REQ S-19 AC-3: Given the delivery manager creates a fixed fee contract, when it is saved, then ...
REQ-019 AC-4 REQ S-19 AC-4: Given a user who is not a delivery manager, when they try to create or change a ...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 9 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-003` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-003-ACC.

## Risks
- The one-active-contract constraint (S-19 AC-2) must be enforced both in service layer and as a DB unique constraint or check; builder must choose the correct approach per DBD-001.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-19; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-003-TASKS; FEAT-003-ACC; FEAT-003-STATUS; Phase 6 PR

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
