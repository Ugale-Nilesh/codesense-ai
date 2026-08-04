# DECISIONS.md

## Phase 02 -- Backend Infrastructure

**Version:** 1.0\
**Status:** Approved

------------------------------------------------------------------------

# Purpose

This document records the architectural decisions for Phase 02. These
decisions are mandatory unless superseded by a future ADR.

------------------------------------------------------------------------

# ADR-001 --- FastAPI

## Decision

Use FastAPI as the backend framework.

## Rationale

-   Excellent async support
-   Automatic OpenAPI generation
-   Strong typing with Pydantic
-   Large ecosystem
-   Ideal for AI-first APIs

## Consequences

-   ASGI deployment
-   Dependency Injection available
-   Automatic Swagger/ReDoc

------------------------------------------------------------------------

# ADR-002 --- PostgreSQL

## Decision

PostgreSQL is the primary relational database.

## Rationale

-   ACID compliance
-   Mature ecosystem
-   JSONB support
-   Excellent SQL features
-   Future scalability

## Rejected

-   SQLite (development only)
-   MySQL
-   MongoDB

------------------------------------------------------------------------

# ADR-003 --- SQLAlchemy 2.x

## Decision

Use SQLAlchemy 2.x as the ORM.

## Rationale

-   Mature ORM
-   Excellent migration support
-   Fine-grained control
-   Strong community adoption

Alembic will manage migrations.

------------------------------------------------------------------------

# ADR-004 --- Repository Pattern

## Decision

All persistence belongs in repositories.

## Rules

-   Services never write SQL.
-   Routers never access the database.
-   Repositories contain persistence only.

------------------------------------------------------------------------

# ADR-005 --- Dependency Injection

## Decision

Use FastAPI dependency injection.

Inject only: - Database session - Settings - Authenticated user - Logger

Never instantiate these directly inside services.

------------------------------------------------------------------------

# ADR-006 --- JWT Authentication

## Decision

Stateless JWT authentication.

Reason: - Scalable - API-first - Works well with SPA frontend

Session-based authentication is rejected.

------------------------------------------------------------------------

# ADR-007 --- Configuration

Configuration must come from:

-   Environment variables
-   Pydantic Settings

Never hardcode secrets.

------------------------------------------------------------------------

# ADR-008 --- Logging

Use structured application logging.

Requirements: - Request IDs - Error stack traces - No credential logging

------------------------------------------------------------------------

# ADR-009 --- API Versioning

Expose APIs under:

/api/v1/

Future breaking changes must use:

/api/v2/

------------------------------------------------------------------------

# ADR-010 --- Future AI Integration

Business logic must remain independent from AI providers.

Future providers (OpenAI, Anthropic, Gemini) will integrate through an
abstraction layer rather than directly inside services.

------------------------------------------------------------------------

# Review Policy

Every future architectural change must either:

1.  Update an existing ADR, or
2.  Introduce a new ADR.

No implementation may silently violate these decisions.
