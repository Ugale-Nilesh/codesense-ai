# Task007 — Frontend Verification

**Project:** CodeSense AI  
**Phase:** Phase 03 — Frontend Foundation  
**Task ID:** Task007  
**Specification ID:** P03-T007  
**Status:** Planned  
**Priority:** Critical  
**Type:** Verification and Quality Gate

---

# 1. Objective

Perform the final engineering verification of the Phase 03 frontend foundation.

This task SHALL verify that the frontend deliverables implemented across the previous Phase 03 tasks work together as one coherent frontend system.

The verification SHALL cover:

- Frontend initialization
- TypeScript configuration
- Vite application startup
- Routing
- Layout architecture
- Theme integration
- Reusable component infrastructure
- Responsive behavior
- Accessibility basics
- Code quality
- Production build readiness

Task007 is a verification and quality-gate task.

Task007 SHALL NOT introduce new product functionality unless a minimal correction is required to fix a verified Phase 03 defect.

---

# 2. Phase 03 Deliverables Under Verification

The Phase 03 roadmap defines the following engineering deliverables:

```text
1. Frontend initialized
2. Routing configured
3. Layout system implemented
4. Theme implementation completed
5. Component library established
6. Responsive framework verified
```

Task007 SHALL verify all six deliverables together.

The verification flow is:

```text
Task001 — Frontend Initialization
        ↓
Task002 — Routing System
        ↓
Task003 — Layout System
        ↓
Task004 — Theme Implementation
        ↓
Task005 — Component Library
        ↓
Task006 — Responsive Framework
        ↓
Task007 — Frontend Verification
```

Task007 SHALL determine whether the Phase 03 frontend foundation is technically ready for final phase completion.

---

# 3. Authoritative References

Before verification, Claude SHALL read and inspect:

1. `CLAUDE.md`
2. `tasks/00_MASTER_ROADMAP.md`
3. `tasks/Phase03_Frontend_Foundation/README.md`
4. `tasks/Phase03_Frontend_Foundation/ARCHITECTURE.md`
5. `tasks/Phase03_Frontend_Foundation/DECISIONS.md`
6. `tasks/Phase03_Frontend_Foundation/CHECKLIST.md`
7. `tasks/Phase03_Frontend_Foundation/Task001_Frontend_Initialization.md`
8. `tasks/Phase03_Frontend_Foundation/Task002_Routing_System.md`
9. `tasks/Phase03_Frontend_Foundation/Task003_Layout_System.md`
10. `tasks/Phase03_Frontend_Foundation/Task004_Theme_Implementation.md`
11. `tasks/Phase03_Frontend_Foundation/Task005_Component_Library.md`
12. `tasks/Phase03_Frontend_Foundation/Task006_Responsive_Framework.md`
13. `docs/02_System_Architecture.md`
14. `docs/03_Technology_Stack.md`
15. `docs/04_Folder_Structure.md`
16. `docs/07_UI_UX_Guidelines.md`

Verification SHALL be based on the actual repository state.

Task007 SHALL NOT mark a requirement as complete solely because a previous task specification says it was planned.

---

# 4. Verification Philosophy

Task007 SHALL verify reality rather than intention.

The following are not sufficient evidence of completion:

```text
A file exists.
A component has been created.
A route has been declared.
A package is listed in package.json.
A previous task says the work is complete.
```

The following types of evidence SHALL be used where applicable:

```text
Source inspection
Application startup
Manual route testing
Browser verification
Responsive inspection
Lint execution
Type checking
Production build
Runtime console inspection
Repository structure inspection
```

The central principle is:

> A requirement is complete only when the implementation and its verification evidence agree.

---

# 5. Scope

## 5.1 In Scope

Task007 SHALL verify:

- Frontend project initialization
- Dependency integrity
- TypeScript configuration
- Strict TypeScript compatibility
- Vite development startup
- React application mounting
- Route configuration
- Route navigation
- Nested route rendering
- Layout boundaries
- Shared application shell
- Theme integration
- Theme consistency
- Component reuse
- Component rendering
- Responsive behavior
- Navigation behavior
- Overflow behavior
- Accessibility basics
- Linting
- Production build
- Runtime errors
- Repository cleanliness
- Documentation consistency

---

