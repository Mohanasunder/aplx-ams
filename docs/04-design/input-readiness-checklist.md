---
id: IRC-005
title: Phase 4 input readiness checklist
phase: 4
version: 0.1
template: input-readiness-checklist
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# Phase 4 input readiness checklist

> **One file per phase.** Each phase produces exactly one `input-readiness-checklist.md` in its own folder. Use `--out docs/0N-<phase-slug>/input-readiness-checklist.md` when calling `new_artifact.py`; never let it auto-name the file as `IRC-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-003 v0.2 â€” Phase 3 summary â€” docs/03-architecture/SUMMARY.md (Approved 2026-10-17)
- SUM-002 v0.4 â€” Phase 2 summary â€” docs/02-requirements/SUMMARY.md (Approved 2026-10-17)
- SUM-001 v0.3 â€” Phase 1 summary â€” docs/01-discovery/SUMMARY.md (Approved 2026-10-17)
- INT-004 v0.1 â€” Phase 4 interview record â€” docs/04-design/interview-record.md
- PIB-004 v0.1 â€” Phase 4 input brief â€” docs/04-design/phase-input-brief.md

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
This checklist records the readiness status of every required input for Phase 4 (Solution design), the overall readiness verdict, and the open assumptions producers must carry into the phase deliverables. It does not assess the quality of Phase 4 deliverables (that is the checker's role).

## Required Inputs Checklist
<!-- guidance: One row per required input: present / partial / missing, source, notes -->
| # | Required input | Status | Source | Notes |
| --- | --- | --- | --- | --- |
| 1 | SUM-003 v0.2 â€” Phase 3 summary | Present | docs/03-architecture/SUMMARY.md | Approved 2026-10-17 by Mohanasunder (Architect / tech lead). |
| 2 | SUM-002 v0.4 â€” Phase 2 summary | Present | docs/02-requirements/SUMMARY.md | Approved 2026-10-17 by Mohanasunder (Product owner). |
| 3 | SUM-001 v0.3 â€” Phase 1 summary | Present | docs/01-discovery/SUMMARY.md | Approved 2026-10-17 by Mohanasunder (Business owner / BA). |
| 4 | ADR-001 v0.3 Â§ A-6, A-7, A-11, A-13, A-17 | Present | docs/03-architecture/adrs.md | Approved with SUM-003. Sections needed: data separation, sessions, audit, CI rules, secrets. |
| 5 | ARC-001 v0.3 Â§ Components, Â§ NFR Mapping | Present | docs/03-architecture/architecture-overview.md | Approved with SUM-003. |
| 6 | THR-001 v0.2 Â§ Mitigations, Â§ Authentication and authorization model | Present | docs/03-architecture/threat-model.md | Approved with SUM-003. |
| 7 | TEC-001 v0.3 Â§ Recommendation | Present | docs/03-architecture/technology-comparison.md | Approved with SUM-003. Governs the approved technology list. |
| 8 | TOP-001 v0.2 Â§ Environments | Present | docs/03-architecture/deployment-topology.md | Approved with SUM-003. |
| 9 | NFR-001 v0.3 (N-1 to N-9) | Present | docs/02-requirements/nfrs.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 10 | REQ-001 v0.3 (S-1 to S-33) | Present | docs/02-requirements/user-stories.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 11 | BR-001 v0.3 (B-1 to B-24) | Present | docs/02-requirements/business-rules.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 12 | GLO-001 v0.3 â€” Domain glossary | Present | docs/02-requirements/domain-glossary.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 13 | PRS-001 v0.3 â€” Product requirement specification | Present | docs/02-requirements/product-requirement-specification.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 14 | BKL-001 v0.3 â€” Backlog | Present | docs/02-requirements/backlog.md | Approved with SUM-002 v0.4 (SCR S-4). |
| 15 | UI library decision (Q1) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | Material UI v6, MIT, default theme. Decision DEC-040. |
| 16 | Phase 2 assumptions A-014 to A-022 (Q2) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | All 7 confirmed as stated. Decision DEC-041. |
| 17 | Sign-in rate limit (Q3) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | 10 req/min per IP, burst 5. Decision DEC-042. |
| 18 | Development tooling (Q4) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | All proposed defaults adopted. Decision DEC-043. |
| 19 | Accessibility target (Q5) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | WCAG 2.1 Level A. Decision DEC-044. |
| 20 | Code coverage targets (Q6) | Available (confirmed) | Mohanasunder, chat, 2026-10-17 | 80% backend Python, 70% frontend TypeScript. Decision DEC-045. |
| 21 | Third-party API documentation | Not applicable | N/A | Greenfield system; no external API integrations in release 1 (SUM-003 v0.2 Â§ Decisions). |

**Overall verdict: Ready with assumptions.**

All required inputs are present and all blocker gaps are resolved. Twelve inherited open assumptions carry into Phase 4 and must be labeled in each deliverable where they affect a design decision. None is a Phase 4 blocker.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Confirmed in the Phase 4 entry interview (update docs/logs/assumptions-log.md to Confirmed):
- A-014: at-risk and breached states evaluated separately per response clock and resolution clock â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-015: monthly report period is calendar month IST; ticket counts are raised, Resolved, Closed per priority â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-016: audit entry stores old value and new value; no user can edit or delete any audit entry â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-019: refused sign-in shows generic error; no account name or password hint â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-020: effort entry must be > 0 hours; 0 or negative values are not saved â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-021: when response % or resolution % denominator is 0, display "no tickets" â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-022: ticket statuses are Open, Awaiting client, Resolved, Closed â€” Confirmed, Mohanasunder, chat, 2026-10-17.

Inherited open assumptions that Phase 4 producers must label (remain Open in docs/logs/assumptions-log.md):
- A-008: supported browsers are current and previous major Chrome and Edge on desktop. Affects: UIS, STD, TST.
- A-026: cost estimate in INR, new spend 0, server capacity share, staff and AI hours. Affects: no Phase 4 deliverable directly.
- A-027: timestamps stored UTC, displayed IST, SLA on IST calendar. Affects: DBD, BED.
- A-028: passwords stored with Argon2id. Affects: BED, STD.
- A-029: report libraries are XlsxWriter, csv, WeasyPrint â€” free open-source. Affects: BED.
- A-031: weekly dump copied to test server; test server holds production data. Affects: BED, STD.
- A-032: database stays under 5 GB for 5 years. Affects: DBD (sizing notes).
- A-033: pg_dump file at most 2 GB; 8 weekly dumps retained. Affects: DBD (sizing notes).
- A-034: peak load 30 concurrent users at at most 15 API req/s; 5 Gunicorn workers. Affects: BED Â§ Capacity.
- A-035: GitHub Actions use stays within free-tier quota on public repository. Affects: STD (CI configuration).
- A-036: operating effort about 8 staff hours per month. Affects: no Phase 4 deliverable directly.
- A-038: no secret manager; secrets as root-only Docker Compose file secrets. Affects: STD.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None. All open questions from Phases 1 to 3 are answered (docs/logs/open-questions-log.md). No new open questions were raised in the Phase 4 entry interview.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-003 v0.2; SUM-002 v0.4; SUM-001 v0.3; INT-004 v0.1; PIB-004 v0.1.
- Downstream: Phase 4 deliverables (DBD, API, BED, UIS, PRM, STD, TST â€” under docs/04-design/).

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
| Comments | Phase 4 intake artifact; content captured in PIB-004 which is Approved. Approving formally to close the Phase 4 record. |
| Timestamp | 2026-10-17 14:11 UTC |
