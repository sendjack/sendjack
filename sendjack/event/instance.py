"""
    instance events
    ---------------

    Listen to all Task Instance events.

"""
from redflag import redflag

import settings
from model.data.task_instance import TASK_INSTANCE
from model.object.task_instance import TaskInstance
from model.object.customer import Customer
from view.emails.instance_status.completed import CompletedInstanceMessage
from view.emails.instance_status.processed import ProcessedInstanceMessage
from view.emails.instance_status.posted import PostedInstanceMessage

from .base import EventFactory, AttributeChangeEvent


class InstanceEventFactory(EventFactory):

    def __init__(self, manager):
        super(InstanceEventFactory, self).__init__(manager)

        event = AttributeChangeEvent(
                TaskInstance.status,
                self.on_status_change)
        self._event_manager.add_attribute_change_handler(event)


    def on_status_change(self, object_, value, old_value):
        status_change_handlers = {
                TASK_INSTANCE.NEW: self._on_new_status,
                TASK_INSTANCE.CREATED: self._on_created_status,
                TASK_INSTANCE.PROCESSED: self._on_processed_status,
                TASK_INSTANCE.CONFIRMED: self._on_confirmed_status,
                TASK_INSTANCE.POSTED: self._on_posted_status,
                TASK_INSTANCE.ASSIGNED: self._on_assigned_status,
                TASK_INSTANCE.COMPLETED: self._on_completed_status,
                TASK_INSTANCE.APPROVED: self._on_approved_status,
                TASK_INSTANCE.EXPIRED: self._on_expired_status,
                TASK_INSTANCE.CANCELED: self._on_canceled_status,
                }

        handler = status_change_handlers.get(value)
        if handler:
            handler(object_)


    def _on_new_status(self, instance):
        pass


    def _on_created_status(self, instance):
        pass


    def _on_processed_status(self, instance):
        domain = settings.EMBEDDABLE_DOMAIN
        customer = Customer.read(instance.customer_id)
        status_message = ProcessedInstanceMessage(domain, customer, instance)
        redflag.send_email_to_customer(
                customer,
                status_message.subject,
                status_message.body_text)


    def _on_confirmed_status(self, instance):
        # trigger an email to our jackalope service to attempt to post the task
        # to a vendor. do not message the user.
        redflag.send_internal_email_from_service(
                "sendjack",
                instance.id,
                "POST THIS TASK",
                "neither the messsage nor subject make a difference")


    def _on_posted_status(self, instance):
        domain = settings.EMBEDDABLE_DOMAIN
        customer = Customer.read(instance.customer_id)
        status_message = PostedInstanceMessage(domain, customer, instance)
        redflag.send_email_to_customer(
                customer,
                status_message.subject,
                status_message.body_text)


    def _on_assigned_status(self, instance):
        pass


    def _on_completed_status(self, instance):
        domain = settings.EMBEDDABLE_DOMAIN
        customer = Customer.read(instance.customer_id)
        status_message = CompletedInstanceMessage(domain, customer, instance)
        redflag.send_email_to_customer(
                customer,
                status_message.subject,
                status_message.body_text)


    def _on_approved_status(self, instance):
        # TODO: email the customer with a canned response a la "Re:
        # <YourApprovedTask>" or "Re: <YourTacitlyApprovedTask>" and make it
        # clear how and why the work was approved.

        # trigger an email to our jackalope service to let the vendor know that
        # the task was approved.
        redflag.send_internal_email_from_service(
                "sendjack",
                instance.id,
                "THIS TASK WAS APPROVED",
                "neither the messsage nor subject make a difference")


    def _on_expired_status(self, instance):
        pass


    def _on_canceled_status(self, instance):
        pass
