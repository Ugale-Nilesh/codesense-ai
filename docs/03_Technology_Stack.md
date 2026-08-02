# 03_Technology_Stack.md

# CodeSense AI

## Technology Stack

**Version:** 1.0\
**Status:** Engineering Baseline

------------------------------------------------------------------------

# Philosophy

Every technology is selected using four principles:

-   Developer productivity
-   Scalability
-   Strong AI ecosystem
-   Long-term maintainability

------------------------------------------------------------------------

# Technology Overview

This table reflects the finalized, single-source-of-truth technology stack. All other documents in this repository must remain consistent with it.

  ---------------------------------------------------------------------------
  Layer                Technology                          Why
  -------------------- ----------------------------------- ------------------
  Frontend             React + Vite + TypeScript            Fast dev server,
                                                           SPA simplicity,
                                                           strong ecosystem

  UI                   Tailwind CSS                         Fast, utility-
                                                           first styling

  Routing              React Router                         Standard SPA
                                                           routing

  Server State          TanStack Query                      Caching, sync,
                                                           and fetching for
                                                           server data

  Client State           Zustand                             Lightweight
                                                           global state

  Editor               Monaco Editor                       VS Code-like
                                                           editing experience

  Backend              Python + FastAPI                     Modular, async,
                                                           best AI/ML
                                                           ecosystem fit

  Database             PostgreSQL                          Relational,
                                                           reliable

  ORM                  SQLAlchemy                           Mature, flexible
                                                           Python ORM

  Migrations           Alembic                               Schema
                                                           versioning for
                                                           SQLAlchemy

  Auth                 JWT                                   Stateless,
                                                           simple session
                                                           handling

  AI Providers         Anthropic Claude API, OpenAI API,     Multi-provider
                       Google Gemini API                    AI orchestration

  OCR                  Tesseract / Vision API              Screenshot
                                                           debugging

  Storage              Supabase Storage                     File uploads and
                                                           reports

  Container            Docker                              Reproducible
                                                           deployments

  CI/CD                GitHub Actions                      Automated testing
                                                           & deployment

  Future — Cache        Redis                                 Deferred until
                                                           needed at scale

  Future — Queue         Celery                                Deferred until
                                                           background job
                                                           volume requires it
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

# Frontend

Responsibilities:

-   Authentication
-   Dashboard
-   File uploads
-   AI Chat
-   Monaco editor
-   Reports
-   Settings

Guidelines:

-   Strict TypeScript
-   Feature-based architecture
-   Reusable components only

------------------------------------------------------------------------

# Backend

Responsibilities:

-   Authentication
-   Business logic
-   AI orchestration
-   File processing
-   Report generation
-   Database access

Architecture:

-   Route (API layer)
-   Service
-   Repository
-   Schema (Pydantic)
-   Validation

------------------------------------------------------------------------

# AI Layer

Supported providers:

-   Anthropic Claude API
-   OpenAI API
-   Google Gemini API

Responsibilities:

-   Prompt construction
-   Context management
-   Provider abstraction (switching providers should not require frontend or backend changes)
-   Response normalization

------------------------------------------------------------------------

# Database

Primary database:

PostgreSQL

Stores:

-   Users
-   Projects
-   Analyses
-   Reports
-   History
-   Settings

------------------------------------------------------------------------

# Development Tools

-   Git
-   GitHub
-   VS Code
-   Claude (implementation)
-   ChatGPT (architecture & planning)

------------------------------------------------------------------------

# Coding Standards

Frontend

-   TypeScript strict mode
-   ESLint
-   Prettier

Backend

-   Black
-   Ruff
-   isort
-   mypy

Repository-wide

-   Conventional Commits
-   Semantic versioning

------------------------------------------------------------------------

# Selection Criteria

A technology is adopted only if it:

-   Is actively maintained
-   Has strong documentation
-   Supports long-term scaling
-   Fits modular architecture

------------------------------------------------------------------------

# Future Upgrades

-   Kubernetes
-   Vector database
-   Event streaming
-   Multi-model AI routing
-   Enterprise authentication

------------------------------------------------------------------------

# Related Documents

-   02_System_Architecture.md
-   04_Folder_Structure.md
-   05_Database_Design.md

------------------------------------------------------------------------

# Revision History

  Version   Date        Changes
  --------- ----------- --------------------------
  1.0       July 2026   Initial technology stack
