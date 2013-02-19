"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions and synchronous requests for a
    task instance.

"""
import requests

from model.object.task_instance import TaskInstance
from view.app.main.body import TaskInstancePostBody

from .crud import CRUDHandler
from .sync import SyncHandler


class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance


    def _function_that_is_not_called(task_instance):
            # check for created
            path = unicode("/sendjack/task/{}").format(task_instance.id)
            url = unicode("{}{}").format("http://localhost:5100", path)
            requests.get(url).json


class TaskInstanceSyncHandler(SyncHandler):

    """Initialize the markup for a request for a new Task Instance form."""

    def _render_body_markup(self, model=None):
        return TaskInstancePostBody()
