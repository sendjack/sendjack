"""

    customer
    ---------

    Define the customer model's table schema.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Enum

from jutil.decorators import constant

from base import BaseModel
from crud import CRUD


class _Customer(object):

    @constant
    def TABLE_NAME(self):
        return "customer"

    @constant
    def ACCOUNT_STATUS(self):
        return "account_status"

    @constant
    def INVITED(self):
        return "invited"

    @constant
    def REQUESTED(self):
        return "requested"

    @constant
    def REGISTERED(self):
        return "registered"

    @constant
    def UNVERIFIED(self):
        return "unverified"

    @constant
    def VERIFIED(self):
        return "verified"

    @constant
    def CLOSED(self):
        return "closed"

CUSTOMER = _Customer()


class CustomerModel(BaseModel, CRUD):

    __tablename__ = CUSTOMER.TABLE_NAME

    id = Column(Integer, primary_key=True)

    # TODO: figure out foreign keys.

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False)
    stripe_token = Column(String)

    status = Column(
            Enum(
                CUSTOMER.INVITED,
                CUSTOMER.REQUESTED,
                CUSTOMER.REGISTERED,
                CUSTOMER.UNVERIFIED,
                CUSTOMER.VERIFIED,
                CUSTOMER.CLOSED,
                name=CUSTOMER.ACCOUNT_STATUS),
            nullable=False)
