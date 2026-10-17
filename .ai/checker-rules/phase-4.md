# Checker rules: Phase 4 (Solution Design)

Applies after the producer(s) in `docs/04-design` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Each deliverable exists as exactly one file with its friendly name; no extra `DBD-NNN.md`, `API-NNN.md`, `BED-NNN.md`, `UIS-NNN.md`, `PRM-NNN.md`, `STD-NNN.md`, or `TST-NNN.md` files (Blocker if extra files exist)
- Schema, API, and UI agree with each other and with the requirements
- OpenAPI validates; error model shared
- Every story has endpoints and screens where needed
- Every user-facing story has a user flow in the UI spec (User Flows, headed with its story ID) that covers the error paths in its acceptance criteria (Major if missing)
- Every page in Pages And Routes has a wireframe (Wireframes, headed with its route) showing loading, empty, and error states; every field shown exists in the API spec (Major if missing; Major if a field is not in the API spec)
- Schema normalized, indexes match query patterns
- Permission matrix complete and matches the auth design
- Table, column, API path and field, and UI label names use the domain glossary terms (`python3 scripts/glossary_check.py check` scans the contract files)
- Agent charter rebuilt (`python3 scripts/build_charter.py check` passes); its stack, conventions, and commands sections are filled from the approved standards and ADRs, not 'not set yet'

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- None defined for this phase (all findings can be accepted by the phase decider with a recorded reason, except Blockers that need the phase approver)

## Who decides on a Fail

Tech lead + UX (see `.ai/standards/review-and-approval.md`).
