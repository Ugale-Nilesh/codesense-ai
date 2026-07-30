# 10_AI_Context.md

# CodeSense AI

## AI Context & Operating Manual

**Version:** 1.0\
**Status:** Active\
**Audience:** AI Coding Assistants (Claude), Human Contributors

------------------------------------------------------------------------

# Purpose

This document provides the persistent context that an AI coding
assistant needs before implementing any feature.

It explains *what CodeSense AI is*, *why it exists*, and *how
implementation decisions should be made*.

------------------------------------------------------------------------

# Project Identity

CodeSense AI is **not** a generic chatbot.

It is an **AI Software Engineering Copilot** that helps developers:

-   Debug code
-   Optimize performance
-   Review software
-   Learn engineering concepts
-   Improve productivity

The product should always prioritize **understanding over automation**.

------------------------------------------------------------------------

# Engineering Principles

Every implementation should follow these priorities:

1.  Correctness
2.  Simplicity
3.  Explainability
4.  Maintainability
5.  Performance

Never sacrifice readability for cleverness.

------------------------------------------------------------------------

# Product Modules

-   Debug
-   Optimize
-   Review
-   Learn
-   Productivity

Each module must remain independently maintainable.

------------------------------------------------------------------------

# AI Responsibilities

When generating features:

-   Explain decisions through code structure.
-   Prefer reusable abstractions.
-   Avoid duplication.
-   Keep modules loosely coupled.
-   Document public interfaces.

------------------------------------------------------------------------

# Constraints

Do NOT:

-   Invent undocumented APIs.
-   Modify architecture without updating documentation.
-   Introduce unnecessary dependencies.
-   Break existing interfaces.

------------------------------------------------------------------------

# Expected Workflow

For every task:

1.  Read Project Vision.
2.  Read Product Requirements.
3.  Read Architecture.
4.  Read Current State.
5.  Implement only the assigned task.
6.  Verify acceptance criteria.
7.  Update documentation if architecture changes.

------------------------------------------------------------------------

# Code Quality Checklist

Before considering work complete:

-   Build succeeds
-   Tests pass
-   Lint passes
-   Documentation updated
-   No duplicated logic
-   No hard-coded secrets

------------------------------------------------------------------------

# Communication Style

Implementation notes should be:

-   Concise
-   Technical
-   Actionable
-   Honest about limitations

Avoid speculative implementations.

------------------------------------------------------------------------

# Long-Term Goal

Every completed feature should move CodeSense AI closer to becoming a
complete Software Engineering Copilot rather than an isolated collection
of AI tools.

------------------------------------------------------------------------

# Related Documents

-   00_Project_Vision.md
-   01_Product_Requirements.md
-   08_Project_Rules.md
-   11_Current_State.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- --------------------------
  1.0       July 2026   Initial AI context guide
