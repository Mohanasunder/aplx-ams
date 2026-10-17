---
id: ADR
title: Use PostgreSQL as the primary datastore
phase: 3
version: 0.1
template: adr
template_version: 1.0
status: Draft
author_agent: solution-architect
approver: Architect / tech lead
date: 2026-10-05
validation: Pass
---

# Use PostgreSQL as the primary datastore

## Input References
NFR v1.0 (p95 latency), NFR-002 v1.0 (audit history), TEC v1.0 (technology comparison).

## Purpose And Scope
Records the choice of primary datastore for the ticketing system. Excludes search and caching, which are decided separately.

## Status And Date
Accepted pending approval, 2026-10-05.

## Context
The system stores tickets, comments, and an audit trail with relational integrity. Expected volume is 50,000 tickets per year. The team has strong relational experience and the approved technology list includes PostgreSQL and MongoDB.

## Options Considered
1. PostgreSQL: relational integrity, transactions, mature tooling; vertical scaling is sufficient at the expected volume.
2. MongoDB: flexible documents; weaker multi-document transactions for the audit trail and less team experience.

## Decision
PostgreSQL. It meets NFR at the expected volume and gives transactional integrity for the audit trail.

## Consequences
Positive: strong integrity, familiar tooling. Negative: schema changes need migrations. Follow-up: DBD defines the schema; revisit if volume exceeds 10 times the estimate.

## Assumptions
A-002: annual volume stays under 500,000 tickets for the first three years.

## Open Questions
None open; OQ-007 (hosting region) is answered in TOP.

## Traceability Links
Upstream: NFR, NFR-002, TEC. Downstream: DBD, TOP.

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
