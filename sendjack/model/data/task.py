"""

    task
    ----

    Provide an abstract superclass with some common functionality for all
    database-backed objects.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import HSTORE, ARRAY

from base import BaseModel
from types import SerializableDateTime


class TaskModel(BaseModel):

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # approximate or specific address and radius in miles
    location = Column(Integer)
    location_radius = Column(String)

    # TODO: all of the below save "steps" should be assembled outside this
    # class in concurrent queries and wrapped up in a composite class in the
    # model's object package.

    # TODO: define some default tags.
    output_method = Column(MutableDict.as_mutable(HSTORE))
    output_type = Column(MutableDict.as_mutable(HSTORE))

    # list of free-form text
    steps = Column(ARRAY(String))

    # dict whose keys are tags and values are annotations on the template
    custom_properties = Column(MutableDict.as_mutable(HSTORE))

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in steps
    category_tags = Column(MutableDict.as_mutable(HSTORE))
    industry_tags = Column(MutableDict.as_mutable(HSTORE))
    skill_tags = Column(MutableDict.as_mutable(HSTORE))
    equipment_tags = Column(MutableDict.as_mutable(HSTORE))
