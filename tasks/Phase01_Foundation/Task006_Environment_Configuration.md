# Task006 – Environment Configuration

## Task Information

| Field | Value |
|-------|-------|
| Phase | Phase 01 – Foundation |
| Task ID | Task006 |
| Priority | Critical |
| Estimated Time | 60–90 minutes |
| Status | Planned |

---

# Objective

Establish a secure, scalable, and maintainable environment configuration system for CodeSense AI.

The objective of this task is to separate application configuration from source code by using environment variables, ensuring that sensitive information and deployment-specific settings are never hardcoded.

This configuration system will be shared across the backend, frontend, local development, testing, and future production deployments.

---

# Business Context

Modern software applications rely on configurable environments to support multiple deployment targets without changing application code.

CodeSense AI will eventually support:

- Local Development
- Testing
- Staging
- Production

Each environment should be configurable through environment variables.

---

# Technical Context

Environment variables will control:

Backend

- Application metadata
- Debug mode
- API configuration
- Database configuration
- Authentication secrets
- AI provider credentials
- GitHub integration
- Logging configuration

Frontend

- API base URL
- Application name
- Environment mode
- Feature flags

Sensitive information must never be committed to Git.

---

# Prerequisites

Completed Tasks

- ✅ Task001 – Initialize Repository Structure
- ✅ Task002 – Setup Development Environment
- ✅ Task003 – Backend Project Setup
- ✅ Task004 – Frontend Project Setup
- ✅ Task005 – Configure Code Quality Tooling

Reference Documents

- docs/02_System_Architecture.md
- docs/03_Technology_Stack.md
- docs/04_Folder_Structure.md
- docs/08_Project_Rules.md

---

# Dependencies

Future tasks depending on this configuration:

- Authentication
- Database Integration
- AI Services
- GitHub Integration
- File Processing
- Deployment
- CI/CD

---

# Scope

## In Scope

Backend

- Environment loading
- Application settings
- Secret management
- Configuration validation

Frontend

- Public environment variables
- API configuration
- Feature flags

Repository

- Example configuration files
- Ignore sensitive files

---

## Out of Scope

- Production secrets
- Cloud secret managers
- Docker secrets
- Kubernetes configuration

---

# Folder Changes

```text
backend/
│
├── .env.example
├── .env
└── app/
    └── core/
        └── config.py

frontend/
│
├── .env.example
└── .env

.gitignore
```

---

# Files To Create

Backend

```
backend/.env.example
```

```
backend/app/core/config.py
```

Frontend

```
frontend/.env.example
```

Repository

```
.gitignore
```

---

# Files To Modify

```
backend/.gitignore
```

```
frontend/.gitignore
```

---

# Backend Environment Variables

Application

```text
APP_NAME=CodeSense AI
APP_VERSION=0.1.0
ENVIRONMENT=development
DEBUG=True
HOST=127.0.0.1
PORT=8000
```

Database

```text
DATABASE_URL=
```

Security

```text
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

AI Providers

```text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
```

GitHub

```text
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=
```

Logging

```text
LOG_LEVEL=INFO
```

---

# Frontend Environment Variables

```text
VITE_APP_NAME=CodeSense AI
VITE_API_BASE_URL=http://localhost:8000
VITE_ENVIRONMENT=development
VITE_ENABLE_ANALYTICS=false
```

---

# Configuration Requirements

Backend

- Load variables using python-dotenv.
- Validate required values.
- Provide default values where appropriate.
- Centralize configuration in a single module.

Frontend

- Use Vite environment variables.
- Access values through `import.meta.env`.
- Never expose secrets to the frontend.

---

# Security Requirements

The following files must never be committed:

```
backend/.env
frontend/.env
```

Only `.env.example` files should exist in the repository.

No API keys or secrets should be stored in source code.

---

# Implementation Steps

## Step 1

Create backend `.env.example`.

---

## Step 2

Create frontend `.env.example`.

---

## Step 3

Create backend configuration module.

```
backend/app/core/config.py
```

---

## Step 4

Configure environment loading.

---

## Step 5

Update `.gitignore` files.

---

## Step 6

Verify environment variables load correctly.

---

## Step 7

Confirm backend starts with configuration.

---

## Step 8

Confirm frontend reads environment variables.

---

# Verification Commands

Backend

```bash
uvicorn app.main:app --reload
```

Frontend

```bash
npm run dev
```

Git

```bash
git status
```

Ensure `.env` files do not appear in staged changes.

---

# Expected Output

Backend

- Environment variables load successfully.
- Application starts without configuration errors.

Frontend

- Environment variables accessible through Vite.
- API URL configured correctly.

Repository

- Sensitive files ignored by Git.

---

# Deliverables

Backend

- Configuration module
- Environment template

Frontend

- Environment template

Repository

- Updated ignore rules

---

# Acceptance Criteria

- Backend reads environment variables successfully.
- Frontend reads environment variables successfully.
- Secrets are not tracked by Git.
- Configuration is centralized.
- No hardcoded credentials exist.

---

# Manual Testing Checklist

- [ ] Backend starts successfully
- [ ] Frontend starts successfully
- [ ] `.env` ignored by Git
- [ ] `.env.example` committed
- [ ] Configuration values load correctly

---

# Troubleshooting

## Variables not loading

- Verify `.env` exists.
- Confirm python-dotenv is installed.
- Restart the application.

---

## Frontend variable undefined

- Ensure the variable begins with `VITE_`.
- Restart the Vite development server.

---

## Secret committed accidentally

Immediately:

1. Remove the secret.
2. Rotate the credential.
3. Rewrite Git history if necessary.
4. Commit the corrected configuration.

---

# Rollback

If configuration fails:

1. Restore the previous commit.
2. Recreate `.env.example`.
3. Verify ignore rules.
4. Reconfigure environment loading.

---

# Definition of Done

This task is complete when:

- Backend configuration is centralized.
- Frontend configuration is centralized.
- Secrets are protected.
- Environment variables load correctly.
- Development can continue without hardcoded configuration values.

---

# Suggested Commit Message

```text
chore(config): configure project environment management
```

---

# Next Task

Task007 – Shared Utilities
