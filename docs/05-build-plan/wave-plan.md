---
id: WAV-001
title: APLX AMS Build Wave Plan
phase: 5
version: 0.1
template: wave-plan
template_version: 1.1
status: Approved
author_agent: dependency-sequencer
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS Build Wave Plan

## Input References
- FBD-001 v0.1 — APLX AMS: Feature Breakdown (In review 2026-10-17; in-phase co-produced artifact — approved at the Phase 5 gate) — 36 features FEAT-000 to FEAT-035, dependency graph, risk tiers
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Shared Paths — globs that force a feature to be alone in its wave
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17) — capacity constraints cited from project.md
- project.md — max_parallel_builder_agents: 3; review_capacity_prs_per_week: 6; max_open_feature_branches: 3
- docs/05-build-plan/feature-NNN-*/plan.md — Files To Create Or Modify and Dependencies sections for all 36 features

## Purpose And Scope
Schedules all 36 features (FEAT-000 to FEAT-035) into 28 sequential build waves for APLX AMS Release 1 (target go-live 2027-01-17). Each wave lists features that can be built in parallel; no wave exceeds max_parallel_builder_agents (3) or review_capacity_prs_per_week (6). Dependencies are satisfied in prior waves; every feature touching a Shared Path glob in STD-001 is alone in its wave. The plan covers wave ordering, reviewer load per wave, and the rationale for parallel groupings.

Does not cover: sprint schedules, calendar dates, resource assignment, or any design decision that belongs to Phase 4.

## Capacity Assumptions
Source: project.md (Approved 2026-10-17).

| Setting | Value | Effect on this plan |
|---|---|---|
| max_parallel_builder_agents | 3 | No wave contains more than 3 features |
| review_capacity_prs_per_week | 6 | No wave produces more than 6 PRs; max in this plan is 3 PRs (Waves 13, 14, 15) |
| max_open_feature_branches | 3 | Branches for Wave N+1 are not opened until Wave N branches are merged |

15 of 36 features touch a Shared Path glob (migrations, CI YAML, package manifests, pyproject.toml, requirements.txt) and must each occupy a wave alone; see STD-001 v0.1 § Shared Paths. This is the primary driver of the 28-wave count.

## Waves

**Shared-path key:** A cell marked SP in the Alone column means the feature lists at least one Shared Path glob (migration file, CI YAML, package manifest, pyproject.toml, or requirements.txt) and must be alone in its wave per STD-001 § Shared Paths.

