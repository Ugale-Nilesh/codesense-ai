# 15_Deployment_Guide.md

# CodeSense AI

## Deployment Guide

**Version:** 1.0\
**Status:** Engineering Standard

------------------------------------------------------------------------

# Purpose

This guide defines how CodeSense AI is developed, deployed, monitored,
and maintained across local, staging, and production environments.

------------------------------------------------------------------------

# Deployment Environments

  Environment   Purpose
  ------------- --------------------------
  Local         Development
  Staging       QA & Integration Testing
  Production    End Users

------------------------------------------------------------------------

# Local Development

Requirements:

-   Node.js (LTS)
-   Python 3.11+
-   PostgreSQL
-   Docker Desktop
-   Git

Steps:

1.  Clone repository
2.  Install dependencies
3.  Configure `.env`
4.  Start database
5.  Start frontend
6.  Start backend

------------------------------------------------------------------------

# Environment Variables

Examples:

-   DATABASE_URL
-   JWT_SECRET
-   ANTHROPIC_API_KEY
-   OPENAI_API_KEY
-   GOOGLE_API_KEY
-   SUPABASE_URL
-   SUPABASE_SERVICE_KEY
-   REDIS_URL (future — required once Redis/Celery are adopted)

Never commit secrets.

------------------------------------------------------------------------

# Docker

Containers:

-   Frontend
-   Backend
-   PostgreSQL
-   Redis (future — added when caching/Celery are introduced)

Use Docker Compose for local development.

------------------------------------------------------------------------

# CI/CD Pipeline

GitHub Actions:

1.  Install dependencies
2.  Lint
3.  Run tests
4.  Build
5.  Deploy to staging
6.  Manual approval
7.  Deploy to production

------------------------------------------------------------------------

# Database Migration

Rules:

-   Use Alembic migrations
-   Review every migration
-   Backup production before applying changes

------------------------------------------------------------------------

# Monitoring

Track:

-   API uptime
-   AI latency
-   Error rates
-   Database health
-   Queue health

------------------------------------------------------------------------

# Logging

Centralized logs should include:

-   Timestamp
-   Service
-   Severity
-   Request ID

Sensitive information must never be logged.

------------------------------------------------------------------------

# Rollback Strategy

If deployment fails:

1.  Stop rollout
2.  Restore previous release
3.  Restore database if required
4.  Investigate root cause

------------------------------------------------------------------------

# Release Checklist

-   Documentation updated
-   Tests passing
-   Security review complete
-   Performance validated
-   Backups confirmed

------------------------------------------------------------------------

# Related Documents

-   12_Development_Roadmap.md
-   14_Testing_Strategy.md
-   16_Claude_Workflow.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- --------------------------
  1.0       July 2026   Initial deployment guide
