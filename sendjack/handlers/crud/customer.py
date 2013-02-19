"""
    customer
    --------

    Handle all CRUD interactions for a customer.

"""
from model.object.customer import Customer

from base import CRUDHandler


class CustomerCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = Customer