# 6. Out of Scope

Task007 SHALL NOT verify:

- Complete backend functionality
- PostgreSQL functionality
- SQLAlchemy behavior
- Alembic migrations
- Authentication business logic
- JWT correctness
- AI provider functionality
- AI orchestration
- OCR
- Supabase Storage integration
- Debug engine functionality
- Project analysis logic
- Production deployment infrastructure
- Docker deployment
- CI/CD deployment

Those areas belong to other project phases.

---

# 7. Verification Preconditions

Task007 SHALL begin only when Tasks 001 through 006 are considered implemented.

Before starting verification, Claude SHALL confirm:

```text
Frontend directory exists
Node.js environment is available
Dependencies are installed
Frontend package configuration exists
Application can be inspected
```

If a required prior deliverable is clearly missing, Task007 SHALL record the failure.

Task007 SHALL NOT silently skip missing deliverables.

---

# 8. Verification Result States

Every verification item SHALL have one of the following states:

```text
PASS
FAIL
BLOCKED
NOT APPLICABLE
```

Definitions:

### PASS

The requirement has been verified successfully.

### FAIL

The requirement was tested or inspected and does not satisfy the specification.

### BLOCKED

Verification cannot continue because of an external or prerequisite problem.

### NOT APPLICABLE

The requirement does not apply to the actual approved implementation.

A requirement SHALL NOT be marked PASS without evidence.

---

# 9. Required Evidence

For every failed or blocked verification item, Claude SHALL record:

```text
Verification ID
Requirement
Actual result
Expected result
Failure evidence
Affected files or area
Root cause if known
Recommended correction
```

Successful items SHOULD also be traceable to a verification method.

---

# 10. Verification Order

The preferred verification order is:

```text
Repository inspection
        ↓
Dependency inspection
        ↓
Static configuration inspection
        ↓
Type checking
        ↓
Linting
        ↓
Production build
        ↓
Development server startup
        ↓
Browser runtime verification
        ↓
Routing verification
        ↓
Layout verification
        ↓
Theme verification
        ↓
Component verification
        ↓
Responsive verification
        ↓
Accessibility inspection
        ↓
Final regression check
```

This order SHALL be followed where practical because earlier failures can invalidate later checks.

---

# 11. Verification Area A — Frontend Initialization

The frontend SHALL be verified against the Phase 03 initialization requirements.

At minimum, verify:

```text
React application exists
Vite configuration exists where required
TypeScript is configured
Frontend dependencies are installed
Development server starts
Application mounts successfully
No critical startup error occurs
```

---

# 12. Frontend Initialization Checks

| ID | Check | Expected Result |
|---|---|---|
| FI-001 | Frontend directory | Exists in approved location |
| FI-002 | package.json | Exists and describes frontend dependencies |
| FI-003 | React dependency | Installed |
| FI-004 | Vite dependency | Installed |
| FI-005 | TypeScript | Configured |
| FI-006 | tsconfig | Present where required |
| FI-007 | Entry point | Exists and mounts application |
| FI-008 | Root component | Renders successfully |
| FI-009 | Dev server | Starts successfully |
| FI-010 | Browser startup | Application loads |
| FI-011 | Startup console | No critical errors |
| FI-012 | Production build | Can proceed through build pipeline |

---

# 13. TypeScript Verification

Task007 SHALL verify that the frontend uses the approved TypeScript architecture.

Checks SHALL include:

```text
TypeScript configuration exists
Strict mode follows approved requirements
No intentional suppression hides unresolved errors
Application source does not rely on unnecessary any types
Imports resolve correctly
Production code compiles
```

Task007 SHALL inspect whether errors have been suppressed through patterns such as:

```text
@ts-ignore
@ts-nocheck
excessive any
unsafe casts used as permanent workarounds
```

Temporary exceptions SHALL be documented.

---

# 14. TypeScript Acceptance Criteria

The frontend SHALL pass the project's configured TypeScript validation.

The implementation SHALL NOT be considered verified if:

```text
Known TypeScript errors are ignored
Strict mode was disabled to pass checks
Type checking was skipped because errors exist
```

If the project does not have a separate type-check command, the production build and configured compiler behavior SHALL be used as evidence.

---

# 15. Verification Area B — Routing

