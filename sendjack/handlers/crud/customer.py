"""
    customer
    --------

    Handle all CRUD interactions for a customer.

"""
from model.object.customer import Customer
from model.data.customer import CUSTOMER
from view.emails.customer_status.created import CreatedCustomerMessage

from base import CRUDHandler


class CustomerCRUDHandler(CRUDHandler):

    def initialize(self):
        super(CustomerCRUDHandler, self).initialize()

        self._status_triggers = {
                CUSTOMER.INVITED: self._trigger_invited_action,
                CUSTOMER.REQUESTED: self._trigger_requested_action,
                CUSTOMER.REGISTERED: self._trigger_registered_action,
                CUSTOMER.UNVERIFIED: self._trigger_unverified_action,
                CUSTOMER.VERIFIED: self._trigger_verified_action,
                CUSTOMER.CLOSED: self._trigger_closed_action,
                }


    def _set_model_class(self):
        self._model_class = Customer


    def _post_process_request(self):
        # the client already advanced the task status for the current request

        if self._is_create_request() or self._is_update_request():
            trigger_function = self._status_triggers.get(self._model.status)
            trigger_function()


    def _trigger_invited_action(self):
        pass


    def _trigger_requested_action(self):
        pass


    def _trigger_registered_action(self):
        if self._is_create_request():
            domain = self.request.body
            status_message = CreatedCustomerMessage(domain, self._model)
            self._trigger_customer_email(self._model, status_message)


    def _trigger_unverified_action(self):
        pass


    def _trigger_verified_action(self):
        pass


    def _trigger_closed_action(self):
        pass
