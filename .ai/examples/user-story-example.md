---
id: REQ
title: Customer raises a support ticket
phase: 2
version: 0.1
template: user-story
template_version: 1.0
status: Draft
author_agent: requirements-analyst
approver: Product owner / BA
date: 2026-10-05
validation: Pass
---

# Customer raises a support ticket

## Input References
BRF v1.0 (business brief), PER v1.0 (persona: support customer), SCP v1.0 (scope statement).

## Purpose And Scope
Lets a signed-in customer report a problem so support can triage it. Covers creating a ticket with a title, description, and category. Excludes attachments (see REQ-004) and email-to-ticket.

## Story Statement
As a signed-in customer, I want to raise a support ticket describing my problem, so that support can triage and resolve it without me phoning in.

## Acceptance Criteria
1. Given a signed-in customer on the new-ticket page, when they submit a title (5 to 120 characters), a description (10 to 4000 characters), and a category, then a ticket is created with status "New" and the customer sees its ticket number.
2. Given a signed-in customer, when they submit with a missing title or description, then no ticket is created and the field-level error from the shared error model is shown.
3. Given an anonymous visitor, when they open the new-ticket page, then they are redirected to sign in.
4. Given a customer submits the form twice within 5 seconds with the same content, then only one ticket is created.

## Business Rules
BR: every ticket has exactly one category from the configured list.

## NFR References
NFR: ticket creation responds in under 400 ms at p95 with 200 concurrent users.

## Priority
Must: it is the entry point of the support flow and a prerequisite for triage.

## Assumptions
A-001: the category list is managed by administrators and has at most 20 entries (to be confirmed, OQ-003).

## Open Questions
OQ-003: who maintains the category list and how often does it change?

## Traceability Links
Upstream: BRF, PER, SCP. Downstream: API (POST /tickets), DBD, UIS, FEAT-004.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
