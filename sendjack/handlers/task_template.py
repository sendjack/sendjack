"""
    task_template
    -------------

    Handle all asynchronous CRUD interactions and synchronous requests for a
    task template.

"""
from model.object.task_template import TaskTemplate
from view.app.main.body import TaskTemplateBody

from .crud import CRUDHandler
from .sync import SyncHandler


class TaskTemplateCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskTemplate


class TaskTemplateSyncHandler(SyncHandler):

    """Initialize the markup for a request for a new Task Template form."""

    def _render_body_markup(self, model=None):
        return TaskTemplateBody()
