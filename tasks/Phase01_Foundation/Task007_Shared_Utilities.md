# Task007 – Shared Utilities

## Task Information

| Field | Value |
|-------|-------|
| Phase | Phase 01 – Foundation |
| Task ID | Task007 |
| Priority | High |
| Estimated Time | 90–120 minutes |
| Status | Planned |

---

# Objective

Design and implement a shared utilities layer that provides reusable helper functions, constants, validators, custom exceptions, logging utilities, and common abstractions for both the backend and frontend.

The purpose of this task is to eliminate duplicated code, improve maintainability, and establish reusable building blocks for future development.

No business-specific logic should be introduced during this task.

---

# Business Context

As CodeSense AI grows, multiple modules—including authentication, AI services, GitHub integration, project management, and analytics—will require common functionality.

Instead of reimplementing these utilities throughout the codebase, a centralized utilities layer promotes consistency and simplifies maintenance.

---

# Technical Context

Shared utilities are foundational components that support application development without depending on any specific feature.

These utilities should remain:

- Independent
- Reusable
- Lightweight
- Well documented
- Fully testable

Feature-specific logic must never be placed in the utilities layer.

---

# Prerequisites

Completed Tasks

- ✅ Task001 – Initialize Repository Structure
- ✅ Task002 – Setup Development Environment
- ✅ Task003 – Backend Project Setup
- ✅ Task004 – Frontend Project Setup
- ✅ Task005 – Configure Code Quality Tooling
- ✅ Task006 – Environment Configuration

Reference Documents

- docs/02_System_Architecture.md
- docs/04_Folder_Structure.md
- docs/09_Coding_Standards.md

---

# Scope

## In Scope

Backend

- Logger
- Response helpers
- Exception classes
- Constants
- Validators
- Utility functions
- Time helpers
- File helpers

Frontend

- Constants
- Utility functions
- Formatters
- Validation helpers
- API helper functions

---

## Out of Scope

- Authentication logic
- AI processing
- Database queries
- Business rules
- API endpoints

---

# Folder Changes

Backend

```text
backend/
└── app/
    └── utils/
        ├── constants.py
        ├── logger.py
        ├── validators.py
        ├── exceptions.py
        ├── helpers.py
        ├── file_utils.py
        ├── time_utils.py
        └── __init__.py
```

Frontend

```text
frontend/
└── src/
    └── utils/
        ├── constants.ts
        ├── validators.ts
        ├── formatters.ts
        ├── helpers.ts
        ├── api.ts
        └── index.ts
```

---

# Files To Create

Backend

- constants.py
- logger.py
- validators.py
- exceptions.py
- helpers.py
- file_utils.py
- time_utils.py

Frontend

- constants.ts
- validators.ts
- formatters.ts
- helpers.ts
- api.ts

---

# Utility Categories

## Backend

### Logger

Responsibilities

- Centralized logging
- Error logging
- Warning logging
- Debug logging

---

### Validators

Examples

- Email validation
- Username validation
- File validation
- UUID validation

---

### Exceptions

Custom exceptions

- ValidationError
- AuthenticationError
- AuthorizationError
- AIServiceError
- GitHubIntegrationError
- FileProcessingError

---

### Constants

Examples

- Supported file extensions
- Maximum upload size
- API version
- Default pagination values

---

### File Utilities

Examples

- Safe filename generation
- Extension extraction
- File size conversion
- Directory creation

---

### Time Utilities

Examples

- UTC timestamps
- Date formatting
- Time conversion

---

# Frontend Utilities

## Validators

Examples

- Email
- Password
- URL
- Empty values

---

## Formatters

Examples

- File size
- Date
- Time
- Percentage

---

## API Helpers

Responsibilities

- API URL builder
- Request headers
- Response parsing
- Error formatting

---

# Design Principles

Utilities should

- Have no business logic
- Be reusable
- Be modular
- Have single responsibility
- Be independently testable

---

# Implementation Steps

## Step 1

Create backend utility directory.

---

## Step 2

Create frontend utility directory.

---

## Step 3

Implement logging utilities.

---

## Step 4

Implement validation helpers.

---

## Step 5

Implement constants.

---

## Step 6

Implement custom exceptions.

---

## Step 7

Implement helper functions.

---

## Step 8

Export reusable utilities.

---

## Step 9

Verify imports across the project.

---

# Verification

Backend

- Logger imports successfully.
- Validators execute.
- Constants accessible.
- Exceptions import correctly.

Frontend

- Utility imports compile.
- Helper functions accessible.
- Formatters execute.

---

# Expected Output

Backend

- Shared utilities available.
- Logging operational.
- Validation operational.

Frontend

- Formatting utilities available.
- Validation utilities available.
- API helper available.

---

# Deliverables

Backend

- Logging utilities
- Validators
- Constants
- Exceptions
- File helpers
- Time helpers

Frontend

- Shared helpers
- Validators
- Formatters
- API helpers

---

# Acceptance Criteria

- Utilities contain no feature-specific logic.
- Backend utilities import without errors.
- Frontend utilities compile successfully.
- Constants are centralized.
- Logging is functional.
- Validators are reusable.

---

# Manual Testing Checklist

- [ ] Logger works
- [ ] Validators work
- [ ] Constants accessible
- [ ] Exceptions usable
- [ ] Helper functions import correctly
- [ ] Frontend builds successfully

---

# AI Implementation Notes

When implementing this task:

- Never place business logic inside utilities.
- Prefer pure functions whenever possible.
- Avoid circular imports.
- Group related utilities together.
- Keep each file focused on a single responsibility.
- Document every public utility function.
- Use descriptive names instead of abbreviations.
- Write utilities to be framework-agnostic where practical.

---

# Troubleshooting

## Circular imports

Move shared functionality into a lower-level utility module.

---

## Duplicate helpers

Merge overlapping functionality instead of creating multiple versions.

---

## Oversized utility files

Split utilities by responsibility rather than allowing a single file to grow excessively.

---

# Rollback

If issues arise:

1. Remove newly added utility modules.
2. Restore previous project state.
3. Reintroduce utilities incrementally.
4. Verify imports after each addition.

---

# Definition of Done

This task is complete when:

- Backend utilities are organized.
- Frontend utilities are organized.
- Shared abstractions exist.
- Logging works.
- Validation helpers exist.
- Constants are centralized.
- Utilities are documented.
- No feature-specific logic exists inside the utilities layer.

---

# Suggested Commit Message

```text
feat(core): establish shared utility layer
```

---

# Next Task

Task008 – Project Verification
