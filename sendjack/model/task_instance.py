"""

    task_instance
    -------------

    Define a CRUD interface for a TaskInstance.

"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from data.sqlalchemy_db import Base

from util.decorators import constant

from base import APIBase


class _TaskInstance(object):

    @constant
    def TABLE_NAME(self):
        return "task_instances"

TASK_INSTANCE = _TaskInstance()


class TaskInstance(Base, APIBase):

    __tablename__ = TASK_INSTANCE.TABLE_NAME

    # TODO: maybe but probably not since it could make the ORM confusing:
    # - abstract fields common to all db-backed objects into ORM subclass
    # - abstract fields common to task template/instance into superclass

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # TODO: will it cause problems for timestamps to be null?
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    deleted_ts = Column(DateTime)

    deadline_ts = Column(DateTime)
    is_urgent = Column(Boolean, nullable=False)

    # TODO: figure out foreign keys.
    customer_id = Column(Integer, nullable=False)
    worker_id = Column(Integer)

    # in US cents per hour
    price = Column(Integer)

    # TODO: it's not clear where this will come from.
    # in seconds
    overhead = Column(Integer)

    # TODO: eventually this should be nullable=False but it will be a while
    # before we are equipped to populate that data from the workflow.
    # in emails back and forth
    interactions = Column(Integer)

    # TODO: figure out what this means. eventually this should be
    # nullable=False but it will be a while before it is available.
    # in some as yet undefined unit of measure
    score = Column(Integer)

    # approximate or specific address and radius in miles
    location = Column(Integer)
    location_radius = Column(String)

    # TODO: define some default tags.
    output_method = Column(String, nullable=False)

    # list of free-form text
    edited_steps = Column(String)

    # dict whose keys are tags and values are annotations on the template
    annotated_custom_properties = Column(String)


    @property
    def deadline(self):
        # TODO: convert DateTime to string.
        pass

    @property
    def price_str(self):
        # TODO: convert to float.
        return "${}".format(self.price / 100)

    @property
    def overhead_str(self):
        return "{} hours".format(self.overhead / 3600)

    @property
    def interactions_str(self):
        return "{} messages".format(self.interactions)

    @property
    def score_str(self):
        return "{} rating".format(self.score)

    @property
    def location_range_str(self):
        return "within {} miles of {}".format(
                self.location_radius,
                self.location)
