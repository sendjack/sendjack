"""

    customers
    ---------

    Define the customers table.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from jutil.decorators import constant

from base import BaseObject
from crud import CRUD


class _Customers(object):

    @constant
    def TABLE_NAME(self):
        return "customers"

CUSTOMERS = _Customers()


class Customers(BaseObject, CRUD):

    __tablename__ = CUSTOMERS.TABLE_NAME

    id = Column(Integer, primary_key=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    stripe_token = Column(String, nullable=False)

    # TODO: define an Enum with various statuses.
    status = Column(String, nullable=False)

    # TODO: figure out foreign keys.
