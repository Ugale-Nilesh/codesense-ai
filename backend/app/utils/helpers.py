"""General-purpose helper functions: API response builders and small
reusable utilities with no feature-specific logic.
"""

from typing import Any


def success_response(data: Any = None, message: str = "Success") -> dict:
    """Build a consistent success payload."""
    return {"success": True, "message": message, "data": data}


def error_response(
    status: int, code: str, message: str, details: list | None = None
) -> dict:
    """Build an error payload matching docs/06_API_Contracts.md's Error Format."""
    return {
        "status": status,
        "code": code,
        "message": message,
        "details": details or [],
    }


def chunk_list(items: list, size: int) -> list[list]:
    """Split a list into chunks of at most size items each."""
    if size <= 0:
        raise ValueError("size must be a positive integer")
    return [items[i : i + size] for i in range(0, len(items), size)]
