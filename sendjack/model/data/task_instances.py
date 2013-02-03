"""

    task_instances
    --------------

    Define the task_instances table.

"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from jutil.decorators import constant

from sqlalchemy_db import BaseObject
from crud import CRUD


class _TaskInstances(object):

    @constant
    def TABLE_NAME(self):
        return "task_instances"

TASK_INSTANCES = _TaskInstances()


class TaskInstances(BaseObject, CRUD):

    __tablename__ = TASK_INSTANCES.TABLE_NAME

    # TODO: maybe but probably not since it could make the ORM confusing:
    # - abstract fields common to all db-backed objects into ORM subclass
    # - abstract fields common to task template/instance into superclass

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # TODO: will it cause problems for timestamps to be null?
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    deleted_ts = Column(DateTime)

    # TODO: figure out foreign keys.
    customer_id = Column(Integer, nullable=False)
    worker_id = Column(Integer)
    template_id = Column(Integer)

    customer_title = Column(String)
    customer_description = Column(String)

    deadline_ts = Column(DateTime)
    is_urgent = Column(Boolean)

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
    output_method = Column(String)
    output_type = Column(String)

    # list of free-form text
    steps = Column(String)

    # dict whose keys are tags and values are annotations on the template
    custom_properties = Column(String)

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in steps
    category_tags = Column(String)
    industry_tags = Column(String)
    skill_tags = Column(String)
    equipment_tags = Column(String)
