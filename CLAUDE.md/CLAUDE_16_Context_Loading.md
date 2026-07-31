# 16. Context Loading

## Purpose

This section defines the mandatory process for loading project context before starting or resuming work.

Correct engineering decisions depend on complete and accurate context.

Never begin implementation without first understanding the current state of the project.

---

# Core Principle

Always understand before acting.

Load context in a consistent order so that implementation decisions remain aligned with the project's documentation and architecture.

---

# Mandatory Context Loading Order

Every new session should load context in the following sequence.

## Step 1 — AI Operating Manual

Read:

```text
CLAUDE.md
```

Load:

- Engineering behaviour
- Workflow
- Architecture rules
- Coding standards
- Decision framework

---

## Step 2 — Project Documentation

Review the relevant documents in:

```text
docs/
```

Prioritize:

- Project Vision
- Product Requirements
- System Architecture
- Technology Stack
- Folder Structure
- Coding Standards
- Project Rules

Only load documents relevant to the current task when the project becomes large.

---

## Step 3 — Master Roadmap

Read:

```text
tasks/00_MASTER_ROADMAP.md
```

Determine:

- Current phase
- Completed milestones
- Remaining work
- Task dependencies

---

## Step 4 — Active Task

Read the current implementation task completely.

Understand:

- Objective
- Acceptance criteria
- Dependencies
- Verification requirements

Do not begin implementation until the task is fully understood.

---

## Step 5 — Existing Code

Inspect the relevant implementation.

Identify:

- Existing abstractions
- Shared utilities
- Dependencies
- Extension points

Reuse existing code whenever appropriate.

---

# Context Recovery

When returning after a break or beginning a new conversation:

1. Reload this operating manual.
2. Review the roadmap.
3. Read the active task.
4. Inspect recently modified files.
5. Continue from the last verified state.

Do not rely solely on previous conversation memory.

---

# Missing Context

If essential project context cannot be determined:

- Pause implementation.
- Explain what information is missing.
- Request the required files or clarification.

Avoid making architectural assumptions.

---

# Final Principle

Reliable engineering begins with reliable context.

Load the right information first, then make implementation decisions.
