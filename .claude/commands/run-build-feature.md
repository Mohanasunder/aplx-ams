---
description: Run Phase 6 for one feature on its own branch (tests first, test approval, build, gates, AI pre-review, validation summary, human review)
argument-hint: FEAT-NNN
---

You are the **Orchestrator**. Run **Phase 6: Build** for the feature in `$ARGUMENTS`, following `.ai/standards/phase-loop.md` and `.ai/standards/branching-standard.md`.

## 1. Entry
- Read `docs/05-build-plan/feature-NNN-*/` (plan.md, tasks.md, acceptance.md, status.md). All three plan files must be `Approved`; confirm that a human selected this feature and that dependencies are Merged.
- Run the entry interview (`phase-intake` subagent, you ask the human) only for gaps: environment access, open questions, anything the plan leaves undecided. Do not re-ask what the plan answers. Have the Phase Input Brief approved.
- Run `python3 scripts/spec_impact.py check FEAT-NNN`. If it fails, stop: the feature cites a spec version that is outdated or being changed (living spec rule in `.ai/standards/phase-loop.md`).
- Run `python3 scripts/context_pack.py check FEAT-NNN`. If it fails, stop: the plan's Context Pack goes back to Phase 5.
- Run `python3 scripts/check_feature_size.py size FEAT-NNN`. If it fails, stop: the plan goes back to Phase 5 to be split.
- Check `.ai/standards/automated-gates.md`: every gate must have a command. If not, stop and raise an open question to the tech lead.

**Task 0 (FEAT-000)** runs first through this same loop; every other feature depends on it, so `/create-feature-branch` refuses them until it is Merged. Its tests are smoke tests for each criterion (the app starts and its health check answers; each gate command runs). Besides the builders, invoke `devops-engineer` for the CI files in its plan. It is done only when every gate in `.ai/standards/automated-gates.md` has a real command that runs green on the skeleton in `.github/workflows/ci.yml` (`check_feature_size.py task0` checks this after merge). Corrections to gate commands found while wiring them are made in `automated-gates.md` within Task 0. After Task 0 merges, run `python3 scripts/build_charter.py build` so the charter's Commands section has the real commands.

## 2. Branch
- Run `/create-feature-branch FEAT-NNN` (script checks preconditions). You must be on `feature/FEAT-NNN-slug` for everything below. Never commit to `main`.

## 3. Tests first (no implementation code yet)
Builder order for 3 and 5: `database-builder` -> `backend-builder` -> `frontend-builder` -> `integration-builder` (only if the plan has integration work). Pass each the plan folder, `FEAT-NNN-ACC`, the output of `python3 scripts/context_pack.py render FEAT-NNN` (inline; not the full contract or design documents), the standards, and the branch name. If a builder reports the pack lacks something, treat it as a plan gap: fix the plan's Context Pack upstream, re-approve, re-render.
- Invoke each builder in **Mode A: tests first**. Each writes failing tests for every acceptance criterion its layer serves, creates only empty stubs, confirms the red run, commits `FEAT-NNN: tests (<layer>)`, and returns its criterion-to-test map.
- Invoke `documentation-writer` to compile `docs/06-build/FEAT-NNN-TESTS.md` (template `feature-test-set`) from the builders' returns, with the test commit SHA.
- Run `/validate 6 docs/06-build/FEAT-NNN-TESTS.md`. A criterion with no test is non-overridable: send back.

## 4. Test approval (human gate, before any implementation)
- Show the human the criteria-to-tests map, the test diff (`git diff main...HEAD -- <test files>`), and the red run evidence. Ask: do these tests express the acceptance criteria, including edge cases and error paths?
- The approver depends on the risk tier (`.ai/standards/review-and-approval.md`, "Test set approval"). Record the decision with `/approve docs/06-build/FEAT-NNN-TESTS.md`.
- Reject or request changes: route the comments to the builder(s) in Mode A, re-validate, and ask again. If the criteria themselves are wrong, fix `FEAT-NNN-ACC` upstream first.
- Do not start step 5 until `FEAT-NNN-TESTS` is `Approved`. From here the listed test files are locked: the `guard-tests.py` hook blocks agent edits, and `scripts/locked_tests.py check` fails CI if they change.

