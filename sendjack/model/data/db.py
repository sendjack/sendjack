"""

    db
    --

    Load the SendJack database.

"""
from sqlalchemy_db import SQLAlchemy

from test import TestTable
from customers import CustomersTable
from task_templates import TaskTemplatesTable
from task_instances import TaskInstancesTable


class _DatabaseSingleton(object):

    table_objects = [
            TestTable,
            CustomersTable,
            TaskTemplatesTable,
            TaskInstancesTable,
            ]


    def __init__(self):
        self._db = SQLAlchemy(self.table_objects)


    @property
    def db(self):
        return self._db


db = _DatabaseSingleton().db
