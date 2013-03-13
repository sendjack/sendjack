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
    def NEW(self):
        """Task is new, but a row exists, probably from a search query."""
        return "new"

    @constant
    def CREATED(self):
        """Task has been submitted to us but not processed yet."""
        return "created"

    @constant
    def PROCESSED(self):
        """Task has been processed by us but not yet created for posting."""
        return "processed"

    @constant
    def CONFIRMED(self):
        """Task has been confirmed but not yet posted to a vendor."""
        return "confirmed"

    @constant
    def POSTED(self):
        """Task has been posted to a vendor."""
        return "posted"

    @constant
    def ASSIGNED(self):
        """Task has been given to a specific worker."""
        return "assigned"

    @constant
    def COMPLETED(self):
        """Work on the task is complete."""
        return "completed"

    @constant
    def APPROVED(self):
        """Task has been approved by the customer."""
        return "approved"

    @constant
    def EXPIRED(self):
        """Task's deadline has passed without being in a completed state."""
        return "expired"

    @constant
    def CANCELED(self):
        """Customer has canceled the task before being completed."""
        return "canceled"


TASK_INSTANCE = _TaskInstance()


class TaskInstanceModel(TaskModel, CRUD):

    """

        customer_title       -> title
        customer_description -> summary
        title                -> TRTitle
        summary              -> TRDescription
        instructions         -> description
        properties           -> description
        output_type          -> description
        output_method        -> description
        description          -> TRPrivateDescription
        more_details         -> TRPrivateDescription

    """
    __tablename__ = TASK_INSTANCE.TABLE_NAME

    # TODO: figure out foreign keys.
    template_id = Column(Integer)
    customer_id = Column(Integer)
    worker_id = Column(Integer)

    customer_title = Column(String)
    customer_description = Column(String)

    description = Column(String)
    more_details = Column(String)

    status = Column(
            Enum(
                TASK_INSTANCE.NEW,
                TASK_INSTANCE.CREATED,
                TASK_INSTANCE.PROCESSED,
                TASK_INSTANCE.CONFIRMED,
                TASK_INSTANCE.POSTED,
                TASK_INSTANCE.ASSIGNED,
                TASK_INSTANCE.COMPLETED,
                TASK_INSTANCE.APPROVED,
                TASK_INSTANCE.EXPIRED,
                TASK_INSTANCE.CANCELED,
                name=TASK_INSTANCE.TASK_STATUS),
            default=TASK_INSTANCE.NEW)

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
