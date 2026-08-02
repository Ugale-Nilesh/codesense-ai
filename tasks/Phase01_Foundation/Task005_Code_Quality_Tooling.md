# Task005 – Configure Code Quality Tooling

## Task Information

| Field | Value |
|-------|-------|
| Phase | Phase 01 – Foundation |
| Task ID | Task005 |
| Priority | Critical |
| Estimated Time | 90–120 minutes |
| Status | Planned |

---

# Objective

Configure a standardized code quality environment for the CodeSense AI project to ensure consistency, maintainability, and reliability across the backend and frontend codebases.

This task establishes automated formatting, linting, static analysis, and Git hooks that every future contribution must follow.

---

# Business Context

CodeSense AI will be developed incrementally with assistance from multiple AI coding tools and potentially multiple developers.

Without a unified code quality standard, the repository will quickly become inconsistent, making future maintenance difficult.

The goal of this task is to ensure that every code contribution follows the same formatting, linting, and quality rules before it reaches the repository.

---

# Technical Context

The project consists of two independent codebases:

- Backend (Python + FastAPI)
- Frontend (React + TypeScript)

Each requires dedicated tooling while maintaining a consistent development experience.

---

# Prerequisites

Completed Tasks

- ✅ Task001 – Initialize Repository Structure
- ✅ Task002 – Setup Development Environment
- ✅ Task003 – Backend Project Setup
- ✅ Task004 – Frontend Project Setup

Reference Documents

- docs/03_Technology_Stack.md
- docs/08_Project_Rules.md
- docs/09_Coding_Standards.md

---

# Dependencies

Future Tasks Depending on This

- Backend Infrastructure
- Frontend Development
- Authentication
- AI Engine
- Database Layer
- Testing
- CI/CD

---

# Scope

## In Scope

### Backend

- Ruff
- Black
- isort
- mypy

### Frontend

- ESLint
- Prettier
- TypeScript linting

### Repository

- Git Hooks
- Pre-commit
- VS Code workspace configuration

---

## Out of Scope

- Unit testing
- CI/CD
- GitHub Actions
- Docker
- Deployment

---

# Target Repository Changes

```text
codesense-ai/

backend/
│
├── pyproject.toml
├── .pre-commit-config.yaml
│
frontend/
│
├── .eslintrc.cjs
├── .prettierrc
├── .prettierignore
│
.vscode/
│
├── settings.json
└── extensions.json
```

---

# Packages

## Backend

Install

```bash
pip install black
pip install ruff
pip install isort
pip install mypy
pip install pre-commit
```

---

Update requirements

```bash
pip freeze > requirements.txt
```

---

## Frontend

Install

```bash
npm install -D eslint
npm install -D prettier
npm install -D eslint-config-prettier
npm install -D eslint-plugin-react-hooks
npm install -D eslint-plugin-react-refresh
```

---

# Files To Create

Backend

```
backend/pyproject.toml
```

```
backend/.pre-commit-config.yaml
```

---

Frontend

```
frontend/.eslintrc.cjs
```

```
frontend/.prettierrc
```

```
frontend/.prettierignore
```

---

Workspace

```
.vscode/settings.json
```

```
.vscode/extensions.json
```

---

# Configuration Requirements

Backend formatter

- Black

Line length

```
88
```

Python version

```
3.12+
```

Import sorting

```
isort
```

Static analysis

```
mypy
```

Linting

```
Ruff
```

---

Frontend formatter

```
Prettier
```

Indentation

```
2 spaces
```

Quotes

```
Single quotes
```

Semicolons

```
Always
```

Trailing commas

```
ES5
```

---

# VS Code Configuration

Workspace should automatically

- format on save
- organize imports
- fix lint errors
- trim whitespace
- insert final newline

---

Recommended Extensions

- Python
- Pylance
- Ruff
- Black Formatter
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- GitLens

---

# Git Hooks

Configure pre-commit to execute

Backend

- Ruff
- Black
- isort

Frontend

- ESLint

The commit should fail if formatting or linting checks do not pass.

---

# Implementation Steps

## Step 1

Install backend quality tools.

---

## Step 2

Configure Python formatting.

---

## Step 3

Configure Ruff.

---

## Step 4

Configure mypy.

---

## Step 5

Install frontend tooling.

---

## Step 6

Configure ESLint.

---

## Step 7

Configure Prettier.

---

## Step 8

Configure VS Code workspace.

---

## Step 9

Configure pre-commit hooks.

---

## Step 10

Run all tools to verify configuration.

---

# Verification Commands

Backend

```bash
black .
```

```bash
ruff check .
```

```bash
isort .
```

```bash
mypy app
```

---

Frontend

```bash
npm run lint
```

```bash
npm run format
```

---

Git

```bash
pre-commit run --all-files
```

---

# Expected Output

Backend

- No formatting errors
- No lint errors
- No import errors

Frontend

- No ESLint errors
- No formatting errors

Git

- Hooks execute successfully

---

# Deliverables

Backend

- Black configured
- Ruff configured
- isort configured
- mypy configured

Frontend

- ESLint configured
- Prettier configured

Workspace

- VS Code settings
- Recommended extensions

Repository

- Pre-commit hooks

---

# Acceptance Criteria

- Backend formatting works.
- Frontend formatting works.
- ESLint passes.
- Ruff passes.
- mypy passes.
- Imports are sorted.
- Git hooks execute successfully.
- VS Code formats automatically.

---

# Manual Testing Checklist

- [ ] Python formatter works
- [ ] Ruff works
- [ ] isort works
- [ ] mypy works
- [ ] ESLint works
- [ ] Prettier works
- [ ] Git hooks run
- [ ] VS Code formats automatically

---

# Troubleshooting

## Python packages not found

- Verify virtual environment is active.
- Reinstall dependencies.

---

## ESLint not detected

- Reinstall node_modules.
- Restart VS Code.

---

## Git hooks not executing

Run

```bash
pre-commit install
```

---

## Formatter conflicts

Ensure only one formatter is configured as the default formatter for each language.

---

# Rollback

If configuration becomes unstable

1. Remove newly added configuration files.
2. Reinstall dependencies.
3. Restore previous commit.
4. Reconfigure tools one at a time.

---

# Definition of Done

This task is complete when:

- Backend formatting is fully automated.
- Frontend formatting is fully automated.
- Static analysis executes successfully.
- Linting executes successfully.
- Git hooks prevent invalid commits.
- VS Code automatically formats code.
- Every future code contribution follows the same standards.

---

# Suggested Commit Message

```text
chore(tooling): configure code quality tooling
```

---

# Next Task

Task006 – Environment Configuration
