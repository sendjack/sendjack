"""

    task_templates
    --------------

    Define the task_templates table.

"""
from sqlalchemy import Column, Integer, String, DateTime

from jutil.decorators import constant

from sqlalchemy_db import BaseObject
from crud import CRUD


class _TaskTemplates(object):

    @constant
    def TABLE_NAME(self):
        return "task_templates"

TASK_TEMPLATES = _TaskTemplates()


class TaskTemplates(BaseObject, CRUD):

    __tablename__ = TASK_TEMPLATES.TABLE_NAME

    # TODO: maybe but probably not since it could make the ORM confusing:
    # - abstract fields common to all db-backed objects into ORM subclass
    # - abstract fields common to task template/instance into superclass

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # TODO: will it cause problems for timestamps to be null?
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    deleted_ts = Column(DateTime)

    # TODO: figure out editor_ids (many-to-many relationship).
    # TODO: figure out foreign key.
    creator_id = Column(Integer, nullable=False)

    # TODO: in the future this might not be stored as a range or at all. for
    # now, we don't know how to split a template and rebalance its instances.
    # in US cents per hour
    min_price = Column(Integer)
    max_price = Column(Integer)

    # TODO: in the future this might not be stored as a range or at all. for
    # now, we don't know how to split a template and rebalance its instances.
    # in seconds
    min_overhead = Column(Integer)
    max_overhead = Column(Integer)

    # TODO: in the future this might not be stored as a range or at all. for
    # now, we don't know how to split a template and rebalance its instances.
    # in emails back and forth
    min_interactions = Column(Integer)
    max_interactions = Column(Integer)

    # TODO: figure out what this means. eventually this should be
    # nullable=False but it will be a while before it is available.
    # in some as yet undefined unit of measure
    min_score = Column(Integer)
    max_score = Column(Integer)

    # approximate or specific address and radius in miles
    location = Column(Integer)
    location_radius = Column(String)

    # TODO: define some default tags for each.
    output_type = Column(String)
    output_method = Column(String)

    # list of free-form text
    steps = Column(String)

    # dict whose keys are tags and can be substitutions in steps
    custom_properties = Column(String)

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in steps
    category_tags = Column(String)
    industry_tags = Column(String)
    skill_tags = Column(String)
    equipment_tags = Column(String)
