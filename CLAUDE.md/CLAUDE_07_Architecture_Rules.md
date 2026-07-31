# 07. Architecture Rules

## Purpose

This section defines the architectural rules that govern every implementation in the CodeSense AI repository.

Architecture is a long-term asset. Every engineering decision must preserve its integrity.

Do not alter the architecture unless the user explicitly approves the change.

---

# Architectural Philosophy

The project follows a modular, layered architecture.

Every layer has a defined responsibility.

Dependencies should flow inward toward business logic.

Avoid tightly coupled modules.

---

# Layer Responsibilities

## Presentation Layer

Frontend user interface.

Responsibilities:

- Pages
- Components
- Layouts
- User interactions
- Client-side state

Never place business logic here.

---

## API Layer

Backend request handling.

Responsibilities:

- Routing
- Validation
- Authentication hooks
- Response formatting

API routes should remain thin.

---

## Service Layer

Contains application and business logic.

Responsibilities:

- Business rules
- AI orchestration
- Repository coordination
- Workflow execution

Business logic belongs here.

---

## Data Layer

Responsibilities:

- Database models
- Repositories
- Persistence
- External storage

No UI logic or business rules belong here.

---

# Separation of Concerns

Keep responsibilities isolated.

Do not mix:

- UI with business logic
- Business logic with persistence
- Infrastructure with domain behaviour

---

# Dependency Rules

Allowed dependency direction:

Presentation
→ API
→ Services
→ Data

Never reverse dependency direction.

Avoid circular dependencies.

---

# Backend Rules

Backend modules should remain small, cohesive, and reusable.

Prefer:

- Services
- Utilities
- Dependency injection
- Configuration modules

Avoid large monolithic files.

---

# Frontend Rules

Frontend should be component driven.

Prefer:

- Reusable UI components
- Shared hooks
- Shared utilities
- Consistent state management

Avoid duplicated UI logic.

---

# File Organization

Create new files only when they improve modularity.

Avoid unnecessary nesting.

Prefer meaningful names over abbreviations.

---

# Naming Conventions

Use descriptive names.

Examples:

- UserService
- ProjectRepository
- AIReviewEngine

Avoid ambiguous names such as:

- Helper1
- Temp
- Utils2

---

# Refactoring Policy

Refactor only when:

- Readability improves
- Duplication is reduced
- Architecture becomes cleaner
- Existing behaviour is preserved

Never refactor unrelated modules during feature implementation.

---

# Forbidden Changes

Do not without approval:

- Rename top-level folders
- Replace frameworks
- Introduce new architectural patterns
- Change project structure
- Remove existing modules

---

# Architectural Review Checklist

Before completing any implementation verify:

- Responsibilities remain separated.
- Dependencies remain correct.
- No unnecessary coupling introduced.
- Existing abstractions reused.
- Folder structure respected.

---

# Final Principle

Every implementation must strengthen the architecture.

If a decision improves today's task but weakens tomorrow's maintainability, reject it.
