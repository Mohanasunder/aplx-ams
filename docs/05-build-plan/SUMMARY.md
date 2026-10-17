---
id: SUM-005
title: Phase 5 Build Planning Summary
phase: 5
version: 0.1
template: phase-summary
template_version: 1.0
status: Approved
author_agent: governance-audit
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# Phase 5 Build Planning Summary

## Input References
- SUM-004 v0.1 — Phase 4 Solution Design Summary — docs/04-design/SUMMARY.md (Approved 2026-10-17, Mohanasunder)
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief — docs/05-build-plan/phase-input-brief.md (Approved 2026-10-17, Mohanasunder)
- FBD-001 v0.1 — APLX AMS: Feature Breakdown — docs/05-build-plan/feature-breakdown.md (Approved 2026-10-17, Mohanasunder)
- DOD-001 v0.1 — APLX AMS: Definition of Done — docs/05-build-plan/definition-of-done.md (Approved 2026-10-17, Mohanasunder)
- WAV-001 v0.1 — APLX AMS Build Wave Plan — docs/05-build-plan/wave-plan.md (Approved 2026-10-17, Mohanasunder)
- ENV-001 v0.1 — APLX AMS Environment Plan — docs/05-build-plan/environment-plan.md (Approved 2026-10-17, Mohanasunder)
- FEAT-000 to FEAT-035 v0.1 — feature plan.md files in docs/05-build-plan/feature-NNN-*/ (all Approved 2026-10-17, Mohanasunder)

## Purpose And Scope
Phase 5 sliced the approved Phase 4 design into 36 features (FEAT-000 to FEAT-035) in 28 sequential build waves, established the Definition of Done, and defined the local and CI environment. It does not schedule calendar dates, assign engineers, or resolve design questions (those belong to Phase 4).

## Decisions
- **DEC-047 (A-039 confirmed):** Soft-delete (`is_deleted` flag) on `effort_effortentry` is the accepted design; reconciles BR B-15 (delete own entries within the calendar month) with NFR N-4 (unlimited retention); DBD-001 v0.1 stands, no SCR required. Source: DBD-001 v0.1; PIB-005 v0.1 Phase 5 entry interview Q4.
- **DEC-048 (migration numbering):** FEAT-007 plan.md migration renamed from `0002_roles_and_rls.py` to `0003_roles_and_rls.py` to avoid collision with FEAT-033's `0002_security_event_type.py`. Source: OQ-067; WAV-001 v0.1; FEAT-007 plan.md; FEAT-033 plan.md.
- **DEC-049 (Phase 5 Run 1 Fail):** Send back to producers — fix 1 Major and 8 Minors before human review. Source: VAL-022 Phase 5 Run 1 Fail.

## Constraints Set
- Technology stack: Django 5.2 LTS (Python), React 18 (TypeScript), PostgreSQL 18, Docker Compose (local dev), GitHub Actions (CI). Source: TEC-001 v0.3, ADR-001 v0.3.
- CI coverage gates: 80% line coverage for backend Python, 70% line coverage for frontend TypeScript. Source: DEC-045, PIB-005 v0.1.
- Test runtime cap: 10 minutes per feature. Source: project.md `max_test_runtime_minutes`.
- Max 10 source files changed per feature, max 4 acceptance criteria per feature. Source: project.md.
- Max 3 parallel builder agents; max 3 open feature branches; max 6 PR reviews per week. Source: project.md.
- Features touching a Shared Path glob (migrations, CI YAML, package manifests, pyproject.toml, requirements.txt) must be alone in their wave; 15 of 36 features are singleton waves for this reason. Source: STD-001 v0.1 § Shared Paths; WAV-001 v0.1.
- FEAT-000 (walking skeleton) must merge before any other feature branch is opened. Source: WAV-001 v0.1 Wave 1.

## Open Items
- A-008 — Supported browsers assumed current and previous major Chrome and Edge on desktop (Open). Owner: Mohanasunder.
- A-031 — Weekly PostgreSQL dump copied to test server; test server holds production data (Open). Owner: Mohanasunder.
- A-032 — Database stays under 5 GB for 5 years (volume estimate, Open). Owner: Mohanasunder.
- A-033 — Weekly dump file count and size on test server (Open). Owner: Mohanasunder.
- A-034 — Peak load sizing: 30 concurrent users, 15 API req/s, 5 Gunicorn workers (Open; to be verified by Phase 7 load test). Owner: Mohanasunder.
- A-035 — GitHub Actions usage under plan quota on public repository (Open). Owner: Mohanasunder.
- A-036 — Operating staff-hours estimate (Open; DevOps to confirm). Owner: Mohanasunder.
- A-038 — Secrets as root-only files on each server; no company secret manager available (Open). Owner: Mohanasunder.
- A-040 — Wave count 28 results from 15 singleton Shared Path features (Open; consistent with `check_feature_size.py waves`). Owner: Mohanasunder.

## Documents
- FBD-001 v0.1 - APLX AMS: Feature Breakdown - docs/05-build-plan/feature-breakdown.md
- DOD-001 v0.1 - APLX AMS: Definition of Done - docs/05-build-plan/definition-of-done.md
- WAV-001 v0.1 - APLX AMS Build Wave Plan - docs/05-build-plan/wave-plan.md
- ENV-001 v0.1 - APLX AMS Environment Plan - docs/05-build-plan/environment-plan.md
- FEAT-000 to FEAT-035 v0.1 - 36 feature plans - docs/05-build-plan/feature-NNN-*/plan.md (each feature has its own subfolder)

## What The Next Phase Needs
Phase 6 (Build) must open each feature's plan in full before building it. The mandatory reads per feature are:

- `FEAT-NNN v0.1 § Files To Create Or Modify` — the only files the builder may change.
- `FEAT-NNN v0.1 § Acceptance Criteria` — used to write the locked test set before any implementation.
- `FEAT-NNN v0.1 § New Packages` — the only packages the builder may add or upgrade (CI-enforced).
- `FEAT-NNN v0.1 § Dependencies` — confirms which waves must be merged first.
- WAV-001 v0.1 § Waves — to identify the wave and confirm no Shared Path collision.
- DOD-001 v0.1 — Definition of Done checklist that every PR must satisfy.
- ENV-001 v0.1 — local and CI environment setup; run once before FEAT-000.

Build order: Wave 1 (FEAT-000) then Wave 2 (FEAT-001) then Wave 3 (FEAT-035) are enabling scaffolds that must merge before any story feature branch is opened.

## Assumptions
- A-039 — Soft-delete on `effort_effortentry` satisfies BR B-15 and NFR N-4; confirmed DEC-047, 2026-10-17.
- A-040 — Wave sequencing treats every feature touching a Shared Path glob as alone in its wave; produces 15 singleton waves and a 28-wave total; consistent with `check_feature_size.py waves`.

## Open Questions
- OQ-067 — Migration numbering collision between FEAT-033 and FEAT-007; Answered 2026-10-17 (DEC-048: FEAT-007 uses `0003_roles_and_rls.py`).

## Traceability Links
- Upstream: SUM-004 v0.1 (Phase 4 Solution Design Summary)
- Downstream: Phase 6 feature branches FEAT-000 to FEAT-035 (one branch per feature, opened in wave order)

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
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Phase 5 Build Planning Summary. Validates clean. Phase 5 complete. |
| Timestamp | 2026-10-17 16:57 UTC |
