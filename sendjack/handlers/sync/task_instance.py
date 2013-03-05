"""
    task_instance
    -------------

    Handle synchronous requests for Task Instance Confirmation Series.

"""
from model.object.task_instance import TaskInstance
from view.app.main.body import TaskInstancePostBody, TaskInstanceApproveBody

from .base import SyncHandler


class TaskInstanceSyncHandler(SyncHandler):

    """Initialize the markup for a request for a new Task Instance form."""

    def _set_markup_class(self):
        self._markup_class = TaskInstancePostBody


    def _pre_process_request(self):
        """Do any class specific pre processing."""
        if self._id is not None:
            task_instance = TaskInstance.read(self._id)

            # if the task's status is complete then show the approval page.
            if task_instance.is_completed():
                self._markup_class = TaskInstanceApproveBody
