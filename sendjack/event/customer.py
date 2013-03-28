"""
    customer events
    ---------------

    Listen to all Customer events.

"""
from redflag import redflag

import settings
from model.data.customer import CUSTOMER
from model.object.customer import Customer
from view.emails.customer_status.created import CreatedCustomerMessage

from .base import EventFactory, AttributeChangeEvent


class CustomerEventFactory(EventFactory):

    def __init__(self, manager):
        super(CustomerEventFactory, self).__init__(manager)

        event = AttributeChangeEvent(Customer.status, self.on_status_change)
        self._event_manager.add_attribute_change_handler(event)


    def on_status_change(self, object_, value, old_value):
        status_change_handlers = {
                CUSTOMER.INVITED: self._on_invited_status,
                CUSTOMER.REQUESTED: self._on_requested_status,
                CUSTOMER.REGISTERED: self._on_registered_status,
                CUSTOMER.UNVERIFIED: self._on_unverified_status,
                CUSTOMER.VERIFIED: self._on_verified_status,
                CUSTOMER.CLOSED: self._on_closed_status,
                }

        handler = status_change_handlers.get(value)
        if handler:
            handler(object_)


    def _on_invited_status(self, customer):
        pass


    def _on_requested_status(self, customer):
        pass


    def _on_registered_status(self, customer):
        domain = settings.EMBEDDABLE_DOMAIN
        status_message = CreatedCustomerMessage(domain, customer)
        redflag.send_email_to_customer(
                customer,
                status_message.subject,
                status_message.body_text)


    def _on_unverified_status(self, customer):
        pass


    def _on_verified_status(self, customer):
        pass


    def _on_closed_status(self, customer):
        pass
