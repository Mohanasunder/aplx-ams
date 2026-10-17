# The Standard Phase Loop

Every phase runs this loop. The Orchestrator (main Claude Code session) runs it; subagents do the producing and checking.

```
Entry interview -> Phase Input Brief approved -> Producer(s) build -> Validate (script + checker)
   -> Validation summary shown to the user -> [Fail: user decides] -> Human review -> /approve -> next phase
```

## Step 1. Prepare

1. Confirm the previous phase's artifacts are `status: Approved` (`/sdlc-status`). If not, stop and name the missing approvals. If the human chooses to proceed anyway, record it as an Override in the decision log (see Recording decisions) before continuing.
2. Collect the phase configuration from the phase command (inputs, producers, templates, checker rules, approver).
3. Context: start from the approved `SUMMARY.md` of every earlier phase, not the full upstream documents. Open a full artifact only for a section a summary points to.

## Step 2. Entry interview

1. Invoke the `phase-intake` subagent with the user's request, the phase configuration, the phase's Purpose and Not this line (CLAUDE.md, "Phases: purpose and boundaries"), and paths to approved upstream artifacts. It returns a gap analysis and questions (it never talks to the human).
2. Ask the human the questions yourself with AskUserQuestion: blockers first, at most 4 per call, offer the suggested options plus "Defer (record as assumption)". Never re-ask what an approved artifact or earlier answer already settles.
3. Re-invoke `phase-intake` with the answers; it returns the filled content for the **Phase Input Brief**, **interview record**, and **input readiness checklist**. Save all three using `new_artifact.py` with `--out` pointing to the phase folder and a fixed friendly filename:
   - `python3 scripts/new_artifact.py --template phase-input-brief       --title "Phase N input brief"   --author orchestrator --out docs/0N-<slug>/phase-input-brief.md`
   - `python3 scripts/new_artifact.py --template interview-record         --title "Phase N interview"     --author orchestrator --out docs/0N-<slug>/interview-record.md`
   - `python3 scripts/new_artifact.py --template input-readiness-checklist --title "Phase N readiness"   --author orchestrator --out docs/0N-<slug>/input-readiness-checklist.md`
   Never let any of these auto-name as `PIB-NNN.md`, `INT-NNN.md`, or `IRC-NNN.md`. Each phase has exactly one of each in its own folder. Returns a verdict: Ready, Ready with assumptions, or Not ready.
4. Not ready (a Blocker gap): stop and tell the human what is needed. Do not start the producers.
5. Show the Phase Input Brief and ask the human to approve it (name and role). Record with `python3 scripts/log_approval.py` after the validation step in Step 4a is done for the brief (validate it like any artifact).
6. Time-box: after 3 interview rounds, escalate to the human lead rather than looping.

## Step 3. Produce

Invoke the producer subagents in the configured order (parallel where the command says so). Pass each one: the phase's Purpose and Not this line (CLAUDE.md), the approved Phase Input Brief path (`docs/0N-<slug>/phase-input-brief.md`), the earlier phases' summaries, the upstream sections it needs as `ID vX.Y § section` (not whole folders), the template slugs, and the output folder. Producers create artifacts with `scripts/new_artifact.py`, fill every section, and return a summary.

