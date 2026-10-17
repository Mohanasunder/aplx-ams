# IDs and Naming

| Kind | Pattern | Example |
| --- | --- | --- |
| Fixed single-instance ID | `PREFIX` only (no number); one file per project | `TPL`, `RUN`, `MON`, `SUM` |
| Numbered artifact ID | `PREFIX-NNN` (prefix from the template, auto-incremented) | `FEAT-004`, `OQ-012`, `DEC-007` |
| Collection sub-ID | `PREFIX X-N` where X is a type letter and N is the sequence within the file | `PER P-2`, `RSK R-3`, `SCR S-2`, `DEF D-21`, `LRN L-3` |
| Feature | `FEAT-NNN`; plan/tasks/acceptance/status share it with a suffix | `FEAT-004`, `FEAT-004-TASKS`, `FEAT-004-ACC`, `FEAT-004-STATUS`; Phase 6 test set: `FEAT-004-TESTS`; `FEAT-000` is reserved for Task 0 |
| Open question | `OQ-NNN` (in `docs/logs/open-questions-log.md`) | `OQ-012` |
| Assumption | `A-NNN` (in `docs/logs/assumptions-log.md`) | `A-004` |
| Domain glossary | `GLO` (template `domain-glossary`, in `docs/02-requirements/`; one per project) | `GLO` |
| Decision | `DEC-NNN` (row in `docs/logs/decision-log.md`, via `scripts/log_decision.py`) | `DEC-007` |
| Learned rule | `LRN L-N` (collection sub-ID in `docs/logs/learned-rules.md`) | `LRN L-3` |
| Phase summary | `SUM` (fixed, one per phase, file `docs/0N-*/SUMMARY.md`) | `SUM` |
| Section citation | `ID vX.Y § section` (or `::` for `§`) in Context Packs, briefs, and summaries | `API v1.1 § POST /tickets` |
| Spec change record | `SCR S-N` (collection sub-ID in `docs/logs/spec-changes.md`) | `SCR S-2` |
| Citation of an input | `ID vX.Y` in Input References and contracts sections | `API v1.1` |
| Defect | `DEF D-N` (collection sub-ID in `docs/07-testing/defects.md`) | `DEF D-21` |
| Test case | `TC TC-N` (collection sub-ID in `docs/07-testing/test-cases.md`) | `TC TC-5` |
| Spike | `SPK S-N` (collection section in `docs/03-architecture/spikes.md`) | `SPK S-2` |
| Branch | `feature/FEAT-NNN-slug` (also for Fix features), `hotfix/HOT-NNN-slug`, `spike/spk-S-N-slug` (slug 1 to 4 lowercase words) | `feature/FEAT-004-ticket-triage` |
| Feature folder | `docs/05-build-plan/feature-NNN-slug/` | `feature-004-ticket-triage/` |
| Validation report | `docs/validation/phase-N-run-M.md` | `phase-1-run-2.md` |

Template prefixes are in each template's `id_prefix` field in `.ai/templates/`. Use `python3 scripts/new_artifact.py --id auto` to take the next free number for numbered IDs; fixed IDs use `--id PREFIX --out <path>`.

## Fixed friendly filenames (phase-loop artifacts)

Some artifacts produced every phase use a fixed friendly filename instead of `PREFIX-NNN.md`. The `id` front matter field is still auto-assigned by `new_artifact.py`; the filename is controlled with `--out`.

| Artifact | Filename | Folder | Produced by |
| --- | --- | --- | --- |
| Phase Input Brief | `phase-input-brief.md` | `docs/0N-<phase-slug>/` | Orchestrator (via phase-loop Step 2.3) |
| Interview Record | `interview-record.md` | `docs/0N-<phase-slug>/` | Orchestrator (via phase-loop Step 2.3) |
| Input Readiness Checklist | `input-readiness-checklist.md` | `docs/0N-<phase-slug>/` | Orchestrator (via phase-loop Step 2.3) |
| Validation Report | `phase-N-run-M.md` | `docs/validation/` | Orchestrator (via phase-loop Step 4c / `/validate`) |