Task007 SHALL verify the routing system implemented in Task002.

The router SHALL be verified through actual navigation rather than route declaration alone.

At minimum, verify:

```text
Router provider is active
Configured routes render
Route navigation works
Nested routes render where used
Layout routes render child content
Unknown routes are handled intentionally
Direct URL loading does not break the SPA runtime
```

---

# 16. Routing Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| RT-001 | Router initialization | Router is mounted |
| RT-002 | Root route | Renders expected content |
| RT-003 | Public route | Renders correctly |
| RT-004 | Application route | Renders inside app shell |
| RT-005 | Navigation links | Navigate without full-page failure |
| RT-006 | Nested route | Renders through outlet |
| RT-007 | Direct URL load | Supported route loads correctly |
| RT-008 | Unknown route | Intentional fallback behavior |
| RT-009 | Back navigation | Browser navigation remains coherent |
| RT-010 | Shared layout persistence | Layout behaves according to route hierarchy |
| RT-011 | Console | No critical route errors |
| RT-012 | Route duplication | No conflicting duplicate route definitions |

---

# 17. Route Verification Procedure

For each implemented route:

1. Start from the application root.
2. Navigate using the application's normal navigation.
3. Confirm the expected page content appears.
4. Confirm the URL changes correctly.
5. Confirm shared application chrome behaves as expected.
6. Reload the route directly.
7. Confirm the route remains renderable.
8. Check the browser console for errors.
9. Repeat for nested routes.

Task007 SHALL not assume route correctness from source code alone.

---

# 18. Verification Area C — Layout System

Task007 SHALL verify the layout system implemented in Task003.

The layout verification SHALL cover:

```text
Public layout boundaries
Application layout boundaries
Shared navigation placement
Header placement where implemented
Main content region
Route outlet placement
Shared chrome reuse
Page framing
Scroll ownership
Overflow behavior
```

---

# 19. Layout Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| LY-001 | Public layout | Public routes use intentional public structure |
| LY-002 | App layout | Application routes use shared shell |
| LY-003 | Navigation region | Structurally separate from page content |
| LY-004 | Header region | Present where approved |
| LY-005 | Main landmark | Main content region exists |
| LY-006 | Route outlet | Child route content renders |
| LY-007 | Shared chrome | Not duplicated across pages |
| LY-008 | Page transition | Content changes correctly |
| LY-009 | Scroll behavior | Ordinary pages remain usable |
| LY-010 | Overflow | No critical clipping |
| LY-011 | Content width | Consistent page framing |
| LY-012 | Workspace readiness | Future wide layouts remain possible |

---

# 20. Layout Acceptance Criteria

The layout system SHALL pass verification when:

```text
Public and application layout boundaries are intentional
Protected application pages use shared structure
Page content renders through the route hierarchy
Navigation and content are structurally separated
No page duplicates the global application shell
Main content remains reachable
No critical clipping occurs
```

---

# 21. Verification Area D — Theme Implementation

Task007 SHALL verify the theme system implemented in Task004.

The verification SHALL inspect:

```text
Theme provider or theme mechanism
Theme tokens
Global styles
Semantic color usage
Typography baseline
Spacing consistency
Background consistency
Surface consistency
Interactive state consistency
Theme persistence if implemented
```

Task007 SHALL verify the actual implementation strategy rather than assuming a particular theme library.

---

# 22. Theme Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| TH-001 | Theme system | Exists according to approved architecture |
| TH-002 | Global styling | Applies successfully |
| TH-003 | Semantic colors | Used consistently |
| TH-004 | Typography | Consistent baseline |
| TH-005 | Background | Intentional application background |
| TH-006 | Surfaces | Consistent structural surfaces |
| TH-007 | Text contrast | Reasonable readability |
| TH-008 | Interactive states | Visible states where applicable |
| TH-009 | Theme provider | Works where implementation requires it |
| TH-010 | Route consistency | Theme survives navigation |
| TH-011 | Hard-coded drift | No widespread inconsistent styling |
| TH-012 | Console/runtime | No critical theme errors |

---

# 23. Theme Toggle Verification

If the approved implementation includes multiple themes or theme switching, Task007 SHALL verify:

