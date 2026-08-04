"""File-related helper functions. No I/O side effects beyond directory creation."""

import os
import re
import uuid


def generate_safe_filename(original_filename: str) -> str:
    """Return a collision-safe filename: a UUID prefix + sanitized original name."""
    name, ext = os.path.splitext(original_filename)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    return f"{uuid.uuid4().hex}_{safe_name}{ext.lower()}"


def get_file_extension(filename: str) -> str:
    """Return the lowercase file extension, including the leading dot."""
    return os.path.splitext(filename)[1].lower()


def format_file_size(size_bytes: int) -> str:
    """Convert a byte count into a human-readable string (e.g. '4.2 MB')."""
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")

    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def ensure_directory(path: str) -> None:
    """Create the directory (and parents) if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)