One `input-readiness-checklist.md` per phase, in that phase's folder. Never auto-named as `IRC-NNN.md`.

## Single-instance collection file (Phase 6 build)

Phase 6 accumulates all PR descriptions in one collection file. Each PR is a `## PR FEAT-NNN:` section; sub-headings use `### `.

| Deliverable | Filename | Front matter `id` | Example citation |
| --- | --- | --- | --- |
| PR descriptions | `pr-descriptions.md` | `PRD` (fixed) | `PRD FEAT-001` |

Rules: never create a separate `PRD-NNN.md` file. The `documentation-writer` appends one `## PR FEAT-NNN: [title]` section per feature after implementation. Approve each section individually with `/approve docs/06-build/pr-descriptions.md --sub-id FEAT-NNN`; the approval log records `PRD FEAT-NNN` as the artifact ID. Per-PR status and review metadata are stored as `<!-- pr_key: value -->` HTML comments within the section.

## Collection files (Phase 6 build — review reports)

Two Phase 6 review outputs are collection files keyed by feature. The `ai-code-reviewer` and `security-scanner` return their sections; the Orchestrator appends them.

| Deliverable | Filename | Front matter `id` | Sub-ID pattern | Example citation |
| --- | --- | --- | --- | --- |
| AI pre-review reports | `docs/06-build/ai-pre-review-reports.md` | `AIR` (fixed) | `FEAT-NNN` | `AIR FEAT-004` |
| Security scan reports | `docs/06-build/security-scan-reports.md` | `SSR` (fixed) | `FEAT-NNN` | `SSR FEAT-004` |

Rules: never create separate `AIR-NNN.md` or `SSR-NNN.md` files. Each feature appends one `## AIR FEAT-NNN: [title]` or `## SSR FEAT-NNN: [title]` section. Approve with `/approve docs/06-build/ai-pre-review-reports.md --sub-id FEAT-NNN`.

## Single-instance and collection files (Phase 7 testing)

Phase 7 has two collection files (test cases, defects) and five single-instance files (all other deliverables).

| Deliverable | Filename | Front matter `id` | Sub-ID / note | Example citation |
| --- | --- | --- | --- | --- |
| Test plan | `docs/07-testing/test-plan.md` | `TPL` (fixed) | single-instance | `TPL` |
| Test cases | `docs/07-testing/test-cases.md` | `TC` (fixed) | sub-ID letter `TC` | `TC TC-5` |
| Test data spec | `docs/07-testing/test-data-spec.md` | `TDS` (fixed) | single-instance | `TDS` |
| Test execution report | `docs/07-testing/test-execution-report.md` | `TER` (fixed) | single-instance | `TER` |
| NFR test report | `docs/07-testing/nfr-test-report.md` | `NTR` (fixed) | single-instance | `NTR` |
| Defects | `docs/07-testing/defects.md` | `DEF` (fixed) | sub-ID letter `D` | `DEF D-3` |
| Release readiness report | `docs/07-testing/release-readiness-report.md` | `RRR` (fixed) | single-instance | `RRR` |
| UAT sign-off | `docs/07-testing/uat-signoff.md` | `UAT` (fixed) | single-instance; approval sub-IDs for scenarios use `S-n` | `UAT` |

Rules: never create separate `TC-NNN.md` or `DEF-NNN.md` files. Append each test case as `## Test Case TC-N: [title]`; each defect as `## Defect D-N: [title]`. Defects are cited downstream as `DEF D-N`. Fix features cite the triggering defect as `Type: Fix DEF D-N` in their plan.md.

## Single-instance files (Phase 8 deployment)

All Phase 8 deliverables are single-instance files per project — one of each per project.

