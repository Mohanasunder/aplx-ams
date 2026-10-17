# Phase 4 checklist: Solution Design

## Entry
- [ ] Previous phase artifacts are Approved (or Phase 1 inputs are in place)
- [ ] Entry interview done; Phase Input Brief approved by a named human
- [ ] Open Blocker questions from earlier phases resolved or accepted as assumptions

## Work
- [ ] Producers ran in the order described in README.md
- [ ] `docs/04-design/database-design.md` created (template `database-design`, id DBD) — no separate `DBD-NNN.md` files
- [ ] `docs/04-design/api-spec.md` created (template `api-spec`, id API) — no separate `API-NNN.md` files
- [ ] `docs/04-design/openapi.yaml` created and valid OpenAPI
- [ ] `docs/04-design/backend-design.md` created (template `backend-design`, id BED) — no separate `BED-NNN.md` files
- [ ] `docs/04-design/ui-spec.md` created (template `ui-spec`, id UIS) — no separate `UIS-NNN.md` files
- [ ] `docs/04-design/permission-matrix.md` created (template `permission-matrix`, id PRM) — no separate `PRM-NNN.md` files
- [ ] `docs/04-design/coding-standards.md` created (template `coding-standards`, id STD) — no separate `STD-NNN.md` files
- [ ] `docs/04-design/test-strategy.md` created (template `test-strategy`, id TST) — no separate `TST-NNN.md` files
- [ ] `python3 scripts/validate_artifact.py docs/04-design --check-links` shows no Fail
- [ ] Checker validation summary shown to the user; Fail decision (if any) recorded
- [ ] Traceability matrix updated

## Exit
- [ ] Agent charter rebuilt and read by the tech lead (`python3 scripts/build_charter.py check` passes)
- [ ] Phase summary `SUMMARY.md` (template phase-summary) drafted, Approved, and `python3 scripts/context_pack.py summaries 4` passes
- [ ] Schema, API, and UI cross-consistent
- [ ] Every story has the endpoints and screens it needs
- [ ] Every page has a wireframe; every user-facing story has a user flow
- [ ] Design package Approved by the tech lead and UX
- [ ] Approvals recorded in `docs/logs/approval-log.md` (via `/approve`)
- [ ] `project.md` phase status updated
