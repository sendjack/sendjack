"""
    Customer Object View
    --------------------

    Base Object View to subclass.

"""
from view.elementary.html import HiddenInput, SubmitButton

from .base import ObjectView
from .field import EmailField


class CustomerView(ObjectView):

    _CUSTOMER_VIEW_CLASS = unicode("customer-view")
    _SUBMIT_TEXT = unicode("Sign Up and Continue")
    _CUSTOMER_ID = unicode("customer")

    _FIRST_NAME = unicode("first_name")
    _LAST_NAME = unicode("last_name")
    _EMAIL = unicode("email")
    _STATUS = unicode("status")
    _STATUS_REQUESTED = unicode("requested")

    def __init__(self):
        super(CustomerView, self).__init__(self._CUSTOMER_ID)
        self.append_class(self._CUSTOMER_VIEW_CLASS)

        first_name = HiddenInput(self._FIRST_NAME)
        last_name = HiddenInput(self._LAST_NAME)
        email = EmailField()
        status = HiddenInput(self._STATUS, self._STATUS_REQUESTED)
        submit = SubmitButton(self._SUBMIT_TEXT)

        first_name.append_class(self._FIRST_NAME)
        last_name.append_class(self._LAST_NAME)
        email.append_class(self._EMAIL)

        self.append_child(first_name)
        self.append_child(last_name)
        self.append_child(email)
        self.append_child(status)
        self.append_child(submit)
