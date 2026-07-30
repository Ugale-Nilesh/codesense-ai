# 08_Project_Rules.md

# CodeSense AI

## Project Constitution

**Version:** 1.0\
**Status:** Mandatory Engineering Rules

------------------------------------------------------------------------

# Purpose

This document defines the non-negotiable engineering rules for CodeSense
AI. Every contributor, including AI coding assistants, must follow these
rules.

------------------------------------------------------------------------

# Core Principles

1.  Architecture before implementation.
2.  Documentation is part of the product.
3.  Every feature must be modular.
4.  Explainability over complexity.
5.  Maintainability over shortcuts.

------------------------------------------------------------------------

# Repository Rules

-   Do not change the repository structure without updating
    documentation.
-   New features belong inside existing modules.
-   No duplicate implementations.

------------------------------------------------------------------------

# Coding Rules

-   Strict TypeScript.
-   ESLint and Prettier required.
-   Meaningful names only.
-   No hard-coded secrets.
-   No commented-out dead code.

------------------------------------------------------------------------

# Backend Rules

-   Business logic only in services.
-   Controllers stay thin.
-   Validate all input.
-   Return consistent API responses.

------------------------------------------------------------------------

# Frontend Rules

-   Presentation components remain stateless where possible.
-   Shared UI belongs in common components.
-   Reuse before creating new components.

------------------------------------------------------------------------

# AI Rules

-   AI output must be explainable.
-   Include confidence when available.
-   Never fabricate project context.
-   Separate facts, assumptions, and recommendations.

------------------------------------------------------------------------

# Database Rules

-   UUID primary keys.
-   Foreign keys enforced.
-   Soft delete where appropriate.
-   Timestamp every record.

------------------------------------------------------------------------

# Testing Rules

Every new feature requires:

-   Unit tests
-   Integration tests (where applicable)
-   Manual verification checklist

------------------------------------------------------------------------

# Documentation Rules

Whenever architecture changes:

-   Update affected docs.
-   Update roadmap if milestones change.
-   Update current state document.

------------------------------------------------------------------------

# Git Rules

Commit style:

-   feat:
-   fix:
-   docs:
-   refactor:
-   test:
-   chore:

Feature branches only. Merge via pull request.

------------------------------------------------------------------------

# Definition of Done

A task is complete only when:

-   Code implemented
-   Tests passing
-   Documentation updated
-   Lint passes
-   Build succeeds
-   Acceptance criteria met

------------------------------------------------------------------------

# Anti-Patterns

Never:

-   Mix UI and business logic.
-   Duplicate APIs.
-   Bypass validation.
-   Commit secrets.
-   Skip documentation.

------------------------------------------------------------------------

# Related Documents

-   01_Product_Requirements.md
-   02_System_Architecture.md
-   09_Coding_Standards.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- ------------------------------
  1.0       July 2026   Initial project constitution
