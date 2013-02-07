"""
    type
    ----

    Provide extremely basic subclasses for externally defined database types.

    For example, ensure that DateTime can be generically encoded to JSON
    outside the data package by massaging the query result value.

"""
from sqlalchemy.types import TypeDecorator, DateTime


class SerializableDateTime(TypeDecorator):

    impl = DateTime


    def process_result_value(self, value, dialect):
        # account for nullable deleted_ts by simply returning None
        return value.isoformat() if value is not None else value
