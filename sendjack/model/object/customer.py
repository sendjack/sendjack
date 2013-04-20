"""

    customer
    --------

    Define the Customer object.

"""
from jutil.base_type import to_unicode

from model.data.customer import CustomerModel


class Customer(CustomerModel):

    @property
    def full_name(self):
        full_name = unicode("")

        if self.first_name is not None and self.last_name is not None:
            full_name = unicode("{} {}").format(
                    self.first_name,
                    self.last_name)
        else:
            first_name = to_unicode(self.first_name)
            last_name = to_unicode(self.last_name)
            full_name = unicode("{}{}").format(first_name, last_name)

        return full_name


    @property
    def short_name(self):
        short_name = unicode("")

        if self.first_name is not None and self.last_name is not None:
            short_name = unicode("{} {}").format(
                    self.first_name,
                    self.last_name[0])

        return short_name
