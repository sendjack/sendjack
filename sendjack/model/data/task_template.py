"""

    task_template
    --------------

    Define the task template model's table schema.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer

from jutil.decorators import constant

from task import TaskModel
from crud import CRUD


class _TaskTemplate(object):

    @constant
    def TABLE_NAME(self):
        return "task_template"

TASK_TEMPLATE = _TaskTemplate()


class TaskTemplateModel(TaskModel, CRUD):

    __tablename__ = TASK_TEMPLATE.TABLE_NAME

    # TODO: figure out editor_ids (many-to-many relationship).
    # TODO: figure out foreign key.
    # TODO: make this nullable=False when we have accounts.
    creator_id = Column(Integer)

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
