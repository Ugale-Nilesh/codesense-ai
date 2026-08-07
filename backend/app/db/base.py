"""Declarative base for all ORM models.

Application models (Task004 onward) will inherit from this Base.
No models are defined in this module.
"""

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Standard Alembic-recommended naming convention. Ensures every index,
# unique constraint, check constraint, foreign key, and primary key gets
# a deterministic, predictable name -- without this, autogenerate produces
# unstable auto-named constraints that cause noisy diffs across environments.
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    metadata = MetaData(naming_convention=NAMING_CONVENTION)
