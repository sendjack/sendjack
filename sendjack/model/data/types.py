"""
    type
    ----

    Provide extremely basic subclasses for externally defined database types.

    For example, ensure that DateTime can be generically encoded to JSON
    outside the data package by massaging the query result value.

"""
from sqlalchemy.types import TypeDecorator, DateTime, String
from sqlalchemy.dialects.postgresql import HSTORE, ARRAY
from sqlalchemy.ext.mutable import MutableDict


class SerializableDateTime(TypeDecorator):

    impl = DateTime

    def process_result_value(self, value, dialect):
        # account for nullable deleted_ts by simply returning None
        return value.isoformat() if value is not None else value


class SerializableStringList(TypeDecorator):

    impl = ARRAY(String)

    def process_bind_param(self, value, dialect):
        #return [s.strip() for s in value.split(',')]
        return value

    def process_result_value(self, value, dialect):
        #return str.join(value)
        return value


class SerializableDict(TypeDecorator):

    impl = MutableDict.as_mutable(HSTORE)

    def process_bind_param(self, value, dialect):
        #return {s.strip(): s.strip() for s in value.split(',')}
        return value


    def process_result_value(self, value, dialect):
        #return str.join(value.keys())
        return value


# TODO: if/when output_method and output_type actually become lists, remove
# this class and use SerializableStringList again instead.
class OutputList(TypeDecorator):

    impl = SerializableStringList

    def process_bind_param(self, value, dialect):
        # WIP: while lots of fields are still nullable, expect bad data.
        return [value] if value else value


    def process_result_value(self, value, dialect):
        # WIP: while lots of fields are still nullable, expect bad data.
        return value[0] if value else value
