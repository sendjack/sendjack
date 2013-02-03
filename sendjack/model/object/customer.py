"""

    customer
    --------

    Define the Customer object.

"""
from model.data.customers import Customers


class Customer(Customers):

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def short_name(self):
        return "{} {}".format(self.first_name, self.last_name[0])
