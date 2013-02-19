"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions for a task instance.

"""
import requests

from model.object.task_instance import TaskInstance

from .base import CRUDHandler


class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance


    def _function_that_is_not_called(task_instance):
            # check for created
            path = unicode("/sendjack/task/{}").format(task_instance.id)
            url = unicode("{}{}").format("http://localhost:5100", path)
            requests.get(url).json
