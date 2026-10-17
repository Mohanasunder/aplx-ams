---
id: IRC-001
title: Phase 1 readiness
phase: 0
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
Not applicable - Phase 0 has no upstream approved artifacts. Project details, approvers, and capacity settings are recorded in `project.md` (filled 2026-10-17 by /sdlc-init, reconfirmed by Mohanasunder on 2026-10-17).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the inputs Phase 1 (Business discovery) needs for project APLX AMS ("An Application Management Services Solution"), where they go (`docs/01-discovery/inputs/`), and their current status.

Does not cover: the content of those inputs, requirements, or technology choices.

## Required Inputs Checklist
<!-- guidance: One row per required input: present / partial / missing, source, notes -->
| # | Required input | Status | Source | Notes |
| --- | --- | --- | --- | --- |
| 1 | Problem or opportunity statement (even rough) | Partial | `docs/01-discovery/inputs/requirements.txt`, `project.md` description | One sentence: "I want to build Application management services solution". Missing: who it serves, what problem it solves, why now |
| 2 | Stakeholder interviews, meeting transcripts, workshop notes | Missing | Mohanasunder (Business owner / BA) | Drop files in `docs/01-discovery/inputs/` |
| 3 | Existing documents: SOPs, proposals, RFPs, current AMS contracts or SLAs | Missing | Mohanasunder (Business owner / BA) | Drop files in `docs/01-discovery/inputs/` |
| 4 | Current systems and tools in use | Missing | Mohanasunder (Business owner / BA) | List in a file in `docs/01-discovery/inputs/` |
| 5 | Business goals, KPIs, budget and timeline constraints | Missing | Mohanasunder (Product owner) | Drop files in `docs/01-discovery/inputs/` |
| 6 | Regulatory and policy constraints | Missing | Mohanasunder (Business owner / BA) | State "none known" if none |
| 7 | Market or competitor information | Missing (optional) | Mohanasunder | Needed only if research-analyst is requested |
| 8 | Named Phase 1 approver (Business owner / BA) | Present | `project.md` | Mohanasunder |

Readiness verdict: Not ready to run discovery until rows 2 to 5 are present or partial, and row 1 states the users and problem.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None. Missing inputs are tracked in the Required Inputs Checklist above; the Phase 1 entry interview (phase-intake) will raise questions about their content.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: Not applicable - first artifact of the project.
- Downstream: Phase 1 Phase Input Brief and discovery artifacts in `docs/01-discovery/`.

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
| Role | Tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Minor findings F-01 to F-04 accepted; missing discovery inputs to be gathered in Phase 1 intake. |
| Timestamp | 2026-10-17 04:38 UTC |
