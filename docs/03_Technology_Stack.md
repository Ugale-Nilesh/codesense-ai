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

  ---------------------------------------------------------------------------
  Layer                Technology                          Why
  -------------------- ----------------------------------- ------------------
  Frontend             Next.js (React + TypeScript)        Modern SSR,
                                                           routing, ecosystem

  UI                   Tailwind CSS + shadcn/ui            Fast, accessible
                                                           UI

  Editor               Monaco Editor                       VS Code-like
                                                           editing experience

  Backend              NestJS                              Modular,
                                                           enterprise-ready
                                                           APIs

  AI Service           Python (FastAPI)                    Best AI/ML
                                                           ecosystem

  Database             PostgreSQL                          Relational,
                                                           reliable

  ORM                  Prisma                              Type-safe database
                                                           access

  Cache                Redis                               Session & response
                                                           caching

  Storage              S3-compatible storage               File uploads and
                                                           reports

  Auth                 JWT + OAuth                         Secure
                                                           authentication

  OCR                  Tesseract / Vision API              Screenshot
                                                           debugging

  Queue                BullMQ                              Background jobs

  Container            Docker                              Reproducible
                                                           deployments

  CI/CD                GitHub Actions                      Automated testing
                                                           & deployment
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

-   Controller
-   Service
-   Repository
-   DTO
-   Validation

------------------------------------------------------------------------

# AI Layer

Responsibilities:

-   Prompt construction
-   Context management
-   Model abstraction
-   Response normalization

Design Goal:

Changing the AI model should not require frontend or backend changes.

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

-   TypeScript strict mode
-   ESLint
-   Prettier
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
