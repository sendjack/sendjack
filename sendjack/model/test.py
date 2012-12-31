"""
    test api object
    ---------------

    Test how to work with SQLAlchemy

"""
from sqlalchemy import Column, Integer, String
from data.sqlalchemy_db import Base

from base import APIBase

TEST_TABLE = unicode("acre")


class Test(Base, APIBase):

    __tablename__ = TEST_TABLE

    id = Column(Integer, primary_key=True)
    stop = Column(String)


    def __repr__(self):
        return "<Test_User('{}', '{}')>".format(self.id, self.stop)
