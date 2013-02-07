"""
    test
    ----

    Define a test table on a SQLAlchemy database.

"""
from sqlalchemy import Column, Integer, String

from base import BaseObject
from crud import CRUD


class Test(BaseObject, CRUD):

    __tablename__ = unicode("acre")

    id = Column(Integer, primary_key=True)
    stop = Column(String)


    def __repr__(self):
        return "<Test_User('{}', '{}')>".format(self.id, self.stop)
