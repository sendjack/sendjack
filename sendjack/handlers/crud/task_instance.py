"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions for a task instance.

"""
from redflag import redflag

import settings
from model.object.task_instance import TaskInstance

from .base import CRUDHandler


class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance


    def _post_process_request(self):
        if self._model.is_created() and not self._is_read():
            email = unicode("{}-{}@{}").format(
                    "sendjack",
                    self._model.id,
                    settings.MAILGUN_DOMAIN)

            redflag.send_email_from_jack(
                    email,
                    "POST THIS TASK",
                    "neither the messsage nor subject make a difference")
