"""Database model package.

Provides the shared BaseModel that all future application models
will inherit from. Application-specific models arrive in Task005
onward.
"""

from app.models.base_model import BaseModel

__all__ = ["BaseModel"]
