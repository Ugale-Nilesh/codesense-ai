# 17. Session Continuity

## Purpose

This section defines how work should continue across multiple development sessions without losing context or repeating completed work.

Long-running software projects require continuity, consistency, and reliable progress.

---

# Core Principle

Treat every new session as a continuation of the same engineering project.

Do not restart analysis from scratch when sufficient project documentation exists.

Recover context before taking action.

---

# Session Startup

At the beginning of every new session:

1. Read `CLAUDE.md`.
2. Load the relevant project documentation.
3. Read `tasks/00_MASTER_ROADMAP.md`.
4. Identify the active phase.
5. Identify the first incomplete task.
6. Inspect recently modified files.
7. Resume from the last verified state.

Never assume conversation memory is complete.

---

# Progress Recovery

Before implementing new work, determine:

- Current project phase
- Last completed task
- Active implementation
- Outstanding blockers
- Pending documentation updates

Resume only after confirming the project state.

---

# Avoid Duplicate Work

Before creating or modifying code:

- Search for existing implementations.
- Check whether the task is already complete.
- Avoid recreating files or utilities.
- Reuse existing modules whenever appropriate.

---

# Session Handoff

At the end of each implementation session, provide:

## Completed Work

Summarize what was finished.

## Files Changed

List created and modified files.

## Verification

Describe how the implementation was validated.

## Outstanding Work

List remaining tasks or blockers.

## Recommended Next Step

Identify the next logical engineering task.

This summary should make it easy to resume work later.

---

# Interrupted Sessions

If a session ends unexpectedly:

- Reload project context.
- Compare documentation with the repository.
- Continue from the last verified implementation.
- Do not repeat completed work unless verification indicates it is necessary.

---

# Repository as Memory

Treat the repository—not the chat history—as the primary memory of the project.

Project documentation, roadmap, tasks, and source code collectively define the current state.

---

# Final Principle

Reliable engineering depends on reliable continuity.

Every new session should resume from verified project state, preserve previous progress, and move the project forward without unnecessary repetition.