```text
Theme can be changed
Visible UI changes correctly
Selection persists if persistence is specified
Navigation does not unexpectedly reset the theme
No unreadable text or surfaces appear
```

If theme switching is not part of the approved implementation, Task007 SHALL not fail the task for its absence.

---

# 24. Verification Area E — Component Library

Task007 SHALL verify the reusable component infrastructure implemented in Task005.

The verification SHALL determine whether shared UI patterns are actually reusable.

At minimum, inspect:

```text
Component organization
Component naming
Component exports
Reuse across pages
Prop typing
Composition behavior
Styling consistency
Accessibility basics
```

Task007 SHALL not require a massive component library.

The goal is an intentional and maintainable shared component foundation.

---

# 25. Component Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| CP-001 | Shared component directory | Exists where architecture specifies |
| CP-002 | Reusable components | Have clear responsibility |
| CP-003 | Props | Typed appropriately |
| CP-004 | Duplication | Shared patterns are not repeatedly copied |
| CP-005 | Composition | Components compose predictably |
| CP-006 | Styling | Uses approved theme approach |
| CP-007 | Accessibility | Interactive components remain usable |
| CP-008 | Imports | Resolve correctly |
| CP-009 | Rendering | Components render successfully |
| CP-010 | Scope | No feature logic hidden in generic components |

---

# 26. Component Reuse Check

Task007 SHALL inspect for unnecessary duplication.

Examples of potential duplication:

```text
Multiple custom buttons with identical responsibilities
Repeated page container markup
Repeated navigation item implementations
Repeated card structures
Repeated loading placeholders
```

Not every visual similarity requires a shared component.

Task007 SHALL only identify duplication where abstraction improves maintainability.

---

# 27. Verification Area F — Responsive Framework

Task007 SHALL verify the responsive framework implemented in Task006.

Verification SHALL include the approved responsive breakpoints and representative viewport sizes.

At minimum, inspect:

```text
Small viewport
Medium viewport
Large viewport
Navigation adaptation
Content width
Horizontal overflow
Text clipping
Interactive control accessibility
Layout wrapping
```

---

# 28. Responsive Viewport Baseline

Unless the approved UI specification defines different values, verification SHOULD inspect representative viewport categories:

```text
Small mobile
Large mobile
Tablet
Laptop
Desktop
Wide desktop
```

Representative widths may be selected according to the actual breakpoint system.

Task007 SHALL verify the categories rather than blindly enforcing arbitrary pixel values.

---

# 29. Responsive Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| RS-001 | Small viewport | Layout remains usable |
| RS-002 | Medium viewport | Layout adapts intentionally |
| RS-003 | Large viewport | Layout uses space appropriately |
| RS-004 | Navigation | Adapts according to approved design |
| RS-005 | Main content | Remains reachable |
| RS-006 | Horizontal overflow | No unintended viewport overflow |
| RS-007 | Text | No critical clipping |
| RS-008 | Controls | Remain reachable |
| RS-009 | Route pages | Do not break structurally |
| RS-010 | Theme | Remains visually coherent |
| RS-011 | Layout variants | Continue to function |
| RS-012 | Console | No critical responsive runtime errors |

---

# 30. Responsive Testing Procedure

For each representative viewport:

1. Open the application.
2. Check the public layout.
3. Check the authenticated application layout.
4. Check at least one standard content page.
5. Check any wide or workspace-oriented page that exists.
6. Inspect navigation.
7. Inspect horizontal overflow.
8. Inspect vertical content reachability.
9. Inspect major interactive controls.
10. Navigate between routes.
11. Resize or switch viewport category.
12. Confirm the layout remains coherent.

---

# 31. Horizontal Overflow

Task007 SHALL specifically inspect for unintended horizontal scrolling.

Unintended overflow may result from:

```text
Fixed widths
Large min-width values
Absolute positioning
Oversized margins
Unwrapped content
Navigation width conflicts
Viewport unit misuse
```

Intentional overflow inside specialized elements such as large tables MAY be acceptable if properly contained.

---

# 32. Verification Area G — Accessibility Basics

Task007 SHALL perform a baseline accessibility review.

This is not a full formal accessibility certification.

At minimum, inspect:

```text
Semantic landmarks
Heading hierarchy
Keyboard reachability
Visible focus behavior
Button semantics
Link semantics
Form labels where forms exist
Color readability
Main content identification
Navigation identification
```

