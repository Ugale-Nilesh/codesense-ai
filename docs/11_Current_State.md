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
- Documentation reconciliation pass (August 2026): stack, folder structure, roadmap, and LICENSE unified — see "Documentation Reconciliation" section below
- Task002 – Setup Development Environment: verified/completed on contributor's local machine (Windows). Python 3.13.11, pip 25.3, venv + conda available, Git 2.55.0, Node.js v24.18.1 LTS, npm 11.16.0, VS Code 1.131.0, all 6 required extensions installed (Python, Pylance, ESLint, Prettier, Tailwind CSS IntelliSense, GitLens).
- Task003 – Backend Project Setup: complete. `.venv` created, fastapi/uvicorn/pydantic/python-dotenv installed and frozen to `requirements.txt`, full `app/` folder structure scaffolded (api, core, models, schemas, services, utils, middleware, dependencies), minimal FastAPI app with `/health` endpoint created, `.env.example` added, `backend/.gitignore` populated (was empty). Server verified running locally with Swagger UI and ReDoc both loading correctly.
- Task004 – Frontend Project Setup: complete. React + Vite + TypeScript project scaffolded via `npm create vite@latest . -- --template react-ts` (ESLint chosen as linter). Installed react-router-dom, axios, lucide-react, plus @tanstack/react-query and zustand (per finalized stack, ahead of Task004's original list). Tailwind CSS v4 configured via `@tailwindcss/vite` plugin + `@import "tailwindcss"` in `index.css`, verified working with a live rendering test (not just installed). Full `src/` folder structure scaffolded (assets, components, features, hooks, layouts, pages, routes, services, styles, utils). `.env.example` added. Dev server verified running at localhost:5173.
- Task005 – Configure Code Quality Tooling: complete. Backend: black, ruff, isort, mypy, pre-commit installed; `backend/pyproject.toml` created with all four tool configs (line-length 88, py312 target). Frontend: prettier, eslint-config-prettier installed (eslint-plugin-react-hooks/react-refresh already present from Task004); `eslint.config.js` extended with Prettier integration (flat config format — Task005's original `.eslintrc.cjs` instruction is obsolete for ESLint 10.8.0, which only reads flat config); `.prettierrc`/`.prettierignore` created; `format` npm script added (missing from Vite's default scaffold). Root `.vscode/settings.json` and `.vscode/extensions.json` created (format-on-save, ESLint/import auto-fix per-language formatters); added `charliermarsh.ruff` and `ms-python.black-formatter` VS Code extensions (in Task005's recommended list but not Task002's, since Task002 predated these tools). Root `.pre-commit-config.yaml` created (black, ruff --fix, trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files) and hook installed at `.git/hooks/pre-commit`. All verification commands passed: `black --check .`, `ruff check .`, `mypy app --ignore-missing-imports`, `npm run lint`, `npm run format` — dev server confirmed still running cleanly after formatting.
- Task006 – Environment Configuration: complete. Backend `.env.example` expanded to full variable set (app metadata, database, security, AI providers x3, GitHub, logging). Frontend `.env.example` expanded (app name, API base URL, environment, feature flag). `backend/app/core/config.py` created — centralized `Settings` class using python-dotenv, with defaults for non-secret app config and `None` defaults for unused secrets (DB/auth/AI keys aren't consumed by any code yet, so hard-validation was deferred rather than breaking startup). `backend/app/main.py` wired to use `settings.APP_NAME`/`APP_VERSION`, and `/health` now returns `environment` from settings — verified live via browser. `frontend/.gitignore` explicitly updated with `.env` (previously relied only on the root `.gitignore` pattern). Both `backend/.env` and `frontend/.env` created from templates and confirmed absent from `git status`. Frontend env variable access verified live via `import.meta.env.VITE_API_BASE_URL` rendered on page (reading it in the browser console directly fails due to a browser-console module-scope limitation, unrelated to the app).

---

# Current Task

Task006 – Environment Configuration (complete)

---

# Next Task

Task007 – Shared Utilities (not started; awaiting explicit instruction to proceed)

---

# Blockers

None.

---

# Tracked Accepted Risks

- **GHSA-qwww-vcr4-c8h2** (React Router: RSC Mode CSRF Bypass, high severity per npm audit, affects `react-router` >=7.12.0 <8.3.0). Current install: `react-router-dom@7.18.2` (latest published v7 release) — falls inside the affected range. **Not upgraded to v8.3.0** because that is a major version bump with breaking changes, and this project has not yet reached the point of implementing routing (Task004 scope is scaffolding only). **Accepted as non-exploitable**: the advisory explicitly states it only affects applications using React Router's unstable RSC (React Server Components) APIs. CodeSense AI's frontend is a plain Vite SPA — client-side rendered only, no SSR, no RSC usage planned per `docs/03_Technology_Stack.md`. Revisit if/when a v8 migration is separately planned, or if RSC usage is ever introduced (it should not be, per the finalized stack).

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
