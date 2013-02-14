"""

    task_instances
    --------------

    Define the task instance model's table schema.

"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean, Enum

from jutil.decorators import constant

from types import SerializableDateTime
from task import TaskModel
from crud import CRUD


class _TaskInstance(object):

    @constant
    def TABLE_NAME(self):
        return "task_instance"

    @constant
    def TASK_STATUS(self):
        return "task_status"

    @constant
    def SAVED(self):
        return "saved"

    @constant
    def CREATED(self):
        return "created"

    @constant
    def POSTED(self):
        return "posted"

    @constant
    def ASSIGNED(self):
        return "assigned"

    @constant
    def COMPLETED(self):
        return "completed"

    @constant
    def APPROVED(self):
        return "approved"

TASK_INSTANCE = _TaskInstance()


class TaskInstanceModel(TaskModel, CRUD):

    __tablename__ = TASK_INSTANCE.TABLE_NAME

    # TODO: figure out foreign keys.
    customer_id = Column(Integer, nullable=False)
    worker_id = Column(Integer)
    template_id = Column(Integer)

    customer_title = Column(String)
    customer_description = Column(String)

    status = Column(
            Enum(
                TASK_INSTANCE.SAVED,
                TASK_INSTANCE.CREATED,
                TASK_INSTANCE.POSTED,
                TASK_INSTANCE.ASSIGNED,
                TASK_INSTANCE.COMPLETED,
                TASK_INSTANCE.APPROVED,
                name=TASK_INSTANCE.TASK_STATUS),
            default=TASK_INSTANCE.SAVED)

    deadline_ts = Column(SerializableDateTime)
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
