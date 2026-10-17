---
id: IRC-002
title: Phase 1 readiness
phase: 1
version: 0.1
template: input-readiness-checklist
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 1 readiness

> **One file per phase.** Each phase produces exactly one `input-readiness-checklist.md` in its own folder. Use `--out docs/0N-<phase-slug>/input-readiness-checklist.md` when calling `new_artifact.py`; never let it auto-name the file as `IRC-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- IRC-001 v0.1 (Phase 0, Approved 2026-10-17).
- `project.md` (Phase 0 Approved 2026-10-17).
- INT-001 v0.1 Phase 1 interview, 2026-10-17.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the status of each Phase 1 required input (`docs/01-discovery/README.md`) after the entry interview, and the readiness verdict for starting the Phase 1 producers.

Does not cover: the content of the discovery deliverables.

## Required Inputs Checklist
<!-- guidance: One row per required input: present / partial / missing, source, notes -->
| # | Required input | Status | Source | Notes |
| --- | --- | --- | --- | --- |
| 1 | Problem or opportunity statement | Present | INT-001 Q1 to Q4 | Internal AMS delivery tool for SAP application support; three problems (SLA visibility, manual effort, fragmented tools) |
| 2 | Stakeholder interviews, transcripts, workshop notes | Partial | INT-001 | Only this interview with Mohanasunder; groups known, names missing (OQ-006) |
| 3 | Existing documents: SOPs, proposals, RFPs, client SLA terms | Missing | Human | Nothing in `docs/01-discovery/inputs/` beyond `requirements.txt` (OQ-004) |
| 4 | Current systems and tools | Present | INT-001 Q6 | Email and spreadsheets; client-side tools unknown (OQ-010) |
| 5 | Business goals, KPIs, budget, timeline | Partial | INT-001 Q7, Q9, Q10, Q16 | KPIs named, no baseline or target (OQ-001); budget: existing staff, AI agents and existing infrastructure; timeline: 3 months (A-001, OQ-013) |
| 6 | Regulatory and policy constraints | Present | INT-001 Q11, Q15 | None known; personal data limited to client contact names and emails |
| 7 | Market or competitor information | Not applicable | INT-001 Q13 | Research not requested |
| 8 | Named Phase 1 approver | Present | `project.md` | Mohanasunder (Business owner / BA); no backup (OQ-014) |
| 9 | Phase 0 approved | Present | IRC-001 v0.1, approval log 2026-10-17 | - |

Verdict: Ready with assumptions. No Blocker. High open questions OQ-001, OQ-004, OQ-005 must be answered or accepted by the Business owner / BA before the Phase 1 gate.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Open): 3-month window starts 2026-10-17.
- A-002 (Confirmed): client users see only their own organization's data.
- A-003 (Confirmed): release 1 is SAP applications only.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Open: OQ-001, OQ-004, OQ-005 (High); OQ-006, OQ-007, OQ-008, OQ-010, OQ-013, OQ-014 (Medium); OQ-011 (Low). Answered: OQ-002, OQ-003, OQ-009, OQ-012. All in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: IRC-001 v0.1; `project.md`; INT-001.
- Downstream: PIB-001; Phase 1 deliverables in `docs/01-discovery/`.

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
| Role | Business owner / BA |
| Version | 0.1 |
| Conditions | None |
| Comments | Minor findings F-01 to F-04 (phase-1-run-1) accepted. |
| Timestamp | 2026-10-17 04:55 UTC |
