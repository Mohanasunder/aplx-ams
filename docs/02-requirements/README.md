# Phase 2: Requirements Analysis

Turn approved discovery into testable epics, stories, acceptance criteria, NFRs, and a prioritized backlog.

- **Command:** `/run-requirements`
- **Human approver:** Product owner / BA
- **Output folder:** `docs/02-requirements/`

## Required inputs

- Approved discovery artifacts
- Answers to open questions
- Stakeholder priorities
- Existing system documentation (if changing an existing system)
- Compliance requirements
- Release or MVP expectations
- Reporting and integration needs

## Producer agents

- `requirements-analyst`
- `traceability`

## Deliverable templates

- `.ai/templates/epic.md`
- `.ai/templates/user-story.md`
- `.ai/templates/acceptance-criteria.md`
- `.ai/templates/nfr.md`
- `.ai/templates/business-rule.md`
- `.ai/templates/backlog-entry.md`

## How it runs

requirements-analyst writes epics, stories, acceptance criteria, NFRs, business rules, and the backlog; then traceability seeds the traceability matrix; the checker applies the requirements QA rules.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
