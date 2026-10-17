# Phase 0: Methodology Setup

Configure the project once: project details, approvers, review capacity, branch protection, CI, and the project-specific standards that agents read.

- **Command:** `/sdlc-init`
- **Human approver:** Tech lead
- **Output folder:** `docs/00-setup/`

## Required inputs

- Organization standards and approved technology list
- Security and compliance policies
- Approver names for each role
- Max parallel builder agents and human review capacity
- Approval turnaround target (SLA)

## Producer agents

- (none: this phase is run by the Orchestrator with the human)

## Deliverable templates

- `.ai/templates/input-readiness-checklist.md`

## How it runs

Run /sdlc-init: it interviews the human, fills project.md and .github/CODEOWNERS, and produces the readiness checklist for Phase 1.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
