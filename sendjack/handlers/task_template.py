"""
    task_template
    -------------

    Handle all asynchronous CRUD interactions and synchronous requests for a
    task template.

"""
from model.object.task_template import TaskTemplate

from view.app.main.body import TaskTemplateBody

from base import BaseHandler
from crud import CRUDHandler


class TaskTemplateCRUDHandler(CRUDHandler):

    """Initialize the model for a TaskTemplate CRUD request."""

    def _init_model(self):
        self._model_object = TaskTemplate()


class TaskTemplateSyncHandler(BaseHandler):

    """Initialize the markup for a request for a new Task Template form."""

    def _render_body_markup(self, model=None):
        return TaskTemplateBody()
