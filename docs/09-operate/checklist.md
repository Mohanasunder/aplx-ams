# Phase 9 checklist: Operate and Feedback

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] Created from template: monitoring-spec
- [ ] Created from template: incident-report
- [ ] Created from template: post-mortem
- [ ] Created from template: feedback-summary
- [ ] Created from template: improvement-backlog-item
- [ ] `python3 scripts/validate_artifact.py docs/09-operate --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 9` passes
- [ ] Alerts map to SLOs and have runbooks
- [ ] Improvement backlog prioritized by the product owner
- [ ] Feedback and incident log built; nothing 'Pending triage'; every improvement item Approved or Rejected (`python3 scripts/feedback_log.py check --gate` passes)
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
