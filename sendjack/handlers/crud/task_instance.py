"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions for a task instance.

"""
from model.object.task_instance import TaskInstance

from .base import CRUDHandler


# TODO: should we create a factory to churn out subclasses of
# TaskInstanceCRUDHandler, or is this giant if/elif block sufficient?

class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance
