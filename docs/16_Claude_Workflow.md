# 16_Claude_Workflow.md

# CodeSense AI

## Claude Implementation Workflow

**Version:** 1.0\
**Status:** Operational Guide

------------------------------------------------------------------------

# Purpose

This document defines the mandatory workflow that Claude must follow
while implementing CodeSense AI.

Claude is responsible for implementation, not architecture.

Architecture decisions originate from the engineering documentation.

------------------------------------------------------------------------

# Core Rule

Before writing a single line of code, Claude must understand the project
context.

Implementation without context is prohibited.

------------------------------------------------------------------------

# Required Reading Order

For every new session, Claude must review:

1.  00_Project_Vision.md
2.  01_Product_Requirements.md
3.  02_System_Architecture.md
4.  08_Project_Rules.md
5.  09_Coding_Standards.md
6.  10_AI_Context.md
7.  11_Current_State.md
8.  Current task specification

Only after understanding these documents should implementation begin.

------------------------------------------------------------------------

# Daily Workflow

## Step 1 --- Understand

-   Read the assigned task.
-   Review related documents.
-   Identify dependencies.
-   Confirm acceptance criteria.

------------------------------------------------------------------------

## Step 2 --- Plan

Before coding:

-   Break task into subtasks.
-   Identify reusable components.
-   Avoid duplicate implementations.
-   Preserve existing architecture.

------------------------------------------------------------------------

## Step 3 --- Implement

During implementation:

-   Follow coding standards.
-   Write modular code.
-   Keep components small.
-   Reuse shared utilities.

------------------------------------------------------------------------

## Step 4 --- Verify

Before completion:

-   Run tests.
-   Run lint.
-   Verify build.
-   Confirm acceptance criteria.

------------------------------------------------------------------------

## Step 5 --- Update

If architecture changed:

-   Update documentation.

Always update:

-   11_Current_State.md

Record:

-   Completed task
-   Progress
-   New decisions
-   Technical debt

------------------------------------------------------------------------

# Forbidden Actions

Claude must NOT:

-   Invent undocumented APIs
-   Ignore coding standards
-   Modify architecture without documentation
-   Duplicate functionality
-   Leave failing tests
-   Skip updating project state

------------------------------------------------------------------------

# Expected Output

Every completed task should include:

-   Summary of implementation
-   Files created
-   Files modified
-   Tests executed
-   Remaining work
-   Risks (if any)

------------------------------------------------------------------------

# Definition of Done

A task is complete only when:

-   Code implemented
-   Tests passing
-   Documentation updated
-   Lint passing
-   Build succeeds
-   Acceptance criteria satisfied

------------------------------------------------------------------------

# Escalation Rules

Claude should request clarification if:

-   Documentation conflicts
-   Acceptance criteria are ambiguous
-   Architectural changes are required
-   Missing dependencies block progress

------------------------------------------------------------------------

# Continuous Improvement

Every implementation should improve:

-   Readability
-   Reusability
-   Maintainability
-   Performance
-   Documentation

------------------------------------------------------------------------

# Long-Term Goal

Claude should treat CodeSense AI as a long-lived engineering project.

Every change should make the codebase easier---not harder---to extend.

------------------------------------------------------------------------

# Related Documents

-   10_AI_Context.md
-   11_Current_State.md
-   12_Development_Roadmap.md
-   13_Feature_Specifications.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- -------------------------------
  1.0       July 2026   Initial Claude workflow guide
