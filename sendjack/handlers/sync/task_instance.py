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

            if task_instance.is_new():
                self._transition_to_new()

            elif task_instance.is_created():
                self._transition_to_created()

            elif task_instance.is_processed():
                self._transition_to_processed()

            elif task_instance.is_confirmed():
                self._transition_to_confirmed()

            elif task_instance.is_posted():
                self._transition_to_posted()

            elif task_instance.is_assigned():
                self._transition_to_assigned()

            elif task_instance.is_completed():
                self._transition_to_completed()

            elif task_instance.is_approved():
                self._transition_to_approved()

            elif task_instance.is_expired():
                self._transition_to_expired()

            elif task_instance.is_canceled():
                self._transition_to_canceled()


    def _transition_to_new(self):
        pass


    def _transition_to_created(self):
        pass


    def _transition_to_processed(self):
        pass


    def _transition_to_confirmed(self):
        pass


    def _transition_to_posted(self):
        pass


    def _transition_to_assigned(self):
        pass


    def _transition_to_completed(self):
        # if the task's status is complete then show the approval page.
        self._markup_class = TaskInstanceApproveBody


    def _transition_to_approved(self):
        pass


    def _transition_to_expired(self):
        pass


    def _transition_to_canceled(self):
        pass
