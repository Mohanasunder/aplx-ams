# Checker rules: Phase 1 (Business Discovery)

Applies after the producer(s) in `docs/01-discovery` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Goals tied to measurable KPIs
- Every claim traceable to a transcript or document
- Stakeholders and personas cover all input sources
- Open questions logged with owner and priority
- Risks have owners and mitigations

## Collection file checks

Phase 1 uses fixed friendly filenames — one file per deliverable type. Check the following in addition to the general layers:

**`personas.md`**
- File exists at `docs/01-discovery/personas.md`
- Contains at least one `## Persona P-N:` section
- Sub-IDs are consecutive starting at P-1 and are not reused
- Every persona section has Profile, Goals, Pain Points, and Key Journeys filled
- No other file in `docs/01-discovery/` matches the `persona` template

**`risks.md`**
- File exists at `docs/01-discovery/risks.md`
- Contains at least one `## Risk R-N:` section
- Sub-IDs are consecutive starting at R-1 and are not reused
- Every risk section has Risk Description, Likelihood And Impact, Mitigation, and Owner filled
- Every risk has a matching row in `docs/logs/risk-register.md`
- No other file in `docs/01-discovery/` matches the `risk-register-entry` template

**`process-maps.md`**
- File exists at `docs/01-discovery/process-maps.md`
- Contains at least one `## Process M-N:` section
- Sub-IDs are consecutive starting at M-1 and are not reused
- Every process section has Process Overview, Steps, Diagram, and Pain Points filled
- Diagram matches the step table for each process
- No other file in `docs/01-discovery/` matches the `as-is-process-map` template

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- None defined for this phase (all findings can be accepted by the phase decider with a recorded reason, except Blockers that need the phase approver)

## Who decides on a Fail

Business owner / BA (see `.ai/standards/review-and-approval.md`).
