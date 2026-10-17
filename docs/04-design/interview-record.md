---
id: INT-004
title: Phase 4 interview record
phase: 4
version: 0.1
template: interview-record
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# Phase 4 interview record

> **One file per phase.** Each phase produces exactly one `interview-record.md` in its own folder. Use `--out docs/0N-<phase-slug>/interview-record.md` when calling `new_artifact.py`; never let it auto-name as `INT-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-003 v0.2 â€” Phase 3 summary â€” docs/03-architecture/SUMMARY.md (Approved 2026-10-17)
- SUM-002 v0.4 â€” Phase 2 summary â€” docs/02-requirements/SUMMARY.md (Approved 2026-10-17)
- docs/logs/assumptions-log.md (A-014 to A-022 confirmed; A-026 to A-029, A-031 to A-036, A-038 still open)
- docs/logs/open-questions-log.md (all OQs answered from Phases 1 to 3)

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
This record documents the Phase 4 entry interview conducted between the phase-intake agent and Mohanasunder on 2026-10-17. It covers every question asked, the answer given, and who gave it. It does not record Phase 4 design decisions made by producers; those go into the phase deliverables and decision-log.md.

## Questions And Answers
<!-- guidance: Table: ID, question, why it matters (template section affected), answer, answered by, date -->
| ID | Priority | Question | Template section affected | Answer | Answered by | Date |
| --- | --- | --- | --- | --- | --- | --- |
| Q1 | BLOCKER | Which React UI component library should the frontend use in release 1? | UIS Â§ Component library; STD Â§ Frontend dependencies | Material UI v6 (MUI), MIT licence, default theme. | Mohanasunder | 2026-10-17 |
| Q2 | BLOCKER | Phase 2 open assumptions A-014 to A-022 remain open. Can you confirm each as stated or provide a correction? | DBD Â§ Schema; API Â§ Endpoints; BED Â§ Service layer; UIS Â§ Screens; PRM Â§ Matrix | All 7 confirmed as stated: A-014 (response and resolution clocks evaluated separately), A-015 (calendar month IST; counts raised, Resolved, Closed per priority), A-016 (old value and new value stored; no edits or deletes), A-019 (generic error, no hint), A-020 (> 0 hours only), A-021 ("no tickets" when denominator is 0), A-022 (Open, Awaiting client, Resolved, Closed). | Mohanasunder | 2026-10-17 |
| Q3 | ADVISORY | What rate limit should apply to the sign-in endpoint (requests per minute per IP, and burst size)? | API Â§ Security; BED Â§ Authentication; STD Â§ Rate limiting | 10 requests per minute per IP address, burst of 5. | Mohanasunder | 2026-10-17 |
| Q4 | ADVISORY | Should the project adopt the following proposed development tooling defaults? (ruff, mypy, pytest + pytest-django, bandit, pip-audit, detect-secrets; eslint + TS plugin, tsc, vitest, playwright) | STD Â§ Linting, Â§ Static analysis, Â§ Test tooling; TST Â§ Tools | Adopt all proposed defaults. | Mohanasunder | 2026-10-17 |
| Q5 | ADVISORY | What WCAG conformance level should Phase 4 UI screens target? | UIS Â§ Accessibility; STD Â§ Accessibility; TST Â§ Accessibility testing | WCAG 2.1 Level A. | Mohanasunder | 2026-10-17 |
| Q6 | ADVISORY | What minimum code coverage percentages should CI enforce (backend Python and frontend TypeScript)? | STD Â§ Coverage gates; TST Â§ Coverage targets | 80% line coverage for backend Python; 70% line coverage for frontend TypeScript; both CI-enforced. | Mohanasunder | 2026-10-17 |

## Deferred Items
<!-- guidance: Questions answered with 'defer' or 'don't know yet'; each links to an assumption (A-xxx) or open question (OQ-xxx) -->
None. All six questions were answered directly by Mohanasunder on 2026-10-17. No question was deferred.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Confirmed in this interview (previously Open; status changes to Confirmed in docs/logs/assumptions-log.md):
- A-014, A-015, A-016, A-019, A-020, A-021, A-022 â€” confirmed by Mohanasunder, chat, 2026-10-17 (Q2).

No new assumptions were raised in this interview. Inherited open assumptions from earlier phases (A-008, A-026 to A-029, A-031 to A-036, A-038) remain Open and carry into Phase 4; producers label them in each deliverable where they affect a design decision.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None. All questions from Phases 1 to 3 are answered (docs/logs/open-questions-log.md). No new open questions were raised in this interview.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-003 v0.2; SUM-002 v0.4; SUM-001 v0.3; docs/logs/assumptions-log.md; docs/logs/open-questions-log.md.
- Downstream: PIB-004 v0.1 (Phase 4 input brief); IRC-005 v0.1 (Phase 4 readiness checklist).

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
