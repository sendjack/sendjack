"""

    db
    --

    Load the SendJack database.

"""
from test import Test
from data.sqlalchemy_db import SQLAlchemy


class _DatabaseSingleton(object):

    api_objects = [Test]


    def __init__(self):
        self._db = SQLAlchemy(self.api_objects)


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