---

# 33. Accessibility Verification Matrix

| ID | Verification | Expected Result |
|---|---|---|
| AC-001 | Main content | Identifiable main region |
| AC-002 | Navigation | Meaningful navigation structure |
| AC-003 | Headings | Logical hierarchy |
| AC-004 | Buttons | Semantic interactive elements |
| AC-005 | Links | Used for navigation |
| AC-006 | Keyboard | Main controls reachable |
| AC-007 | Focus | Focus is not globally hidden |
| AC-008 | Contrast | Basic readability maintained |
| AC-009 | Labels | Inputs have accessible identification |
| AC-010 | Content order | Logical DOM order |

---

# 34. Keyboard Verification

Where practical, Task007 SHALL verify basic keyboard navigation.

At minimum:

```text
Tab moves through interactive elements
Focus remains visible
Primary navigation is reachable
Main content controls are reachable
Focus does not disappear unexpectedly
```

Task007 SHALL record obvious keyboard traps as failures.

---

# 35. Verification Area H — Code Quality

Task007 SHALL run the configured frontend quality tools.

Depending on the approved frontend setup, this may include:

```text
npm run lint
npm run typecheck
npm run build
npm test
```

Claude SHALL inspect `package.json` and use the actual configured commands.

Task007 SHALL NOT invent a command and treat it as project verification.

---

# 36. Lint Verification

The configured lint command SHALL be executed where available.

A successful lint result SHALL require:

```text
Exit code 0
No unresolved lint errors
No critical rules disabled solely to bypass errors
```

Warnings SHALL be reviewed according to the repository policy.

---

# 37. Type Check Verification

If a dedicated type-check script exists, it SHALL be executed.

If no dedicated script exists, Task007 SHALL document the verification method used.

The verification SHALL ensure the project does not hide known compile errors.

---

# 38. Production Build Verification

The production build is mandatory for Task007 unless the environment is blocked.

The build SHALL verify:

```text
Source compilation
Dependency resolution
Asset generation
Route-related imports
Production bundling
```

A production build failure SHALL prevent Task007 from being marked fully complete.

---

# 39. Development Server Verification

The development server SHALL be started using the repository's configured command.

Task007 SHALL verify:

```text
Server starts
Application URL is available
Application renders
No immediate fatal error occurs
```

The server SHALL be stopped cleanly after verification where appropriate.

---

# 40. Browser Console Verification

During manual verification, Claude SHALL inspect for critical browser errors.

Examples of critical errors:

```text
Uncaught exceptions
React rendering failures
Failed module imports
Router crashes
Provider crashes
Repeated fatal runtime errors
```

Non-critical development warnings SHALL be evaluated individually.

---

# 41. Network Verification

Task007 SHALL only verify frontend network behavior that belongs to Phase 03.

If the frontend intentionally does not yet connect to a backend, missing backend API calls SHALL NOT automatically be treated as a Phase 03 failure.

Unexpected failed requests created by broken frontend initialization SHOULD be investigated.

---

# 42. Verification Area I — Repository Structure

Task007 SHALL verify that the implemented frontend follows the approved repository organization.

The verification SHALL inspect:

```text
Frontend location
Source directory
Layouts
Routes
Pages
Components
Styles
Configuration
```

Task007 SHALL not enforce speculative folders that are not required by the approved architecture.

---

# 43. Repository Structure Checks

| ID | Verification | Expected Result |
|---|---|---|
| ST-001 | Frontend root | Matches approved architecture |
| ST-002 | Source structure | Understandable |
| ST-003 | Routes | Centrally organized |
| ST-004 | Layouts | Centrally organized |
| ST-005 | Pages | Route-level responsibility |
| ST-006 | Components | Reusable patterns organized |
| ST-007 | Styles | Theme architecture is clear |
| ST-008 | Configuration | Not scattered unnecessarily |
| ST-009 | Dead duplicates | No obvious duplicate architecture |
| ST-010 | Generated files | Not committed unless intended |

---

# 44. .gitignore Verification

Task007 SHALL inspect the frontend-related `.gitignore` behavior.

Generated or local-only files SHOULD not be accidentally committed when excluded by project policy.

