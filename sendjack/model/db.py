"""

    db
    --

    Load the SendJack database.

"""
from data.sqlalchemy_db import SQLAlchemy

from test import Test
from task_template import TaskTemplate
from task_instance import TaskInstance


class _DatabaseSingleton(object):

    api_objects = [
            Test,
            TaskTemplate,
            TaskInstance,
            ]


    def __init__(self):
        self._db = SQLAlchemy(self.api_objects)


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
