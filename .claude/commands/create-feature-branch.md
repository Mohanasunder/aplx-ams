---
description: Create the feature branch for an approved feature (after a human selects it)
argument-hint: FEAT-NNN
---

Create the branch for `$ARGUMENTS`.

1. Confirm that a human selected this feature to build now, and show its risk tier and wave from `docs/05-build-plan/`.
2. Run `bash scripts/create-feature-branch.sh <FEAT-NNN>` (add `--push` only if the human wants it pushed). The script checks approvals, dependencies Merged, review capacity, clean tree, and fresh `main`.
3. If it fails, show the precondition that failed and what must change; do not work around it.
4. On success, open a draft PR: `gh pr create --draft --title "FEAT-NNN: <name>" --body "<link to plan.md, stories, acceptance criteria>"` (ask for confirmation if the push needs approval).
