# Phase 8 checklist: Deployment

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] Created from template: deployment-runbook
- [ ] Created from template: rollback-plan
- [ ] Created from template: go-live-checklist
- [ ] Created from template: release-notes
- [ ] Created from template: config-validation-report
- [ ] `python3 scripts/validate_artifact.py docs/08-deployment --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 8` passes
- [ ] IaC validates and passes policy checks
- [ ] Rollback plan exists
- [ ] Go-live checklist Approved by the release manager (and tech lead for Critical changes)
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
