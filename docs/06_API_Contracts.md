# 06_API_Contracts.md

# CodeSense AI

## API Contracts

**Version:** 1.0\
**Status:** Engineering Baseline

------------------------------------------------------------------------

# Purpose

This document defines the REST API surface for Version 1 of CodeSense
AI. All endpoints return JSON and use versioned routes (`/api/v1`).

------------------------------------------------------------------------

# Standards

-   Authentication: JWT Bearer Token
-   Content-Type: application/json
-   File Upload: multipart/form-data
-   Status Codes: HTTP standard

------------------------------------------------------------------------

# Authentication

## POST /api/v1/auth/register

Registers a new user.

### Request

``` json
{
  "name":"John Doe",
  "email":"john@example.com",
  "password":"********"
}
```

### Response

``` json
{
  "userId":"uuid",
  "message":"Registration successful"
}
```

------------------------------------------------------------------------

## POST /api/v1/auth/login

Returns access token and refresh token.

------------------------------------------------------------------------

# Projects

## GET /api/v1/projects

Returns all projects for authenticated user.

## POST /api/v1/projects

Creates a new project.

Fields:

-   name
-   description
-   language
-   framework

------------------------------------------------------------------------

# File Upload

## POST /api/v1/uploads

Supports:

-   Source files
-   ZIP archives
-   Screenshots

Response includes upload id and processing status.

------------------------------------------------------------------------

# GitHub Analysis

## POST /api/v1/github/analyze

Request

``` json
{
  "repositoryUrl":"https://github.com/org/repo"
}
```

Returns repository analysis job id.

------------------------------------------------------------------------

# AI Analysis

## POST /api/v1/analysis/debug

Input:

-   projectId

Output:

-   Root cause
-   Explanation
-   Suggested fix
-   Prevention tips
-   Confidence score

------------------------------------------------------------------------

## POST /api/v1/analysis/review

Returns:

-   Code quality
-   Maintainability
-   Security issues
-   Best practices

------------------------------------------------------------------------

## POST /api/v1/analysis/optimize

Returns:

-   Complexity analysis
-   Performance suggestions
-   Refactoring ideas

------------------------------------------------------------------------

# Reports

## GET /api/v1/reports/{id}

Downloads generated report.

------------------------------------------------------------------------

# Dashboard

## GET /api/v1/dashboard

Returns:

-   Recent analyses
-   Project statistics
-   Learning progress

------------------------------------------------------------------------

# Error Format

``` json
{
  "status":400,
  "code":"INVALID_REQUEST",
  "message":"Validation failed",
  "details":[]
}
```

------------------------------------------------------------------------

# Versioning

Current version:

`/api/v1`

Breaking changes require `/api/v2`.

------------------------------------------------------------------------

# Related Documents

-   02_System_Architecture.md
-   05_Database_Design.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- -----------------------
  1.0       July 2026   Initial API contracts
