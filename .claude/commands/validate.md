---
description: Validate artifacts (script + checker), show the validation summary, and handle a Fail decision
argument-hint: <phase number> <paths or folder>
---

You are the **Orchestrator**. Validate the artifacts in `$ARGUMENTS` (first token: phase number; rest: paths or folders).

1. Run `python3 scripts/validate_artifact.py <paths> --check-links`.
2. Invoke the `checker` subagent with the phase number and paths (it applies `.ai/checker-rules/phase-N.md`).
3. Save its report as `docs/validation/phase-N-run-M.md` (template `validation-report`, via `python3 scripts/new_artifact.py --template validation-report --title "Phase N validation run M" --author checker --out docs/validation/phase-N-run-M.md`). M is the run count for this phase (check existing files in `docs/validation/` and increment). Set each artifact's `validation` value with `python3 scripts/fm.py set <file> validation "<verdict>"`.
4. **Always show the validation summary** in the format of `.ai/standards/checker-and-fail-decision.md`.
5. If the verdict is **Fail**, ask the user with AskUserQuestion: A) Send back to producer, B) Proceed to human review (reason required; Blockers need the phase approver; non-overridable findings cannot be accepted), C) Send back with modified instructions. Execute only the chosen option. For B, set `validation` to `Proceeded on Fail` and invoke `governance-audit` to log it in `docs/logs/fail-decisions-log.md`.
6. Respect `loop_limit_failed_validations` in `project.md`.