Examples may include:

```text
node_modules
dist
coverage
environment-specific local files
editor-specific temporary files
```

Task007 SHALL not add ignores blindly without checking repository requirements.

---

# 45. Dependency Verification

Task007 SHALL inspect the actual dependency configuration.

The verification SHALL identify:

```text
Required dependencies
Duplicate or conflicting dependencies
Unused critical dependencies
Unexpected version conflicts
```

Task007 SHALL not perform a major dependency upgrade during verification unless necessary to fix a verified Phase 03 blocker.

---

# 46. Package Script Verification

Task007 SHALL inspect available package scripts.

The verification report SHALL state the actual commands used.

Typical commands may include:

```text
dev
build
lint
test
typecheck
```

Only commands actually defined by the project SHALL be reported as executed.

---

# 47. Runtime Regression Verification

After fixing any Task007 defect, Claude SHALL re-run affected verification checks.

At minimum, after a structural correction:

```text
Re-run lint
Re-run type checking if applicable
Re-run production build
Re-open affected route
Re-check affected viewport
```

A fix SHALL not be accepted merely because the original error disappeared.

---

# 48. No New Feature Rule

Task007 SHALL NOT become a feature-development task.

The following are examples of prohibited scope expansion:

```text
Adding AI chat because a page looks empty
Implementing authentication because protected routes exist
Adding a database because future pages need data
Building a dashboard feature
Implementing project management
Adding Monaco Editor workflows
Creating backend APIs
```

Only corrections required to verify the existing Phase 03 frontend foundation are permitted.

---

# 49. Allowed Corrections

Task007 MAY correct:

```text
Broken imports
Broken route configuration
Incorrect layout nesting
Missing provider integration
Theme integration regressions
Component rendering defects
Responsive defects
TypeScript errors
Lint errors
Build errors
Accessibility regressions directly caused by Phase 03 work
```

Corrections SHALL remain focused.

---

# 50. Failure Classification

Failures SHOULD be classified as:

```text
Critical
Major
Minor
Informational
```

### Critical

Prevents the application or required verification from functioning.

Examples:

```text
Application cannot start
Production build fails
Router crashes
Core layout does not render
```

### Major

Core functionality works but a required deliverable is materially incomplete.

### Minor

Does not prevent Phase 03 completion but should be corrected.

### Informational

Observation with no current failure.

---

# 51. Critical Failure Gate

The following failures SHALL block Task007 completion:

```text
Frontend cannot start
React application cannot render
Required routes fail
Core application layout fails
Required theme system is broken
Responsive framework has critical structural failures
Configured lint has unresolved errors
Production build fails
```

Blocked external tooling SHALL be documented separately.

---

# 52. Verification Report Format

At the end of Task007, Claude SHALL produce a verification report containing:

```text
Verification date
Repository state checked
Frontend path
Commands executed
Overall result
Passed checks
Failed checks
Blocked checks
Files changed during verification
Known limitations
Recommendation
```

The report SHALL distinguish verified facts from assumptions.

---

# 53. Required Command Evidence

The final report SHALL include the actual relevant command results.

Example structure:

```text
Command:
npm run lint

Result:
PASS
```

Example:

```text
Command:
npm run build

Result:
PASS
```

If a command is unavailable:

```text
Command:
npm run typecheck

Result:
NOT AVAILABLE
Reason:
No typecheck script exists in package.json.
Alternative evidence:
Production build performed TypeScript validation.
```

---

# 54. Verification Checklist

## Initialization

- [ ] Frontend directory verified
- [ ] package.json verified
- [ ] Dependencies installed
- [ ] React verified
- [ ] Vite verified
- [ ] TypeScript verified
- [ ] Entry point verified
- [ ] Development server verified

## Routing

- [ ] Router mounted
- [ ] Public routes verified
- [ ] Application routes verified
- [ ] Nested routes verified
- [ ] Navigation verified
- [ ] Direct route loading verified
- [ ] Unknown route behavior verified

## Layout

- [ ] Public layout verified
- [ ] Application shell verified
- [ ] Navigation region verified
- [ ] Header region verified where applicable
- [ ] Main content verified
- [ ] Route outlet verified
- [ ] Scroll behavior verified
- [ ] Overflow verified

## Theme

