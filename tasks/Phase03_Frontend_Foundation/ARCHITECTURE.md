# Phase 03 — Frontend Foundation

**Document:** Architecture
**Phase:** Phase 03 – Frontend Foundation
**Version:** 1.0
**Status:** Approved
**Priority:** Critical

---

# 1. Purpose

This document defines the architectural structure of the CodeSense AI frontend foundation.

Phase 03 establishes the frontend platform on which all future CodeSense AI modules will be built.

The architecture SHALL provide clear separation between:

* Application infrastructure
* Routing
* Pages
* Features
* Shared UI
* Client state
* Server state
* API communication
* Authentication
* Configuration

The architecture SHALL support future CodeSense AI modules without requiring a fundamental frontend restructuring.

---

# 2. Technology Baseline

The frontend implementation SHALL use the technology baseline established during Phase 01:

* React
* TypeScript
* Vite
* Tailwind CSS
* React Router
* Axios

Additional dependencies SHALL only be introduced when required by an approved task and justified by the architecture.

---

# 3. Frontend Architectural Model

The frontend SHALL follow a feature-oriented architecture built around an application shell.

```text
Browser
   │
   ▼
Application Bootstrap
   │
   ▼
Application Providers
   │
   ▼
Router
   │
   ├── Public Routes
   │
   └── Protected Routes
          │
          ▼
        Pages
          │
          ▼
       Features
          │
          ├── Shared UI
          ├── Hooks
          ├── API Services
          └── State
                  │
                  ▼
              API Client
                  │
                  ▼
             Backend API
```

---

# 4. Application Layer

The application layer owns global frontend infrastructure.

Responsibilities include:

* Application bootstrap
* Provider registration
* Router initialization
* Global configuration
* Global error handling
* Theme initialization
* Application-level state initialization

The application layer SHALL NOT contain feature-specific business logic.

---

# 5. Routing Layer

Routing SHALL be centralized.

The routing architecture SHALL support:

* Public routes
* Protected routes
* Nested routes
* Route parameters
* Not-found handling
* Route-level loading states
* Future lazy-loaded routes

The router SHALL not contain business logic.

---

# 6. Page Layer

Pages SHALL represent route-level application screens.

Examples of future pages include:

```text
Login
Dashboard
Projects
Project Workspace
Debug
Review
Optimize
Learn
Productivity
Settings
```

Pages SHALL compose features and shared components.

Pages SHALL NOT directly implement reusable infrastructure.

---

# 7. Feature Layer

Feature modules SHALL represent user-facing product capabilities.

Future examples include:

```text
auth/
projects/
debug/
optimize/
review/
learn/
productivity/
```

A feature SHALL own its feature-specific:

* Components
* Hooks
* Types
* Validation
* API services
* State
* Utilities

Feature modules SHALL remain independently maintainable.

---

# 8. Shared UI Layer

Reusable UI components SHALL live outside feature modules.

Examples:

```text
Button
Input
Modal
Dialog
Dropdown
Tabs
Card
Table
Badge
Toast
Skeleton
```

Shared components SHALL remain domain-agnostic.

A shared UI component SHALL NOT depend on:

```text
debug/
projects/
review/
learn/
```

or other product-specific features.

---

# 9. State Architecture

Frontend state SHALL be divided according to ownership.

## Local UI State

Used for short-lived component state such as:

* Modal visibility
* Active tabs
* Temporary form values
* Dropdown state

Local state SHALL remain local whenever possible.

## Client/Application State

Used for genuinely global client-owned state such as:

* Theme
* UI preferences
* Navigation state
* Session-related client state

## Server State

Used for backend-owned data such as:

* User information
* Projects
* Analyses
* Reports
* Conversations
* Repository information

Server-owned data SHALL NOT be unnecessarily duplicated into global client state.

---

# 10. API Architecture

All HTTP communication SHALL pass through a centralized API layer.

```text
Component
    │
    ▼
Feature Service
    │
    ▼
API Client
    │
    ├── Base Configuration
    ├── Authentication
    ├── Request Handling
    ├── Response Handling
    └── Error Normalization
    │
    ▼
FastAPI Backend
```

UI components SHALL NOT directly construct backend HTTP requests.

Direct use of HTTP clients inside presentation components is prohibited.

---

# 11. Backend Contract

The frontend SHALL consume the backend API established in Phase 02.

The backend remains authoritative for:

* Authentication
* Authorization
* Validation
* Persistent state
* Business rules

The frontend SHALL never duplicate backend business rules merely for convenience.

---

# 12. Authentication Architecture

The frontend authentication layer SHALL integrate with the JWT authentication foundation established by Phase 02.

