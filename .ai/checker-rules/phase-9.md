# Checker rules: Phase 9 (Operate and Feedback)

Applies after the producer(s) in `docs/09-operate` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Alerts map to SLOs
- The operational runbook (OPR, from Phase 8) has a response for each alert, including alerts added after incidents; revisions of the Approved monitoring spec or runbook have an SCR
- Incident reports have timeline, impact, cause, actions
- Backlog items cite evidence by ID (`INC I-N`, `PMT PM-N`, `FBK F-N`, or `DEF D-N`), so the feedback and incident log links them (Major if an item cites no ID)
- `docs/logs/feedback-incident-log.md` is current (`python3 scripts/feedback_log.py check`); no item left 'Pending triage' at the gate

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- None defined for this phase (all findings can be accepted by the phase decider with a recorded reason, except Blockers that need the phase approver)

## Who decides on a Fail

Product owner / ops lead (see `.ai/standards/review-and-approval.md`).
