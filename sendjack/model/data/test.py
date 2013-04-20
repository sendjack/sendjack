"""
    test
    ----

    Define a test table on a SQLAlchemy database.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean, Enum

from base import BaseModel
from crud import CRUD
from types import SerializableStringList, SerializableDict
from types import OutputList, TagList

class TestModel(BaseModel, CRUD):

    __tablename__ = unicode("crud_test")

    test_id = Column(Integer, primary_key=True)
    test_int = Column(Integer)
    test_str = Column(String)
    test_bool = Column(Boolean)
    test_enum = Column(
            Enum(
                unicode("enum1"),
                unicode("enum2"),
                unicode("enum3"),
                name="test_enums"),
            default=unicode("default"))
    test_list = Column(SerializableStringList)
    test_dict = Column(SerializableDict)
    test_output = Column(OutputList)
    test_tags = Column(TagList)


    def __repr__(self):
        return "<Test_User('{}','{}','{}','{}','{}','{}','{}','{}','{}')>".format(
                self.test_id,
                self.test_int,
                self.test_str,
                self.test_bool,
                self.test_enum,
                self.test_list,
                self.test_dict,
                self.test_output,
                self.test_tags)
