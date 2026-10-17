# Glossary

One vocabulary for all agents and reviewers. Humans extend this file; agents propose additions in their summaries. This file holds **methodology** terms; the product's **business** terms are in the domain glossary (`docs/02-requirements/domain-glossary.md`), which the agent charter also lists.

| Term | Meaning |
| --- | --- |
| Artifact | A versioned, templated deliverable with front matter, produced by an agent and approved by a human |
| Orchestrator | The main Claude Code session that runs the phase loop and talks to the human |
| Producer | A subagent that builds artifacts or code |
| Checker | A read-only subagent that validates artifacts independently of the producer |
| Phase Input Brief | The approved, consolidated inputs for one phase (PIB) |
| Gate | A human approval point; recorded in `docs/logs/approval-log.md` |
| Epic | A group of related stories delivering one capability |
| Story | A single requirement (REQ S-N) with Given/When/Then acceptance criteria |
| Feature | A vertical, buildable slice (FEAT-NNN) sized for one builder session: at most max_acceptance_criteria_per_feature criteria and max_source_files_per_feature source files (project.md), no open design decisions; one feature, one branch, one PR |
| Task 0 | FEAT-000, the first, Enabling feature: the walking skeleton (scaffold, deployable empty app, test harness, lint, type checks, security scans, all in CI); every feature depends on it |
| Go / no-go | The recorded decision to deploy one release tag to production: `/approve` on the go-live checklist by the release manager and the tech lead (Reject = No-go); verified by `scripts/go_live.py check` before deployment |
| Operational runbook | `OPR`: the single operational runbook file (`docs/08-deployment/operational-runbook.md`) covering how the running system is monitored, supported, and operated (alert responses, support, escalation by role, common operations, known issues); Approved before go-live, kept current in Phase 9 |
| Production configuration | Files holding production environment settings (the Production Configuration globs in `.ai/standards/coding-standards.md`). Builders never read or change them; only the `devops-engineer` drafts them in Phase 8, reviewed at Critical tier and applied by a human |
| Fix feature | A feature (`Type: Fix DEF D-N`) that fixes a Code defect: the failed criteria copied unchanged, a regression test approved first, a plan approved by the tech lead; it re-proves criteria another feature owns and is never a shortcut around planning (defect rule in `.ai/standards/phase-loop.md`) |
| Enabling feature | A feature that delivers no story (Type: Enabling); its criteria link to NFR-, TST-, or STD- IDs instead of REQ- |
| Review depth | How deeply the human reviews a PR: Deep (High, Critical), Standard, or Light (Standard tier, docs, copy, or covered refactors only); confirmed in `/approve` |
| Spike | SPK S-N: a time-boxed, human-approved experiment on a throwaway `spike/spk-S-N-slug` branch that answers one architecture or design question; all spikes are sections in `docs/03-architecture/spikes.md`; never merged; deleted once its ADR is approved |
| Pilot measures | First-pass acceptance, spec-gap rework, learned rules per week, and review minutes per feature; computed by `scripts/pilot_metrics.py` |
| Domain glossary | GLO: the product's business terms, each with one definition, a source, and the synonyms to avoid; produced in Phase 2, checked by `scripts/glossary_check.py`, listed in the agent charter |
| Agent charter | `.ai/standards/agent-charter.md`: the one document builders and the AI reviewer load (stack, conventions, forbidden actions, definition of done, commands, learned rules), generated from its source files by `scripts/build_charter.py` |
| Decision log | `docs/logs/decision-log.md`: DEC-NNN entries for decisions too small for an ADR and for overrides, each with a named human owner and reason; append-only, written by `scripts/log_decision.py` |
| Change summary | The Requirements Covered, Known Gaps, Deviations From Plan, and Blockers sections of a PR description; checked by `scripts/pr_summary.py` |
| Learned rule | `LRN L-N`: an imperative rule for agents (collection sub-ID in `docs/logs/learned-rules.md`), created when a review category recurs across features and approved by the tech lead; listed in `.ai/standards/learned-rules.md` |
| Review category | Kebab-case slug for the kind of mistake a review finding reports (for example `missing-authz-check`); logged in `docs/logs/review-feedback-log.md` |
| Phase summary | `SUM`, `docs/0N-*/SUMMARY.md`: half a page of decisions, constraints, open items, and the phase's document index; the next phase starts from it |
| Context pack | The exact sections (`ID vX.Y § section`) a feature's builders and reviewer load; in plan.md, rendered by `scripts/context_pack.py render FEAT-NNN` |
| Spec change record | `SCR S-N`: the record of a change to an approved artifact (collection sub-ID in `docs/logs/spec-changes.md`; `ID vOLD -> vNEW`, trigger, reason, impact, approval); listed in `docs/logs/spec-change-log.md` |
| Living spec rule | When an approved artifact is wrong: stop affected work, record an SCR, revise and re-approve the spec, then regenerate code; never code around the spec |
| Test set | The tests for one feature (FEAT-NNN-TESTS), written before implementation from its acceptance criteria and approved by a human; once Approved its test files are locked |
| Wave | A set of features that can be built in parallel |
| Contract | The OpenAPI spec and DB schema that all builders build against |
| NFR | Non-functional requirement with a measurable target |
| ADR | Architecture Decision Record |
| RTM | Requirements traceability matrix (`docs/logs/traceability-matrix.md`) |
| Definition of Done | The checklist every feature PR must meet |
| Risk tier | Standard, High, or Critical; sets the number of human approvers |
