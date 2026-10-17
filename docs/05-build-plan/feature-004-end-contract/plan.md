---
id: FEAT-004
id_prefix: FEAT
title: "FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One"
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
# FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-27
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-27: S-27: Delivery Manager Ends a Contract and Sets Up a New One. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-27 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-003

## Inputs And Contracts
- REQ-001 v0.3 § S-27 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-27
- API-001 v0.1 § Contract management (F-4, F-5)
- DBD-001 v0.1 § Module: organizations
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Contract management (F-4, F-5)
- UIS-001 v0.1 § REQ S-27 — Delivery manager ends a contract and sets up a new one

## Files To Create Or Modify
- `src/aplx_ams_django/organizations/services.py`
- `src/aplx_ams_django/organizations/views.py`
- `src/aplx_ams_django/organizations/serializers.py`
- `src/aplx_ams_django/organizations/dal.py`
- `src/aplx_ams_django/organizations/urls.py`
- `src/frontend/src/pages/ContractSetup.tsx`
- `src/frontend/src/api/contracts.ts`

## New Packages
- None

## Out Of Scope
Effort recording — FEAT-027. Effort review — FEAT-028. Finance export — FEAT-029. Engineer effort correction — FEAT-030. DM effort correction — FEAT-031.

## Risk Tier
Tier: High
Ending a contract affects hours bank balance and effort tracking; incorrect logic causes financial data corruption.

## Implementation Steps
1. Add `end_contract(contract_id)` to `services.py`: sets `is_active=False`, preserves effort entries and balance.
2. Add PATCH `/api/contracts/{id}/end/` action to `views.py`; DM-only.
3. Add `get_effort_entries_for_contract` query to `dal.py`.
4. Update `ContractSerializer` to expose `is_active`, `ended_at` fields in `serializers.py`.
5. Register end-contract URL in `urls.py`.
6. Update `src/frontend/src/pages/ContractSetup.tsx` with 'End contract' button (DM-only, confirmed dialog).
7. Update `src/frontend/src/api/contracts.ts` with `endContract(id)` call.

## Test Plan
REQ-027 AC-1 REQ S-27 AC-1: Given client organization A has an active hours bank contract with hours bank ba...
REQ-027 AC-2 REQ S-27 AC-2: Given client organization A has no active contract, when a support engineer trie...
REQ-027 AC-3 REQ S-27 AC-3: Given organization A's contract has ended, when the delivery manager sets up a n...
REQ-027 AC-4 REQ S-27 AC-4: Given a user who is not a delivery manager, when they try to end a contract, the...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 7 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-004` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-004-ACC.

## Risks
- A-023 (Confirmed): ended contract balance is NOT carried over to the new contract; each contract starts fresh. Builder must not copy the old balance.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-27; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-004-TASKS; FEAT-004-ACC; FEAT-004-STATUS; Phase 6 PR

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
