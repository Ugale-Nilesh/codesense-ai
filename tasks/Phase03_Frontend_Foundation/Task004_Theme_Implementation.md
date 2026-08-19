# Task 004 --- Theme Implementation

**Phase:** Phase 03 --- Frontend Infrastructure\
**Task ID:** Task004\
**Specification ID:** P03-T004\
**Status:** Planned\
**Priority:** High

**Dependency:** - Task001 --- Frontend Initialization - Task003 ---
Layout System

------------------------------------------------------------------------

# 1. Objective

Implement the CodeSense AI visual theme and establish the frontend
design-system foundation.

The theme SHALL provide a consistent visual language across the
application and SHALL be reusable by the layout system and shared
component library.

The implementation SHALL follow the project's approved UI/UX Guidelines.

This task establishes the theme foundation.

It SHALL NOT implement feature-specific UI.

------------------------------------------------------------------------

# 2. Roadmap Alignment

The Phase 03 Master Roadmap defines the phase objective as:

> Develop the frontend architecture, routing system, UI framework,
> layouts, reusable components, and design system.

The Phase 03 deliverables explicitly include:

-   Theme implementation
-   Component library
-   Responsive framework

This task is responsible specifically for:

``` text
Theme implementation
```

The component library SHALL consume this theme rather than defining an
independent visual system.

------------------------------------------------------------------------

# 3. Authoritative References

Before implementation, Claude SHALL read:

1.  `CLAUDE.md`
2.  `tasks/00_MASTER_ROADMAP.md`
3.  `tasks/Phase03_Frontend_Foundation/README.md`
4.  `tasks/Phase03_Frontend_Foundation/ARCHITECTURE.md`
5.  `tasks/Phase03_Frontend_Foundation/DECISIONS.md`
6.  `tasks/Phase03_Frontend_Foundation/Task001_Frontend_Initialization.md`
7.  `tasks/Phase03_Frontend_Foundation/Task003_Layout_System.md`
8.  `docs/03_Technology_Stack.md`
9.  `docs/07_UI_UX_Guidelines.md`

The UI/UX Guidelines SHALL be the authoritative source for the visual
requirements of this task.

------------------------------------------------------------------------

# 4. Scope

## 4.1 In Scope

This task SHALL establish:

-   Dark-first visual theme
-   Color system
-   Semantic status colors
-   Typography system
-   Code typography
-   Surface hierarchy
-   Border treatment
-   Focus states
-   Theme integration with the application shell
-   Theme compatibility with shared components
-   Accessible contrast baseline
-   Centralized theme configuration

------------------------------------------------------------------------

# 5. Out of Scope

This task SHALL NOT implement:

-   Dashboard widgets
-   Debug screens
-   AI chat
-   Project management UI
-   Authentication screens
-   Monaco Editor implementation
-   Feature-specific page styling
-   Business logic
-   Backend functionality
-   AI functionality
-   Responsive framework implementation

Those belong to other tasks or later phases.

------------------------------------------------------------------------

# 6. Visual Identity

The approved CodeSense AI visual identity is:

``` text
Theme:
Dark-first

Accent:
Electric Blue

Success:
Green

Warning:
Amber

Error:
Red
```

Typography:

``` text
Headings:
Inter

Code:
JetBrains Mono
```

These values SHALL remain consistent throughout the frontend.

------------------------------------------------------------------------

# 7. Dark-First Theme

The application SHALL use a dark-first visual design.

The dark theme SHALL provide clear hierarchy between:

``` text
Application background
Surface
Elevated surface
Border
Primary text
Secondary text
Muted text
Interactive elements
Status indicators
```

The implementation SHALL avoid excessive visual noise.

The interface should feel like a modern developer tool rather than a
traditional content-heavy web application.

This follows the UI/UX principle:

> Clarity over decoration.

------------------------------------------------------------------------

# 8. Color System

