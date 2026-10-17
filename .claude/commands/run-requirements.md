---
description: Run Phase 2 (Requirements Analysis) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 2: Requirements Analysis** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Turn approved discovery into testable epics, stories, acceptance criteria, NFRs, and a prioritized backlog.
- **Output folder:** `docs/02-requirements/`
- **Required inputs:**
  - Approved discovery artifacts
  - Answers to open questions
  - Stakeholder priorities
  - Existing system documentation (if changing an existing system)
  - Compliance requirements
  - Release or MVP expectations
  - Reporting and integration needs
- **Producer subagents:**
  1. `requirements-analyst`
  2. `traceability`
- **Sequence:** requirements-analyst writes epics, stories, acceptance criteria, NFRs, business rules, the backlog, and the domain glossary (GLO); terms it finds used with two meanings come back as open questions for the human; then traceability seeds the traceability matrix; the checker applies the requirements QA rules.
- **Deliverable files (friendly filenames — one file per type, all entries as sections within):**
  | File | Template | Contents |
  | --- | --- | --- |
  | `docs/02-requirements/epics.md` | `epic` | All epics as `## Epic E-N:` sections |
  | `docs/02-requirements/user-stories.md` | `user-story` | All stories as `## Story S-N:` sections with inline AC-n criteria |
  | `docs/02-requirements/nfrs.md` | `nfr` | All NFRs as `## NFR N-N:` sections |
  | `docs/02-requirements/business-rules.md` | `business-rule` | All business rules as `## Rule B-N:` sections |
  | `docs/02-requirements/backlog.md` | `backlog-entry` | Full backlog as `## Entry BL-N:` sections |
  | `docs/02-requirements/domain-glossary.md` | `domain-glossary` | Single domain glossary (GLO) |
- **Checker rules file:** `.ai/checker-rules/phase-2.md` (invoke the `checker` subagent)
- **Human approver:** Product owner / BA
- **Exit criteria:**
  - Every brief goal covered by at least one epic with an in-scope story, or put out of scope by a product owner decision (DEC-NNN): `python3 scripts/traceability.py check --phase 2` passes
  - NFRs have measurable targets
  - Domain glossary Approved; stories use its terms (`python3 scripts/glossary_check.py check` passes)
  - Stories, NFRs, and backlog Approved by the product owner / BA

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
