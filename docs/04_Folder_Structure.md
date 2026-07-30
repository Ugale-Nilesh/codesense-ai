# 04_Folder_Structure.md

# CodeSense AI

## Project Folder Structure

**Version:** 1.0\
**Status:** Engineering Baseline

------------------------------------------------------------------------

# Purpose

This document defines the canonical repository structure. Every
contributor and AI coding assistant (Claude) must follow this layout.
New features should extend existing modules rather than introduce
parallel structures.

------------------------------------------------------------------------

# Repository Layout

``` text
codesense-ai/
├── docs/                 # Engineering documentation
├── tasks/                # Implementation specifications
├── frontend/             # Next.js application
├── backend/              # Backend services
├── .github/              # CI/CD workflows
├── docker/               # Container configs
├── scripts/              # Utility scripts
├── README.md
├── LICENSE
└── .gitignore
```

------------------------------------------------------------------------

# Frontend Structure

``` text
frontend/
├── app/
├── components/
│   ├── common/
│   ├── layout/
│   ├── debug/
│   ├── optimize/
│   ├── review/
│   ├── learn/
│   └── productivity/
├── features/
├── hooks/
├── lib/
├── services/
├── store/
├── styles/
├── types/
└── utils/
```

Guidelines:

-   Components remain presentation-focused.
-   Business logic belongs in services/features.
-   Shared utilities live in `utils`.
-   Reusable UI belongs in `components/common`.

------------------------------------------------------------------------

# Backend Structure

``` text
backend/
├── src/
│   ├── modules/
│   │   ├── auth/
│   │   ├── users/
│   │   ├── debug/
│   │   ├── optimize/
│   │   ├── review/
│   │   ├── learn/
│   │   ├── productivity/
│   │   ├── github/
│   │   ├── files/
│   │   └── reports/
│   ├── common/
│   ├── config/
│   ├── database/
│   └── main.ts
├── prisma/
├── tests/
└── package.json
```

Rules:

-   Each module owns its controllers, services, DTOs and tests.
-   Cross-module communication occurs through service interfaces.
-   Shared utilities belong in `common`.

------------------------------------------------------------------------

# Documentation

``` text
docs/
00_Project_Vision.md
01_Product_Requirements.md
02_System_Architecture.md
03_Technology_Stack.md
04_Folder_Structure.md
05_Database_Design.md
...
16_Claude_Workflow.md
```

------------------------------------------------------------------------

# Tasks

``` text
tasks/
├── Phase01/
├── Phase02/
├── Phase03/
└── ...
```

Each phase contains atomic implementation tasks with acceptance
criteria.

------------------------------------------------------------------------

# Naming Conventions

-   kebab-case: folders
-   PascalCase: React components
-   camelCase: variables/functions
-   SCREAMING_SNAKE_CASE: constants

------------------------------------------------------------------------

# File Ownership

  Area       Owner
  ---------- ------------------------
  docs       ChatGPT (Architecture)
  tasks      ChatGPT (Planning)
  frontend   Claude
  backend    Claude

------------------------------------------------------------------------

# Architectural Rules

1.  No business logic inside UI components.
2.  No circular module dependencies.
3.  Every feature must have tests.
4.  Every API must be documented.
5.  New features require updates to documentation.

------------------------------------------------------------------------

# Related Documents

-   02_System_Architecture.md
-   03_Technology_Stack.md
-   05_Database_Design.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- --------------------------
  1.0       July 2026   Initial folder structure