| Wave | Features | PRs | Alone | Risk Tier(s) | Dependencies satisfied before this wave | Parallel rationale |
|------|----------|-----|-------|--------------|----------------------------------------|-------------------|
| Wave 1 | FEAT-000 | 1 | SP | Critical | none | Walking skeleton; no deps. Alone: pyproject.toml, requirements.txt, .github/workflows/ci.yml match Shared Paths. |
| Wave 2 | FEAT-001 | 1 | SP | Critical | FEAT-000 (W1) | Frontend scaffold. Alone: .github/workflows/ci.yml, src/frontend/package.json match Shared Paths. |
| Wave 3 | FEAT-035 | 1 | SP | Critical | FEAT-001 (W2) | E2E CI scaffold. Alone: .github/workflows/e2e.yml matches Shared Paths. Depends on FEAT-001 (W2); must come before story features use the E2E gate. |
| Wave 4 | FEAT-002 | 1 | SP | Standard | FEAT-001 (W2) | Org and SAP model. Alone: organizations/migrations/0001_initial.py matches Shared Paths. |
| Wave 5 | FEAT-003 | 1 | SP | High | FEAT-002 (W4) | Contract model migration. Alone: organizations/migrations/0002_contract.py matches Shared Paths. |
| Wave 6 | FEAT-005 | 1 | SP | High | FEAT-002 (W4) | User accounts model migration. Alone: accounts/migrations/0001_initial.py matches Shared Paths. FEAT-003 (W5) and FEAT-005 (W6) both depend only on FEAT-002; they cannot share a wave because each must be alone. |
| Wave 7 | FEAT-004, FEAT-006 | 2 | No | High, Critical | FEAT-003 (W5), FEAT-005 (W6) | FEAT-004 (organizations/* + ContractSetup.tsx + api/contracts.ts) and FEAT-006 (accounts/authentication.py, accounts/views.py, accounts/urls.py, settings/base.py, aplx_ams_django/urls.py, Login.tsx, api/auth.ts, AuthContext.tsx, App.tsx) share no files and touch no Shared Paths. |
| Wave 8 | FEAT-010 | 1 | SP | Standard | FEAT-006 (W7) | Holiday list and SLA model. Alone: sla/migrations/0001_initial.py matches Shared Paths. FEAT-008 and FEAT-009 also depend on FEAT-006 but are deferred because FEAT-010 must be alone and must precede FEAT-011. |
| Wave 9 | FEAT-011 | 1 | SP | Standard | FEAT-010 (W8) | Raise ticket model. Alone: tickets/migrations/0001_initial.py matches Shared Paths. FEAT-008 and FEAT-009 cannot join (FEAT-011 must be alone). |
| Wave 10 | FEAT-027 | 1 | SP | High | FEAT-003 (W5), FEAT-011 (W9) | Record effort model. Alone: effort/migrations/0001_initial.py matches Shared Paths. Both required dependencies (FEAT-003 W5, FEAT-011 W9) are now satisfied. |
| Wave 11 | FEAT-032 | 1 | SP | High | FEAT-027 (W10) | Ticket audit trail model. Alone: audit/migrations/0001_initial.py matches Shared Paths. Scheduled immediately after FEAT-027 to unblock the FEAT-033 → FEAT-034 → FEAT-007 chain. |
| Wave 12 | FEAT-033 | 1 | SP | Critical | FEAT-032 (W11) | Security events model. Alone: audit/migrations/0002_security_event_type.py matches Shared Paths. |
| Wave 13 | FEAT-008, FEAT-034, FEAT-013 | 3 | No | High, High, Standard | FEAT-006 (W7), FEAT-033 (W12), FEAT-011 (W9) | FEAT-008 (accounts/*), FEAT-034 (audit/views.py, audit/serializers.py, audit/dal.py, audit/urls.py, SecurityEvents.tsx, api/audit.ts), FEAT-013 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/dal.py, tickets/urls.py, TicketDetail.tsx) share no files across all three. |
| Wave 14 | FEAT-009, FEAT-014, FEAT-028 | 3 | No | High, Standard, High | FEAT-006 (W7), FEAT-013 (W13), FEAT-027 (W10) | FEAT-009 (accounts/services.py, accounts/views.py, accounts/urls.py, accounts/serializers.py, ChangePassword.tsx, api/auth.ts), FEAT-014 (tickets/*), FEAT-028 (effort/views.py, effort/serializers.py, effort/dal.py, effort/urls.py, organizations/services.py, EffortReview.tsx, api/effort.ts) share no files. |
| Wave 15 | FEAT-012, FEAT-031, FEAT-029 | 3 | No | Standard, High, High | FEAT-011 (W9), FEAT-027 (W10), FEAT-028 (W14) | FEAT-012 (tickets/views.py, tickets/serializers.py, tickets/urls.py, TicketList.tsx, TicketDetail.tsx), FEAT-031 (effort/services.py, effort/views.py, effort/serializers.py, effort/dal.py, effort/urls.py, EffortReview.tsx, api/effort.ts), FEAT-029 (reports/views.py, reports/services.py, reports/urls.py, FinanceExport.tsx, api/reports.ts) share no files. |
| Wave 16 | FEAT-030 | 1 | No | High | FEAT-027 (W10) | FEAT-030 (effort/services.py, effort/views.py, effort/serializers.py, effort/dal.py, effort/urls.py, TicketDetail.tsx, api/effort.ts) touches TicketDetail.tsx, which every remaining ticket-workflow feature also touches. No compatible parallel partner exists; FEAT-031 conflicts (effort files). Alone by file conflict. |
| Wave 17 | FEAT-016 | 1 | No | Standard | FEAT-011 (W9) | FEAT-016 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/dal.py, tickets/urls.py, TicketDetail.tsx) conflicts with all other available ticket features. No non-ticket partner is available after Wave 15. Alone by file conflict. |
| Wave 18 | FEAT-019 | 1 | No | Standard | FEAT-011 (W9) | FEAT-019 (sla/services.py, sla/dal.py, tickets/services.py, tickets/serializers.py, tickets/views.py, TicketDetail.tsx, api/tickets.ts) conflicts with FEAT-018 and all other ticket features. Scheduled here to unblock FEAT-020 and FEAT-021 (which unblock FEAT-024 → FEAT-025 → FEAT-007). Alone by file conflict. |
| Wave 19 | FEAT-018 | 1 | No | Standard | FEAT-011 (W9) | FEAT-018 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/dal.py, tickets/urls.py, TicketDetail.tsx) conflicts with all remaining ticket features. Scheduled here to unblock FEAT-022 (migration). Alone by file conflict. |
| Wave 20 | FEAT-022 | 1 | SP | Standard | FEAT-018 (W19) | Client comment model. Alone: tickets/migrations/0003_comment.py matches Shared Paths. |
| Wave 21 | FEAT-021 | 1 | No | Standard | FEAT-019 (W18) | FEAT-021 (sla/services.py, tickets/serializers.py, tickets/views.py, TicketList.tsx, TicketDetail.tsx) conflicts with FEAT-020 (same files) and all remaining ticket features. Scheduled before FEAT-020 to unblock FEAT-024 → FEAT-025 → FEAT-007 chain sooner. Alone by file conflict. |
| Wave 22 | FEAT-024 | 1 | SP | Standard | FEAT-021 (W21) | Live dashboard bootstrap migration. Alone: reports/migrations/0001_initial.py matches Shared Paths. |
| Wave 23 | FEAT-025 | 1 | SP | High | FEAT-024 (W22) | Monthly report model migration. Alone: reports/migrations/0002_monthlyclientreport.py matches Shared Paths. |
| Wave 24 | FEAT-020, FEAT-026 | 2 | No | Standard, Standard | FEAT-019 (W18), FEAT-025 (W23) | FEAT-020 (sla/services.py, tickets/serializers.py, tickets/views.py, TicketList.tsx, TicketDetail.tsx) and FEAT-026 (reports/views.py, reports/serializers.py, reports/urls.py, reports/services.py, ReportList.tsx, ReportDetail.tsx, api/reports.ts) share no files. |
| Wave 25 | FEAT-007 | 1 | SP | Critical | FEAT-025 (W23), FEAT-032 (W11) | Client data boundary and RLS. Alone: audit/migrations/0003_roles_and_rls.py matches Shared Paths. Both dependencies satisfied: FEAT-032 done at W11, FEAT-025 done at W23. |
| Wave 26 | FEAT-015 | 1 | No | Standard | FEAT-011 (W9) | FEAT-015 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/dal.py, tickets/urls.py, TicketDetail.tsx) conflicts with all remaining ticket features. No compatible non-ticket partner after W24. Alone by file conflict. |
| Wave 27 | FEAT-017 | 1 | No | Standard | FEAT-016 (W17) | FEAT-017 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/dal.py, tickets/urls.py, TicketDetail.tsx) conflicts with FEAT-023. Alone by file conflict. |
| Wave 28 | FEAT-023 | 1 | No | Standard | FEAT-022 (W20) | FEAT-023 (tickets/services.py, tickets/views.py, tickets/serializers.py, tickets/urls.py, TicketDetail.tsx) is the last unscheduled feature. Alone by file conflict with all prior ticket features. |

## Review Load

Reviewer capacity: 6 PRs per week (project.md). Maximum PRs in any wave: 3 (Waves 13, 14, 15). All 28 waves are within capacity.

| PRs per wave | Wave count | Waves |
|---|---|---|
| 1 PR | 23 | W1, W2, W3, W4, W5, W6, W8, W9, W10, W11, W12, W16, W17, W18, W19, W20, W21, W22, W23, W25, W26, W27, W28 |
| 2 PRs | 2 | W7, W24 |
| 3 PRs | 3 | W13, W14, W15 |

No staggering is required: every wave is at or below the 6 PR/week limit. The single reviewer (Mohanasunder) reviews and merges before the next wave opens. Waves with 3 PRs (Waves 13–15) represent the highest review load; if approval turnaround exceeds 1 business day (approval_sla_business_days: 1), the tech lead may reduce to 2 features per wave for those waves — this requires a human decision recorded in the decision log.

## Assumptions
- A-040: Wave sequencing treats every feature that lists a file matching any Shared Path glob in STD-001 § Shared Paths as "alone in its wave." This is the definition used by `check_feature_size.py waves`. 15 of 36 features are so classified, producing 15 singleton waves and driving the 28-wave count. Logged in docs/logs/assumptions-log.md.

## Open Questions
- OQ-067 — Answered 2026-10-17: FEAT-007/plan.md uses migration 0003_roles_and_rls.py (Wave 25); DEC-048 records this decision.

## Traceability Links
- Upstream: FBD-001 v0.1; PIB-005 v0.1; STD-001 v0.1 § Shared Paths; project.md capacity settings
- Downstream: FEAT-000 through FEAT-035 plan.md (Phase 6 build order); Phase 6 PRs (feature/FEAT-NNN-slug branches opened in wave order)

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
| Comments | Phase 5 validation passed (VAL-023). 28 waves, 0 collisions, OQ-067 resolved. |
| Timestamp | 2026-10-17 16:50 UTC |
