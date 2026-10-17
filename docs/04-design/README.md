# Phase 4: Solution Design

Specify the schema, APIs, backend and UI design, permissions, coding standards, and test strategy that builders will follow.

- **Command:** `/run-design`
- **Human approver:** Tech lead + UX
- **Output folder:** `docs/04-design/`

## Required inputs

- Approved architecture, ADRs, and stack
- Approved requirements and acceptance criteria
- Brand and UX guidelines or design system
- Existing database schemas (for migrations)
- Third-party API documentation
- Role and permission definitions
- Organization coding standards

## Producer agents

- `database-designer`
- `api-designer`
- `backend-designer`
- `ux-ui-designer`
- `standards-author`

## Deliverable templates

- `.ai/templates/database-design.md`
- `.ai/templates/api-spec.md`
- `.ai/templates/backend-design.md`
- `.ai/templates/ui-spec.md`
- `.ai/templates/permission-matrix.md`
- `.ai/templates/coding-standards.md`
- `.ai/templates/test-strategy.md`

## How it runs

database-designer and api-designer in parallel; then backend-designer (backend design, permission matrix) and ux-ui-designer; standards-author last (coding standards, automated gate commands, test strategy). The checker applies the design consistency rules across all artifacts. standards-author also fills the project-specific files in .ai/standards that builders, testers, and reviewers read.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
