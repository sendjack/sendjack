"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions and synchronous requests for a
    task instance.

"""
from model.object.task_instance import TaskInstance

from view.app.main.body import TaskInstancePostBody

from base import BaseHandler
from crud import CRUDHandler


class TaskInstanceCRUDHandler(CRUDHandler):

    """Initialize the model for a TaskInstance CRUD request."""

    def _init_model(self):
        self._model_object = TaskInstance()


class TaskInstanceSyncHandler(BaseHandler):

    """Initialize the markup for a request for a new Task Instance form."""

    def _render_body_markup(self, model=None):
        return TaskInstancePostBody()
