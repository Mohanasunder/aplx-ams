# Checker rules: Phase 5 (Build Planning)

Applies after the producer(s) in `docs/05-build-plan` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Every design element is assigned to a feature
- No circular dependencies
- Task 0 (`FEAT-000`, Type: Enabling) builds the walking skeleton: scaffold, deployable empty app with a health check, test harness, lint, type check, SAST, dependency and secrets scans, wired into CI; every other feature depends on it
- Each Feature covers at least one story criterion (REQ-); each Enabling feature links to NFR-, TST-, or STD- IDs instead
- Each feature is a vertical slice (testable behavior end to end), not a single layer
- Each feature fits one builder session: `python3 scripts/check_feature_size.py size` passes (criteria and source file limits in project.md, 'Open design decisions: None', Out Of Scope filled)
- Expected test runtime in Size Check is minutes, not hours
- Each plan has a Context Pack naming exact sections (`ID vX.Y § section`), not whole design documents; `python3 scripts/context_pack.py check FEAT-NNN` passes
- The Context Pack covers every contract, schema, UI, and ADR section the feature's acceptance criteria need (judgment: would a builder have to open anything else?)
- Every acceptance criterion (REQ S-N AC-n) belongs to exactly one feature; any story split across features is listed for human confirmation (`python3 scripts/traceability.py check --phase 5` passes)
- Each plan has acceptance criteria and a Definition of Done
- A Fix feature (`Type: Fix DEF D-N`, planned in Phase 7 or 9) cites an existing defect entry classified Code, copies the failed criteria unchanged, lists only the files the fix needs, depends on the feature that owns the criteria, and starts its Test Plan with a regression test that reproduces the defect; a fix that needs a criterion, design, or contract changed is a Spec defect instead
- Wave plan fits builder and review capacity
- Wave plan is collision-free: every feature in one wave, dependencies in earlier waves, no file shared within a wave, and a feature that changes a Shared Path (`.ai/standards/coding-standards.md`) alone in its wave (`python3 scripts/check_feature_size.py waves` passes)

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- Task 0 missing, not Enabling, or a feature that does not depend on it (`check_feature_size.py task0` fails)
- A feature over the acceptance criteria or source file limit (`check_feature_size.py size` fails): split it
- A feature plan with an open design decision: send it back to Phase 4 as an open question
- A Context Pack entry that does not resolve, cites an outdated or unapproved version, or a pack over max_context_pack_lines (`context_pack.py check` fails)
- A plan, acceptance file, or test set citing an outdated or unapproved spec version (`spec_impact.py check FEAT-NNN` fails)
- A feature plan listing a production configuration file (Production Configuration in `.ai/standards/coding-standards.md`; `check_feature_size.py size` fails): production configuration is drafted only in Phase 8
- A wave with two features changing the same file, or a feature that changes a Shared Path sharing its wave (`check_feature_size.py waves` fails)
- A story criterion in no feature or in two, or a feature criterion that is not in an Approved, in-scope story (`traceability.py check --phase 5` fails)

## Who decides on a Fail

Tech lead (see `.ai/standards/review-and-approval.md`).
