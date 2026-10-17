# Phase 2 checklist: Requirements Analysis

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] `docs/02-requirements/epics.md` created (template `epic`); all epics as `## Epic E-N:` sections — no separate `EPC-NNN.md` files
- [ ] `docs/02-requirements/user-stories.md` created (template `user-story`); all stories as `## Story S-N:` sections — no separate `REQ-NNN.md` files
- [ ] `docs/02-requirements/nfrs.md` created (template `nfr`); all NFRs as `## NFR N-N:` sections — no separate `NFR-NNN.md` files
- [ ] `docs/02-requirements/business-rules.md` created (template `business-rule`); all rules as `## Rule B-N:` sections — no separate `BR-NNN.md` files
- [ ] `docs/02-requirements/backlog.md` created (template `backlog-entry`); all entries as `## Entry BL-N:` sections — no separate `BKL-NNN.md` files
- [ ] `docs/02-requirements/domain-glossary.md` created (template `domain-glossary`, id GLO)
- [ ] `python3 scripts/validate_artifact.py docs/02-requirements --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Domain glossary (GLO) Approved; `python3 scripts/glossary_check.py check` passes
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 2` passes
- [ ] Every brief goal (BRF G-n) covered by an epic with an in-scope story, or out of scope by a DEC-NNN (`python3 scripts/traceability.py check --phase 2` passes)
- [ ] NFRs have measurable targets
- [ ] Stories, NFRs, and backlog Approved by the product owner / BA
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
