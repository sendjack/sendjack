"""

    task
    ----

    Provide an abstract superclass with some common functionality for all
    database-backed objects.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from base import BaseModel
from types import SerializableStringList, SerializableDict
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
    output_method = Column(SerializableStringList)
    output_type = Column(SerializableStringList)

    # list of free-form text
    steps = Column(SerializableStringList)

    # dict whose keys are tags and values are annotations on the template
    custom_properties = Column(SerializableDict)

    # TODO: define some default tags for each.
    # lists whose split values can be substitutions in steps
    category_tags = Column(SerializableStringList)
    industry_tags = Column(SerializableStringList)
    skill_tags = Column(SerializableStringList)
    equipment_tags = Column(SerializableStringList)
