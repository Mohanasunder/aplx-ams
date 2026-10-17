# Phase 1 checklist: Business Discovery

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] `business-brief.md` created (template `business-brief`)
- [ ] `personas.md` created (template `persona`; all personas as P-1, P-2, … sections)
- [ ] `scope-statement.md` created (template `scope-statement`)
- [ ] `process-maps.md` created (template `as-is-process-map`; all processes as M-1, M-2, … sections)
- [ ] `risks.md` created (template `risk-register-entry`; all Phase 1 risks as R-1, R-2, … sections)
- [ ] `research-summary.md` created (template `research-summary`; only if research-analyst was invoked)
- [ ] No duplicate or extra files for the same deliverable type exist in docs/01-discovery/
- [ ] Each risk in `risks.md` is recorded in `docs/logs/risk-register.md` as `RSK R-N`
- [ ] `python3 scripts/validate_artifact.py docs/01-discovery --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 1` passes
- [ ] All Blocker open questions resolved
- [ ] `business-brief.md`, `personas.md`, `scope-statement.md`, `process-maps.md`, and `risks.md` Approved by the business owner / BA
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
