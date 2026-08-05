# ADR-002 — Database Selection

**Status:** Accepted

**Date:** 2026-08-04

## Context

CodeSense AI requires a relational database capable of supporting transactional workloads, structured relationships, JSON data, future scalability, and consistent behavior across all environments. The project also uses SQLAlchemy and Alembic for ORM and database migrations, which benefit from running against the same database engine throughout the development lifecycle.

## Decision

CodeSense AI SHALL use **PostgreSQL** as the primary and only relational database for all environments.

This includes:

- Development
- Testing
- Staging
- Production

All developers SHALL run PostgreSQL locally during development.

The application, migrations, tests, and deployment environments SHALL target PostgreSQL to ensure behavioral consistency and eliminate environment-specific differences.

## Rationale

PostgreSQL was selected because it provides:

- Excellent compatibility with SQLAlchemy and Alembic
- Strong ACID compliance
- Advanced indexing capabilities
- Native JSON/JSONB support
- High scalability for future growth
- Consistent behavior across local and production environments
- Mature ecosystem and community support

Using PostgreSQL in every environment eliminates discrepancies between development and production, reduces migration issues, and simplifies long-term maintenance.

## Rejected Alternatives

### SQLite (including development-only usage)

Rejected because:

- Different SQL dialect and behavior from PostgreSQL
- Limited concurrency support
- Missing PostgreSQL-specific features
- Increased risk of environment-specific bugs
- Does not accurately represent the production environment

### MySQL

Rejected because:

- Inferior JSON capabilities for project requirements
- Less aligned with planned PostgreSQL-specific features
- No architectural advantage for CodeSense AI

### MongoDB

Rejected because:

- The project requires a relational data model
- SQLAlchemy and Alembic are part of the selected architecture
- Document storage does not match the application's core data model

## Consequences

Positive:

- Identical database behavior across all environments
- Simpler migration workflow
- Easier debugging
- Consistent developer experience
- Better production reliability

Negative:

- PostgreSQL must be installed locally by every developer
- Slightly higher initial setup effort compared to SQLite

## Review

This decision SHALL remain valid unless superseded by a future Architecture Decision Record (ADR).
