# Checker rules: Phase 6 (Build)

Applies after the producer(s) in `docs/06-build` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

Test set (`FEAT-NNN-TESTS`, checked before implementation):

- Every acceptance criterion in `FEAT-NNN-ACC` maps to at least one test; edge cases and error paths in the criteria are covered
- Tests assert observable behavior from the contract, UI spec, or permission matrix, not only that code runs
- Red run evidence shows each new test failing for the missing behavior (not syntax, import, or setup errors)
- The Test Commit SHA exists on the feature branch and contains only test files and empty stubs

Code and PR (checked after implementation):

- An Approved `FEAT-NNN-TESTS` exists, and its version is the one cited in the PR description
- Locked tests unchanged: `python3 scripts/locked_tests.py check` passes
- No workarounds for locked tests: no skip or xfail markers, renamed copies, or test-runner config that excludes them
- The Context Pack still resolves (`python3 scripts/context_pack.py check` passes); builder summaries report no document read outside the pack, or report it as a plan gap
- The PR description states the tier and review depth matching the plan; a Light claim only for docs, UI copy and layout, or refactors covered by existing tests (Major if the diff touches logic, data, auth, or contracts)
- Code follows every applicable rule in `.ai/standards/learned-rules.md` (a violation is Major); the AI pre-review has a Learned Rules Check and a category on every finding
- Code matches plan and contract; nothing outside plan scope: `python3 scripts/check_feature_size.py scope` passes
- Every package added or upgraded in a manifest is named, at that version, in the plan's New Packages: `python3 scripts/check_feature_size.py packages` passes
- Lint, types, unit tests, SAST, dependency and secrets scans clean
- For Task 0 (FEAT-000): every gate in `automated-gates.md` has a real command, each runs green in CI on the skeleton, and the app starts and answers its health check
- Coverage threshold met
- Migrations reversible and apply on top of current main
- Docs and status updated
- Change summary accurate: Requirements Covered lists every criterion with a test from the approved test set; Known Gaps and Deviations From Plan match the diff and builder summaries; Blockers 'None' (`python3 scripts/pr_summary.py check` passes)

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- Secrets found in code or history
- Failing security scan
- Failing tests
- An acceptance criterion with no test in the test set
- Implementation commits before the test set was Approved
- Locked test files changed after approval without a re-approved test set version, or `scripts/locked_tests.py check` fails
- A locked test skipped, excluded, or worked around
- A change summary that omits a criterion, hides a deviation (says 'None' while files changed outside the plan), or lists open Blockers (`pr_summary.py check` fails)
- `.ai/standards/learned-rules.md` does not match the Approved learned rules (`learned_rules.py check` fails)
- The feature cites an outdated or unapproved spec version (`spec_impact.py check` fails), or a change to an approved spec has no Approved spec change record (`spec_impact.py records` fails)
- Code that works around the approved spec instead of an SCR changing it
- Files changed outside the plan's Files To Create Or Modify (`check_feature_size.py scope` fails): send back, or fix the plan upstream and re-approve it
- A package added or upgraded that the plan's New Packages does not name at that version (`check_feature_size.py packages` fails): send back, or revise the plan through an SCR and re-approve it

## Who decides on a Fail

Human developer reviewer (see `.ai/standards/review-and-approval.md`).
