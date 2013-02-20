"""
    task_instance
    -------------

    Handle synchronous requests for Task Instance Confirmation Series.

"""
from view.app.main.body import TaskInstancePostBody

from .base import SyncHandler


class TaskInstanceSyncHandler(SyncHandler):

    """Initialize the markup for a request for a new Task Instance form."""

    def _set_markup_class(self):
        self._markup_class = TaskInstancePostBody
