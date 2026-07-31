# 03. Project Knowledge Sources

## Purpose

This section defines where project knowledge originates and the exact order in which it must be loaded before any engineering work begins.

Never rely on memory alone when authoritative documentation exists.

---

# Source of Truth

Project knowledge is distributed across multiple documents.

Each document has a specific responsibility.

Never treat all documents as equal.

---

## Knowledge Priority

When information overlaps or conflicts, use the following order of precedence:

1. Explicit user instructions
2. CLAUDE.md
3. Documentation in `docs/`
4. Master roadmap
5. Phase task documents
6. Existing implementation

If two authoritative sources conflict, stop and request clarification.

Never invent requirements.

---

# Mandatory Context Loading

Before beginning any implementation session, review the following in order.

## Step 1

Read:

```text
CLAUDE.md
```

Purpose:

- Load engineering behaviour
- Load workflow
- Load quality standards
- Load operating rules

---

## Step 2

Read project documentation.

Recommended order:

```text
docs/
├── 00_Project_Vision.md
├── 01_Product_Requirements.md
├── 02_System_Architecture.md
├── 03_Technology_Stack.md
├── 04_Folder_Structure.md
├── 05_Database_Design.md
├── 08_Project_Rules.md
└── 09_Coding_Standards.md
```

These documents define what the product should become.

---

## Step 3

Read:

```text
tasks/00_MASTER_ROADMAP.md
```

Determine:

- Current phase
- Upcoming milestones
- Dependencies
- Overall progress

---

## Step 4

Open the current phase directory.

Read:

- Phase README
- Current implementation task
- Related completed tasks if required

Understand the objective before writing code.

---

## Step 5

Inspect the existing implementation.

Never rewrite functionality without first understanding:

- Current architecture
- Existing abstractions
- Shared utilities
- Dependency relationships

---

# Continuous Awareness

While implementing:

Always remain aware of:

- Current phase
- Current task
- Active module
- Related documentation
- Existing implementation
- Architectural boundaries

Implementation decisions should always consider the entire project, not only the current file.

---

# Assumption Policy

If documentation answers the question:

Use the documentation.

If documentation is incomplete:

Infer conservatively.

If uncertainty affects architecture, security, or product behaviour:

Stop and request clarification.

Never guess.

---

# Repository Knowledge Maintenance

Whenever implementation changes documented behaviour:

Update the relevant documentation.

Documentation and implementation must remain synchronized.

---

# Final Principle

Professional engineers understand a system before changing it.

Understanding precedes implementation.

Documentation precedes assumptions.

Consistency precedes speed.
