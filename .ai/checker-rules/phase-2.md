# Checker rules: Phase 2 (Requirements Analysis)

Applies after the producer(s) in `docs/02-requirements` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- Each story testable and unambiguous; Given/When/Then present
- No duplicate or conflicting stories
- NFRs have numbers and units
- Every brief goal is covered: `python3 scripts/traceability.py check --phase 2` passes (every goal `BRF G-n` of the Approved brief is cited by an epic whose Stories lists an in-scope story, or a decision DEC-NNN puts it out of scope); also judge whether the cited stories really move the goal's KPI (Major if not)
- No requirement without a source
- Domain glossary defines every business term used in the brief, stories, criteria, and business rules, once, with a source; terms used with two meanings are open questions, not silent choices
- Stories and criteria use the glossary terms, never an avoided synonym
- All epics are in `docs/02-requirements/epics.md` as `## Epic E-N:` sections; no separate `EPC-NNN.md` files (Blocker if extra files exist)
- All stories are in `docs/02-requirements/user-stories.md` as `## Story S-N:` sections; no separate `REQ-NNN.md` files (Blocker if extra files exist)
- All NFRs are in `docs/02-requirements/nfrs.md` as `## NFR N-N:` sections; no separate `NFR-NNN.md` files (Blocker if extra files exist)
- All business rules are in `docs/02-requirements/business-rules.md` as `## Rule B-N:` sections; no separate `BR-NNN.md` files (Blocker if extra files exist)
- All backlog entries are in `docs/02-requirements/backlog.md` as `## Entry BL-N:` sections; no separate `BKL-NNN.md` files (Blocker if extra files exist)
- Sub-IDs within each collection file are consecutive starting at 1; no gaps or duplicates (Major)
- Downstream citations use `REQ S-N AC-n` format (not bare `REQ-NNN AC-n`)

### PRS — Product Requirement Specification checks

The file `docs/02-requirements/product-requirement-specification.md` is required in Phase 2. Apply these checks after the general layer:

**Structural (Blocker if violated):**
- File `docs/02-requirements/product-requirement-specification.md` exists; no separate `PRS-NNN.md` files exist in `docs/02-requirements/`
- Product Goals sub-IDs (`G-N`) are consecutive starting at G-1; no gaps or duplicates
- Non-Goals sub-IDs (`NG-N`) are consecutive starting at NG-1; no gaps or duplicates
- Feature sub-IDs (`F-N`) are consecutive starting at F-1; no gaps or duplicates
- A removed goal, non-goal, or feature keeps its row or block with `Removed - SCR S-N`; it is never silently deleted after approval

**Content (Major if violated):**
- Every product goal has a measurable success metric that includes a number and unit (e.g. "adoption ≥ 40 % of active users within 90 days"); vague targets (`improve`, `enhance`, `fast`) are Major
- Every product goal cites at least one upstream brief goal as `BRF G-N`; a goal citing a non-existent BRF goal ID is Major
- Every non-goal has a named reason or a `DEC-NNN` reference; "not in scope" alone is not sufficient
- In Scope and Out of Scope are both filled; a capability present in both or absent from both is Major
- Every feature (`PRS F-N`) has a MoSCoW priority from the approved vocabulary (Must / Should / Could / Won't) and a one-line reason
- Every feature cites at least one product goal (`PRS G-N`) it serves; a feature with no goal link is Major
- Every Must or Should priority feature cites at least one linked story (`REQ S-N`); a Must/Should feature with no story is Major
- Could and Won't features may cite `None - <reason>` for linked stories; judge whether the reason is specific (Minor if vague)
- No product goal is a duplicate of a brief goal verbatim — PRS goals must be product-level elaborations, not copies (Major)
- No feature overlaps with an Out of Scope item without a named human decision (`DEC-NNN`) that overrides it (Major)

**Minor (flag but do not block):**
- A product goal that does not trace to any `PRS F-N` feature (orphan goal)
- A feature that exists in the PRS but has no backlog entry in `docs/02-requirements/backlog.md`
- Priority reasoning is a single word with no context

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- An avoided term used in an Approved artifact, or a malformed glossary (`python3 scripts/glossary_check.py check` fails)
- A brief goal with no epic and in-scope story and no out-of-scope decision, an epic citing no goal or a goal that does not exist, or an epic with no in-scope story (`python3 scripts/traceability.py check --phase 2` fails)
- `docs/02-requirements/product-requirement-specification.md` is absent when the phase validation runs
- A `PRS G-N`, `PRS NG-N`, or `PRS F-N` sub-ID is reused or out of sequence after an Approved version

## Who decides on a Fail

Product owner / BA (see `.ai/standards/review-and-approval.md`).
