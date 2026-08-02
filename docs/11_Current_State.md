# CodeSense AI
## Current Project State

**Status:** Active Development

---

# Repository Version

Version: 1.0

---

# Current Development Phase

Phase 01 — Foundation

---

# Current Milestone

Establish a production-ready repository, documentation, development workflow, and engineering foundation before implementation begins.

---

# Completed

- Repository initialized
- Documentation structure completed
- Master roadmap created
- Phase 01 task breakdown completed
- Backend structure planned
- Frontend structure planned
- Task001 – Initialize Repository Structure: verified/completed (root .gitignore added)

---

# Current Task

Task001 – Initialize Repository Structure (complete)

---

# Next Task

Task002 – Setup Development Environment (not started; awaiting explicit instruction to proceed)

---

# Blockers

None.

---

# Documentation Reconciliation (August 2026)

The technology stack was finalized and the repository was reconciled
against it. Summary of what changed:

- Backend stack unified to Python + FastAPI + SQLAlchemy + Alembic
  across `docs/02`, `docs/03`, `docs/04`, `docs/05`, `docs/15`, and
  `tasks/00_MASTER_ROADMAP.md`. NestJS, Express, and Prisma references
  removed.
- Frontend stack unified to React + Vite + TypeScript + Tailwind CSS +
  React Router + TanStack Query + Zustand across `docs/02`, `docs/03`,
  and `docs/04`. Next.js references removed.
- AI provider layer now explicitly names Anthropic Claude API, OpenAI
  API, and Google Gemini API (`docs/02`, `docs/03`).
- Storage unified to Supabase Storage; Auth unified to JWT only.
- Redis and Celery are documented as explicitly deferred ("Future")
  rather than active V1 dependencies.
- Repository name confirmed as `codesense-ai` (kept, not renamed).
  References to `CodeSense-AI` in `tasks/Task001` and `tasks/Task005`
  corrected.
- MIT `LICENSE` added at root.
- `docs/12_Development_Roadmap.md` converted to a summary that points
  to `tasks/00_MASTER_ROADMAP.md` as the sole authoritative roadmap.
- `CLAUDE.md/CLAUDE_09_Backend_Standards.md` confirmed present and
  already consistent with the finalized backend stack.
- `ai/README.md` no longer references prompt files that don't exist.

---

# Repository Health

Documentation: Complete

Architecture: Defined

Tasks: Defined

Implementation: Not Started

Testing: Pending

Deployment: Pending

---

# AI Instructions

Whenever implementation begins:

1. Read CLAUDE instructions.
2. Read the roadmap.
3. Read the current task.
4. Implement the first incomplete task.
5. Verify implementation.
6. Update this document.
7. Continue until a stop condition is reached.