| Deliverable | Filename | Front matter `id` | Example citation |
| --- | --- | --- | --- |
| Deployment runbook | `docs/08-deployment/deployment-runbook.md` | `RUN` (fixed) | `RUN` |
| Rollback plan | `docs/08-deployment/rollback-plan.md` | `RBK` (fixed) | `RBK` |
| Monitoring spec | `docs/08-deployment/monitoring-spec.md` | `MON` (fixed) | `MON` |
| Operational runbook | `docs/08-deployment/operational-runbook.md` | `OPR` (fixed) | `OPR` |
| Release notes | `docs/08-deployment/release-notes.md` | `REL` (fixed) | `REL` |
| Go-live checklist | `docs/08-deployment/go-live-checklist.md` | `GLC` (fixed) | `GLC` |
| Config validation report | `docs/08-deployment/config-validation-report.md` | `CFG` (fixed) | `CFG` |

Rules: never create `RUN-NNN.md`, `MON-NNN.md`, `GLC-NNN.md`, etc. Each is created once and updated in place (subject to the living spec rule for Approved artifacts). `MON` and `OPR` are created in Phase 8 and revised from production data in Phase 9; revisions to an Approved version require an `SCR S-N`. Every template carries a `> **Single file.**` notice with the exact `--id` and `--out` flags to use.

## Collection files (Phase 9 operate)

Phase 9 has four collection files, one per deliverable type.

| Deliverable | Filename | Front matter `id` | Sub-ID letter | Example citation |
| --- | --- | --- | --- | --- |
| Incidents | `docs/09-operate/incidents.md` | `INC` (fixed) | `I` | `INC I-3` |
| Post-mortems | `docs/09-operate/post-mortems.md` | `PMT` (fixed) | `PM` | `PMT PM-2` |
| Feedback summaries | `docs/09-operate/feedback-summaries.md` | `FBK` (fixed) | `F` | `FBK F-1` |
| Improvement backlog | `docs/09-operate/improvement-backlog.md` | `IMP` (fixed) | `IM` | `IMP IM-4` |

Rules: never create separate `INC-NNN.md`, `PMT-NNN.md`, `FBK-NNN.md`, or `IMP-NNN.md` files. Each entry is appended as its `## TYPE X-N: [title]` section with `### ` sub-headings. Sub-IDs start at 1, are consecutive, and are never reused or renumbered after approval. `backlog-curator` cites source artifacts as `INC I-N`, `PMT PM-N`, `FBK F-N`, or `DEF D-N`. Every template carries a `> **Collection file.**` notice with the file path and section pattern.

## Cross-phase collection files and single-instance files (logs, charter, summaries)

| Deliverable | Filename | Front matter `id` | Sub-ID / note | Example citation |
| --- | --- | --- | --- | --- |
| Spec changes | `docs/logs/spec-changes.md` | `SCR` (fixed) | sub-ID letter `S` | `SCR S-2` |
| Learned rules | `docs/logs/learned-rules.md` | `LRN` (fixed) | sub-ID letter `L` | `LRN L-3` |
| Phase summaries | `docs/0N-<slug>/SUMMARY.md` | `SUM` (fixed) | single-instance per phase | `SUM` |
| Agent charter | `.ai/standards/agent-charter.md` | `CHR` (fixed) | generated; never edit directly | `CHR` |

Rules: never create `SCR-NNN.md`, `LRN-NNN.md`, or separate SCR/LRN files. Approve SCR sections with `/approve docs/logs/spec-changes.md --sub-id S-N`; approve LRN sections with `/approve docs/logs/learned-rules.md --sub-id L-N`.

## Single-instance files (Phase 5 build planning)

All Phase 5 deliverables are single-instance files per project — one of each per project. All use friendly filenames via `--out` with a fixed `--id`.

| Deliverable | Filename | Front matter `id` | Example citation |
| --- | --- | --- | --- |
| Feature breakdown | `feature-breakdown.md` | `FBD` (fixed) | `FBD` |
| Definition of Done | `definition-of-done.md` | `DOD` (fixed) | `DOD` |
| Wave plan | `wave-plan.md` | `WAV` (fixed) | `WAV` |
| Environment plan | `environment-plan.md` | `ENV` (fixed) | `ENV` |

