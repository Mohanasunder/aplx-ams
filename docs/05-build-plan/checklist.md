# Phase 5 checklist: Build Planning

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] Created from template: feature-breakdown
- [ ] Created from template: feature-plan
- [ ] Created from template: feature-tasks
- [ ] Created from template: feature-acceptance
- [ ] Created from template: feature-status
- [ ] Created from template: wave-plan
- [ ] Created from template: definition-of-done
- [ ] Created from template: environment-plan
- [ ] Task 0 (FEAT-000, Enabling) planned and every feature depends on it (`python3 scripts/check_feature_size.py task0` passes)
- [ ] Every plan has a Context Pack and `python3 scripts/context_pack.py check FEAT-NNN` passes
- [ ] `python3 scripts/check_feature_size.py size` passes (every feature within the sizing limits, no open design decisions)
- [ ] Risk tier and expected test runtime set per feature
- [ ] `python3 scripts/validate_artifact.py docs/05-build-plan --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 5` passes
- [ ] Every design element assigned to a feature
- [ ] No circular dependencies; wave plan fits review capacity
- [ ] Plans, tasks, acceptance files, and wave plan Approved by the tech lead
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