- [ ] Theme architecture verified
- [ ] Global styling verified
- [ ] Semantic styling verified
- [ ] Typography baseline verified
- [ ] Theme consistency verified
- [ ] Theme switching verified if applicable

## Components

- [ ] Shared component organization verified
- [ ] Reuse verified
- [ ] Props verified
- [ ] Rendering verified
- [ ] Accessibility basics verified

## Responsive

- [ ] Small viewport verified
- [ ] Medium viewport verified
- [ ] Large viewport verified
- [ ] Navigation adaptation verified
- [ ] Content reachability verified
- [ ] Horizontal overflow verified

## Quality

- [ ] Lint passed
- [ ] Type check passed or equivalent verified
- [ ] Production build passed
- [ ] Runtime errors checked
- [ ] Console checked

## Repository

- [ ] Architecture reviewed
- [ ] Structure reviewed
- [ ] .gitignore reviewed
- [ ] Documentation consistency reviewed
- [ ] No unrelated files introduced

---

# 55. End-to-End Smoke Test

Task007 SHALL perform an end-to-end frontend smoke test.

The minimum smoke test is:

1. Start the frontend.
2. Open the application root.
3. Confirm React renders.
4. Navigate through all representative implemented routes.
5. Confirm route content renders.
6. Confirm the shared layout behaves correctly.
7. Confirm theme styling remains coherent.
8. Confirm reusable components render.
9. Resize through representative viewport categories.
10. Check for critical console errors.
11. Run lint.
12. Run production build.

---

# 56. Smoke Test Success Criteria

The smoke test SHALL pass only if:

```text
Application starts
Routes work
Layouts work
Theme works
Components render
Responsive behavior is coherent
No critical runtime error exists
Quality checks pass
Production build passes
```

---

# 57. Regression Strategy

If Task007 modifies any frontend file, verification SHALL use targeted regression testing.

Examples:

```text
Route fix
→ Verify affected routes and shared layout

Theme fix
→ Verify multiple representative pages

Component fix
→ Verify all direct consumers

Responsive fix
→ Verify all affected viewport categories
```

Task007 SHALL not assume a local correction has no side effects.

---

# 58. Documentation Verification

Task007 SHALL compare the implemented frontend with Phase 03 documentation.

The following SHALL be checked:

```text
Task status accuracy
Architecture consistency
Decision consistency
Checklist consistency
Technology stack consistency
File naming consistency
```

If implementation intentionally differs from documentation, the difference SHALL be documented.

---

# 59. Architecture Drift

Architecture drift occurs when implementation diverges materially from approved design without documentation.

Examples:

```text
A second routing system exists
Pages recreate global layouts
A different styling system was introduced
State management conflicts with approved architecture
Duplicate component libraries exist
```

Task007 SHALL identify material drift.

Task007 SHALL not invent drift where implementation details merely differ from illustrative examples.

---

# 60. Technology Stack Compliance

The frontend SHALL remain consistent with the approved Phase 03 technology baseline.

The verification SHALL confirm relevant frontend choices remain aligned with:

```text
React
Vite
TypeScript
Tailwind CSS
React Router
TanStack Query where introduced
Zustand where introduced
```

Task007 SHALL not require unused future technologies to be integrated prematurely.

---

# 61. Deferred Technology Rule

Some approved technologies may belong to later implementation stages.

Task007 SHALL distinguish:

```text
Required now
```

from:

```text
Approved for future use
```

A technology SHALL NOT be marked missing merely because it is not yet required by the current frontend foundation.

---

# 62. Performance Sanity Check

Task007 SHALL perform a basic frontend performance sanity check.

This is not a formal performance benchmark.

Inspect for obvious problems such as:

```text
Infinite render loops
Repeated route remounting caused by broken architecture
Console error floods
Unnecessary full application crashes
Uncontrolled layout thrashing
```

Task007 SHALL not introduce premature performance optimization.

---

# 63. Error Boundary Compatibility

If error boundaries are part of the current architecture, Task007 SHALL verify that they render intentionally.

If they are not yet implemented, their absence SHALL only be treated as a failure if required by an approved specification.

---

# 64. Loading State Compatibility

Task007 SHALL verify that the frontend architecture remains capable of future loading states.