**Risks, in every phase.** Tell each producer to report new risks and changes to existing ones in its summary. A new risk becomes a `risk-register-entry` artifact in the phase folder (`python3 scripts/new_artifact.py --template risk-register-entry --title "..." --author <producer> --out docs/0N-<phase-slug>/risks.md`, then `python3 scripts/fm.py set <file> phase N`; validation blocks the entry until its phase is set, and its approver is the phase's approver) and a row in `docs/logs/risk-register.md`. A change to an existing risk (likelihood, impact, mitigation, status) is a row update in the index, not a new entry version. New entries are validated and approved with the phase.

Last, the phase's first producer drafts the **phase summary**: `python3 scripts/new_artifact.py --template phase-summary --id SUM --title "Phase N summary" --author <producer> --out docs/0N-*/SUMMARY.md` (N = phase number; not for Phase 0, where `project.md` serves, or Phase 6, where each PR description serves). About half a page: decisions, constraints, open items, the document index (`ID vX.Y`), and what the next phase must open in full.

## Step 4. Validate

a. Run `python3 scripts/validate_artifact.py <folder or paths> --check-links`.
b. Invoke the `checker` subagent with the phase number and artifact paths. It re-runs the script, applies `.ai/checker-rules/phase-N.md`, and returns a validation report.
c. Save the report as `docs/validation/phase-N-run-M.md` (template `validation-report`, via `python3 scripts/new_artifact.py --template validation-report --title "Phase N validation run M" --author checker --out docs/validation/phase-N-run-M.md`). Increment M for each re-run of the same phase. Set each validated artifact's `validation` field with `python3 scripts/fm.py set <file> validation "<Pass|Pass with warnings|Fail>"`.

## Step 5. Show the validation summary (always, whatever the verdict)

Present it in the format in `.ai/standards/checker-and-fail-decision.md`: header, verdict, scorecard per layer, findings by severity, top issues, unresolved earlier findings, recommendation.

## Step 6. On Fail: the user decides

Use AskUserQuestion with the options below. **Never loop back automatically.**

- **A. Send back to producer:** pass the findings to the same producer; it revises; increment the loop count; re-run Step 4.
- **B. Proceed to human review:** allowed only with a stated reason; Blockers need the phase approver; non-overridable findings cannot be accepted. Set `validation` to `Proceeded on Fail`, and invoke `governance-audit` to record the decision in `docs/logs/fail-decisions-log.md`. The reviewers see the banner "Proceeded with N findings unresolved".
- **C. Send back with modified instructions:** the user adds guidance or selects which findings to fix, then as A.

After `loop_limit_failed_validations` (project.md) failed rounds, tell the user the loop is not converging and recommend revising the upstream input or escalating.

## Step 7. Human review

Set the artifacts to `In review` (`scripts/fm.py`). Tell the human exactly what to review and where. Humans give feedback in chat; you route it: wording or content changes to the producer; a flaw in an approved upstream artifact means reopening that upstream artifact first through the living spec rule below (change flows backward).

## Step 8. Approval and close

Risk review: show the human every Open or Mitigating row in `docs/logs/risk-register.md` and ask the phase approver to confirm each one's status, or change it; route changes to the phase's first producer, which updates the rows and sets Last reviewed to `Phase N, YYYY-MM-DD`. Marking a risk Accepted needs the approver's named decision (`scripts/log_decision.py`). The phase summary lists the Open risks under its open items.

At the Phase 2, Phase 5, and Phase 7 gates, `python3 scripts/traceability.py check --phase N` must also pass (Phase 2: every brief goal covered by an epic with an in-scope story, or out of scope by a DEC-NNN; Phases 5 and 7 repeat that goal check); its output, not the hand-kept matrix, decides whether there are traceability gaps.

At the Phase 9 gate, `python3 scripts/feedback_log.py check --gate` must also pass: every incident, feedback summary, and production defect has an outcome (an improvement backlog item, defect report, SCR, or a named 'no action' decision), and every improvement backlog item is Approved or Rejected by the product owner.

Run `python3 scripts/context_pack.py summaries N`; it must pass (the summary indexes every Approved artifact of the phase at its current version). The summary is approved with the phase. Only after a named human says to, run `/approve <path>` (which uses `scripts/log_approval.py`). Then: run `python3 scripts/build_charter.py build` (the agent charter picks up any newly approved ADR, standard, Definition of Done, or rule), run `python3 scripts/feedback_log.py build` (Phase 9, or whenever a Phase 9 artifact changed), run the `traceability` subagent, have `governance-audit` update `project.md`, and propose the next phase command.

## Recording decisions

Any time a human makes a decision in chat that no artifact will record (a small technical choice, a scope trim, an exception, an override of a check or the phase order), run `python3 scripts/log_decision.py add --decision "..." --owner "<name>" --reason "..." --context "<IDs>" [--kind Override] [--alternatives "..."]`. The permission prompt is the human's confirmation. Never log a decision the human did not make; propose an ADR instead when the decision is significant or hard to reverse. Checker Fail decisions keep their own log (`fail-decisions-log.md`); approvals stay in `approval-log.md`.

## Where agents write

Each phase's agents write only in that phase's folder (`docs/0N-*/`); everything earlier is read-only input. Shared logs are written only through their owners: approvals by `scripts/log_approval.py` (`/approve`), decisions by `scripts/log_decision.py`, fail decisions and phase status by `governance-audit`, the traceability matrix by `traceability`, the feedback and incident log by `scripts/feedback_log.py`, open questions, assumptions, and the risk register by appending rows. Validation reports go to `docs/validation/`.

Exceptions, all still subject to the approved-artifact hook:

| Who | Writes outside its phase folder | When |
| --- | --- | --- |
| Producer of an upstream artifact | That artifact, under an open SCR (living spec rule below) | Any phase finds it wrong |
| `build-planner` | A Fix feature folder in `docs/05-build-plan/` | Phase 7 or 9, for a Code defect |
| Builders and `create-feature-branch.sh` | The feature's `status.md` in `docs/05-build-plan/` | Phase 6 |
| `monitoring-engineer` | The monitoring spec and operational runbook in `docs/08-deployment/` | Phase 9 revisions, under an SCR once Approved |
| `solution-architect` | A new ADR in `docs/03-architecture/` | Any phase, for an SCR that changes an architecture or contract artifact |
| Any producer | A risk entry (RSK R-N) in risks.md in the current phase folder and a row in `docs/logs/risk-register.md` | Any phase |

An Approved artifact (front matter `status: Approved`) is never edited in place. `.claude/hooks/guard-approved.py` blocks agent edits, shell writes, and `scripts/fm.py set` on it until an open spec change record (Draft or In review) names its ID. `/approve` is not blocked. `scripts/spec_impact.py records` in CI is the backstop.

## Defect rule: every fix is planned work

Applies to every defect, from Phase 7 testing or from production in Phase 9. `defect-triage` classifies it in the defect report (Classification And Route) and nobody patches code until its route is approved.

| Class | Meaning | Route |
| --- | --- | --- |
| Code | The code fails an approved criterion | A Fix feature: `build-planner` plans `FEAT-NNN` with `Type: Fix DEF D-N` (the failed criteria copied unchanged, only the files the fix needs); the tech lead approves the plan with `/approve`; it is built like any feature (`/create-feature-branch`, `/run-build-feature`), starting with an approved regression test that reproduces the defect |
| Spec | A criterion, design, or contract is wrong or missing | The living spec rule below (SCR first), then a revised or new feature |
| Test | The test case or suite is wrong; the product is right | `test-designer` or `test-automation` revises it; the QA lead approves |
| Environment | Data, configuration, or infrastructure | Its owner |

Status moves Open -> Fixing -> Fixed (fix merged) -> Closed (retest passed in the newest execution report). Won't fix needs a named human's decision (DEC-NNN). At the Phase 7 gate `python3 scripts/traceability.py check --phase 7` fails on an unclassified defect, a Code defect with no Fix feature, a Spec defect with no SCR, a Fixed defect whose fix is not Merged, or an open Blocker. Urgent production fixes use `hotfix/HOT-NNN` (`.ai/standards/branching-standard.md`) and are planned as a Fix feature afterwards.

## Living spec rule: changing an approved artifact

Applies whenever any phase (a builder's spec conflict, a review, a defect, test results, production feedback) shows that an approved artifact is wrong or incomplete. Code never becomes the source of truth: the spec changes first, then the code is regenerated.

1. **Stop.** Run `python3 scripts/spec_impact.py impact <ID>`. Set every affected feature that is In progress or In review to `State: Blocked` in its status.md, citing the coming SCR under Blockers. Tell the human what stopped.
2. **Record.** Have the artifact's producer append a new `## SCR S-N: [title]` section to the collection file `docs/logs/spec-changes.md` (template `spec-change`; create from template with `python3 scripts/new_artifact.py --template spec-change --id SCR --out docs/logs/spec-changes.md` if absent). List every changed approved artifact as `ID vOLD -> vNEW`, including downstream artifacts revised because of this change; fill Trigger, Change, Reason, Decision Record, Impact (from the impact output), Work Stopped, Resume Criteria. If a changed artifact is an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model), the `solution-architect` also drafts a new ADR in `docs/03-architecture/` recording the change, with options considered and consequences. When an ADR itself changes, the new ADR supersedes it and the old one's Status And Date becomes 'Superseded by ADR A-N' (list it under Changed Artifact). The SCR's Decision Record cites the new ADR A-N.
3. **Revise.** The producer updates the artifact and bumps its version (it returns to Draft). Artifacts cite their inputs as `ID vX.Y`.
4. **Validate and approve.** Validate the SCR and the revised artifact (Step 4). A new ADR from item 2 is validated with the SCR and approved by the architect / tech lead; `spec_impact.py records` fails an Approved SCR whose ADR is not Approved. The approver of the changed artifact's phase approves both with `/approve`. `python3 scripts/spec_impact.py records` fails until every change to an approved artifact has an Approved SCR.
5. **Propagate.** For each item in Impact: revise and re-approve the downstream artifact against the new version (plans, acceptance files, test sets; a locked test set is unlocked only by the human's Reject in `/approve`), re-test merged work, or record 'No change - reason' in the SCR. `python3 scripts/spec_impact.py stale` lists approved artifacts still citing old versions.
6. **Resume.** When the Resume Criteria are met and `python3 scripts/spec_impact.py check FEAT-NNN` passes, set the feature's State back and continue. Run `python3 scripts/spec_impact.py log` to refresh `docs/logs/spec-change-log.md`.
