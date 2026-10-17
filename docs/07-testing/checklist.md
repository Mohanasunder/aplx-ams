# Phase 7 checklist: Testing

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] Created from template: test-plan
- [ ] Created from template: test-case
- [ ] Created from template: test-data-spec
- [ ] Created from template: test-execution-report
- [ ] Created from template: nfr-test-report
- [ ] Created from template: defect-report
- [ ] Created from template: uat-signoff
- [ ] Created from template: release-readiness-report
- [ ] `python3 scripts/validate_artifact.py docs/07-testing --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 7` passes
- [ ] Every acceptance criterion has a passing test
- [ ] No open Blocker defects
- [ ] QA lead sign-off and UAT sign-off recorded
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
- [ ] UAT script covers every user-facing story (scenarios cite REQ S-N AC-n); every scenario ran; every Fail has a defect report
