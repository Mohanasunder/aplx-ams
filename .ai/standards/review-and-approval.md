# Review and Approval

Humans review and approve; they never edit code or artifacts. Feedback goes to agents, which regenerate. Every approval is a recorded decision by a named person.

## Approvers by phase

| Phase | Approver |
| --- | --- |
| 1 Discovery | Business owner / BA |
| 2 Requirements | Product owner / BA |
| 3 Architecture | Architect / tech lead |
| 4 Design | Tech lead + UX |
| 5 Build planning | Tech lead |
| 6 Build (PR) | Human developer reviewer |
| 7 Testing | QA lead |
| 8 Deployment | Release manager / DevOps |
| 9 Operate | Product owner / ops lead |

## Approval tiers (Phase 6 PRs)

| Risk | Examples | Required | Review depth |
| --- | --- | --- | --- |
| Standard | UI components, CRUD features | 1 human developer | Standard (Light only for docs, UI copy and layout, or refactors covered by existing tests) |
| High | Auth, permissions, data migrations, integrations, payments, personal data | 2 approvers including the tech lead | Deep |
| Critical | Production deploys, infrastructure, production configuration, security configuration | Tech lead + release manager | Deep |

## Review depth (Phase 6 PRs)

The tier sets how deeply the human reviews, not only who approves. The reviewer confirms the depth when approving: `/approve` passes it to `scripts/log_approval.py --depth`, which refuses an approval below the tier's depth and records it in the approval log.

| Depth | When | The reviewer does all of these |
| --- | --- | --- |
| Deep | High, Critical | Reads every changed line of logic; reviews security against the threat model and permission matrix (auth, validation, secrets, data exposure); runs the feature locally, including failure paths; checks migrations and rollback; reads every test for behavior |
| Standard | Standard | Checks every acceptance criterion against the running or previewed feature; checks the change against the contract and UI spec; spot-checks logic and edge cases in the riskiest files; reads the tests' assertions |
| Light | Standard, only for docs, UI copy and layout, or refactors covered by existing tests | Reads the PR description and test results; skims the diff to confirm it stays within that kind of change; previews UI changes |

The reviewer also states the minutes spent reviewing (`--review-minutes`), recorded as `[review: N min]` for the pilot measures. The PR description states the tier and depth and carries the depth checklist. The checker flags a Light claim on a change that touches logic, data, auth, or contracts.

## Test set approval (Phase 6, before implementation)

Builders write tests first; a human approves them before any implementation code. The approved test files are then locked: builders never edit, skip, or weaken them.

- **Enforcement:** the `.claude/hooks/guard-tests.py` hook blocks agent edits to locked test files and to the approved test set; `scripts/locked_tests.py check` (CI and automated gates) fails if a locked file differs from the test set's Test Commit. Non-overridable.
- **Unlocking:** only a named human, by rejecting the test set version with `/approve` and a reason. The builder revises, and the new version is validated and approved before implementation resumes.

| Risk | Test set approver |
| --- | --- |
| Standard | 1 human developer reviewer |
| High | Tech lead |
| Critical | Tech lead |

Test reviewer checklist:

- [ ] Every acceptance criterion has at least one test
- [ ] Edge cases and error paths from the criteria are tested
- [ ] Tests assert behavior a user or caller can observe, not internals
- [ ] Red run shows the tests fail for the missing behavior
- [ ] Nothing beyond the criteria is being tested into scope

## Learned rules

A review category that recurs in `learned_rule_threshold` features (project.md) becomes a proposed learned rule (`LRN L-N`, drafted by `standards-author`). The tech lead approves each rule with `/approve`; only then does `scripts/learned_rules.py build` add it to `.ai/standards/learned-rules.md`, and `scripts/build_charter.py build` add it to the agent charter that every builder and the AI reviewer load. To retire a rule, the tech lead rejects it with `/approve` and a reason, and the index is rebuilt.

## Residual security risk (Phase 7)

