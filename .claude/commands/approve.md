---
description: Human-only. Record an approval, conditional approval, or rejection for an artifact
argument-hint: <artifact path> [--sub-id FEAT-NNN|S-N|L-N]
disable-model-invocation: true
---

This command records a **human** decision. Only run it because the human invoked `/approve`. Never infer an approval from earlier chat, never approve on a human's behalf, and never use another person's name.

1. Parse `$ARGUMENTS`: the artifact path, and optionally `--sub-id <value>` for per-section approvals: `FEAT-NNN` for PR description sections (`docs/06-build/pr-descriptions.md`), `S-N` for spec-change sections (`docs/logs/spec-changes.md`), or `L-N` for learned-rule sections (`docs/logs/learned-rules.md`). Read the artifact. Show its ID, version, title, current `status` and `validation`. If `validation` is `Pending` or `Fail` and no `--sub-id` is present, say that approval is blocked and propose `/validate` first.
2. Ask the human (AskUserQuestion): decision (Approve / Approve with conditions / Reject); their **name** and **role** (they must be the approver named for this phase in `project.md`); comments; and conditions if conditional.
3. For a PR description section (`--sub-id FEAT-NNN` on `docs/06-build/pr-descriptions.md`): read the `### Risk Tier And Review Depth` sub-section inside the `## PR FEAT-NNN:` section and show the reviewer the depth checklist for that tier from `.ai/standards/review-and-approval.md` (Deep for High and Critical; Standard; Light only for docs, UI copy, or test-covered refactors). Ask the reviewer to confirm they did every item. If they did not, the decision can only be Reject or a later approval after they finish. Pass the confirmed depth as `--depth <Deep|Standard|Light>`. Also ask how many minutes they spent reviewing (their own estimate; required for PR approvals and rejections) and pass `--review-minutes <N>`.
4. For High or Critical risk PRs, check that the required second approver has also approved (see `docs/logs/approval-log.md`); if not, record this approval and say who is still needed.
5. Run the approval script (the permission prompt is expected: the human confirms):
   - For a PR description section: `python3 scripts/log_approval.py --artifact docs/06-build/pr-descriptions.md --sub-id <FEAT-NNN> --decision "<decision>" --approver "<name>" --role "<role>" --depth <Deep|Standard|Light> --review-minutes <N> [--comments "..."] [--conditions "..."]`
   - For a spec-change section: `python3 scripts/log_approval.py --artifact docs/logs/spec-changes.md --sub-id <S-N> --decision "<decision>" --approver "<name>" --role "<role>" [--comments "..."] [--conditions "..."]`
   - For a learned-rule section: `python3 scripts/log_approval.py --artifact docs/logs/learned-rules.md --sub-id <L-N> --decision "<decision>" --approver "<name>" --role "<role>" [--comments "..."] [--conditions "..."]`
   - For all other artifacts: `python3 scripts/log_approval.py --artifact <path> --decision "<decision>" --approver "<name>" --role "<role>" --comments "<comments>" [--conditions "<conditions>"]`
6. Report the result. On Reject, ask what feedback to route and to which producer or upstream artifact. On Approve, run the `traceability` subagent and the `governance-audit` subagent (update `project.md`).
