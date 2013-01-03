"""

    customer
    --------

    Define the Customer API object.

"""
from model.data.customers import CustomersTable


class Customer(CustomersTable):

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def short_name(self):
        return "{} {}".format(self.first_name, self.last_name[0])
