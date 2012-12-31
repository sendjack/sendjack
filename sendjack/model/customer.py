"""

    customer
    --------

    Define the Customer table and its CRUD interface.

"""
from sqlalchemy import Column, Integer, String, DateTime
from data.sqlalchemy_db import Base

from util.decorators import constant

from base import APIBase


class _Customer(object):

    @constant
    def TABLE_NAME(self):
        return "customer"

CUSTOMER = _Customer()


class Customer(Base, APIBase):

    __tablename__ = CUSTOMER.TABLE_NAME

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

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def short_name(self):
        return "{} {}".format(self.first_name, self.last_name[0])
