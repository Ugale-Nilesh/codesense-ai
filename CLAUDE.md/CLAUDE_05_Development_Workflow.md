# 05. Development Workflow

## Purpose

This section defines the standard engineering workflow to be followed during every development session.

The objective is to ensure that all implementation work is predictable, traceable, maintainable, and aligned with the project's architecture.

Never begin coding immediately after receiving a request.

Always follow the complete workflow.

---

# Standard Development Lifecycle

Every implementation session must follow the sequence below.

1. Load project context.
2. Understand the current repository state.
3. Identify the next implementation task.
4. Validate dependencies.
5. Design the implementation.
6. Implement the solution.
7. Verify correctness.
8. Document changes.
9. Report completion.
10. Await the next instruction or continue when appropriate.

---

# Phase 1 — Context Loading

Before writing code:

- Read CLAUDE.md
- Load relevant documentation
- Review the current roadmap
- Read the active task
- Inspect related source code

Do not skip context loading.

---

# Phase 2 — Repository Analysis

Understand:

- Existing architecture
- Current implementation
- Dependencies
- Reusable modules
- Project conventions

Avoid duplicate implementations whenever possible.

---

# Phase 3 — Task Selection

Determine the next logical task by consulting:

1. Master Roadmap
2. Current Phase
3. Active Task
4. Repository State

Never implement work outside the roadmap unless explicitly instructed.

---

# Phase 4 — Implementation Planning

Before modifying code:

- Identify affected modules.
- Determine dependencies.
- Consider edge cases.
- Minimize architectural impact.

Think before implementing.

---

# Phase 5 — Implementation

During implementation:

- Follow documented architecture.
- Write production-ready code.
- Prefer reusable components.
- Maintain consistent style.
- Keep functions focused.
- Avoid unnecessary complexity.

---

# Phase 6 — Verification

Before considering the work complete:

Verify:

- Build succeeds
- No syntax errors
- Imports resolve
- Existing functionality remains intact
- Acceptance criteria satisfied

Do not declare success without verification.

---

# Phase 7 — Documentation

If implementation changes documented behaviour:

- Update relevant documentation.
- Update task status where appropriate.
- Keep documentation synchronized with implementation.

---

# Phase 8 — Completion Report

Every completed implementation should include:

## Files Created

List all new files.

## Files Modified

List all modified files.

## Summary

Briefly explain the implementation.

## Verification

Describe how the implementation was validated.

## Next Recommended Task

Recommend the next logical implementation step.

---

# Engineering Behaviour

Always:

- Think before coding.
- Understand before modifying.
- Reuse before creating.
- Verify before completing.
- Document before finishing.

---

# Workflow Rules

Never:

- Skip verification.
- Ignore documentation.
- Break architecture.
- Leave incomplete implementations.
- Mark work complete without validation.

---

# Final Principle

The development workflow exists to produce reliable software.

Speed is valuable only when quality is preserved.

Every completed task should leave the repository in a better state than before.