## 5. Implement (one subagent at a time, in plan order)
Invoke each builder in **Mode B: implement**, also passing the approved `FEAT-NNN-TESTS`. Each writes code until the approved tests pass, commits small with `FEAT-NNN:` in the message, and ticks `tasks.md`. Builders never edit, skip, or weaken a locked test.
- If a builder says an approved test is wrong: stop, show the human the test, the reason, and the proposed change. Only the human can unlock it: `/approve docs/06-build/FEAT-NNN-TESTS.md` with **Reject** and the reason (recorded in the approval log). Then the builder revises the test in Mode A, `FEAT-NNN-TESTS` gets a new version and Test Commit, and steps 3 (validate) and 4 (approve) repeat. Never work around a locked test (skip markers, renamed copies, weakened assertions elsewhere).
- Builders change only the files in plan.md's Files To Create Or Modify. If the work needs another file, the builder stops and reports it; never widen scope. Treat it as a plan gap.
- If a builder reports a plan, contract, or design gap or a spec conflict, stop: raise it with the human and run the living spec rule (`.ai/standards/phase-loop.md`): impact, SCR, revise and re-approve upstream, then regenerate. Never patch code around it.

## 6. Automated gates
Run every command in `.ai/standards/automated-gates.md` and the artifact validation. Gate failures (tests, SAST, dependency, secrets) go back to the builders without human involvement and are **non-overridable**.

## 7. Independent review inputs
- `documentation-writer`: updates docs and appends a `## PR FEAT-NNN:` section to `docs/06-build/pr-descriptions.md` (template `pr-description`, collection file), including the change summary: Requirements Covered (each criterion with its passing test), Known Gaps, Deviations From Plan, and Blockers. Run `python3 scripts/pr_summary.py check FEAT-NNN`; Blockers must be 'None' before human review.
- Pass `ai-code-reviewer` the rendered Context Pack, the plan folder, the approved test set, and the diff.
- `security-scanner` and `ai-code-reviewer` (read-only): you save their reports by appending a `## AIR FEAT-NNN:` section to `docs/06-build/ai-pre-review-reports.md` and a `## SSR FEAT-NNN:` section to `docs/06-build/security-scan-reports.md` (templates `ai-pre-review-report`, `security-scan-report`, collection files). Create each file from the template via `scripts/new_artifact.py` if it does not yet exist.
- Append every Major or Blocker finding from the AI pre-review and the checker to `docs/logs/review-feedback-log.md` (date, FEAT-NNN, source, category, severity, issue, reviewer).
- Run `/validate 6 docs/06-build/pr-descriptions.md docs/06-build/ai-pre-review-reports.md docs/06-build/security-scan-reports.md`. Show the validation summary; on Fail the user decides (non-overridable findings: only send back).

## 8. Human review
- Push the branch if allowed and ensure the draft PR is marked ready; set status.md State to `In review` and the PR link.
- Tell the reviewer the tier's **review depth** (Deep, Standard, or Light) and its checklist from `.ai/standards/review-and-approval.md`; `/approve` will ask them to confirm it.
- Tell the reviewer what to review (see the PR reviewer checklist in `.ai/standards/review-and-approval.md`): run or preview the feature, check every acceptance criterion, plan adherence, security paths.
- Append each human comment that requests a change to `docs/logs/review-feedback-log.md` with a category (ask the reviewer to confirm the category if unclear).
- Route feedback: **request changes** -> back to the builders with precise comments; **reject** -> the plan or design is wrong, fix upstream, regenerate.
- High risk tier: two approvers including the tech lead; Critical: tech lead and release manager. Record each with `/approve`.

## 9. After approval
You never merge. A human or the platform merges (squash or rebase, message referencing FEAT, REQ, PR IDs). After the merge: update status.md State to `Merged`, run the `traceability` subagent, and run `python3 scripts/learned_rules.py recurring`. For each recurring category: invoke `standards-author` to append a `## LRN L-N:` section to `docs/logs/learned-rules.md`, run `/validate docs/logs/learned-rules.md`, ask the tech lead to `/approve docs/logs/learned-rules.md --sub-id L-N`, then run `python3 scripts/learned_rules.py build` and `python3 scripts/build_charter.py build` so later builders load it. Then ask the human to pick the next feature (respect review capacity).
