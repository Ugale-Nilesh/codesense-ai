# 13. Documentation Workflow

## Purpose

This section defines how documentation is created, maintained, and synchronized throughout the lifecycle of CodeSense AI.

Documentation is treated as a first-class engineering artifact, not an afterthought.

---

# Documentation Philosophy

Documentation should be:

- Accurate
- Current
- Concise
- Actionable
- Consistent

Never allow implementation and documentation to diverge.

---

# Source Documents

The repository documentation is organized into:

- `docs/` — Permanent project knowledge
- `tasks/` — Implementation specifications
- `README.md` — Repository overview
- `CLAUDE.md` — AI engineering operating manual

Each serves a different purpose and should not duplicate the others unnecessarily.

---

# When Documentation Must Be Updated

Update documentation whenever:

- A feature changes user-visible behavior.
- Architecture changes.
- Folder structure changes.
- APIs change.
- Environment setup changes.
- A completed task materially changes implementation details.

Do not update documentation for insignificant internal refactors.

---

# Documentation Responsibilities

## docs/

Contains long-lived project knowledge.

Examples:

- Vision
- Requirements
- Architecture
- Technology stack
- Coding standards

## tasks/

Tracks implementation work.

Each task should accurately reflect:

- Status
- Scope
- Deliverables
- Acceptance criteria

---

# Synchronization Rules

Whenever implementation changes documented behaviour:

1. Identify affected documents.
2. Update only the relevant sections.
3. Preserve formatting and structure.
4. Avoid introducing conflicting information.

---

# Documentation Quality

Every document should:

- Have a clear purpose.
- Be well structured.
- Use consistent terminology.
- Avoid unnecessary repetition.
- Be easy for a new contributor to understand.

---

# Completion Checklist

Before considering documentation complete:

- Implementation matches documentation.
- Task status is accurate.
- References remain valid.
- No contradictory information exists.

---

# Reporting

If documentation is updated, include:

- Files updated
- Reason for the update
- Summary of changes

---

# Final Principle

Good documentation reduces future engineering effort.

Keep documentation synchronized with implementation so the repository remains trustworthy over time.
