"""
    Alpha Sign Up Bodies
    --------------------

    All the Bodies for the alpha sign up series.
    <body>

"""
from view.app.base.body import AppBody

from page import CreateInstancePage, CreateCustomerPage
from page import CreateInstanceThanksPage

from page import ConfirmInstancePage, CardCustomerPage
from page import ConfirmInstanceThanksPage

from page import ApproveInstancePage, ApproveInstanceThanksPage


class CreateInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                CreateInstancePage(),
                CreateCustomerPage(),
                CreateInstanceThanksPage()
                ]


class ConfirmInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                ConfirmInstancePage(),
                CardCustomerPage(),
                ConfirmInstanceThanksPage()
                ]


class ApproveInstanceBody(AppBody):

    def _construct_pages(self):
        return [ApproveInstancePage(), ApproveInstanceThanksPage()]
