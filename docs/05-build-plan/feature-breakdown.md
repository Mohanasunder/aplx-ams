---
id: FBD-001
title: APLX AMS: Feature Breakdown
phase: 5
version: 0.1
template: feature-breakdown
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# APLX AMS: Feature Breakdown

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- BKL-001 v0.3 — APLX AMS: Backlog (Approved 2026-10-17) — 33 stories BL-1 to BL-33
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) — S-1 to S-33
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17)

## Purpose And Scope
Lists all 36 features (FEAT-000 through FEAT-035) planned for APLX AMS Release 1 (2027-01-17). Each feature is sized for one builder session within the limits of project.md (max 4 AC, max 10 source files, max 10 min test runtime). FEAT-000, FEAT-001, and FEAT-035 are Enabling features; FEAT-002 to FEAT-034 are Story features covering REQ S-1 to S-33. S-18 has 3 AC (within the 4-AC limit); all other stories have 4 AC. FEAT-035 has 2 AC (Enabling CI scaffold).

Does not cover: Phase 6 build order schedule, sprint planning, or resource allocation.

## Feature List

| FEAT-ID | Title | Type | Criteria Covered | AC Count | Source Files | Risk Tier | Depends On |
|---|---|---|---|---|---|---|---|
| FEAT-000 | Walking Skeleton — Backend Scaffold and CI Pipeline | Enabling | STD-001 AC-1, STD-001 AC-2, TST-001 AC-3, STD-001 AC-4 | 4 | 10 | Critical | none |
| FEAT-001 | Frontend Scaffold — React 18, Nginx, and Frontend CI Gates | Enabling | STD-001 AC-1..2; TST-001 AC-1..2 | 4 | 10 | Critical | FEAT-000 |
| FEAT-002 | S-18: Org and SAP Application Setup | Feature | REQ-018 AC-1..3 | 3 | 10 | Standard | FEAT-001 |
| FEAT-003 | S-19: Contract Setup | Feature | REQ-019 AC-1..4 | 4 | 9 | High | FEAT-002 |
| FEAT-004 | S-27: End Contract | Feature | REQ-027 AC-1..4 | 4 | 7 | High | FEAT-003 |
| FEAT-005 | S-20: User Accounts | Feature | REQ-020 AC-1..4 | 4 | 10 | High | FEAT-002 |
| FEAT-006 | S-21: Sign-In Auth | Feature | REQ-021 AC-1..4 | 4 | 9 | Critical | FEAT-005 |
| FEAT-007 | S-22: Client Data Boundary and RLS | Feature | REQ-022 AC-1..4 | 4 | 7 | Critical | FEAT-025, FEAT-032 |
| FEAT-008 | S-30: Temporary Password | Feature | REQ-030 AC-1..4 | 4 | 7 | High | FEAT-006 |
| FEAT-009 | S-31: Change Own Password | Feature | REQ-031 AC-1..4 | 4 | 6 | High | FEAT-006 |
| FEAT-010 | S-24: Holiday List | Feature | REQ-024 AC-1..4 | 4 | 10 | Standard | FEAT-006 |
| FEAT-011 | S-1: Raise Ticket | Feature | REQ-001 AC-1..4 | 4 | 10 | Standard | FEAT-010 |
| FEAT-012 | S-2: Follow Tickets | Feature | REQ-002 AC-1..4 | 4 | 5 | Standard | FEAT-011 |
| FEAT-013 | S-3: L1 Acknowledge | Feature | REQ-003 AC-1..4 | 4 | 6 | Standard | FEAT-011 |
| FEAT-014 | S-4: Priority Change | Feature | REQ-004 AC-1..4 | 4 | 6 | Standard | FEAT-013 |
| FEAT-015 | S-5: Escalate Ticket | Feature | REQ-005 AC-1..4 | 4 | 6 | Standard | FEAT-011 |
| FEAT-016 | S-6: Set Resolved | Feature | REQ-006 AC-1..4 | 4 | 6 | Standard | FEAT-011 |
| FEAT-017 | S-7: Close Ticket | Feature | REQ-007 AC-1..4 | 4 | 6 | Standard | FEAT-016 |
| FEAT-018 | S-8: Awaiting Client | Feature | REQ-008 AC-1..4 | 4 | 6 | Standard | FEAT-011 |
| FEAT-019 | S-9: SLA Computation | Feature | REQ-009 AC-1..4 | 4 | 7 | Standard | FEAT-011 |
| FEAT-020 | S-10: SLA States Visible | Feature | REQ-010 AC-1..4 | 4 | 5 | Standard | FEAT-019 |
| FEAT-021 | S-11: Escalation Flag | Feature | REQ-011 AC-1..4 | 4 | 5 | Standard | FEAT-019 |
| FEAT-022 | S-28: Client Comment | Feature | REQ-028 AC-1..4 | 4 | 8 | Standard | FEAT-018 |
| FEAT-023 | S-29: Internal Comment | Feature | REQ-029 AC-1..4 | 4 | 5 | Standard | FEAT-022 |
| FEAT-024 | S-12: Live Dashboard | Feature | REQ-012 AC-1..4 | 4 | 8 | Standard | FEAT-021 |
| FEAT-025 | S-13: Generate Monthly Report | Feature | REQ-013 AC-1..4 | 4 | 8 | High | FEAT-024 |
| FEAT-026 | S-14: View and Download Report | Feature | REQ-014 AC-1..4 | 4 | 7 | Standard | FEAT-025 |
| FEAT-027 | S-15: Record Effort | Feature | REQ-015 AC-1..4 | 4 | 10 | High | FEAT-003, FEAT-011 |
| FEAT-028 | S-16: Review Effort | Feature | REQ-016 AC-1..4 | 4 | 7 | High | FEAT-027 |
| FEAT-029 | S-17: Finance Export | Feature | REQ-017 AC-1..4 | 4 | 5 | High | FEAT-028 |
| FEAT-030 | S-25: Engineer Edit Effort | Feature | REQ-025 AC-1..4 | 4 | 7 | High | FEAT-027 |
| FEAT-031 | S-26: DM Correct Effort | Feature | REQ-026 AC-1..4 | 4 | 7 | High | FEAT-027 |
| FEAT-032 | S-23: Ticket Audit Trail | Feature | REQ-023 AC-1..4 | 4 | 10 | High | FEAT-027 |
| FEAT-033 | S-32: Security Events Recorded | Feature | REQ-032 AC-1..4 | 4 | 5 | Critical | FEAT-032 |
| FEAT-034 | S-33: View Security Events | Feature | REQ-033 AC-1..4 | 4 | 6 | High | FEAT-033 |
| FEAT-035 | E2E CI Scaffold | Enabling | TST-001 AC-5, STD-001 AC-5 | 2 | 2 | Critical | FEAT-001 |

