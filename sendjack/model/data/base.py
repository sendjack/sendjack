"""

    base
    ----

    Provide an abstract superclass with some common functionality for all
    database-backed objects.

"""
from datetime import datetime
from sqlalchemy import Column

from database import DeclarativeModel
from types import SerializableDateTime


class BaseModel(DeclarativeModel):

    __abstract__ = True

    _utcnow = datetime.utcnow()

    created_ts = Column(
            SerializableDateTime,
            nullable=False,
            default=_utcnow)
    updated_ts = Column(
            SerializableDateTime,
            nullable=False,
            default=_utcnow)
    deleted_ts = Column(SerializableDateTime)


    def to_dict(self):
        """Return this as a dict keyed on table columns."""
        # TODO: does this work with foreign keys?

        # http://stackoverflow.com/questions/5022066
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
