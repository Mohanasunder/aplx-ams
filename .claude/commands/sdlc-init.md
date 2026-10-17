---
description: Phase 0. Collect project details, approvers, and capacity; prepare the project for Phase 1
argument-hint: [optional project name]
---

You are the **Orchestrator**. Run **Phase 0: Methodology Setup**.

1. Use AskUserQuestion to collect, in one or two calls: project name, description, project manager, tech lead (name and description are required; the rest can be deferred). Then collect approver names for: Business owner / BA, Product owner, Architect / tech lead, UX, human developer reviewers, QA lead, release manager / DevOps, plus backup approvers.
2. Collect capacity settings: max parallel builder agents, human review capacity (PRs per week), max open feature branches, approval SLA in business days. Offer the defaults already in `project.md`.
3. Echo the values back and ask the human to confirm before writing.
4. Fill `project.md` (details table, approvers table, settings block) and set today's date as Created. Fill `.github/CODEOWNERS` with the approver names (leave platform usernames as placeholders if unknown).
5. Create the readiness checklist for Phase 1 with `python3 scripts/new_artifact.py --template input-readiness-checklist --title "Phase 1 readiness" --author orchestrator --out docs/00-setup/input-readiness-checklist.md`, fill it (inputs expected in `docs/01-discovery/inputs/`), validate it, and ask the tech lead to approve it with `/approve`.
6. List the **human-only setup actions** you cannot do: configure branch protection on the Git platform (no direct pushes to `main`, required checks, human approval, CODEOWNERS review, dismiss stale approvals, linear history); add CI secrets; provision scoped agent credentials (feature/hotfix branches only).
7. Update the Phase 0 row of `project.md` and tell the human the next step: drop discovery inputs in `docs/01-discovery/inputs/` and run `/run-discovery`.

Notes from the user: $ARGUMENTS
