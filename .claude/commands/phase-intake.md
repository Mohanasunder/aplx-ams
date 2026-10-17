---
description: Run only the entry interview for a phase (produces the approved Phase Input Brief)
argument-hint: <phase number 1-9> [notes]
---

You are the **Orchestrator**. Run **only the entry interview** (Step 2 of `.ai/standards/phase-loop.md`) for the phase in `$ARGUMENTS`.

1. Read the phase's command file (`.claude/commands/`) and its `docs/NN-*/README.md` for the inputs, templates, producers, and approver. Phase 6 uses the feature plan folder as its input; ask which FEAT-ID.
2. Invoke the `phase-intake` subagent for the gap analysis. Ask the human its questions yourself with AskUserQuestion (blockers first, up to 4 per call, with a "Defer" option). Re-invoke it with the answers; save the three artifacts it returns using `--out` with fixed friendly filenames in the phase folder:
   - `docs/0N-<slug>/phase-input-brief.md`
   - `docs/0N-<slug>/interview-record.md`
   - `docs/0N-<slug>/input-readiness-checklist.md`
   Never save these as `PIB-NNN.md`, `INT-NNN.md`, or `IRC-NNN.md`.
3. Validate the drafted artifacts (Step 4 of the loop), show the validation summary (saved as `docs/validation/phase-N-run-1.md`), then ask the human to approve the brief; record the approval with `/approve`.
4. Report the readiness verdict and the next command to run.
