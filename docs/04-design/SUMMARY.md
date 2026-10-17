---
id: SUM-004
title: Phase 4 Solution Design Summary
phase: 4
version: 0.1
template: phase-summary
template_version: 1.0
status: Draft
author_agent: governance-audit
approver: Approver of the phase
date: 2026-10-17
validation: Pass
---
# Phase 4 Solution Design Summary

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-004 v0.1 — Phase 4 input brief (Approved 2026-10-17)
- INT-004 v0.1 — Phase 4 interview record (Draft; see Open Items — not in approval log)
- IRC-005 v0.1 — Phase 4 readiness checklist (Draft; see Open Items — not in approval log)
- SUM-003 v0.2 and the Phase 3 artifacts it indexes (Approved 2026-10-17): ARC-001, TEC-001, ADR-001 v0.3; THR-001, TOP-001, CST-001, RSK-003 v0.2.
- SUM-002 v0.4 and the Phase 2 artifacts it indexes (Approved 2026-10-17): REQ-001, NFR-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3.
- Human decisions DEC-040 to DEC-046, Mohanasunder, chat and gate, 2026-10-17.

## Purpose And Scope
<!-- guidance: One or two sentences: which phase this summarizes. File docs/0N-*/SUMMARY.md -->
Summarises Phase 4 (Solution design) of APLX AMS so Phase 5 (Build planning) can start from this page and open full documents only for the sections listed below.

## Decisions
<!-- guidance: Bullets: the decision, the reason in one clause, and its source 'ID vX.Y § section'. Only decisions later phases must respect -->
- DEC-040: UI library is Material UI v6 (MUI), MIT licence, default theme — no brand guide in approved artifacts; MUI provides a complete accessible component set (PIB-004 Q1).
- DEC-041: Phase 2 open assumptions A-014 to A-022 confirmed as stated — producers verified all seven at the Phase 4 entry interview (PIB-004 Q2).
- DEC-042: Sign-in rate limit 10 req/min/IP, burst of 5, enforced at the Nginx reverse proxy — aligns with the 5-attempt lockout in NFR N-5; ADR A-14 deferred the concrete value to Phase 4 (PIB-004 Q3; ADR-001 v0.3 A-14).
- DEC-043: Development tooling defaults adopted: Python ruff, mypy --strict, pytest+pytest-django, bandit, pip-audit, detect-secrets; TypeScript eslint+TS plugin, tsc --noEmit, vitest, playwright; factory-boy, freezegun for test fixtures — ADR A-2 deferred tooling to Phase 4 coding standards; all tools are free and open-source (PIB-004 Q4; ADR-001 v0.3 A-2).
- DEC-044: Accessibility target WCAG 2.1 Level A — minimum for the internal pilot (no external client users in release 1); upgrade to AA before external clients join (PIB-004 Q5).
- DEC-045: CI coverage gates 80% line coverage backend Python, 70% line coverage frontend TypeScript — accounts for higher business-rule density in the backend; no numeric target existed in approved artifacts (PIB-004 Q6).
- DEC-046: Phase 4 Run 2 Fail — send all 8 findings (2 Major, 6 Minor) back to producers (Run 3) — both Majors must be resolved before Phase 5; fixing all Minors in the same pass avoids a Run 4 (VAL-020; DEC-046).

## Constraints Set
<!-- guidance: Bullets: limits later phases must work within (technology, NFR targets, scope exclusions, compliance), each with its source ID -->
- Database: PostgreSQL 18, 10 tables across 7 apps, row-level security enforced; no other storage (DBD-001 v0.1; ADR-001 v0.3 A-4, A-6).
- API: 46 REST endpoints, 8 features (F-1 to F-8), session cookie auth; no JWT or OAuth; contract frozen in openapi.yaml (API-001 v0.1; ADR-001 v0.3 A-3).
- Backend: Django 5.2 LTS modular monolith, 7 apps (accounts, organizations, tickets, sla, effort, reports, audit); Gunicorn + Nginx (BED-001 v0.1; ADR-001 v0.3 A-2).
- Frontend: React 18 + TypeScript + MUI v6, 12 routes, Vite build; Node.js only in CI (UIS-001 v0.1; DEC-040; ADR-001 v0.3 A-3).
- Permissions: 46 endpoints x 4 roles (l1_support, l2l3_support, delivery_manager, client_user) fixed in PRM-001; any change requires an SCR (PRM-001 v0.1).
- Coverage gates: 80% backend / 70% frontend, enforced in CI (STD-001 v0.1; DEC-045).
- Accessibility: WCAG 2.1 Level A (UIS-001 v0.1; DEC-044).
- Testing: 6 test levels, 9 E2E journeys, RLS two-organization CI requirement (TST-001 v0.1; ADR-001 v0.3 A-6).
- Stack limited to the TEC-001 v0.3 Recommendation list; anything else requires a new ADR (SUM-003 § Constraints Set).