The theme SHALL provide semantic color roles rather than encouraging
arbitrary colors throughout components.

At minimum, the theme SHALL define roles for:

``` text
Background
Surface
Elevated Surface
Border
Primary Text
Secondary Text
Muted Text
Accent
Success
Warning
Error
```

Components SHOULD consume semantic roles rather than hard-coded color
values.

------------------------------------------------------------------------

# 9. Electric Blue Accent

Electric Blue SHALL be the primary interactive accent.

It SHALL be used consistently for appropriate elements such as:

-   Primary interactive actions
-   Active navigation state
-   Focus-related visual treatment where appropriate
-   Links
-   Selected states
-   Important interactive indicators

The accent SHALL not be applied indiscriminately to every element.

------------------------------------------------------------------------

# 10. Semantic Status Colors

The theme SHALL provide semantic states:

``` text
Success → Green
Warning → Amber
Error   → Red
```

Status colors SHALL communicate meaning consistently.

Color SHALL NOT be the sole mechanism for communicating important state.

Where appropriate, status SHALL also use:

-   Text
-   Icons
-   Labels
-   Supporting descriptions

------------------------------------------------------------------------

# 11. Typography

The typography system SHALL follow the UI/UX Guidelines.

## Headings

Use:

``` text
Inter
```

for headings and primary interface typography.

The implementation SHALL establish a consistent hierarchy for:

-   Page titles
-   Section headings
-   Subheadings
-   Body text
-   Secondary text
-   Muted text

------------------------------------------------------------------------

# 12. Code Typography

Code content SHALL use:

``` text
JetBrains Mono
```

This applies to code-oriented interfaces such as:

-   Code blocks
-   Error output
-   Terminal commands
-   Future Monaco Editor content
-   Technical identifiers where appropriate

The theme SHALL not replace code typography with the normal UI font.

------------------------------------------------------------------------

# 13. Surface Hierarchy

The theme SHALL establish clear visual separation between application
surfaces.

The system SHOULD distinguish between:

``` text
Base background
Primary surface
Elevated surface
Interactive surface
```

The hierarchy SHALL be created using appropriate combinations of:

-   Background tones
-   Borders
-   Spacing
-   Elevation
-   Contrast

The implementation SHALL avoid excessive shadows or decorative effects.

------------------------------------------------------------------------

# 14. Borders

Borders SHALL be subtle and consistent.

They SHALL help establish:

-   Component boundaries
-   Input boundaries
-   Navigation separation
-   Surface hierarchy
-   Focus-related states where appropriate

Border treatment SHALL remain consistent across reusable components.

------------------------------------------------------------------------

# 15. Focus States

Interactive elements SHALL have clearly visible focus states.

Focus indicators SHALL:

-   Remain visible against the dark theme.
-   Be distinguishable from hover states.
-   Support keyboard navigation.
-   Meet the project's accessibility baseline.

Focus styling SHALL be centralized where possible.

------------------------------------------------------------------------

# 16. Accessibility

The UI/UX Guidelines specify:

``` text
WCAG AA contrast
Keyboard navigation
Focus indicators
Screen reader labels
```

The theme implementation SHALL support these requirements.

Claude SHALL verify that the selected theme colors provide appropriate
contrast for normal interface usage.

The theme SHALL not rely exclusively on subtle color differences to
communicate interaction states.

------------------------------------------------------------------------

# 17. Interactive States

The theme SHALL support consistent visual states for interactive
elements.

Where applicable:

``` text
Default
Hover
Focus
Active
Disabled
Selected
Error
Loading
```

The exact states SHALL be implemented by the relevant shared components,
but the theme SHALL provide the visual foundation required for them.

------------------------------------------------------------------------

# 18. Disabled State

Disabled elements SHALL remain distinguishable from enabled elements
without becoming unreadable.

Disabled styling SHALL:

-   Reduce emphasis.
-   Preserve sufficient readability.
-   Prevent confusion with normal interactive states.