Note: individual feature folders (`docs/05-build-plan/feature-NNN-slug/`) contain `FEAT-NNN`-keyed artifacts (plan.md, tasks.md, acceptance.md, status.md) which use numbered IDs, not fixed IDs.

## Collection files (Phase 4 design)

All Phase 4 deliverables are single-instance files per project — no collection sub-IDs. All use friendly filenames via `--out` with a fixed `--id`.

| Deliverable | Filename | Front matter `id` | Example citation |
| --- | --- | --- | --- |
| Database design | `database-design.md` | `DBD` (fixed) | `DBD` |
| API spec | `api-spec.md` | `API` (fixed) | `API` |
| OpenAPI definition | `openapi.yaml` | n/a | `docs/04-design/openapi.yaml` |
| Backend design | `backend-design.md` | `BED` (fixed) | `BED` |
| UI spec | `ui-spec.md` | `UIS` (fixed) | `UIS` |
| Permission matrix | `permission-matrix.md` | `PRM` (fixed) | `PRM` |
| Coding standards | `coding-standards.md` | `STD` (fixed) | `STD` |
| Test strategy | `test-strategy.md` | `TST` (fixed) | `TST` |

## Collection files (Phase 3 architecture)

Phase 3 has two collection files (ADRs and Spikes) and five single-instance files (all other deliverables). All use friendly filenames via `--out`.

| Deliverable | Filename | Front matter `id` | Sub-ID letter | Example citation |
| --- | --- | --- | --- | --- |
| ADRs | `adrs.md` | `ADR` (fixed) | `A` | `ADR A-3` |
| Spikes *(optional)* | `spikes.md` | `SPK` (fixed) | `S` | `SPK S-2` |
| Architecture overview | `architecture-overview.md` | `ARC` (fixed) | n/a | `ARC` |
| Technology comparison | `technology-comparison.md` | `TEC` (fixed) | n/a | `TEC` |
| Threat model | `threat-model.md` | `THR` (fixed) | n/a | `THR`; threats within use `THR T-n` |
| Deployment topology | `deployment-topology.md` | `TOP` (fixed) | n/a | `TOP` |
| Cost estimate | `cost-estimate.md` | `CST` (fixed) | n/a | `CST` |

ADR rules: sub-IDs start at A-1, are consecutive, and are never reused. A new decision is appended as the next `## ADR A-N:` section; never create a separate `ADR-NNN.md` file. A superseded ADR is marked `Superseded by ADR A-M - SCR S-N` in place.

Spike rules: all spikes live in the single collection file `docs/03-architecture/spikes.md` (id: `SPK`). Each spike is a `## Spike S-N: [Title]` section (S-1, S-2, …); sub-IDs are consecutive and never reused. A closed spike is marked `Closed - ADR A-N` in its heading. Never create a separate `SPK-NNN.md` file. A specific spike is cited as `SPK S-N`; its branch is `spike/spk-S-N-slug`.

## Collection files (Phase 2 requirements)

Phase 2 templates also produce single **collection files**, one per deliverable type. Sub-IDs use a type letter + sequence number within each file.

| Deliverable | Filename | Front matter `id` | Sub-ID letter | Example citation |
| --- | --- | --- | --- | --- |
| Epics | `epics.md` | `EPC` (fixed) | `E` | `EPC E-2` |
| User stories | `user-stories.md` | `REQ` (fixed) | `S` | `REQ S-3` |
| Acceptance criteria (inline) | within `user-stories.md` | part of `REQ` | `AC` | `REQ S-3 AC-2` |
| NFRs | `nfrs.md` | `NFR` (fixed) | `N` | `NFR N-1` |
| Business rules | `business-rules.md` | `BR` (fixed) | `B` | `BR B-4` |
| Backlog entries | `backlog.md` | `BKL` (fixed) | `BL` | `BKL BL-2` |
| Domain glossary | `domain-glossary.md` | `GLO` (fixed) | n/a | `GLO` |

