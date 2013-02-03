"""

    db
    --

    Load the SendJack database.

"""
from sqlalchemy_db import SQLAlchemy

from test import Test
from customers import Customers
from task_templates import TaskTemplates
from task_instances import TaskInstances


class _DatabaseSingleton(object):

    _objects = [
            Test,
            Customers,
            TaskTemplates,
            TaskInstances,
            ]


    def __init__(self):
        self._db = SQLAlchemy(self._objects)


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
