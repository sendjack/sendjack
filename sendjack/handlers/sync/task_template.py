"""
    task_template
    -------------

    Handle all synchronous requests for a task template.

"""
from view.app.alt_theme.body import TaskTemplateBody

from .base import SyncHandler


class TaskTemplateSyncHandler(SyncHandler):

    """Handle create template."""

    def _set_markup_class(self):
        self._markup_class = TaskTemplateBody
