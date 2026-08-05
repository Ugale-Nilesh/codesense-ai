# ARCHITECTURE.md

## Phase 02 -- Backend Infrastructure

**Version:** 1.0\
**Status:** Approved Architecture Specification\
**Owner:** CodeSense AI Team

------------------------------------------------------------------------

# Purpose

This document is the **authoritative architecture specification** for
Phase 02.

Every implementation task (Task001--Task016) MUST follow this document.
If a task conflicts with this architecture, **this document takes
precedence**.

------------------------------------------------------------------------

# Architectural Goals

-   Production-ready backend foundation
-   Clear separation of concerns
-   High maintainability
-   Testability
-   Scalability
-   Security by default
-   Extensibility for future AI features

------------------------------------------------------------------------

# High-Level Architecture

``` text
Browser
    │
    ▼
React + Vite Frontend
    │
REST API
    │
    ▼
FastAPI
    │
──────────────
 Middleware
──────────────
    │
    ▼
API Routers
    │
Dependency Injection
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
SQLAlchemy ORM
    │
    ▼
PostgreSQL
```

------------------------------------------------------------------------

# Request Lifecycle

``` text
HTTP Request
      │
      ▼
Middleware
      │
Authentication
      │
Dependency Injection
      │
Router
      │
Service
      │
Repository
      │
Database
      │
Response Model
      │
HTTP Response
```

------------------------------------------------------------------------

# Backend Layers

## API Layer

Responsibilities

-   Receive requests
-   Validate input
-   Return response models
-   Never contain business logic

------------------------------------------------------------------------

## Service Layer

Responsibilities

-   Business rules
-   AI orchestration (future)
-   Validation beyond schema
-   Transaction coordination

------------------------------------------------------------------------

## Repository Layer

Responsibilities

-   Database queries
-   ORM interaction
-   No business logic

------------------------------------------------------------------------

## Database Layer

Responsibilities

-   SQLAlchemy models
-   Session management
-   Alembic migrations

------------------------------------------------------------------------

# Folder Structure

``` text
backend/
└── app/
    ├── api/
    │   └── v1/
    ├── core/
    ├── db/
    ├── middleware/
    ├── models/
    ├── repositories/
    ├── schemas/
    ├── services/
    ├── utils/
    └── main.py
```

------------------------------------------------------------------------

# Dependency Injection Rules

Dependencies may inject:

-   Database Session
-   Application Settings
-   Authenticated User
-   Logger

Services must never instantiate these directly.

------------------------------------------------------------------------

# Error Handling

Global handlers will standardize:

-   Validation Errors
-   Authentication Errors
-   Authorization Errors
-   Database Errors
-   Unexpected Exceptions

Every error must produce a structured JSON response.

------------------------------------------------------------------------

# Logging Pipeline

``` text
Request
   │
Middleware
   │
Structured Logger
   │
Console
   │
Future File / Observability
```

Never log secrets or tokens.

------------------------------------------------------------------------

# Security Principles

-   JWT Authentication
-   Environment-based secrets
-   Principle of least privilege
-   Parameterized database queries
-   Input validation using Pydantic
-   HTTPS-ready configuration

------------------------------------------------------------------------

# Performance Principles

-   Reuse database engine
-   Scoped database sessions
-   Avoid N+1 queries
-   Lazy loading only where appropriate
-   Keep routers lightweight

------------------------------------------------------------------------

# Future Expansion

This architecture intentionally reserves extension points for:

-   AI Provider Abstraction
-   Background Workers
-   File Processing
-   WebSockets
-   Project Analysis Engine
-   Code Review Engine

These additions must not require architectural refactoring.

------------------------------------------------------------------------

# Engineering Constraints

Every implementation task MUST:

1.  Follow this architecture.
2.  Keep routers thin.
3.  Keep business logic inside services.
4.  Keep persistence inside repositories.
5.  Never bypass dependency injection.
6.  Never hardcode configuration.

------------------------------------------------------------------------

# Architecture Exit Criteria

Phase 02 architecture is considered implemented only when:

-   Folder structure matches specification.
-   Layer responsibilities are respected.
-   Dependency Injection is operational.
-   Database abstraction is complete.
-   Authentication integrates without structural changes.
-   Future AI modules can be added without redesign.
