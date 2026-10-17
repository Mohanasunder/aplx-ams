# Checker: Validation Layers, Summary, and Fail Decision

The `checker` subagent validates every artifact before human review. It is read-only and advisory. The Orchestrator always shows the user the validation summary; on a Fail the **user decides**.

## Verdict rules

Any **Blocker** or **Major** finding = **Fail**. Only **Minor** = **Pass with warnings**. None = **Pass**.

## Layers

| Layer | Checks |
| --- | --- |
| Structural | Required sections and order, complete metadata, no empty sections, valid unique IDs, naming, formats, controlled values (`scripts/validate_artifact.py`) |
| Input conformance | Inputs are cited as `ID vX.Y` and are Approved at the stated versions (`scripts/spec_impact.py`); a changed approved artifact has an Approved spec change record; Phase Input Brief and interview answers reflected; nothing invented (requirements, systems, endpoints, libraries); nothing outside the phase's boundary: the artifact does none of what its phase's Not this line in CLAUDE.md excludes (Major); the artifact sits in its producing phase's folder or an allowed exception ("Where agents write" in `.ai/standards/phase-loop.md`), and no upstream artifact changed without an open SCR (Major) |
| Completeness | Every section has real content; every upstream item covered downstream; open questions and assumptions logged and linked |
| Consistency | Within the artifact; across artifacts (API vs schema, UI vs API, permissions vs auth design, ADRs vs architecture); standards and glossary |
| Traceability | Links resolve, no orphans, matrix updated; at the phase gate, the phase summary indexes every Approved artifact (`scripts/context_pack.py summaries N`) |
| Content quality | Testable and unambiguous requirements; measurable NFRs; explicit scope; no vague words; risks have owners and mitigations; every risk the phase raised has an RSK entry and a row in `docs/logs/risk-register.md`; at the phase gate, every Open or Mitigating risk shows Last reviewed in this phase (Major) |
| Producer self-check | Quality checklist complete; checker spot-checks claims |

Deterministic checks run first (script); AI judgment covers ambiguity, hallucination, conflicts, and plan adherence.

## Validation summary (shown on every run)

1. **Header:** artifact ID and version, phase, producer, run number, loop count
2. **Verdict:** Pass | Pass with warnings | Fail
3. **Scorecard:** result per layer
4. **Findings:** counts by severity, then detail (ID, location, description, severity, suggested fix)
5. **Top issues:** 3 to 5 in plain language
6. **Unresolved from earlier runs**
7. **Recommendation:** send back or proceed, with reasoning

## Decision on a Fail

| Option | Effect |
| --- | --- |
| A. Send back to producer | Findings go to the producer; it revises; loop count +1; checker re-runs |
| B. Proceed to human review | Artifact goes to reviewers with the report attached and failed items flagged |
| C. Send back with modified instructions | User adds guidance or picks findings to fix; as A |

Safeguards for B:

- A reason is required and recorded in `docs/logs/fail-decisions-log.md` (who, when, findings accepted, reason).
- Set `validation: Proceeded on Fail`; reviewers see "Proceeded with N findings unresolved".
- Blocker findings: B only by the phase approver (or with a second confirmation).
- **Non-overridable** (listed per phase in `.ai/checker-rules/`): secrets in code or config, failing security scans, failing tests in Build. For these only A or C is allowed.
- Accepted findings stay in the report and are tracked after approval.

Who decides on a Fail: product owner / BA (Phases 1 to 2), tech lead (3 to 5), human developer reviewer (6), QA lead (7), release manager (8).

## Loop limit

After `loop_limit_failed_validations` failed rounds, recommend escalating or revising the upstream input instead of another loop. If reviewers keep catching issues the checker missed, propose new checks (humans add them to the rule files).