The architecture SHALL support:

```text
Authentication State
        │
        ├── Authenticated
        ├── Unauthenticated
        └── Loading
```

Authentication infrastructure SHALL provide the information required by protected routing and authenticated API requests.

Client-side authentication state SHALL be treated as a UX mechanism.

It SHALL NOT be considered a security boundary.

Backend authorization remains authoritative.

---

# 13. Protected Route Architecture

Routes SHALL be categorized as:

```text
Public
Protected
```

Examples:

```text
/login
/register
```

may be public.

Future application routes such as:

```text
/dashboard
/projects
/settings
/debug
```

may require authentication.

Unauthenticated users SHALL be redirected to an appropriate public authentication route.

---

# 14. Application Shell

Authenticated product areas SHALL use a common application shell.

Conceptually:

```text
┌──────────────────────────────────────────────┐
│                 Top Navigation               │
├───────────────┬──────────────────────────────┤
│               │                              │
│    Sidebar    │         Main Content         │
│               │                              │
│               │                              │
└───────────────┴──────────────────────────────┘
```

The shell SHALL provide the structural foundation for future modules.

It SHALL support:

* Primary navigation
* Account controls
* Responsive navigation
* Theme controls
* Route-aware navigation
* Collapsible sidebar

Feature-specific logic SHALL remain outside the shell.

---

# 15. Design System

The frontend SHALL maintain a consistent visual system.

The design system SHALL define reusable conventions for:

* Typography
* Spacing
* Colors
* Borders
* Radius
* Shadows
* Focus states
* Disabled states
* Error states
* Loading states

Reusable UI components SHALL consume these conventions consistently.

---

# 16. Theme Architecture

The frontend SHALL provide a centralized theme mechanism.

The architecture SHALL support:

```text
Light
Dark
System
```

where supported by the approved product requirements.

Theme state SHALL NOT be independently implemented by individual components.

---

# 17. Responsive Architecture

The frontend SHALL support:

* Desktop
* Laptop
* Tablet
* Mobile

Responsive behavior SHALL be part of component and layout design rather than a later patch.

The application shell SHALL adapt navigation and content layout according to available screen space.

---

# 18. Loading Architecture

Asynchronous operations SHALL have intentional loading states.

The architecture SHALL support:

* Full-page loading
* Route loading
* Component loading
* Button submission states
* Skeleton states
* Background refresh states

Loading indicators SHALL not unnecessarily block unrelated UI.

---

# 19. Error Architecture

Frontend errors SHALL be handled at appropriate boundaries.

The architecture SHALL distinguish between:

* Network errors
* Validation errors
* Authentication errors
* Authorization errors
* Not-found errors
* Conflict errors
* Server errors
* Unexpected client errors

User-facing errors SHALL be understandable.

Internal implementation details SHALL NOT be exposed to users.

---

# 20. Environment Configuration

Frontend configuration SHALL be environment-aware.

Supported environments:

```text
Development
Testing
Production
```

Only public configuration may be exposed to the browser.

Secrets SHALL NEVER be placed in frontend environment variables.

The frontend SHALL NOT contain:

```text
API keys
Database credentials
JWT signing secrets
Private service credentials
```

---

# 21. Dependency Direction

Dependencies SHALL flow from higher-level product composition toward lower-level infrastructure.

```text
Pages
  ↓
Features
  ↓
Shared Components / Hooks
  ↓
Application Infrastructure
  ↓
API Client
  ↓
Backend
```

Shared infrastructure SHALL NOT depend on individual product features.

Circular dependencies SHALL be prohibited.

---

# 22. Type Safety

TypeScript SHALL be used throughout the frontend.

The project SHALL use strict typing.

The use of `any` SHALL require explicit technical justification.

API request and response structures SHALL have explicit types.

Types SHALL be owned by the layer that understands their meaning.

---

# 23. Accessibility

Accessibility SHALL be treated as a foundational requirement.

The frontend SHALL support:

* Semantic HTML
* Keyboard navigation
* Focus management
* Accessible labels
* Accessible form errors
* Screen-reader compatibility
* Visible focus states
* Appropriate contrast

Accessibility SHALL be considered during component creation rather than added at the end of development.

---

# 24. Security Architecture

The frontend SHALL:

* Never trust client-side authorization.
* Never expose secrets.
* Never expose backend internals.
* Validate user input.
* Handle authentication failures consistently.
* Avoid unnecessary persistent sensitive information.
* Use secure transport in production.

Client-side validation SHALL improve UX but SHALL NOT replace backend validation.

---

# 25. Performance Architecture

