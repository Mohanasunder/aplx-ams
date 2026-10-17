# Phase 6 checklist: Build

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] Created from template: feature-test-set (FEAT-NNN-TESTS), validated, and Approved before any implementation commit
- [ ] Approved test files unchanged since the Test Commit
- [ ] PR description section `## PR FEAT-NNN:` appended to `docs/06-build/pr-descriptions.md` (template `pr-description`)
- [ ] Created from template: ai-pre-review-report
- [ ] Created from template: security-scan-report
- [ ] `python3 scripts/validate_artifact.py docs/06-build --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated
- [ ] Change summary complete (`python3 scripts/pr_summary.py check FEAT-NNN` passes; Blockers None)
- [ ] Major/Blocker review findings and human change requests logged in `docs/logs/review-feedback-log.md` with categories
- [ ] After merge: `python3 scripts/learned_rules.py recurring` run; any recurring category has a drafted learned rule

## Exit
- [ ] Task 0 only: every gate in `automated-gates.md` has a real command and runs green in CI on the skeleton
- [ ] Human reviewer confirmed the tier's review depth in `/approve` (recorded in the approval log)
- [ ] Automated gates green
- [ ] Checker verdict recorded
- [ ] PR approved by a named human (two for High risk; tech lead and release manager for Critical)
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
