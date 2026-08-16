# Phase 03 — Frontend Infrastructure Decisions

**Phase:** Phase 03 — Frontend Infrastructure  
**Document:** Architecture Decision Records  
**Version:** 1.1  
**Status:** Approved

---

# Purpose

This document records the architectural decisions governing Phase 03.

These decisions are mandatory for Phase 03 implementation unless explicitly superseded by a later Architecture Decision Record.

The Master Roadmap remains authoritative for phase scope and sequencing.

---

# ADR-001 — Frontend Framework

**Status:** Accepted

## Decision

CodeSense AI SHALL use:

- React
- TypeScript
- Vite

as the frontend application foundation.

## Rationale

The project requires a maintainable client-side application capable of supporting:

- Interactive developer workflows
- Complex UI state
- Code-oriented interfaces
- Future AI interactions
- Responsive application layouts
- Reusable component architecture

React provides the component model and ecosystem required by the product.

TypeScript provides static type safety.

Vite provides the development and production build foundation.

## Rejected Alternative

### Next.js

Next.js is rejected as the frontend framework for the current implementation architecture.

The repository contains earlier documentation that specifies Next.js. That documentation conflicts with the implementation-oriented frontend standards and task architecture.

The project SHALL use React + Vite for the current frontend implementation.

## Consequences

Positive:

- Clear client-side application architecture.
- Fast development workflow.
- Straightforward deployment model.
- Strong TypeScript integration.
- Compatible with the existing frontend foundation.

Negative:

- Server-side rendering and React Server Components are not part of the current architecture.
- Future requirements requiring SSR would require an explicit architecture decision.

---

# ADR-002 — Frontend Routing

**Status:** Accepted

## Decision

CodeSense AI SHALL use React Router for client-side routing.

Routing SHALL be centralized and SHALL support:

- Route configuration
- Nested routes
- Public routes
- Future protected routes
- Not-found handling
- Layout composition

## Rationale

The application is a client-side React application and requires a predictable routing boundary.

Routing SHALL remain independent from feature business logic.

---

# ADR-003 — Styling Framework

**Status:** Accepted

## Decision

CodeSense AI SHALL use Tailwind CSS as its primary styling framework.

The frontend SHALL use a centralized design language rather than arbitrary styling decisions distributed throughout the application.

## Rationale

Tailwind provides:

- Responsive utilities
- Consistent styling primitives
- Efficient component development
- Strong TypeScript/React compatibility
- A foundation for the project's design system

---

# ADR-004 — UI Component Strategy

**Status:** Accepted

## Decision

The frontend SHALL use reusable, composable UI components.

Components SHALL be divided between:

### Shared UI

Generic components such as:

- Buttons
- Inputs
- Cards
- Dialogs
- Tables
- Badges
- Loading indicators

### Feature Components

Components that belong specifically to a product capability.

Shared UI components SHALL remain domain-agnostic.

---

# ADR-005 — Feature-Oriented Architecture

**Status:** Accepted

## Decision

Frontend product functionality SHALL be organized around features.

Future examples include:

```text
features/
├── auth/
├── projects/
├── debug/
├── optimize/
├── review/
├── learn/
└── productivity/
