# Phase 0 checklist: Methodology Setup

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] `input-readiness-checklist.md` created in `docs/00-setup/` (template `input-readiness-checklist`; one file only, no `IRC-NNN.md`)
- [ ] `python3 scripts/validate_artifact.py docs/00-setup --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] project.md filled (approvers, capacity, SLA)
- [ ] Branch protection and required checks configured on the Git platform (human action)
- [ ] Readiness checklist for Phase 1 approved by the tech lead
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
