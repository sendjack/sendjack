"""
    instance events
    ---------------

    Listen to all Task Instance events.

"""
from redflag import redflag

import settings
from model.data.task_instance import TASK_INSTANCE
from model.object.task_instance import TaskInstance
from model.object.task_template import TaskTemplate
from model.object.customer import Customer
from view.emails.instance_status.completed import CompletedInstanceMessage
from view.emails.instance_status.processed import (
        ControlProcessedInstanceMessage,
        TestProcessedInstanceMessage)
from view.emails.instance_status.posted import PostedInstanceMessage

from .base import EventFactory, AttributeChangeEvent


class InstanceEventFactory(EventFactory):

    def __init__(self, manager):
        super(InstanceEventFactory, self).__init__(manager)

        # TaskInstance.status change event
        event = AttributeChangeEvent(
                TaskInstance.status,
                self.on_status_change)
        self._event_manager.add_attribute_change_handler(event)

        # TaskInstance.template_id change event
        event = AttributeChangeEvent(
                TaskInstance.template_id,
                self.on_template_id_change)
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


    def on_template_id_change(self, object_, value, old_value):
        pass
        # TODO: get the diff and check that instead of self._model.

        # TODO: write copy() into model.data.crud or
        # model.data.task_instance. if this isn't the right call, then
        # at least programmatically get the common columns to construct
        # the fields dict below.

        #if self._model.price:
        #    # TODO: add a second button to be more clear about this.
        #    self._change_state("processed")
        task_template = TaskTemplate.read(value)

        fields = {
                "title": task_template.title,
                "instructions": task_template.instructions,
                "properties": task_template.properties,
                "output_type": task_template.output_type,
                "output_method": task_template.output_method,
                "category_tags": task_template.category_tags,
                "industry_tags": task_template.industry_tags,
                "skill_tags": task_template.skill_tags,
                "equipment_tags": task_template.equipment_tags,
                }

        TaskInstance.update(object_.id, fields)


    def _on_new_status(self, instance):
        pass


    def _on_created_status(self, instance):
        # send notification email to us
        # TODO: Pull subject and body_test from a StatusMesage
        redflag.send_email_to_notification_account(
                unicode("Task Created"),
                instance.title,
                instance.summary)


    def _on_processed_status(self, instance):
        domain = settings.EMBEDDABLE_DOMAIN
        customer = Customer.read(instance.customer_id)

        # TODO: create a factory or static wrapper that chooses test or control
        # based on the parameters passed to instantiate it (ex: customer).
        if customer.control_group:
            status_message = ControlProcessedInstanceMessage(
                    domain,
                    customer,
                    instance)
        else:
            status_message = TestProcessedInstanceMessage(
                    domain,
                    customer,
                    instance)

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