## Open Items
<!-- guidance: Open questions (OQ-), assumptions (A-), and risks (RSK-) still open, with owner; or 'None' -->
All owned by Mohanasunder.
- Open assumptions: A-039 (soft-delete behavior on effort_effortentry reconciles BR B-15 delete right with NFR N-4 unlimited retention; Open pending data retention clarification) — logged in docs/logs/assumptions-log.md.
- Inherited open assumptions from Phase 3: A-026 to A-029, A-031 to A-036, A-038 (unchanged, carried from SUM-003).
- Open OQs: none raised in Phase 4.
- Risks: inherited from SUM-003; no new phase-4 risk register entries.
- Governance gap (escalated to human): INT-004 v0.1 (interview-record.md) and IRC-005 v0.1 (input-readiness-checklist.md) have status Draft and no entry in the approval log. Human decision required: approve these artifacts or confirm they are subsumed by PIB-004 approval.

## Documents
<!-- guidance: One line per Approved artifact of the phase: 'ID vX.Y - title - path'. Checked by scripts/context_pack.py summaries -->
Phase 4 intake:
- PIB-004 v0.1 - Phase 4 input brief - docs/04-design/phase-input-brief.md (Approved 2026-10-17)
- INT-004 v0.1 - Phase 4 interview record - docs/04-design/interview-record.md (Draft — not in approval log; governance gap)
- IRC-005 v0.1 - Phase 4 readiness checklist - docs/04-design/input-readiness-checklist.md (Draft — not in approval log; governance gap)

Phase 4 design deliverables, approved 2026-10-17 by Mohanasunder (Architect / tech lead + UX):
- DBD-001 v0.1 - APLX AMS: Database Design - docs/04-design/database-design.md
- API-001 v0.1 - APLX AMS: API Specification - docs/04-design/api-spec.md
- openapi.yaml - OpenAPI 3.1 contract (companion to API-001) - docs/04-design/openapi.yaml
- BED-001 v0.1 - APLX AMS: Backend Design - docs/04-design/backend-design.md
- UIS-001 v0.1 - APLX AMS: UI Specification - docs/04-design/ui-spec.md
- PRM-001 v0.1 - APLX AMS: Permission Matrix - docs/04-design/permission-matrix.md
- STD-001 v0.1 - APLX AMS: Coding Standards - docs/04-design/coding-standards.md
- TST-001 v0.1 - APLX AMS: Test Strategy - docs/04-design/test-strategy.md

## What The Next Phase Needs
<!-- guidance: The few documents or sections the next phase should open in full, as 'ID vX.Y § section'; everything else is covered above -->
- DBD-001 v0.1 § Tables (all 10 tables; column names, types, and FK constraints the feature slicer needs for shared-path identification).
- API-001 v0.1 § Endpoints (full endpoint list with HTTP methods, roles, and feature groupings F-1 to F-8 for feature slicing).
- PRM-001 v0.1 (full document; role-per-endpoint grid the dependency sequencer reads).
- STD-001 v0.1 § CI Gate Commands (gate command list used by the environment plan and branch scripts).
- TST-001 v0.1 § Test Levels and § E2E Journeys (defines what the Phase 5 wave plan must schedule per feature).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-039 (Open, owner Mohanasunder): soft-delete on effort_effortentry reconciles BR B-15 with NFR N-4; logged in docs/logs/assumptions-log.md.
- Inherited: A-026 to A-029, A-031 to A-036, A-038 (Open, from Phase 3); A-014 to A-022 Confirmed (DEC-041).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- None raised in Phase 4. All Phase 3 OQs (OQ-052 to OQ-066) remain Answered.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-004; INT-004; IRC-005; SUM-003; SUM-002; SUM-001; ARC-001; TEC-001; ADR-001; THR-001; NFR-001; REQ-001; BR-001; PRS-001.
- Indexes: DBD-001; API-001; openapi.yaml; BED-001; UIS-001; PRM-001; STD-001; TST-001.
- Downstream: Phase 5 input brief (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Documents lists every Approved artifact of the phase as 'ID vX.Y'
- [x] About half a page: a reader can start the next phase from this summary alone

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
