"""Reusable, framework-agnostic input validators.

Each validator is a pure function returning True/False. None of these
raise exceptions or perform I/O - callers decide how to handle a failed
validation (e.g. by raising a ValidationError from exceptions.py).
"""

import re
import uuid

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{3,30}$")


def is_valid_email(value: str) -> bool:
    """Return True if value looks like a valid email address."""
    return bool(_EMAIL_PATTERN.match(value.strip()))


def is_valid_username(value: str) -> bool:
    """Return True if value is 3-30 chars of letters, digits, - or _."""
    return bool(_USERNAME_PATTERN.match(value.strip()))


def is_valid_uuid(value: str) -> bool:
    """Return True if value is a syntactically valid UUID."""
    try:
        uuid.UUID(str(value))
        return True
    except (ValueError, AttributeError, TypeError):
        return False


def is_valid_file_extension(filename: str, allowed: set[str]) -> bool:
    """Return True if filename's extension is present in the allowed set."""
    if "." not in filename:
        return False
    ext = "." + filename.rsplit(".", 1)[-1].lower()
    return ext in allowed
