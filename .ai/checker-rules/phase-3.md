# Checker rules: Phase 3 (Solution Architecture)

Applies after the producer(s) in `docs/03-architecture` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Each NFR mapped to an architectural answer
- All ADRs are in `docs/03-architecture/adrs.md` as `## ADR A-N:` sections; no separate `ADR-NNN.md` files (Blocker if extra files exist)
- ADR sub-IDs (A-1, A-2, …) are consecutive from 1 with no gaps (Major)
- Each ADR section lists at least two options with trade-offs and a rationale for the chosen one
- Threat model is in `docs/03-architecture/threat-model.md`; no separate `THR-NNN.md` files (Blocker if extra files exist)
- Threat rows use IDs T-1, T-2, … cited as `THR T-n`; every threat has a control or accepted-risk note and a Phase 7 verification method
- Architecture overview, technology comparison, deployment topology, and cost estimate each exist as a single file with the correct friendly name; no extra `ARC-NNN.md`, `TEC-NNN.md`, `TOP-NNN.md`, or `CST-NNN.md` files (Blocker if extra files exist)
- Stack is within the approved list or an exception ADR section exists
- Cost and scale assumptions stated
- A spike, if any: one question, two or more options, time box within max_spike_days, measurable success criteria; its findings and the ADR section in `adrs.md` that cites it are recorded before the phase closes

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- Spike work reached `main`, a spike branch remains after its ADR is approved, or a spike passed its time box (`python3 scripts/spike.py check` fails)

## Who decides on a Fail

Architect / tech lead (see `.ai/standards/review-and-approval.md`).
