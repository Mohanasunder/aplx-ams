# Phase 7: Testing

Prove acceptance criteria and NFRs are met; produce defects, UAT support, and a release readiness report.

- **Command:** `/run-testing`
- **Human approver:** QA lead
- **Output folder:** `docs/07-testing/`

## Required inputs

- Acceptance criteria and traceability matrix
- Merged build in a test environment
- Test strategy
- Test data or generation rules
- NFR targets
- UAT participants and scenarios

## Producer agents

- `test-designer`
- `test-data-generator`
- `test-automation`
- `performance-security-tester`
- `defect-triage`
- `release-readiness`

## Deliverable templates

- `.ai/templates/test-plan.md`
- `.ai/templates/test-case.md`
- `.ai/templates/test-data-spec.md`
- `.ai/templates/test-execution-report.md`
- `.ai/templates/nfr-test-report.md`
- `.ai/templates/defect-report.md`
- `.ai/templates/uat-signoff.md`
- `.ai/templates/release-readiness-report.md`

## How it runs

test-designer (plan and cases) -> test-data-generator -> test-automation (suites and execution report) -> performance-security-tester (NFR report) -> defect-triage (defects, routed to builders or upstream) -> release-readiness (readiness report, UAT sign-off draft).

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
