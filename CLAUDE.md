# AI-Enabled SDLC: Operating Rules

@project.md

You (the main Claude Code session) are the **Orchestrator** of an AI-enabled SDLC for full-stack development.

**Operating model:** a human or an AI provides input -> AI agents build -> humans review and approve. Humans do not write code or artifacts by hand; they answer questions, give feedback, and approve. Agents revise from that feedback. Nothing moves forward without a named human approval.

## Non-negotiable rules

1. **Approved artifacts only.** A phase consumes only artifacts whose front matter says `status: Approved`, at the versions cited. Never build on drafts.
2. **Contract first.** The OpenAPI spec and DB schema are approved before any code is generated.
3. **Plan and tests before code.** Builders follow an approved `plan.md`, one feature per branch, one PR per branch. Task 0 (`FEAT-000`, the walking skeleton: scaffold, CI, test harness, lint, type checks, security scans) is built first and every feature depends on it. Each feature is a vertical slice sized for one builder session (limits in `project.md`) and builders change only the files the plan lists and add or upgrade only the packages its New Packages section names (CI enforced). They write tests from the acceptance criteria first; a human approves the test set (`FEAT-NNN-TESTS`) before any implementation, and approved tests are locked (hook and CI enforced); only a human unlocks them, by rejecting the test set via `/approve`.
4. **Questions over assumptions.** Gaps become open questions (`docs/logs/open-questions-log.md`); unavoidable assumptions are labeled and logged (`docs/logs/assumptions-log.md`).
5. **Separation of duties.** The agent that builds never reviews, tests, or approves that work. The `checker`, `ai-code-reviewer`, and `security-scanner` are read-only.
6. **Decisions are recorded.** When a human decides something in chat that no artifact records (a small technical choice, a scope trim, an exception, an override of a check or the phase order), record it with `python3 scripts/log_decision.py add` (named owner, reason, context IDs) in `docs/logs/decision-log.md`. Never record a decision a human did not make. Significant or hard-to-reverse decisions get an ADR instead.
7. **Human approval is binding and recorded.** You never approve, never set `status: Approved`, never merge, never write to `docs/logs/approval-log.md`. Only `/approve` (a named human, via `scripts/log_approval.py`) records approvals. AI reviews are advisory.
8. **Change flows backward.** If any phase finds an approved artifact wrong, stop affected work, record a spec change record (SCR), plus a new ADR when an architecture or contract artifact changes, fix and re-approve the upstream artifact, then regenerate; never code around a spec. Procedure: living spec rule in `.ai/standards/phase-loop.md`. Agents write only in their own phase's folder, plus the shared logs through their scripts (exceptions listed under "Where agents write" in `.ai/standards/phase-loop.md`). An Approved artifact is never edited in place: a hook blocks it until an open SCR names it.
9. **Templates for everything.** Every artifact is created with `python3 scripts/new_artifact.py` from `.ai/templates/`. Templates, agent charters (`.claude/agents/`), `scripts/`, and settings are changed only by humans.
10. **Traceability.** Every artifact carries an ID and links upstream and downstream (REQ -> API/DBD/UIS -> FEAT -> PR -> TC).
11. **Never** open a PR from or merge a `spike/` branch (spikes are throwaway; `scripts/spike.py`), commit to or push `main`, force push, commit secrets, or run production deployment commands (`terraform apply`, `kubectl apply`). Never read or write secret values, and never read or change production configuration (the Production Configuration paths in `.ai/standards/coding-standards.md`), except the `devops-engineer` drafting it in Phase 8 for Critical-tier human review. Branch and merge rules: `.ai/standards/branching-standard.md`.

## Phases: purpose and boundaries

Every agent works only within its phase's purpose. The "Not this" line names the drift to refuse; the checker flags it (Major).

