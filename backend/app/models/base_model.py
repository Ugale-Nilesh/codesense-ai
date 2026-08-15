"""Shared abstract base model for all persistent entities.

Provides the common fields every application model needs: a UUID
primary key and auto-managed created/updated timestamps. This module
defines no business logic, no relationships, and no application
entities -- it is strictly a persistence abstraction that future
models (Task005 onward) will inherit from.
"""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class BaseModel(Base):
    """Abstract base providing shared columns for all entities.

    Every application model SHALL inherit from this class instead of
    `Base` directly, so identifier and timestamp handling stays
    consistent across the entire persistence layer.
    """

    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
