"""

    task_template
    -------------

    Define the TaskTemplate table and its CRUD interface.

"""
from sqlalchemy import Column, Integer, String, DateTime
from data.sqlalchemy_db import Base

from util.decorators import constant

from base import APIBase


class _TaskTemplate(object):

    @constant
    def TABLE_NAME(self):
        return "task_templates"

TASK_TEMPLATE = _TaskTemplate()


class TaskTemplate(Base, APIBase):

    __tablename__ = TASK_TEMPLATE.TABLE_NAME

    # TODO: maybe but probably not since it could make the ORM confusing:
    # - abstract fields common to all db-backed objects into ORM subclass
    # - abstract fields common to task template/instance into superclass

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # TODO: figure out editor_ids (many-to-many relationship).
    # TODO: figure out foreign key.
    creator_id = Column(Integer, nullable=False)

    # TODO: will it cause problems for timestamps to be null?
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    deleted_ts = Column(DateTime)

    # in US cents per hour
    min_price = Column(Integer, nullable=False)
    max_price = Column(Integer, nullable=False)

    # in seconds
    min_overhead = Column(Integer)
    max_overhead = Column(Integer)

    # TODO: eventually this should be nullable=False but it will be a while
    # before we are equipped to populate that data from the workflow.
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
    output_type = Column(String, nullable=False)
    output_method = Column(String, nullable=False)

    # list of free-form text
    steps = Column(String, nullable=False)

    # dict whose keys are tags and can be substitutions in steps
    custom_properties = Column(String)

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in steps
    category_tags = Column(String)
    industry_tags = Column(String)
    skill_tags = Column(String)
    equipment_tags = Column(String)


    @property
    def price_range(self):
        return (self.min_price, self.max_price)

    @property
    def price_range_str(self):
        return "${} to ${} per hour".format(
                self.min_price / 100,
                self.max_price / 100)

    @property
    def overhead_range(self):
        return (self.min_overhead, self.max_overhead)

    @property
    def overhead_range_str(self):
        return "{} to {} hours".format(
                self.min_overhead / 3600,
                self.max_overhead / 3600)

    @property
    def interactions_range(self):
        return (self.min_interactions, self.max_interactions)

    @property
    def interactions_range_str(self):
        return "{} to {} messages".format(
                self.min_interactions,
                self.max_interactions)

    @property
    def score_range(self):
        return (self.min_score, self.max_score)

    @property
    def score_range_str(self):
        return "{} to {} rating".format(self.min_score, self.max_score)

    @property
    def location_range_str(self):
        return "within {} miles of {}".format(
                self.location_radius,
                self.location)

    @property
    def output_str(self):
        return "{} via {}".format(self.output_type, self.output_method)

    def has_custom_property(self, tag):
        return tag in self.custom_properties

    def custom_property(self, tag):
        return self.custom_properties[tag]

    @property
    def category_str(self):
        return ", ".join(self.category_tags)

    @property
    def industry_str(self):
        return ", ".join(self.industry_tags)

    @property
    def skill_str(self):
        return ", ".join(self.skill_tags)

    @property
    def equipment_str(self):
        return ", ".join(self.equipment_tags)
