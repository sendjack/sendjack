"""

    db
    --

    Load the SendJack database.

"""
from database import SQLAlchemy

from test import TestModel
from customer import CustomerModel
from task_template import TaskTemplateModel
from task_instance import TaskInstanceModel


class _DatabaseSingleton(object):

    _db = None


    def __init__(self):
        self._db = SQLAlchemy([
                TestModel,
                CustomerModel,
                TaskTemplateModel,
                TaskInstanceModel,
                ])


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
