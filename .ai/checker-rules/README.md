# Checker rules

One file per phase, read by the `checker` subagent together with `.ai/standards/checker-and-fail-decision.md`.
Each file lists the phase-specific focus items and the checks that cannot be overridden by the user.
The deterministic structural checks are run first by `scripts/validate_artifact.py`.
