"""

    db
    --

    Load the SendJack database.

"""
import database

from test import TestModel
from customer import CustomerModel
from task_template import TaskTemplateModel
from task_instance import TaskInstanceModel


class _DatabaseSingleton(object):

    _db = None

    def __init__(self):
        self._db = database.SQLAlchemy([
                TestModel,
                CustomerModel,
                TaskTemplateModel,
                TaskInstanceModel,
                ])

        database.set_db(self._db)


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
