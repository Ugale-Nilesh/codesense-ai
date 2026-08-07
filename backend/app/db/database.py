"""SQLAlchemy engine configuration.

Creates a single, reusable SQLAlchemy Engine instance bound to the
configured DATABASE_URL. No other module should construct an Engine.
"""

from sqlalchemy import Engine, create_engine

from app.core.config import settings

if not settings.DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. Configure it in your .env file before "
        "starting the application."
    )

engine: Engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)
