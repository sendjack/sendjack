"""
    task_template
    -------------

    Handle all synchronous requests for a task template.

"""
from view.app.main.body import TaskTemplateBody

from .base import SyncHandler


class TaskTemplateSyncHandler(SyncHandler):

    """Initialize the markup for a request for a new Task Template form."""

    def _set_markup_class(self):
        self._markup_class = TaskTemplateBody
