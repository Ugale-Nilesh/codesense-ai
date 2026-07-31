# 06. Task Execution Engine

## Purpose

This section defines the operational process for executing implementation tasks from the project roadmap.

Every task must be treated as an engineering specification, not merely a coding request.

---

# Guiding Principle

A task is complete only when:

- Requirements are implemented.
- Code is verified.
- Architecture is preserved.
- Documentation remains accurate.
- The repository is left in a better state than before.

---

# Task Discovery

Before beginning work:

1. Read `tasks/00_MASTER_ROADMAP.md`.
2. Identify the current project phase.
3. Locate the first task that is not completed.
4. Read the complete task specification.
5. Verify prerequisite tasks are complete.

Never skip dependencies.

---

# Task Analysis

Before writing code, identify:

- Objective
- Scope
- Files to create
- Files to modify
- Dependencies
- Acceptance criteria
- Verification steps

If information is missing, ask before implementing.

---

# Implementation Strategy

Break every task into smaller engineering steps.

Example:

1. Prepare folders.
2. Create core files.
3. Implement functionality.
4. Add validation and error handling.
5. Verify behaviour.
6. Update documentation if required.

Avoid attempting large unrelated changes in a single step.

---

# Existing Code Policy

Before creating any new module:

- Search for similar functionality.
- Reuse existing abstractions.
- Extend existing modules where appropriate.

Avoid duplicate implementations.

---

# Completion Checklist

Before declaring a task complete, confirm:

- All acceptance criteria are satisfied.
- Code builds successfully.
- Imports resolve correctly.
- Existing behaviour is preserved.
- Formatting and linting requirements are met.
- Documentation reflects the implementation.

---

# Reporting Format

After each completed task provide:

## Summary

A concise description of what was implemented.

## Files Created

List every new file.

## Files Modified

List every modified file.

## Verification

Explain how the implementation was validated.

## Risks

Mention any remaining limitations or assumptions.

## Suggested Next Task

Recommend the next logical implementation step.

---

# Escalation Rules

Pause and request user input if:

- Product requirements are ambiguous.
- An architectural change is required.
- A destructive action is proposed.
- Security implications are unclear.
- Credentials or secrets are required.

Never guess in these situations.

---

# Final Principle

Treat every task as a professional engineering deliverable.

Finish completely.

Verify thoroughly.

Then move to the next task with confidence.
