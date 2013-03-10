"""
    task_instance
    -------------

    Handle synchronous requests for all task_instance focused series.

"""
#from model.object.task_instance import TaskInstance
from view.app.main.body import ConfirmInstanceBody, ApproveInstanceBody
from view.app.alpha_signup.body import CreateInstanceBody

from .base import SyncHandler


class CreateInstanceSyncHandler(SyncHandler):

    """Handle create instance series.

    Note: search --> tasks/create --> users/create --> tasks/create/thanks

    """

    def _set_markup_class(self):
        self._markup_class = CreateInstanceBody


class ConfirmInstanceSyncHandler(SyncHandler):

    """Handle confirm instance series.

    Note: tasks/ID/confirm --> users/ID/card --> tasks/ID/confirm/thanks

    """

    def _set_markup_class(self):
        self._markup_class = ConfirmInstanceBody

    def _pre_process_request(self):
        """Do any class specific pre processing."""
        # check to make sure the task has an ID and is in the correct state.
        pass


class ApproveInstanceSyncHandler(SyncHandler):

    """Handle confirm instance series.

    Note: tasks/ID/approve --> tasks/ID/approve/thanks

    """

    def _set_markup_class(self):
        self._markup_class = ApproveInstanceBody

    def _pre_process_request(self):
        """Do any class specific pre processing."""
        # check to make sure the task has an ID and is in the correct state.
        #if self._id is not None:
        #    task_instance = TaskInstance.read(self._id)

        #    # if the task's status is complete then show the approval page.
        #    if task_instance.is_completed():
        #        self._markup_class = TaskInstanceApproveBody
        pass

#       if self._id is not None:
#           task_instance = TaskInstance.read(self._id)
#
#           if task_instance.is_new():
#               self._transition_to_new()
#
#           elif task_instance.is_created():
#               self._transition_to_created()
#
#           elif task_instance.is_processed():
#               self._transition_to_processed()
#
#           elif task_instance.is_confirmed():
#               self._transition_to_confirmed()
#
#           elif task_instance.is_posted():
#               self._transition_to_posted()
#
#           elif task_instance.is_assigned():
#               self._transition_to_assigned()
#
#           elif task_instance.is_completed():
#               self._transition_to_completed()
#
#           elif task_instance.is_approved():
#               self._transition_to_approved()
#
#           elif task_instance.is_expired():
#               self._transition_to_expired()
#
#           elif task_instance.is_canceled():
#               self._transition_to_canceled()
#
#
#   def _transition_to_new(self):
#       pass
#
#
#   def _transition_to_created(self):
#       pass
#
#
#   def _transition_to_processed(self):
#       pass
#
#
#   def _transition_to_confirmed(self):
#       pass
#
#
#   def _transition_to_posted(self):
#       pass
#
#
#   def _transition_to_assigned(self):
#       pass
#
#
#   def _transition_to_completed(self):
#       pass
#
#
#   def _transition_to_approved(self):
#       pass
#
#
#   def _transition_to_expired(self):
#       pass
#
#
#   def _transition_to_canceled(self):
#       pass
