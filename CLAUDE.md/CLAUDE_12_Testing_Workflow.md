# 12. Testing Workflow

## Purpose

This section defines the minimum verification process required before any implementation is considered complete.

Writing code is only one part of software engineering.

Every change must be validated.

---

# Testing Philosophy

Every implementation should be:

- Correct
- Stable
- Reproducible
- Maintainable

Never assume code works because it compiles.

Always verify behaviour.

---

# Verification Levels

Every completed task should pass the following checks where applicable.

## Level 1 — Static Validation

Verify:

- No syntax errors
- Imports resolve correctly
- Formatting is correct
- Linting passes
- Type checking passes

---

## Level 2 — Functional Validation

Confirm:

- Feature behaves as expected
- Acceptance criteria are satisfied
- Existing functionality is unaffected

---

## Level 3 — Integration Validation

Ensure new code integrates cleanly with:

- Existing modules
- Shared utilities
- APIs
- Data models
- Configuration

---

## Level 4 — Manual Verification

Where automated testing is unavailable:

- Execute the relevant workflow.
- Inspect outputs.
- Confirm expected behaviour.
- Record any limitations.

---

# Regression Awareness

Before completing work, consider whether the implementation could unintentionally affect existing behaviour.

If risk exists:

- Test related functionality.
- Document any known limitations.

---

# Build Validation

When applicable verify:

- Backend starts successfully.
- Frontend builds successfully.
- Dependencies resolve.
- No runtime errors occur during startup.

---

# Completion Checklist

Before reporting success confirm:

- Requirements implemented
- Verification completed
- No obvious regressions
- Documentation updated when required
- Repository remains buildable

---

# Reporting

After verification provide:

## Validation Summary

Briefly describe what was verified.

## Remaining Risks

List known limitations or assumptions.

## Recommended Next Step

Identify the next logical implementation task.

---

# Final Principle

A feature is not complete when the code is written.

A feature is complete only after it has been verified with reasonable confidence.
