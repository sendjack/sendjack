"""
    Customer Object View
    --------------------

    Base Object View to subclass.

"""
from view.elementary.html import HiddenInput

from .base import ObjectView
from .field import FirstNameField, LastNameField, EmailField, CreditCardField
from .field import ExpiryMonthField, ExpiryYearField, CVCField, IDField


class CustomerView(ObjectView):

    _OBJECT_VIEW_ID = unicode("customer")
    _OBJECT_TYPE_CLASS = unicode("customer-view")

    _STATUS_REQUESTED = unicode("requested")

    allowed_fields = [
            IDField,
            FirstNameField,
            LastNameField,
            EmailField,
            #StripeTokenField,
            #StatusField,
            #TestCohortName,
            #ControlGroup,
            CreditCardField,
            ExpiryMonthField,
            ExpiryYearField,
            CVCField,
            ]


    def __init__(self, object_view_id=None, submit_text=None):
        super(CustomerView, self).__init__(
                self._OBJECT_TYPE_CLASS,
                self._get_object_view_id(object_view_id),
                self._SUBMIT_TEXT)
        self.append_class(self._OBJECT_TYPE_CLASS)

        self.append_child(StatusHiddenInput(self._STATUS_REQUESTED))


class StatusHiddenInput(HiddenInput):

    NAME = unicode("status")

    def __init__(self, value=""):
        super(StatusHiddenInput, self).__init__(self.NAME)
