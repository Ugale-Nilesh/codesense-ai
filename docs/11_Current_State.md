# CodeSense AI

## Current Project State

**Status:** Active Development

---

# Repository Version

Version: 1.0

---

# Current Development Phase

Phase 02 — Backend Infrastructure

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
- Task007 – Shared Utilities: complete. Backend `app/utils/` — `constants.py` (API version, file extensions, upload limits, pagination), `logger.py` (centralized `get_logger()` reading `settings.LOG_LEVEL`), `validators.py` (email/username/UUID/file-extension checks), `exceptions.py` (`AppError` base + 6 typed exceptions with `status_code`/`code` matching `docs/06_API_Contracts.md`'s error shape exactly), `helpers.py` (`success_response`/`error_response` builders + `chunk_list`), `file_utils.py` (safe filenames, extension extraction, human-readable size), `time_utils.py` (UTC timestamps, duration formatting), `__init__.py` (re-exports). All imports and function outputs smoke-tested directly (`is_valid_email`, `format_file_size`, `utc_now_iso` all confirmed working). Frontend `src/utils/` — `constants.ts`, `validators.ts`, `formatters.ts`, `helpers.ts`, `api.ts` (uses `axios.isAxiosError` type guard, no `any` per coding standards), `index.ts` (barrel export). Verified via `npm run lint` (clean) and full `npm run build` (`tsc -b && vite build` succeeded). Backend confirmed still starts cleanly after the new package was added to the import chain.
- Task008 – Project Verification: complete. Full cross-cutting verification of Phase01 (Tasks001-007) performed. See Verification Report below. One real gap found and fixed: `backend/app/__init__.py` was missing since Task003 — uvicorn tolerated it, but mypy could not, failing with "Source file found twice under different module names" (`utils.exceptions` vs `app.utils.exceptions`). Added the missing `__init__.py`; mypy now passes cleanly (11 source files, no issues).
- Task009 – Phase 01 Completion Review: complete. All checklists in `tasks/Phase01_Foundation/Task009_Phase01_Completion.md` checked off; Lessons Learned, Technical Debt, and Risks Before Phase 02 sections filled in with genuine observations from this phase (documentation reconciliation required before Task001, stale tooling instructions in Task005/Task009, the react-router CSRF advisory investigation, and the app/__init__.py gap caught in Task008). Formal sign-off checklist completed. **Phase 01 – Foundation is officially closed.**

## Phase 02 — Backend Infrastructure

- Task001 – Database Setup: complete. Installed SQLAlchemy 2.0.51, psycopg 3.3.4 (psycopg3, `postgresql+psycopg://` driver string — not psycopg2), Alembic 1.19.0 (install only, no migrations yet), pydantic-settings 2.14.2 (installed per task spec; actual `BaseSettings` migration deferred to Task005 per that task's explicit dependency chain — flagged and confirmed before implementation). Created local PostgreSQL 18.4 database `codesense_ai` via `createdb`. Created `app/db/` package: `database.py` (single reusable `Engine`, `pool_pre_ping=True`), `session.py` (`SessionLocal` sessionmaker + `get_db()` generator dependency with guaranteed session close), `base.py` (empty `DeclarativeBase` — no models per scope), `__init__.py` (re-exports). `app/core/config.py` already had `DATABASE_URL` wired from Task006 (Phase01) — no changes needed there. Verified with a live query (`SELECT version()` round-tripped successfully against the real database, not just an import check), full `db` package import test, `black`/`ruff`/`mypy` all clean, and `uvicorn app.main:app --reload` starts without errors. Noted for Task002: Task001 deliberately kept the engine/session config minimal (FR-2/FR-3/FR-4 satisfied at a basic level) since Task002 owns the hardened version (connection pooling, full session lifecycle) — avoided duplicate/conflicting work.
- Task002 – SQLAlchemy Configuration: complete. Hardened the `app/db/database.py` engine from Task001 with configurable connection pooling — added `DB_POOL_SIZE` (default 5), `DB_MAX_OVERFLOW` (default 10), `DB_POOL_RECYCLE_SECONDS` (default 1800, avoids cloud-provider idle-connection drops), and `DB_ECHO` (default False, SQL statement logging for local debugging only) to `app/core/config.py` and `.env.example`. Wired structured logging via the existing `app/utils/logger.py` `get_logger()` utility — logs engine creation (`environment=` only) and connection success/failure, never the URL or password (masked as `***` in engine repr by SQLAlchemy itself). Added a fail-fast live connection check (`SELECT 1`) at import time so the app errors loudly on startup if Postgres is unreachable, rather than starting silently broken. Created `app/models/__init__.py` (empty package, no models per scope — models arrive in Task004). `session.py` and `base.py` needed no changes — Task001's versions already satisfied FR-002/FR-003. Verified: live connection + logging confirmed via `python -c "import app.main; from app.db import engine"` (both log lines fired), `black`/`ruff`/`mypy` clean across all touched files, `uvicorn app.main:app --reload` starts/stops cleanly, Swagger UI loads at `/docs` (`CodeSense AI 0.1.0`, OAS 3.1, existing `/health` endpoint from Phase01 visible). Noted limitation: the engine/connection log lines don't yet fire during a real `uvicorn` boot because `app/main.py` doesn't import `app.db` anywhere — that wiring is explicitly Task006 (Dependency Injection)'s responsibility; verification was done via direct import instead to stay within Task002's scope boundary.

---

# Task008 Verification Report

| Category | Status | Notes |
|----------|--------|-------|
| Repository | ✅ Pass | All docs/tasks/root files confirmed present via direct GitHub check |
| Backend | ✅ Pass | venv active, all deps installed, uvicorn starts clean, Swagger + ReDoc both render |
| Frontend | ✅ Pass | Vite dev server starts clean, ESLint clean, full `tsc -b && vite build` succeeds |
| Environment | ✅ Pass | `.env` confirmed git-ignored (backend + frontend), `.env.example` tracked, no secrets in `git status` |
| Tooling | ✅ Pass | ruff/black/isort/mypy all pass (after `app/__init__.py` fix); npm lint/build both pass |
| Git | ✅ Pass | Working tree clean pre-fix; commits from Task002 onward follow Conventional Commits. Pre-Task001 commits ("Add files via upload" etc.) predate formal convention — noted, not fixed, since rewriting history isn't warranted |
| Documentation | ✅ Pass | All required docs/ and tasks/ files present |
| Utilities | ✅ Pass | All Task007 utilities import and execute correctly (re-verified this session) |

---

# 🏁 Phase 01 – Foundation: Complete

9/9 tasks completed. 0 blocking issues. Ready for Phase 02 – Backend Infrastructure.

---

# Current Task

None — Task002 (SQLAlchemy Configuration) just completed.

---

# Next Task

Phase 02 Task003 – Alembic Migrations (`tasks/Phase02_Backend_Infrastructure/Task003_Alembic_Migrations.md`). Not started; awaiting explicit instruction to proceed.

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
