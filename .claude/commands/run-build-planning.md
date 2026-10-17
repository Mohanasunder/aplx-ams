---
description: Run Phase 5 (Build Planning) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 5: Build Planning** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Slice the design into small, vertical features, each sized for one builder session (limits in project.md), with plan-mode markdown, sequenced to fit builder and human review capacity.
- **Output folder:** `docs/05-build-plan/`
- **Required inputs:**
  - Approved design package
  - Prioritized backlog and release scope
  - Maximum parallel builder agents and human review capacity (project.md)
  - Repo structure and branching strategy
  - Deadlines and milestones
  - Definition of Done
  - Known technical risks and dependencies
- **Producer subagents:**
  1. `build-planner`
  2. `dependency-sequencer`
  3. `environment-setup`
- **Sequence:** build-planner creates the feature breakdown, one docs/05-build-plan/feature-NNN-slug/ folder per feature (plan.md, tasks.md, acceptance.md, status.md) and the Definition of Done; dependency-sequencer then writes the wave plan; environment-setup writes the environment plan. build-planner plans **Task 0** first (`FEAT-000`, Type: Enabling: the walking skeleton) and makes every other feature depend on it. Each plan.md includes a Context Pack (exact sections as `ID vX.Y § section`). Before validation, run `python3 scripts/context_pack.py check FEAT-NNN` for every feature `python3 scripts/check_feature_size.py size`, and `python3 scripts/check_feature_size.py task0` and include its output in the validation summary; a failure goes back to `build-planner` to split the feature. The checker applies the build-planning rules.
- **Deliverable templates:** `feature-breakdown`, `feature-plan`, `feature-tasks`, `feature-acceptance`, `feature-status`, `wave-plan`, `definition-of-done`, `environment-plan`
- **Checker rules file:** `.ai/checker-rules/phase-5.md` (invoke the `checker` subagent)
- **Human approver:** Tech lead
- **Exit criteria:**
  - Every design element assigned to a feature
  - Task 0 (FEAT-000) planned as an Enabling feature; every feature depends on it (`check_feature_size.py task0` passes)
  - Every feature within the sizing limits, with no open design decisions (`check_feature_size.py size` passes)
  - Every feature's Context Pack resolves within max_context_pack_lines (`context_pack.py check` passes)
  - Phase summary `docs/05-build-plan/SUMMARY.md` Approved (`context_pack.py summaries 5` passes)
  - No circular dependencies; wave plan fits review capacity
  - Plans, tasks, acceptance files, and wave plan Approved by the tech lead

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
