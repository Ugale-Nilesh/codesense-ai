"""Time and date helper functions. All timestamps are UTC."""

from datetime import UTC, datetime


def utc_now() -> datetime:
    """Return the current UTC datetime."""
    return datetime.now(UTC)


def utc_now_iso() -> str:
    """Return the current UTC datetime as an ISO 8601 string."""
    return utc_now().isoformat()


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object using the given strftime pattern."""
    return dt.strftime(fmt)


def seconds_to_human(seconds: float) -> str:
    """Convert a duration in seconds into a short human-readable string."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes, secs = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m {int(secs)}s"
    hours, mins = divmod(minutes, 60)
    return f"{int(hours)}h {int(mins)}m"
