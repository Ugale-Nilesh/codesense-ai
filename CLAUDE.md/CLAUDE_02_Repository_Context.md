# 02. Repository Context

## Purpose

Before implementing any feature, modifying any file, or making any engineering decision, develop a complete understanding of the repository.

Never begin implementation immediately after receiving a request.

Understand the current state of the project before changing it.

The repository is the single source of truth for implementation.

---

# Repository Overview

The repository is divided into clearly defined areas.

Each directory has a single responsibility.

Never mix responsibilities between directories.

---

# Root Directory

```text
codesense-ai/
├── backend/
├── frontend/
├── docs/
├── tasks/
├── README.md
├── CLAUDE.md
└── .gitignore
```

The root should remain clean and contain only project-level files.

---

# backend/

Purpose:

Contains the complete server-side application.

Responsibilities include:

- Business logic
- API endpoints
- Authentication
- AI orchestration
- Database access
- Background jobs
- Core services
- Shared backend utilities

No frontend code belongs here.

---

# frontend/

Purpose:

Contains the complete client-side application.

Responsibilities include:

- User interface
- Dashboard
- AI chat
- Code review screens
- Project explorer
- Authentication UI
- API communication
- Client-side state management

No backend implementation belongs here.

---

# docs/

Purpose:

Permanent project knowledge.

Contains:

- Vision
- Product requirements
- Architecture
- Technology stack
- Folder structure
- Database design
- Coding standards
- Project rules

Documentation defines the intended system.

Implementation should follow documentation whenever possible.

---

# tasks/

Purpose:

Implementation specifications.

Tasks define:

- Objectives
- Scope
- Implementation steps
- Acceptance criteria
- Verification
- Completion requirements

Tasks describe what to build.

They do not redefine architecture.

---

# CLAUDE.md

Purpose:

Defines your operating procedures.

It specifies:

- How to think
- How to make decisions
- How to navigate the repository
- How to implement work
- How to maintain quality

This document defines behaviour.

---

# Repository Rules

Always:

- Respect the documented folder structure.
- Keep responsibilities separated.
- Reuse existing modules before creating new ones.
- Avoid duplicate implementations.
- Maintain consistency across the repository.

Never:

- Rename core directories.
- Move architectural components without approval.
- Create parallel implementations for the same responsibility.

---

# Repository Navigation Strategy

Before implementing anything:

1. Read CLAUDE.md.
2. Load relevant project documentation.
3. Review the roadmap.
4. Locate the current implementation task.
5. Inspect existing code.
6. Identify dependencies.
7. Begin implementation.

Never skip repository analysis.

---

# Repository Awareness

Always know:

- Current development phase
- Current task
- Completed work
- Pending work
- Existing implementation
- Architectural boundaries

Every change should fit naturally into the existing system.

---

# Final Principle

A professional engineer understands the system before changing it.

Understand first.

Implement second.

Refactor third.

Document throughout.
