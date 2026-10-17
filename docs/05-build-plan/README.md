# Phase 5: Build Planning

Slice the design into small features with plan-mode markdown, sequenced to fit builder and human review capacity.

- **Command:** `/run-build-planning`
- **Human approver:** Tech lead
- **Output folder:** `docs/05-build-plan/`

## Required inputs

- Approved design package
- Prioritized backlog and release scope
- Maximum parallel builder agents and human review capacity (project.md)
- Repo structure and branching strategy
- Deadlines and milestones
- Definition of Done
- Known technical risks and dependencies

## Producer agents

- `build-planner`
- `dependency-sequencer`
- `environment-setup`

## Deliverable templates

- `.ai/templates/feature-breakdown.md`
- `.ai/templates/feature-plan.md`
- `.ai/templates/feature-tasks.md`
- `.ai/templates/feature-acceptance.md`
- `.ai/templates/feature-status.md`
- `.ai/templates/wave-plan.md`
- `.ai/templates/definition-of-done.md`
- `.ai/templates/environment-plan.md`

## How it runs

build-planner creates the feature breakdown, one docs/05-build-plan/feature-NNN-slug/ folder per feature (plan.md, tasks.md, acceptance.md, status.md) and the Definition of Done; dependency-sequencer then writes the wave plan; environment-setup writes the environment plan. The checker applies the build-planning rules.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
