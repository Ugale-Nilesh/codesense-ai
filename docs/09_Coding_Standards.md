# 09_Coding_Standards.md

# CodeSense AI

## Coding Standards

**Version:** 1.0\
**Status:** Engineering Standard

------------------------------------------------------------------------

# Purpose

This document defines the coding standards that every contributor and AI
coding assistant must follow to keep the CodeSense AI codebase
consistent, maintainable, and scalable.

------------------------------------------------------------------------

# General Principles

-   Readability over cleverness.
-   Consistency over personal preference.
-   Simplicity before optimization.
-   Self-documenting code whenever possible.

------------------------------------------------------------------------

# Naming Conventions

## Variables

-   camelCase
-   Descriptive names only

## Functions

-   Verb-based names
-   One responsibility per function

## Classes

-   PascalCase

## Files

-   kebab-case for folders
-   PascalCase for React components

------------------------------------------------------------------------

# TypeScript Rules

-   Enable `strict` mode.
-   Avoid `any`.
-   Prefer interfaces for public contracts.
-   Validate external inputs.

------------------------------------------------------------------------

# React Standards

-   Functional components only
-   Hooks before helper functions
-   Keep components focused
-   Move business logic into services/hooks

------------------------------------------------------------------------

# Backend Standards

Structure each module as:

``` text
module/
├── controller
├── service
├── dto
├── repository
├── tests
└── types
```

Controllers orchestrate. Services contain business logic. Repositories
access data.

------------------------------------------------------------------------

# Error Handling

Every API returns:

-   status
-   message
-   code
-   optional details

Never expose stack traces to clients.

------------------------------------------------------------------------

# Logging

Use structured logs.

Log:

-   Requests
-   Errors
-   Processing time
-   AI calls

Never log passwords, secrets, or tokens.

------------------------------------------------------------------------

# Documentation

Every exported function should include concise documentation when intent
is not obvious.

Complex logic must explain *why*, not *what*.

------------------------------------------------------------------------

# Testing

Minimum expectations:

-   Unit tests for services
-   Integration tests for APIs
-   Manual verification before merge

------------------------------------------------------------------------

# Git Standards

Commit format:

-   feat:
-   fix:
-   docs:
-   refactor:
-   test:
-   chore:

One logical change per commit.

------------------------------------------------------------------------

# Code Review Checklist

Before merging:

-   Build passes
-   Tests pass
-   Lint passes
-   No dead code
-   No duplicated logic
-   Documentation updated

------------------------------------------------------------------------

# Related Documents

-   08_Project_Rules.md
-   02_System_Architecture.md
-   12_Development_Roadmap.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- --------------------------
  1.0       July 2026   Initial coding standards
