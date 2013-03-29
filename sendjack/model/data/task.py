"""

    task
    ----

    Provide an abstract superclass with some common functionality for all
    database-backed objects.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from base import BaseModel
from types import SerializableStringList, SerializableDictList, OutputList
from types import TagList


class TaskModel(BaseModel):

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # approximate or specific address and radius in miles
    location = Column(Integer)
    location_radius = Column(String)

    # string broadly describing a task, which may include substitutions from
    # properties key/value pairs
    summary = Column(String)

    # ordered list of free-form text strings describing work, which often
    # includes substitutions from properties key/value pairs
    instructions = Column(SerializableStringList)

    # TODO: most of the below (not "instructions") should be assembled outside
    # this class in concurrent queries and wrapped up in a composite class in
    # the model's object package.

    # TODO: if/when these actually become lists, remove OutputList and use
    # SerializableStringList again instead.
    # TODO: define some default tags.
    output_method = Column(OutputList)
    output_type = Column(OutputList)

    # ordered list of dicts whose keys are tags and values are task annotations
    properties = Column(SerializableDictList)

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in instructions
    category_tags = Column(TagList)
    industry_tags = Column(TagList)
    skill_tags = Column(TagList)
    equipment_tags = Column(TagList)
