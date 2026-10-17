# Checker rules: Phase 7 (Testing)

Applies after the producer(s) in `docs/07-testing` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Every acceptance criterion has at least one test
- Test cases cite their criteria in Linked Criteria as `REQ S-N AC-n`, one per line
- The traceability matrix is complete with no gaps: `python3 scripts/traceability.py check --phase 7` passes, and the matrix rows agree with `traceability.py report`
- Tests assert behavior, not trivial passes
- Test data contains no real personal data
- NFR tests have thresholds
- Security is reviewed against the threat model: the NFR test report's Threat Model Coverage has a row for every threat (THR T-n) with how its control was verified on the running system, the evidence, and a result: Verified, Failed (with its defect), or Not testable (with a risk the tech lead accepted, DEC-NNN)
- Defects classified with severity and owner
- UAT script (UAT sign-off Scenarios) drafted from the acceptance criteria: every user-facing story (story IDs in the approved UI spec's Pages And Routes) has at least one scenario citing its `REQ S-N AC-n`, covering the main path and an error path; the Coverage table lists every such story (Major if a story has no scenario)
- UAT results come only from participants: a scenario result with no tester, a Fail with no `DEF D-N`, or an Outcome of Accepted while a scenario is Not run or a Fail has no defect entry (Major)
- Every defect has Class, Route, and Status (defect rule, `.ai/standards/phase-loop.md`): a Code defect routes to a Fix feature that names it, a Spec defect to an SCR; a Fixed or Closed defect's Fix feature is Merged, and Closed means it passed in the newest execution report

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- Failing tests for Blocker or Major criteria
- A threat with no Threat Model Coverage row, a Failed control with no defect report, or a Not testable control whose residual risk the tech lead has not accepted (`traceability.py check --phase 7` fails)
- Code changed for a defect outside an approved Fix feature (a commit or PR citing `DEF D-N` on a branch whose feature is not `Type: Fix DEF D-N`)
- A traceability gap at the gate (`traceability.py check --phase 7` fails): a story criterion with no feature or in two, a feature not Merged or without an Approved test set, a criterion missing from its test set, a criterion with no test case, or a linked test case failing in the newest test execution report

## Who decides on a Fail

QA lead (see `.ai/standards/review-and-approval.md`).
