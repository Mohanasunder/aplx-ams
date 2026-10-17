---
id: UAT
id_prefix: UAT
title: <fill: title>
phase: 7
version: 0.1
template: uat-signoff
template_version: 1.1
status: Draft
author_agent: <fill: agent name>
approver: QA lead
default_approver: QA lead
default_folder: docs/07-testing
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved): the stories (REQ S-N), the UI spec (UIS) whose Pages And Routes defines the user-facing stories, the test plan (TPL), and the newest test execution report (TER) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Participants
<!-- guidance: Names and roles of the real users or stakeholders who run the scenarios -->
<fill: participants>

## Scenarios
<!-- guidance: The UAT script. Table: scenario ID (UAT S-n), story and criteria covered ('REQ S-N AC-n', one or more), steps a user follows in the running system, expected result (from the criteria's Then clauses, in business terms from the domain glossary), tester, result (Pass | Fail | Not run), notes (a Fail cites its DEF D-N). Draft at least one scenario per user-facing story (every story ID in the UI spec's Pages And Routes), covering its main path and at least one error path from its criteria. Scenarios supplied by participants are added as extra rows and still cite the criteria they exercise, or 'No criterion - exploratory'. Agents draft every column except tester, result, and notes; those are recorded from what the participants report -->
<fill: scenarios>

## Coverage
<!-- guidance: Table: each user-facing story (REQ S-N), its scenario IDs, and its result (all Pass, Fail, or Not run). A user-facing story with no scenario is a gap to fix before UAT starts -->
<fill: coverage>

## Outcome
<!-- guidance: Accepted | Accepted with conditions | Rejected. Accepted only when every scenario has run and every Fail has a defect report whose severity the QA lead accepted for release; list any conditions -->
<fill: outcome>

## Sign-off
<!-- guidance: Named human sign-off (recorded via /approve) -->
<fill: sign-off>

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every user-facing story has at least one scenario, including an error path
- [ ] Every scenario cites the criteria it exercises (or is marked exploratory)
- [ ] Every Fail cites a defect report
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