**Totals:** 36 features, 141 acceptance criteria (4 AC × 2 = 8 for FEAT-000 and FEAT-001 + 2 AC for FEAT-035 + 3 AC for FEAT-002 + 4 AC × 32 story features FEAT-003 to FEAT-034 = 8+2+3+128 = 141), all within project.md limits.

## Dependencies

Dependency graph (direct only; all transitively reach FEAT-000):

```
FEAT-000 (none)
└── FEAT-001
    ├── FEAT-035
    └── FEAT-002
        ├── FEAT-003
        │   ├── FEAT-004
        │   └── FEAT-027 (also ← FEAT-011)
        │       ├── FEAT-028
        │       │   └── FEAT-029
        │       ├── FEAT-030
        │       ├── FEAT-031
        │       └── FEAT-032
        │           ├── FEAT-033
        │           │   └── FEAT-034
        │           └── FEAT-007 (also ← FEAT-025)
        └── FEAT-005
            └── FEAT-006
                ├── FEAT-008
                ├── FEAT-009
                └── FEAT-010
                    └── FEAT-011
                        ├── FEAT-012
                        ├── FEAT-013
                        │   └── FEAT-014
                        ├── FEAT-015
                        ├── FEAT-016
                        │   └── FEAT-017
                        ├── FEAT-018
                        │   └── FEAT-022
                        │       └── FEAT-023
                        └── FEAT-019
                            ├── FEAT-020
                            └── FEAT-021
                                └── FEAT-024
                                    └── FEAT-025
                                        ├── FEAT-026
                                        └── FEAT-007 (also ← FEAT-032)
```

No circular dependencies. Every feature transitively depends on FEAT-000. `check_feature_size.py task0` confirms: 36 features, 0 problems.

## Release Mapping

All 36 features (FEAT-000 through FEAT-035) target Release 1, go-live 2027-01-17 (BKL-001 v0.3). No features are deferred.

## Assumptions
- A-039 (Confirmed): soft-delete on effort_effortentry (DEC-047, 2026-10-17).
- A-014 to A-022: all Confirmed (DEC-041, 2026-10-17); details in docs/logs/assumptions-log.md.
- A-023, A-024, A-025: Confirmed (DEC-041, 2026-10-17).

## Open Questions
None. All Phase 1–4 open questions are answered (PIB-005 v0.1 § Open Questions). A-014 to A-022 are confirmed.

## Traceability Links
- Upstream: PIB-005 v0.1; BKL-001 v0.3; REQ-001 v0.3; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1
- Downstream: FEAT-000 through FEAT-035 plan.md, acceptance.md, tasks.md, status.md; Phase 6 PRs

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
| Comments | Phase 5 validation passed (VAL-023). All 36 features sized correctly; 28-wave plan; context packs clean. |
| Timestamp | 2026-10-17 16:50 UTC |