Rules: sub-IDs start at 1, are consecutive, and are never reused. A new entry is appended as the next section; never create a second file for the same collection type. Agents use `--out docs/02-requirements/<filename>` when calling `new_artifact.py`. Acceptance criteria (`AC-n`) are inline within their parent story section and cited downstream as `REQ S-N AC-n` (not bare `REQ-NNN AC-n`).

## Single-instance file with sub-IDs (Phase 2 requirements)

The Product Requirement Specification is a single-instance file (one per project) that carries multiple sub-ID series within it.

| Deliverable | Filename | Front matter `id` | Sub-ID series | Example citation |
| --- | --- | --- | --- | --- |
| Product Requirement Specification | `product-requirement-specification.md` | `PRS` (fixed) | Goals: `G` · Non-Goals: `NG` · Features: `F` | `PRS G-2`, `PRS NG-1`, `PRS F-3` |

Rules: create with `python3 scripts/new_artifact.py --template product-requirement-specification --id PRS --title "<title>" --author <agent> --out docs/02-requirements/product-requirement-specification.md`. Never create a separate `PRS-NNN.md` file. Sub-IDs within each series start at 1, are consecutive, and are never reused. A dropped goal keeps its table row with `Removed - SCR S-N`; a dropped non-goal or feature keeps its row or block with `Removed - SCR S-N`. Downstream artifacts cite product goals as `PRS G-N`, non-goals as `PRS NG-N`, and features as `PRS F-N`.

## Single-instance files (Phase 1 discovery)

Two Phase 1 deliverables are single-instance artifacts with a fixed `id` (no number suffix), cited by prefix alone.

| Deliverable | Filename | Front matter `id` | Example citation |
| --- | --- | --- | --- |
| Business brief | `business-brief.md` | `BRF` (fixed) | `BRF` |
| Scope statement | `scope-statement.md` | `SCP` (fixed) | `SCP` |
| Research summary *(optional)* | `research-summary.md` | `RSM` (fixed) | `RSM` |

## Collection files (Phase 1 discovery)

Some Phase 1 templates produce a single **collection file** that holds all entries of that type. Within the file, each entry carries a sub-ID using a type letter + sequence number. These are not separate artifact files; the sub-ID is only meaningful in combination with the parent artifact ID.

| Deliverable | Filename | Front matter `id` | Sub-ID letter | Example citation |
| --- | --- | --- | --- | --- |
| Personas | `personas.md` | `PER` (fixed) | `P` | `PER P-2` |
| Phase risks | `risks.md` | `RSK` (fixed) | `R` | `RSK R-3` |
| As-is process maps | `process-maps.md` | `PRC` (fixed) | `M` | `PRC M-1` |

Rules: sub-IDs start at 1, are consecutive, and are never reused. A new entry is appended as the next section; never create a second file for the same collection type in the same phase. Agents use `--out docs/01-discovery/<filename>` when calling `new_artifact.py` so the file gets a friendly name while the `id` front matter field retains the `PREFIX-NNN` format the scripts expect.

## Front matter (required on every artifact)

`id, title, phase, version, template, template_version, status, author_agent, approver, date, validation`

- `status`: Draft | In review | Approved | Rejected (Approved and Rejected are set only by `scripts/log_approval.py`)
- `validation`: Pending | Pass | Pass with warnings | Fail | Proceeded on Fail
- `version`: `0.x` while drafting; `1.0` on first approval; bump on changes after approval (a changed approved artifact returns to Draft)

## Formats

Documents: markdown with YAML front matter. APIs: OpenAPI (`docs/04-design/openapi.yaml`). Diagrams: Mermaid. Schema: SQL. Dates: `YYYY-MM-DD`.

## Severity and status vocabularies

Finding severity: Blocker | Major | Minor. Risk tier: Standard | High | Critical. Risk status (risk register): Open | Mitigating | Closed | Accepted. Priority: Must | Should | Could | Won't (MoSCoW).
