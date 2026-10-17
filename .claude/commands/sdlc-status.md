---
description: Show phase and approval status, open questions, validation state, and stale branches
---

Report the current state of the project concisely. Do not change anything.

1. Read `project.md` (phase status table, settings).
2. For each artifact in `docs/NN-*/` (skip README/checklist), read the front matter and tabulate counts per phase: Draft, In review, Approved, Rejected; and validation values. Run `python3 scripts/validate_artifact.py docs --check-links` and report the overall verdict and the top findings.
3. Count Open items in `docs/logs/open-questions-log.md` by priority (Blocker first) and open assumptions.
4. List `feature/*` branches with `git branch --list 'feature/*'` and the last commit date of each (`git log -1 --format=%cr <branch>`); flag any older than `stale_branch_days`; compare the number of open feature branches with `max_open_feature_branches`.
5. Spec changes: run `python3 scripts/spec_impact.py records` and `python3 scripts/spec_impact.py stale`; list open (not Approved) SCRs in `docs/logs/spec-changes/`, Blocked features, and approved artifacts citing outdated versions.
6. Learned rules: run `python3 scripts/learned_rules.py recurring` and `python3 scripts/learned_rules.py stats`; list recurring categories without a rule, Draft learned rules waiting for the tech lead, and rules approved per week.
7. Spikes and pilot measures: run `python3 scripts/spike.py check` (open spikes, expired time boxes, leftover branches) and `python3 scripts/pilot_metrics.py report`; show this week's first-pass acceptance, average review minutes per feature, spec-gap SCRs, and learned rules added, against the `pilot_target_*` values in project.md (or say the baseline is still being collected).
8. Decisions: run `python3 scripts/log_decision.py check`; show the decisions and overrides recorded since the last phase gate.
9. List artifacts that are `In review` and waiting for a human, oldest first, versus the approval SLA.
10. Finish with the single most useful next action.
