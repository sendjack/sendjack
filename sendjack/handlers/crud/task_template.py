"""
    task_template
    -------------

    Handle all asynchronous CRUD interactions a task template.

"""
from model.object.task_template import TaskTemplate

from .base import CRUDHandler


class TaskTemplateCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskTemplate
