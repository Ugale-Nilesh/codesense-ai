# 15. Stop Conditions

## Purpose

This section defines situations where implementation must pause until additional guidance is available.

A professional engineer does not guess when uncertainty could compromise correctness, security, architecture, or product quality.

When a stop condition is reached, pause implementation, explain the reason, and request clarification.

---

# Core Principle

Continue autonomously whenever the documented information is sufficient.

Pause immediately when continuing would require making significant assumptions.

Never fabricate requirements or invent architecture.

---

# Mandatory Stop Conditions

Stop implementation if any of the following conditions are encountered.

## 1. Conflicting Requirements

Pause when:

- Documentation contradicts another document.
- User instructions conflict with the roadmap.
- Existing implementation conflicts with approved architecture.

Explain the conflict and identify the affected sources.

---

## 2. Architectural Changes

Stop before:

- Changing the system architecture.
- Replacing major frameworks or libraries.
- Reorganizing top-level folders.
- Introducing new architectural patterns.

These decisions require explicit approval.

---

## 3. Missing Product Requirements

Stop when:

- User behaviour is undefined.
- Business rules are incomplete.
- Acceptance criteria are missing.
- Multiple valid implementations produce materially different outcomes.

Do not guess product behaviour.

---

## 4. Security-Sensitive Operations

Pause before:

- Handling credentials.
- Managing secrets.
- Modifying authentication.
- Changing authorization logic.
- Altering security configuration.

Request confirmation when appropriate.

---

## 5. Destructive Actions

Never perform destructive operations without approval.

Examples:

- Deleting files
- Removing modules
- Dropping databases
- Breaking backward compatibility
- Large-scale refactoring

Explain the impact before proceeding.

---

## 6. External Dependencies

Stop when implementation requires:

- API keys
- Cloud credentials
- Paid services
- Third-party accounts
- Access unavailable in the repository

Request the required information rather than inventing placeholders.

---

## 7. Significant Technical Risk

Pause if implementation introduces:

- High migration risk
- Data loss risk
- Performance uncertainty
- Major compatibility concerns

Present available options and trade-offs.

---

# Clarification Format

When a stop condition is reached, respond using:

## Reason

Explain why implementation paused.

## Information Required

State exactly what information or approval is needed.

## Possible Options

List available approaches if multiple solutions exist.

## Recommendation

Recommend the safest engineering path.

---

# Continue Conditions

Resume implementation immediately once:

- Required information is available.
- Conflicts are resolved.
- Approval has been granted.

Do not repeat completed work unnecessarily.

---

# Final Principle

Good engineers know when to continue.

Great engineers know when to stop.

Prioritize correctness, safety, and architectural integrity over speed.
