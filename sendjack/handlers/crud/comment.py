"""
    comment
    -------

    Handle all async CRUD interactions for comments.

"""
from redflag import redflag

import settings
from model.object.task_instance import TaskInstance
from model.object.customer import Customer

from .base import CRUDHandler


class CommentCRUDHandler(CRUDHandler):

    # TODO: These should be in the model.data.comment.py.
    MESSAGE = unicode("message")
    IS_FROM_CUSTOMER = unicode("is_from_customer")
    TASK_ID = unicode("task_id")
    JACK_SERVICE = unicode("jack")

    def _set_model_class(self):
        pass

    def post(self, id=None):
        object_dict = self._get_request_body()
        task_id = object_dict.get(self.TASK_ID)
        message = object_dict.get(self.MESSAGE)
        is_from_customer = object_dict.get(self.IS_FROM_CUSTOMER)

        if is_from_customer:
            email = unicode("{}-{}-{}@{}").format(
                    "sendjack",
                    task_id,
                    "comment",
                    settings.MAILGUN_DOMAIN)

            redflag.send_email_from_jack(
                    email,
                    "SUBJECT",
                    message)

        else:
            task_instance = TaskInstance.read(task_id)
            customer = Customer.read(task_instance.customer_id)

            full_name = customer.full_name
            email = customer.email

            recipient = unicode("{} <{}>").format(
                    full_name,
                    email)

            redflag.send_comment_on_task(
                    self.JACK_SERVICE,
                    task_id,
                    recipient,
                    message)

    def get(self, id=None):
        pass


    def put(self, id):
        pass


    def delete(self, id):
        pass
