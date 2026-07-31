# 11. Git Workflow

## Purpose

This section defines how source control is managed throughout the CodeSense AI project.

Every change should be traceable, reviewable, and reversible.

---

# Core Principles

Use Git as the single source of version history.

Every commit should represent one logical unit of work.

Never mix unrelated changes in the same commit.

---

# Branch Strategy

Default branch:

```text
main
```

Feature work should normally be completed in dedicated branches when collaborating.

For this project, follow the user's preferred workflow.

Do not create or rename branches unless instructed.

---

# Commit Philosophy

Commit only after:

- Implementation is complete.
- Verification has passed.
- The repository builds successfully.
- Documentation is updated when required.

Avoid committing incomplete or broken work.

---

# Commit Messages

Use Conventional Commits.

Examples:

```text
feat(auth): add JWT authentication

fix(api): resolve validation error

refactor(services): simplify AI orchestration

docs(tasks): update Phase01 completion

test(core): add repository tests

chore(config): update lint configuration
```

---

# Repository Hygiene

Before recommending a commit:

- Remove dead code.
- Remove debugging statements.
- Remove unused imports.
- Verify formatting.
- Verify linting.

Never commit secrets or credentials.

---

# Change Summary

After implementation provide:

## Files Created

List all new files.

## Files Modified

List all modified files.

## Breaking Changes

Explicitly state whether breaking changes exist.

## Verification

Summarize how the work was validated.

---

# Version Control Rules

Always:

- Keep commits focused.
- Preserve history.
- Respect existing project structure.

Never:

- Rewrite history without approval.
- Delete unrelated files.
- Commit generated secrets.
- Commit temporary artifacts.

---

# Suggested Workflow

1. Complete implementation.
2. Verify correctness.
3. Review changed files.
4. Prepare a commit message.
5. Commit.
6. Push when instructed by the user.

---

# Final Principle

Version control is part of software engineering.

Every commit should improve the repository and make future maintenance easier.
