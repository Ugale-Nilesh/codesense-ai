# 05_Database_Design.md

# CodeSense AI

## Database Design

**Version:** 1.0\
**Status:** Engineering Baseline

------------------------------------------------------------------------

# 1. Purpose

This document defines the logical database design for CodeSense AI. The
schema is designed to support modular growth while maintaining strong
data integrity and high query performance.

Primary database: **PostgreSQL**\
ORM: **SQLAlchemy**\
Migrations: **Alembic**

------------------------------------------------------------------------

# 2. Design Principles

-   Normalize transactional data.
-   Prefer UUID primary keys.
-   Track creation and update timestamps.
-   Use foreign keys for referential integrity.
-   Support future multi-tenant expansion.

------------------------------------------------------------------------

# 3. Core Entities

``` text
User
 ├── Projects
 │     ├── Uploads
 │     ├── Analyses
 │     ├── Reports
 │     └── GitHub Repositories
 └── AI Conversations
```

------------------------------------------------------------------------

# 4. Tables

## users

Stores user accounts.

Fields:

-   id (UUID)
-   name
-   email
-   password_hash
-   avatar_url
-   role
-   created_at
-   updated_at

------------------------------------------------------------------------

## projects

Represents a logical coding project.

Fields:

-   id
-   owner_id
-   name
-   description
-   language
-   framework
-   created_at

Relationship:

One User → Many Projects

------------------------------------------------------------------------

## uploads

Stores uploaded files and ZIP archives.

Fields:

-   id
-   project_id
-   filename
-   type
-   size
-   storage_path
-   uploaded_at

------------------------------------------------------------------------

## github_repositories

Stores imported repositories.

Fields:

-   id
-   project_id
-   repository_url
-   default_branch
-   last_scan

------------------------------------------------------------------------

## analyses

Stores every AI analysis.

Fields:

-   id
-   project_id
-   analysis_type
-   status
-   summary
-   confidence_score
-   started_at
-   completed_at

Types include:

-   Debug
-   Review
-   Optimize
-   Learn

------------------------------------------------------------------------

## findings

Stores detailed issues discovered during analysis.

Fields:

-   id
-   analysis_id
-   severity
-   title
-   description
-   recommendation
-   file_path
-   line_number

------------------------------------------------------------------------

## ai_conversations

Stores chat history.

Fields:

-   id
-   user_id
-   title
-   created_at

------------------------------------------------------------------------

## ai_messages

Stores individual prompts and responses.

Fields:

-   id
-   conversation_id
-   sender
-   content
-   timestamp

------------------------------------------------------------------------

## reports

Generated reports.

Fields:

-   id
-   analysis_id
-   format
-   file_path
-   created_at

------------------------------------------------------------------------

# 5. Relationships

-   User 1:N Projects
-   Project 1:N Uploads
-   Project 1:N Analyses
-   Analysis 1:N Findings
-   Analysis 1:N Reports
-   User 1:N Conversations
-   Conversation 1:N Messages

------------------------------------------------------------------------

# 6. Index Strategy

Indexes:

-   users.email
-   projects.owner_id
-   analyses.project_id
-   findings.analysis_id
-   github_repositories.repository_url

------------------------------------------------------------------------

# 7. Data Lifecycle

1.  User creates project.
2.  Files or GitHub repository uploaded.
3.  Analysis created.
4.  Findings stored.
5.  Report generated.
6.  History retained for dashboard.

------------------------------------------------------------------------

# 8. Future Tables

-   notifications
-   teams
-   pull_requests
-   api_keys
-   billing
-   model_usage
-   feature_flags

------------------------------------------------------------------------

# 9. Backup Strategy

-   Daily automated backups
-   Point-in-time recovery
-   Monthly archive snapshots

------------------------------------------------------------------------

# 10. Related Documents

-   02_System_Architecture.md
-   03_Technology_Stack.md
-   06_API_Contracts.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- -------------------------
  1.0       July 2026   Initial database design