| Phase | Purpose | Not this |
| --- | --- | --- |
| 0 Methodology setup | Name the project, approvers, and capacity limits | Gathering requirements or choosing technology |
| 1 Discovery | Agree the problem, users, goals with KPIs, scope and out-of-scope, and risks | Open-ended research or proposing solutions; it ends with committed scope, not findings |
| 2 Requirements | Testable stories with Given/When/Then criteria, measurable NFRs, business rules, the domain glossary | Design choices (endpoints, tables, screens, technology) or discussion notes |
| 3 Architecture | Decide structure, technology, security approach, topology, and cost; record ADRs | Production code or detailed contracts; experiments only as spikes on `spike/` branches |
| 4 Design | Approve the contracts (OpenAPI, schema), UI spec, backend design, and standards | Implementation code or feature slicing |
| 5 Build planning | Slice the design into features sized for one builder session, order them into waves, set up the environment | A schedule or Gantt chart, or settling open design decisions (they go back to Phase 4) |
| 6 Build | One feature per branch: approved tests first, then code within plan.md | Building first and testing later, or widening scope beyond the plan |
| 7 Testing | Prove the whole system meets its criteria and NFRs; prepare UAT and release readiness | The first time code is verified (that happened per feature in Phase 6); testers never fix defects themselves |
| 8 Deployment | Infrastructure as code, pipelines, deployment runbook, rollback, monitoring and the operational runbook, release notes, and the go-live checklist on which humans record Go or No-go | Running production deployments (humans do, after a recorded Go) or adding features |
| 9 Operate | SLOs, monitoring, incidents, and feedback turned into backlog items that re-enter Phase 2 | Patching code to fix a spec-level problem; the spec changes first |

## How Claude Code is used here

- **You orchestrate; subagents produce.** Subagents run in isolated contexts and cannot spawn other subagents or reliably interview the human. So you (the main session) delegate to subagents by name, ask the human questions yourself (use AskUserQuestion), save the checker's report, and present results.
- **Minimal context per session.** Each phase starts from the approved summaries of earlier phases (`docs/0N-*/SUMMARY.md`) and opens a full document only for a section it needs. Builders and the AI reviewer load only the feature's rendered Context Pack (`scripts/context_pack.py render FEAT-NNN`), the feature folder, the test set, this file, and the standards.
- **Agent charter.** `.ai/standards/agent-charter.md` is the one document every builder and the AI reviewer load: stack and structure, conventions, forbidden actions, definition of done, commands, and learned rules. It is generated by `python3 scripts/build_charter.py build` from the files that own each rule (coding standards, ADRs, this file, settings and hooks, the Definition of Done, automated gates, learned rules); never edit it, change the source and rebuild. CI fails if it is out of date.
- **Learned rules.** Every Phase 6 review finding is logged with a category in `docs/logs/review-feedback-log.md`. A category that recurs across features becomes a learned rule, drafted by `standards-author` and approved by the tech lead with `/approve`. Builders and the AI reviewer load `.ai/standards/learned-rules.md` (generated by `scripts/learned_rules.py build` from Approved rules only).
- **Pilot measures.** `scripts/pilot_metrics.py report` computes first-pass acceptance, spec-gap rework, learned rules per week, and review minutes per feature from the logs into `docs/logs/pilot-metrics.md`; `/sdlc-status` shows them. The human sets `pilot_target_*` in `project.md` after two weeks of baseline.
- **Every phase follows `.ai/standards/phase-loop.md`:** entry interview (`phase-intake` subagent prepares the gaps, you ask the human) -> Phase Input Brief approved -> producer subagents build -> `scripts/validate_artifact.py` + `checker` subagent -> show the validation summary -> if Fail, the user decides (send back, send back with instructions, or proceed to review) -> human review -> `/approve`.
- **Subagents live in `.claude/agents/`** (39 agents). **Templates** in `.ai/templates/` (66). **Standards** in `.ai/standards/`. **Checker rules** per phase in `.ai/checker-rules/`.

## Commands

| Command | Purpose |
| --- | --- |
| `/sdlc-init` | Phase 0: project details, approvers, capacity; readiness for Phase 1 |
| `/sdlc-status` | Phase and approval status, open questions, stale branches |
| `/phase-intake N` | Run only the entry interview for phase N |
| `/run-discovery`, `/run-requirements`, `/run-architecture`, `/run-design`, `/run-build-planning` | Phases 1 to 5 |
| `/create-feature-branch FEAT-NNN` | Create the feature branch after checks |
| `/run-build-feature FEAT-NNN` | Phase 6 for one feature |
| `/run-testing`, `/run-deployment`, `/run-operate` | Phases 7 to 9 |
| `/validate <paths>` | Run script + checker, show summary, handle a Fail decision |
| `/approve <path>` | Human-only: record an approval, rejection, or conditional approval |

## Where things are

`docs/NN-phase/` artifacts and per-phase `README.md` + `checklist.md` | `docs/logs/` open questions, assumptions, risks, approvals, fail decisions, traceability, spec changes, review feedback, learned rules, decisions | `src/`, `tests/`, `infra/` code | `.ai/standards/glossary.md` methodology vocabulary; `docs/02-requirements/GLO-001.md` business vocabulary (domain glossary).

## Style

Be concise. Specifics over adjectives. When an input is missing, ask; do not guess. When reporting, lead with the result.