The task SHALL not require every future feature to implement loading UI before the feature exists.

The layout and component structure SHALL not prevent later loading-state integration.

---

# 65. Empty State Compatibility

The frontend foundation SHALL remain capable of representing pages before backend features exist.

Temporary placeholder content SHALL not be mistaken for missing architecture if routing, layout, theme, and component responsibilities are already verified.

---

# 66. Security Sanity Check

Task007 SHALL perform only frontend-foundation-level security sanity checks.

Examples:

```text
No committed secrets discovered in frontend source
No API keys hard-coded in committed application code
Environment variable usage follows project conventions where present
```

Task007 SHALL not perform a complete security audit.

---

# 67. Secret Handling Check

If frontend environment variables exist, Task007 SHALL inspect whether obvious secrets are exposed incorrectly.

The verification SHALL NOT print or reproduce secret values.

Potentially sensitive files SHALL be handled according to repository policy.

---

# 68. Final Acceptance Matrix

| Area | Required | Result |
|---|---|---|
| Frontend initialization | Yes | PASS / FAIL |
| TypeScript | Yes | PASS / FAIL |
| Development startup | Yes | PASS / FAIL |
| Routing | Yes | PASS / FAIL |
| Layout system | Yes | PASS / FAIL |
| Theme implementation | Yes | PASS / FAIL |
| Component library | Yes | PASS / FAIL |
| Responsive framework | Yes | PASS / FAIL |
| Accessibility basics | Yes | PASS / FAIL |
| Lint | Yes | PASS / FAIL |
| Production build | Yes | PASS / FAIL |
| Runtime sanity | Yes | PASS / FAIL |
| Documentation consistency | Yes | PASS / FAIL |
| Repository structure | Yes | PASS / FAIL |

---

# 69. Task007 Completion Criteria

Task007 SHALL be marked complete only when:

```text
All required Phase 03 deliverables have been verified
        +
No unresolved critical verification failures remain
        +
Required routes work
        +
Layout architecture works
        +
Theme implementation works
        +
Reusable components render correctly
        +
Responsive verification passes
        +
Lint passes
        +
Production build passes
        +
Runtime has no critical errors
        +
Documentation reflects the verified state
        =
Task007 Complete
```

---

# 70. Failure Condition

Task007 SHALL remain incomplete if any required critical gate fails.

A partial verification report SHALL still be produced.

The report SHALL clearly state:

```text
PHASE 03 VERIFICATION: FAILED
```

or:

```text
PHASE 03 VERIFICATION: BLOCKED
```

The next task SHALL not claim final Phase 03 completion until blocking issues are resolved.

---

# 71. Handoff

If Task007 passes, the verified frontend foundation SHALL be handed to:

```text
Task008 — Phase03 Completion
```

Task008 SHALL perform the final phase-level acceptance and completion process.

Task007 SHALL not itself declare the entire Phase 03 officially closed.

Its responsibility is:

> Verify that the frontend foundation is ready to be accepted.

---

# 72. Git Requirements

Verification-related corrections SHALL be committed in focused commits.

Recommended examples:

```text
fix(frontend): resolve phase 03 verification issues
```

or, if no code changes are needed:

```text
docs(frontend): record phase 03 verification
```

Unrelated feature work SHALL not be included.

---

# 73. Claude Execution Contract

Claude SHALL:

1. Read all authoritative references.
2. Inspect the actual repository.
3. Verify Tasks 001 through 006 against implementation.
4. Run the actual configured quality commands.
5. Start the frontend where possible.
6. Verify representative routes.
7. Verify layout boundaries.
8. Verify theme integration.
9. Verify shared components.
10. Verify representative responsive viewports.
11. Inspect critical runtime errors.
12. Check repository and documentation consistency.
13. Fix only verified Phase 03 defects within scope.
14. Re-run affected checks after fixes.
15. Produce a verification report.
16. Update Task007 status and checklist evidence where required.
17. Stop after verification is complete.

Claude SHALL NOT automatically start Task008.

---

# 74. Stop Condition

Task007 ends when the Phase 03 frontend foundation has been verified as an integrated system, all required quality gates have passed, no unresolved critical defects remain, the production build succeeds, and the verification evidence is documented.

The next task begins only after explicit approval.
