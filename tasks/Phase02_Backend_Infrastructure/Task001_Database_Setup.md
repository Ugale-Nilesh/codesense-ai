# Task001_Database_Setup.md

## Phase 02 -- Backend Infrastructure

**Task ID:** P02-T001\
**Estimated Effort:** 1--2 Hours\
**Priority:** Critical\
**Status:** Not Started

------------------------------------------------------------------------

# Objective

Create the production-ready database foundation for CodeSense AI.

This task establishes PostgreSQL connectivity and project-level database
configuration. **No business models or application features are
implemented in this task.**

------------------------------------------------------------------------

# References (Read First)

Before implementation, read:

1.  README.md
2.  ARCHITECTURE.md
3.  DECISIONS.md
4.  CHECKLIST.md
5.  docs/02_System_Architecture.md
6.  docs/03_Technology_Stack.md
7.  docs/09_Coding_Standards.md

------------------------------------------------------------------------

# Scope

## In Scope

-   Install PostgreSQL dependencies
-   Configure SQLAlchemy database engine
-   Configure database session factory
-   Create database package structure
-   Create configuration placeholders
-   Verify database connectivity

## Out of Scope

-   Alembic migrations
-   ORM models
-   Authentication
-   CRUD APIs
-   Seed data

------------------------------------------------------------------------

# Deliverables

``` text
backend/
└── app/
    ├── db/
    │   ├── __init__.py
    │   ├── base.py
    │   ├── session.py
    │   └── database.py
    └── core/
        └── config.py
```

------------------------------------------------------------------------

# Required Packages

Install only:

-   SQLAlchemy 2.x
-   psycopg\[binary\]
-   Alembic (installation only)
-   Pydantic Settings

Versions should be compatible with the project's locked dependency
strategy.

------------------------------------------------------------------------

# Functional Requirements

### FR-1

Database connection URL must come from environment variables.

Never hardcode credentials.

------------------------------------------------------------------------

### FR-2

Only one SQLAlchemy Engine instance.

------------------------------------------------------------------------

### FR-3

Session creation must use a reusable SessionLocal/sessionmaker.

------------------------------------------------------------------------

### FR-4

Sessions must be safely closed after use.

------------------------------------------------------------------------

### FR-5

Database configuration must support:

-   Development
-   Testing
-   Production

without code changes.

------------------------------------------------------------------------

# Non-Functional Requirements

-   Thread-safe configuration
-   Type annotated code
-   Production-ready structure
-   No duplicated configuration

------------------------------------------------------------------------

# Security Requirements

-   Credentials stored only in `.env`
-   No secrets committed to Git
-   SSL support must remain configurable
-   Use parameterized ORM queries only

------------------------------------------------------------------------

# Coding Rules

-   Follow repository pattern.
-   No SQL inside routers.
-   No global mutable state.
-   No direct engine creation outside db/session.py.

------------------------------------------------------------------------

# Manual Verification

The following must succeed:

-   Backend starts successfully.
-   Database connection initializes.
-   No import errors.
-   No configuration warnings.

------------------------------------------------------------------------

# Acceptance Criteria

-   [ ] PostgreSQL package installed
-   [ ] SQLAlchemy installed
-   [ ] Engine configured
-   [ ] Session factory configured
-   [ ] Environment variables used
-   [ ] Folder structure matches specification
-   [ ] Backend launches successfully

------------------------------------------------------------------------

# Git Commit

``` text
feat(backend): setup database foundation
```

------------------------------------------------------------------------

# Stop Condition

After completing this task:

-   Update CHECKLIST.md
-   Commit changes
-   Push to GitHub
-   Do NOT continue to Task002 until verification passes.
