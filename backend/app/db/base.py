"""Declarative base for all ORM models.

Application models (Task004 onward) will inherit from this Base.
No models are defined in this module.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    pass