The frontend SHALL be designed for scalable performance.

The architecture SHALL allow:

* Route-level lazy loading
* Code splitting
* Efficient rendering
* API caching
* Asset optimization
* Large-list optimization where required

Performance optimization SHALL remain evidence-driven.

Premature optimization SHALL be avoided.

---

# 26. Future CodeSense Modules

The architecture SHALL support future modules without changing the application foundation.

Expected future areas include:

```text
Debug
Optimize
Review
Learn
Productivity
Project Management
Repository Intelligence
AI Chat
```

Each future module SHALL be implemented as a feature rather than by modifying unrelated foundation code.

---

# 27. Future AI Compatibility

The frontend SHALL remain independent from specific AI providers.

Future AI capabilities may include:

* Streaming responses
* AI conversations
* Code analysis
* Debugging
* Code review
* Optimization
* Learning
* AI-generated recommendations

The frontend SHALL communicate through stable application/API contracts rather than provider-specific implementations.

---

# 28. Future Streaming Compatibility

The architecture SHALL remain capable of supporting future:

* Server-Sent Events
* WebSockets
* Streaming HTTP responses

without forcing a redesign of the application shell.

Streaming functionality itself SHALL only be implemented when required by the Master Roadmap.

---

# 29. Proposed Frontend Structure

The implementation SHALL evolve toward:

```text
frontend/
├── src/
│   ├── app/
│   │   ├── router/
│   │   ├── providers/
│   │   └── config/
│   │
│   ├── pages/
│   │
│   ├── features/
│   │
│   ├── components/
│   │   ├── ui/
│   │   ├── layout/
│   │   └── feedback/
│   │
│   ├── hooks/
│   │
│   ├── services/
│   │
│   ├── stores/
│   │
│   ├── types/
│   │
│   ├── utils/
│   │
│   ├── styles/
│   │
│   ├── App.tsx
│   └── main.tsx
│
├── public/
└── tests/
```

This is a target architecture.

Claude SHALL create directories incrementally as required by individual approved tasks.

Unused architectural abstractions SHALL NOT be created prematurely.

---

# 30. Architectural Constraints

The implementation SHALL NOT:

* Place API requests directly inside presentational components.
* Place business logic inside shared UI components.
* Use global state for data that can remain local.
* Treat frontend authorization as a security boundary.
* Hard-code backend URLs.
* Store secrets in frontend configuration.
* Couple the UI to a specific AI provider.
* Introduce unnecessary dependencies.
* Create circular module dependencies.
* Duplicate backend business logic.

---

# 31. Phase 03 Boundary

Phase 03 establishes the frontend foundation:

```text
Application Structure
Routing
Application Shell
UI Foundation
State Infrastructure
API Infrastructure
Authentication UI Foundation
Loading Infrastructure
Error Infrastructure
Responsive Foundation
```

Phase 03 SHALL NOT implement:

```text
AI Engine
Debug Engine
Project Analysis
Code Review Engine
Learning Engine
Productivity Engine
Deployment
```

Those remain governed by their respective phases in the Master Roadmap.

---

# 32. Implementation Discipline

Claude SHALL implement this architecture incrementally.

Claude SHALL:

1. Read the Master Roadmap.
2. Read the active Phase 03 task.
3. Inspect existing frontend implementation.
4. Reuse existing abstractions.
5. Implement only the approved task scope.
6. Verify the implementation.
7. Update documentation when required.

Claude SHALL NOT create speculative infrastructure solely because this architecture document mentions future functionality.

---

# 33. Architecture Change Policy

Any change affecting:

* Frontend technology
* Application boundaries
* Routing architecture
* State ownership
* API communication
* Authentication architecture
* Feature boundaries
* Dependency direction

requires an explicit architecture decision or approved architecture update.

---

# 34. Acceptance Criteria

Phase 03 frontend architecture SHALL be considered established when:

* Application boundaries are defined.
* Routing boundaries are defined.
* Feature boundaries are defined.
* Shared UI boundaries are defined.
* State ownership is defined.
* API communication is centralized.
* Authentication integration is defined.
* Responsive behavior is defined.
* Error and loading boundaries are defined.
* Architecture remains compatible with Phase 02.
* Architecture does not conflict with the Master Roadmap.

---

# 35. Final Principle

The frontend SHALL be treated as a scalable product platform, not a collection of isolated screens.

Future CodeSense AI capabilities SHALL be added as independent features on top of this foundation.

**Architecture before implementation.**

**Clear boundaries before complexity.**

**Reuse before duplication.**

**Verify before completion.**

**Follow the Master Roadmap.**
