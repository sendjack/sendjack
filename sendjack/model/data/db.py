"""

    db
    --

    Load the SendJack database.

"""
from database import SQLAlchemy

from test import Test
from customers import Customers
from task_templates import TaskTemplates
from task_instances import TaskInstances


class _DatabaseSingleton(object):

    _db = None


    def __init__(self):
        self._db = SQLAlchemy([
                Test,
                Customers,
                TaskTemplates,
                TaskInstances,
                ])


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
