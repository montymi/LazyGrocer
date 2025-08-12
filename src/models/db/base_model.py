"""Base model class with common fields."""
from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BaseModel(Base):
    """Abstract base model with common fields."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    is_shared = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)

    def to_dict(self, exclude=None, include_relationships=False):
        """Convert model to dictionary."""
        exclude = exclude or []
        result = {}

        for column in self.__table__.columns:
            if column.name not in exclude:
                value = getattr(self, column.name)
                if isinstance(value, datetime):
                    value = value.isoformat()
                result[column.name] = value

        if include_relationships:
            for relationship in self.__mapper__.relationships:
                if relationship.key not in exclude:
                    related = getattr(self, relationship.key)
                    if related:
                        if hasattr(related, '__iter__'):
                            result[relationship.key] = [
                                item.to_dict() if hasattr(item, 'to_dict') else str(item)
                                for item in related
                            ]
                        else:
                            result[relationship.key] = (
                                related.to_dict() if hasattr(related, 'to_dict') else str(related)
                            )

        return result

    def update(self, **kwargs):
        """Update model fields."""
        for key, value in kwargs.items():
            if hasattr(self, key) and key not in ['id', 'created_at', 'updated_at']:
                setattr(self, key, value)
        return self

    def soft_delete(self):
        """Soft delete the record."""
        self.is_deleted = True
        self.updated_at = datetime.utcnow()
        return self

    def restore(self):
        """Restore soft deleted record."""
        self.is_deleted = False
        self.updated_at = datetime.utcnow()
        return self

    @classmethod
    def query_active(cls, session):
        """Query only active (non-deleted) records."""
        return session.query(cls).filter(cls.is_deleted == False)

    def __repr__(self):
        """String representation."""
        return f"<{self.__class__.__name__}(id={self.id})>"