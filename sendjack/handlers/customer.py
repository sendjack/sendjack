"""
    customer
    --------

    Handle all asynchronous CRUD interactions for a customer.

"""
from model.object.customer import Customer

from crud import CRUDHandler


class CustomerCRUDHandler(CRUDHandler):

    """Initialize the model for a Customer CRUD request."""

    def _init_model(self):
        self._model_object = Customer()