Disabled elements SHALL not be represented solely by opacity if that
causes accessibility problems.

------------------------------------------------------------------------

# 19. Loading State

The UI/UX Guidelines specify:

``` text
Skeleton screens
Progress indicators
```

The theme SHALL support these states.

Loading visuals SHALL remain consistent with the dark-first theme.

Loading indicators SHALL not introduce unnecessary visual distraction.

------------------------------------------------------------------------

# 20. Error State

Error presentation SHALL follow the approved UI/UX direction:

``` text
Friendly language
Recovery actions
Retry button
```

The theme SHALL provide the visual foundation for error states.

This task does not implement feature-specific error workflows.

------------------------------------------------------------------------

# 21. Empty State Compatibility

The UI/UX Guidelines require empty pages to provide:

-   Explanation
-   Action button
-   Helpful examples

The theme SHALL provide sufficient visual hierarchy for those elements.

Actual empty-state components belong to the component-library task.

------------------------------------------------------------------------

# 22. Navigation Theme Integration

The theme SHALL support the navigation system established by Task003.

Navigation SHALL have visually distinguishable:

``` text
Normal state
Hover state
Active state
Focus state
Disabled state where applicable
```

The active navigation state SHOULD use the approved Electric Blue accent
appropriately.

------------------------------------------------------------------------

# 23. Layout Integration

The theme SHALL integrate with the application shell created by Task003.

The implementation SHALL ensure that:

-   Header surfaces use the theme.
-   Sidebar surfaces use the theme.
-   Main application background uses the theme.
-   Content surfaces use the theme.
-   Borders remain consistent.
-   Typography remains consistent.

The theme SHALL not duplicate the layout system.

------------------------------------------------------------------------

# 24. Tailwind Integration

The project technology stack specifies:

``` text
Tailwind CSS
```

The theme SHALL integrate with the project's existing Tailwind
configuration.

Claude SHALL inspect the existing configuration before modifying it.

Claude SHALL reuse existing configuration where appropriate.

A second CSS framework SHALL NOT be introduced.

------------------------------------------------------------------------

# 25. Theme Tokens

Where the project's architecture supports design tokens, semantic tokens
SHOULD be established for:

``` text
Background
Surface
Surface Elevated
Border
Text Primary
Text Secondary
Text Muted
Accent
Success
Warning
Error
```

The exact token implementation SHALL follow the existing frontend
architecture.

The purpose is to prevent components from scattering raw color values
throughout the codebase.

------------------------------------------------------------------------

# 26. Component Library Integration

Task005 SHALL consume the theme established here.

The following component categories SHALL be capable of using the theme:

``` text
Buttons
Inputs
Cards
Badges
Dialogs
Tabs
Loading states
Error states
Empty states
```

Task004 SHALL NOT implement all of these components.

It establishes the visual foundation they consume.

------------------------------------------------------------------------

# 27. Responsive Compatibility

The theme SHALL remain compatible with:

``` text
Desktop
Tablet
Mobile
```

Responsive implementation belongs to Task006.

Task004 SHALL not introduce viewport-specific theme duplication.

------------------------------------------------------------------------

# 28. Feature Independence

Theme infrastructure SHALL remain independent of product-specific
features.

The theme SHALL NOT contain logic such as:

``` text
if debugging
if project analysis
if AI review
if dashboard
```

Feature-specific styling SHALL consume the shared theme.

------------------------------------------------------------------------

# 29. Type Safety

If theme configuration is represented through TypeScript objects or
constants, it SHALL be typed appropriately.

The implementation SHALL:

-   Avoid unnecessary `any`.
-   Avoid duplicated token definitions.
-   Keep theme configuration discoverable.
-   Preserve strict TypeScript configuration.

------------------------------------------------------------------------

# 30. Configuration Ownership

Theme configuration SHALL have one clear owner.

There SHALL NOT be multiple competing sources defining:

``` text
Primary accent
Success color
Warning color
Error color
Typography
```

If an existing theme configuration exists, Claude SHALL extend or
correct it rather than creating another theme system.

------------------------------------------------------------------------

# 31. Security

The theme contains no secrets and SHALL not introduce any.

Claude SHALL ensure that theme implementation does not:

-   Embed credentials.
-   Read sensitive backend configuration.
-   Expose environment secrets.
-   Introduce unsafe HTML rendering.

------------------------------------------------------------------------

# 32. Functional Requirements

### FR-001 --- Dark Theme

The frontend SHALL provide the approved dark-first visual baseline.

### FR-002 --- Accent

Electric Blue SHALL be available as the primary accent.

### FR-003 --- Semantic Colors

Green, Amber, and Red SHALL represent success, warning, and error states
respectively.

### FR-004 --- Typography

Inter SHALL be used for interface typography and headings.

### FR-005 --- Code Typography

JetBrains Mono SHALL be used for code-oriented content.

### FR-006 --- Semantic Tokens

Theme roles SHALL be centrally defined.

### FR-007 --- Layout Integration

The theme SHALL integrate with the application shell.

### FR-008 --- Component Compatibility

Shared components SHALL be able to consume the theme.

### FR-009 --- Accessibility

The theme SHALL support the documented accessibility baseline.

### FR-010 --- Responsive Compatibility

The theme SHALL work across supported viewport sizes.

------------------------------------------------------------------------

# 33. Non-Functional Requirements

### NFR-001 --- Consistency

Equivalent interface elements SHALL use consistent visual treatment.

### NFR-002 --- Maintainability

Theme values SHALL not be duplicated unnecessarily.

### NFR-003 --- Accessibility

The theme SHALL support WCAG AA contrast requirements.

### NFR-004 --- Extensibility

The design system SHALL support future components without requiring a
complete theme rewrite.

### NFR-005 --- Simplicity

The theme SHALL avoid unnecessary visual complexity.

------------------------------------------------------------------------

# 34. Expected Files / Directories

Claude SHALL inspect the current frontend implementation before deciding
exact file locations.

Potential locations include:

``` text
frontend/
└── src/
    ├── styles/
    ├── theme/
    └── ...
```

or the project's existing Tailwind/configuration structure.

Claude SHALL follow the existing Phase 03 architecture.

### Create

Only theme-related files that are actually required.

### Modify

Only existing styling/configuration files required for theme
integration.

### Do Not Modify

Unless explicitly required:

``` text
backend/
database/
AI services
future product features
```

------------------------------------------------------------------------

# 35. Verification Matrix

  ID       Verification       Expected Result
  -------- ------------------ -----------------------------------------
  VR-001   Frontend startup   Application starts
  VR-002   Theme loading      Theme loads without errors
  VR-003   Dark baseline      Dark-first theme is active
  VR-004   Accent             Electric Blue is available
  VR-005   Success            Green semantic state available
  VR-006   Warning            Amber semantic state available
  VR-007   Error              Red semantic state available
  VR-008   Typography         Inter applied correctly
  VR-009   Code typography    JetBrains Mono available
  VR-010   Layout             Header/sidebar/main surfaces use theme
  VR-011   Focus              Focus indicators are visible
  VR-012   Contrast           WCAG AA baseline verified
  VR-013   Components         Shared components can consume theme
  VR-014   Responsive         Theme remains usable at supported sizes
  VR-015   Type check         No new TypeScript errors
  VR-016   Lint               Configured lint checks pass
  VR-017   Build              Production build succeeds
  VR-018   Runtime            No new critical runtime errors

------------------------------------------------------------------------

# 36. Acceptance Criteria

Task004 SHALL be considered complete only when:

-   [ ] Dark-first theme is implemented.
-   [ ] Electric Blue accent is implemented.
-   [ ] Green success state is available.
-   [ ] Amber warning state is available.
-   [ ] Red error state is available.
-   [ ] Inter typography is implemented.
-   [ ] JetBrains Mono is available for code content.
-   [ ] Semantic theme roles are centralized.
-   [ ] Application shell consumes the theme.
-   [ ] Focus states are visible.
-   [ ] WCAG AA contrast baseline is verified.
-   [ ] Theme works with shared components.
-   [ ] Theme remains responsive-compatible.
-   [ ] No duplicate theme system exists.
-   [ ] Type checking passes where configured.
-   [ ] Linting passes where configured.
-   [ ] Production build succeeds.
-   [ ] Verification matrix passes.
-   [ ] No unrelated functionality is modified.

------------------------------------------------------------------------

# 37. Failure Handling

If theme implementation or verification fails, Claude SHALL:

1.  Identify the affected theme token or integration point.
2.  Reproduce the issue.
3.  Identify the root cause.
4.  Apply the smallest appropriate correction.
5.  Re-run the failed verification.
6.  Re-run the complete Task004 verification matrix.

Claude SHALL NOT:

-   Create a second theme system.
-   Replace the approved visual identity.
-   Disable accessibility checks.
-   Hard-code theme values throughout components.
-   Introduce another CSS framework.
-   Modify unrelated product functionality.

------------------------------------------------------------------------

# 38. Rollback / Recovery

If Task004 introduces a regression:

1.  Identify Task004-specific changes.
2.  Restore the last verified Task003 state where necessary.
3.  Re-run Task003 verification.
4.  Isolate the theme regression.
5.  Re-implement the smallest safe correction.
6.  Re-run Task004 verification.

The layout foundation SHALL remain recoverable.

------------------------------------------------------------------------

# 39. Documentation Requirements

After implementation:

-   Update task status.
-   Update `CHECKLIST.md` where appropriate.
-   Document material theme decisions.
-   Keep the implementation synchronized with `ARCHITECTURE.md`.
-   Keep visual requirements synchronized with
    `docs/07_UI_UX_Guidelines.md`.

The UI/UX Guidelines SHALL remain authoritative for the approved visual
identity.

------------------------------------------------------------------------

# 40. Git Requirements

Task004 SHALL be committed as a focused implementation change.

Recommended commit:

``` text
feat(frontend): implement application theme
```

The commit SHOULD contain only Task004-related implementation, tests,
and directly related documentation.

------------------------------------------------------------------------

# 41. Definition of Done

``` text
Dark-first theme
        +
Electric Blue accent
        +
Semantic status colors
        +
Inter typography
        +
JetBrains Mono code typography
        +
Centralized theme roles
        +
Layout integration
        +
Accessibility verification
        +
Component compatibility
        +
Responsive compatibility
        +
Production build passed
        =
Task004 Complete
```

------------------------------------------------------------------------

# 42. Handoff

After Task004 is successfully verified, the theme SHALL be ready to
serve as the visual foundation for:

``` text
Task005 — Component Library
```

Task005 SHALL consume the theme rather than creating its own independent
visual system.

------------------------------------------------------------------------

# 43. Claude Execution Contract

Claude SHALL:

1.  Read the Master Roadmap.
2.  Read the UI/UX Guidelines.
3.  Read Phase 03 architecture.
4.  Read Phase 03 decisions.
5.  Read Task001 and Task003.
6.  Inspect the existing frontend styling/configuration.
7.  Implement only Task004.
8.  Reuse existing theme infrastructure where available.
9.  Verify visual and accessibility requirements.
10. Run type/lint/build checks where configured.
11. Report files created.
12. Report files modified.
13. Report verification results.
14. Stop after Task004 is verified.

Claude SHALL NOT automatically implement Task005.

------------------------------------------------------------------------

# 44. Stop Condition

Task004 ends when the CodeSense AI theme has been implemented,
integrated with the existing frontend layout, and verified against the
project's documented UI/UX requirements.

The next task begins only after explicit approval.
