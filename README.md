# AI-Enabled SDLC: Claude Code Agent Project

A Claude Code project for full-stack delivery where **a human or AI provides input, AI agents build, and humans review and approve**. Humans do not write code or artifacts; they answer questions, give feedback, and approve at every gate.

## Quick start

1. Install Claude Code and open this folder: `cd ai-sdlc-agent-project && claude`. Run `git init` (and create a `main` branch with a first commit) if this is not yet a repository.
2. `/sdlc-init` to set project details, approvers, and capacity. Then do the human-only setup it lists (branch protection, CI secrets, scoped agent credentials).
3. Drop discovery material (notes, transcripts, documents) into `docs/01-discovery/inputs/`, then run the phases in order:
   `/run-discovery` -> `/run-requirements` -> `/run-architecture` -> `/run-design` -> `/run-build-planning` -> for each feature `/run-build-feature FEAT-NNN` -> `/run-testing` -> `/run-deployment` -> `/run-operate`.
4. Approve each artifact with `/approve <path>` after reviewing it. `/sdlc-status` shows where things stand.

## What is in the box

| Path | Contents |
| --- | --- |
| `CLAUDE.md` | Operating rules loaded in every session; the main session is the Orchestrator |
| `.claude/agents/` | 39 subagents: phase producers, builders, checkers, intake, traceability, governance |
| `.claude/commands/` | Slash commands for each phase, `/validate`, `/approve`, `/sdlc-status`, branch creation |
| `.claude/settings.json` | Permissions (deny merging, force pushes, secrets, edits to templates/agents/scripts) and a git guard hook |
| `.claude/hooks/guard-git.py` | Blocks commits or pushes on `main`, merges (except syncing `main` into a feature branch), force pushes, committing secrets |
| `.ai/templates/` | 66 artifact templates (front matter, fixed sections, quality checklist, approval record) |
| `.ai/standards/` | Phase loop, IDs, glossary, branching, review and approval, checker and fail decision, coding standards, gates |
| `.ai/checker-rules/` | Per-phase checker focus and non-overridable checks |
| `.ai/examples/` | Filled-in example artifacts |
| `docs/NN-*/` | Per-phase artifact folders with `README.md` and `checklist.md`; `docs/logs/` for questions, assumptions, approvals, fail decisions, traceability |
| `scripts/` | `new_artifact.py`, `validate_artifact.py`, `fm.py`, `log_approval.py`, branch scripts |
| `src/`, `tests/`, `infra/` | Where builders put code |

## The phase loop (every phase)

Entry interview (the `phase-intake` subagent finds the gaps; the Orchestrator asks you) -> Phase Input Brief approved -> producer subagents build from templates -> `validate_artifact.py` plus the `checker` subagent -> **validation summary shown to you** -> on a Fail **you decide**: send back, send back with instructions, or proceed to human review (reason recorded; non-overridable findings can only be sent back) -> human review -> `/approve`.

## Design notes and limits

- **Subagents cannot nest or interview you**, so the main session orchestrates: it delegates by name, asks the questions, saves the checker's report, and shows results. The checker, AI code reviewer, and security scanner are read-only subagents that return reports.
- **Agents cannot change templates, charters, scripts, or settings** (denied in `settings.json`). Project-specific details (stack, gate commands, coverage targets) are filled by the `standards-author` into `.ai/standards/` in Phase 4, which every builder, tester, and reviewer reads.
- **Approvals are human-only:** `scripts/log_approval.py` is on the "ask" list, refuses approval while validation is Pending or Fail, and is the only thing that sets `status: Approved`. `scripts/fm.py` refuses to set Approved or Rejected.
- **Humans must configure the Git platform:** branch protection, required checks, CODEOWNERS review, and scoped agent credentials cannot be done by the agents.
- Agents prepare deployment (IaC, pipelines, runbook) but never apply it; `terraform apply` and `kubectl apply` require your confirmation.
- Permission rule syntax and slash-command frontmatter follow Claude Code's documented formats at the time of writing; check `/permissions`, `/agents`, and the current docs if a setting is ignored.

## Scripts

```bash
python3 scripts/new_artifact.py --template user-story --title "..." --author requirements-analyst
python3 scripts/validate_artifact.py docs --check-links
python3 scripts/fm.py get docs/02-requirements/REQ-001.md validation
python3 scripts/log_approval.py --artifact <path> --decision Approve --approver "Name" --role "Role"   # human-confirmed
bash scripts/create-feature-branch.sh FEAT-004 [--push]
bash scripts/check-branch-name.sh feature/FEAT-004-ticket-triage
```
