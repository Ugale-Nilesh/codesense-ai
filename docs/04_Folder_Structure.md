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
├── ai/                   # AI development prompts and workflows
├── CLAUDE.md/             # AI engineering operating manual
├── frontend/             # React + Vite application
├── backend/              # FastAPI application
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
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── common/
│   │   ├── layout/
│   │   ├── debug/
│   │   ├── optimize/
│   │   ├── review/
│   │   ├── learn/
│   │   └── productivity/
│   ├── features/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── routes/
│   ├── services/
│   ├── styles/
│   ├── types/
│   ├── utils/
│   ├── store/            # Zustand stores
│   ├── App.tsx
│   └── main.tsx
├── .env.example
├── package.json
├── vite.config.ts
└── tsconfig.json
```

Guidelines:

-   Components remain presentation-focused.
-   Business logic belongs in services/features.
-   Server state (API data) is managed with TanStack Query; client-only state lives in Zustand stores under `store/`.
-   Shared utilities live in `utils`.
-   Reusable UI belongs in `components/common`.
-   Routing is handled with React Router; route definitions live in `routes/`.

------------------------------------------------------------------------

# Backend Structure

``` text
backend/
├── app/
│   ├── api/               # Route handlers (thin, delegate to services)
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
│   ├── core/               # Config, security, app-wide setup
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic request/response schemas
│   ├── services/           # Business logic
│   ├── repositories/       # Data access layer
│   ├── middleware/
│   ├── dependencies/
│   ├── utils/
│   └── main.py
├── alembic/                # Alembic migrations
├── tests/
├── requirements.txt
└── .env.example
```

Rules:

-   Each feature area owns its routes, services, schemas, and tests.
-   Cross-module communication occurs through service interfaces.
-   Shared utilities belong in `app/utils`.
-   Database access goes through `repositories/`; business rules live in `services/`; routes stay thin.

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
