# Phase 3 checklist: Solution Architecture

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] `docs/03-architecture/architecture-overview.md` created (template `architecture-overview`, id ARC) — no separate `ARC-NNN.md` files
- [ ] `docs/03-architecture/adrs.md` created (template `adr`); all decisions as `## ADR A-N:` sections — no separate `ADR-NNN.md` files
- [ ] `docs/03-architecture/technology-comparison.md` created (template `technology-comparison`, id TEC) — no separate `TEC-NNN.md` files
- [ ] `docs/03-architecture/threat-model.md` created (template `threat-model`, id THR) — no separate `THR-NNN.md` files
- [ ] `docs/03-architecture/deployment-topology.md` created (template `deployment-topology`, id TOP) — no separate `TOP-NNN.md` files
- [ ] `docs/03-architecture/cost-estimate.md` created (template `cost-estimate`, id CST) — no separate `CST-NNN.md` files
- [ ] `python3 scripts/validate_artifact.py docs/03-architecture --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] No open spikes: each spike's findings and ADR approved and its branch deleted (`python3 scripts/spike.py check` passes)
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 3` passes
- [ ] Every NFR mapped to an architectural answer
- [ ] Every significant decision has an ADR
- [ ] Architecture package Approved by the architect / tech lead
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
