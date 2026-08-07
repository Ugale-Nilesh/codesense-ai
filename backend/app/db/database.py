"""SQLAlchemy engine configuration.

Creates the single, reusable SQLAlchemy Engine instance for the
application. Connection pool sizing is configurable via environment
variables so the same code path works across Development, Testing,
and Production without modification.
"""

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)

if not settings.DATABASE_URL:
    logger.error("DATABASE_URL is not configured.")
    raise RuntimeError(
        "DATABASE_URL is not set. Configure it in your .env file before "
        "starting the application."
    )

engine: Engine = create_engine(
    settings.DATABASE_URL,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_recycle=settings.DB_POOL_RECYCLE_SECONDS,
    pool_pre_ping=True,
    echo=settings.DB_ECHO,
    future=True,
)

logger.info("SQLAlchemy engine created for environment=%s", settings.ENVIRONMENT)

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    logger.info("Database connection verified successfully.")
except SQLAlchemyError:
    logger.exception("Database connection failed during engine initialization.")
    raise
