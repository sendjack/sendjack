"""

    customers
    ---------

    Define the customers table.

"""
from sqlalchemy import Column, Integer, String, DateTime

from jutil.decorators import constant

from sqlalchemy_db import BaseObject
from crud import CRUD


class _Customers(object):

    @constant
    def TABLE_NAME(self):
        return "customers"

CUSTOMERS = _Customers()


class Customers(BaseObject, CRUD):

    __tablename__ = CUSTOMERS.TABLE_NAME

    # TODO: maybe but probably not since it could make the ORM confusing:
    # - abstract fields common to all db-backed objects into ORM subclass
    # - abstract fields common to task template/instance into superclass

    id = Column(Integer, primary_key=True)

    # TODO: will it cause problems for timestamps to be null?
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    deleted_ts = Column(DateTime)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    stripe_token = Column(String, nullable=False)

    # TODO: define an Enum with various statuses.
    status = Column(String, nullable=False)

    # TODO: figure out foreign keys.
