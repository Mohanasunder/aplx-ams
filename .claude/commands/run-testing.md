---
description: Run Phase 7 (Testing) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 7: Testing** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Prove acceptance criteria and NFRs are met; produce defects, UAT support, and a release readiness report.
- **Output folder:** `docs/07-testing/`
- **Required inputs:**
  - Acceptance criteria and traceability matrix
  - Merged build in a test environment
  - Test strategy
  - Test data or generation rules
  - NFR targets
  - Approved threat model (threats with IDs, controls, and how to verify them)
  - UAT participants (names and roles); any extra scenarios they want to run (optional: the UAT script is drafted from the acceptance criteria)
- **Producer subagents:**
  1. `test-designer`
  2. `test-data-generator`
  3. `test-automation`
  4. `performance-security-tester`
  5. `defect-triage`
  6. `release-readiness`
- **Sequence:** test-designer (plan and cases) -> test-data-generator -> test-automation (suites and execution report) -> performance-security-tester (NFR report, including Threat Model Coverage: every threat's control verified on the running system) -> defect-triage (defects classified and routed) -> release-readiness (readiness report; UAT script drafted from the acceptance criteria before UAT starts, results recorded from what participants report).
- **Defect routing:** a Code defect becomes a Fix feature: `build-planner` plans it (`Type: Fix DEF D-N`), the tech lead approves the plan with `/approve`, and it is built with `/create-feature-branch` and `/run-build-feature` (regression test approved first). A Spec defect follows the living spec rule (SCR first). Test and Environment defects go to their owner. After fixes merge, `test-automation` re-runs the suites into a new execution report and `defect-triage` updates each defect's Status. Testers and builders never patch code for a defect outside an approved Fix feature.
- **Deliverable templates:** `test-plan`, `test-case`, `test-data-spec`, `test-execution-report`, `nfr-test-report`, `defect-report`, `uat-signoff`, `release-readiness-report`
- **Checker rules file:** `.ai/checker-rules/phase-7.md` (invoke the `checker` subagent)
- **Human approver:** QA lead
- **Exit criteria:**
  - Every acceptance criterion has a passing test
  - No traceability gaps: `python3 scripts/traceability.py check --phase 7` passes (every story criterion in a Merged feature, in its approved test set, and in a test case that did not fail in the newest execution report)
  - No open Blocker defects; every Code defect routed to a Fix feature and every Spec defect to an SCR (checked by the same `traceability.py check --phase 7`)
  - Every threat in the threat model Verified, or Failed with a defect, or Not testable with a risk the tech lead accepted (DEC-NNN) (checked by the same `traceability.py check --phase 7`)
  - Every user-facing story has a UAT scenario that ran; every UAT Fail has a defect report; QA lead sign-off and UAT sign-off recorded

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