The tech lead judges residual security risk before release. For each threat whose control is Not testable, the `performance-security-tester` raises a risk (RSK R-N); the tech lead either accepts it, recorded with `scripts/log_decision.py` and the risk marked Accepted with that DEC-NNN in `docs/logs/risk-register.md`, or rejects it, which makes it a blocking defect or a Spec change. A Failed control is a defect under the defect rule. Agents never accept a risk.

## Go / no-go (Phase 8, before every production deployment)

The go-live checklist (GLC) records the decision for one release tag. `/approve` on it is the decision: Approve = Go, Approve with conditions = Go with the conditions stated, Reject = No-go with the reason in the comments. Production deploys are Critical, so both the release manager and the tech lead record a Go at the checklist's current version. Before the release manager deploys, `python3 scripts/go_live.py check` must print GO: every piece of evidence Approved (release readiness, UAT sign-off, deployment runbook, rollback plan, operational runbook, monitoring spec, release notes, config validation), the traceability gate passing, the release tag in git, and both Go records with no later No-go. A changed checklist or a different tag needs a new Go. Agents never deploy and never record a Go.

## Phase summaries

Each phase's `SUMMARY.md` (SUM) is approved by that phase's approver at the phase gate, together with the phase's artifacts. Later phases rely on it instead of rereading full documents, so check that its decisions and constraints are complete.

## Spec change records

A spec change record (SCR S-N) is approved by the approver of the changed artifact's phase (table above), together with the new artifact version. Stopped work resumes only after both are Approved.

## Recording

`/approve <path>` runs `scripts/log_approval.py` with the approver's name and role. It refuses approval while validation is Pending or Fail. Decision: Approve | Approve with conditions | Reject. The script records the decision in three places: the front matter (`status`, `approver`), the document's own Approval Record table (decision, approver, role, version, conditions, comments, timestamp; a second decision at the same version, such as a High or Critical second approver, is appended after `; `), and `docs/logs/approval-log.md`, which is the authoritative, append-only record. Approvals are invalidated by new commits or edits (the artifact returns to Draft and is re-validated).

## Review comment format (feedback an agent can act on)

- **Location:** file and line, or artifact section
- **Issue:** what is wrong
- **Expected outcome:** the behavior or content that is right
- **Severity:** blocker | should fix | suggestion
- **Category:** a kebab-case slug for the kind of mistake, reused across features so recurrences can be counted. Starter set: `missing-authz-check`, `input-validation`, `error-model-mismatch`, `contract-drift`, `missing-edge-case-test`, `n-plus-one-query`, `secret-handling`, `logging-pii`, `accessibility`, `naming-convention`. Add new slugs when none fits.

A flaw in the plan or design is rejected upstream: fix and re-approve that artifact, then regenerate.

## PR reviewer checklist

- [ ] Ran or previewed the feature (not only read the diff)
- [ ] Every acceptance criterion is met
- [ ] Change summary read: Known Gaps acceptable, Deviations From Plan justified (or the plan fixed upstream), Blockers 'None'
- [ ] No changes outside the plan
- [ ] No packages added or upgraded beyond the plan's New Packages; each new package's license, maintenance, and known vulnerabilities checked
- [ ] Tests assert behavior, not just pass
- [ ] Approved test set (`FEAT-NNN-TESTS`) unchanged since approval; implementation started after it
- [ ] Auth, permissions, input validation, secrets, and data handling checked
- [ ] Migrations reversible and consistent with the schema design
- [ ] Contract (OpenAPI) and UI spec followed
- [ ] Applicable learned rules (`.ai/standards/learned-rules.md`) followed
- [ ] Checker validation summary and AI pre-review read; any "Proceeded on Fail" findings examined
- [ ] Second approver obtained if High or Critical

## Capacity and continuity

Size work to review capacity, not agent speed. Target turnaround: `approval_sla_business_days` (project.md); escalate when exceeded. Name backup approvers in `project.md`.
