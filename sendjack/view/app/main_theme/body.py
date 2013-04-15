"""
    Alpha Sign Up Bodies
    --------------------

    All the Bodies for the alpha sign up series.
    <body>

"""
from view.app.base.body import AppBody

from .page import (
        SearchPage,
        CreateInstancePage,
        CreateCustomerPage,
        CreateInstanceThanksPage,
        ProcessInstancePage,
        ConfirmInstancePage,
        CardCustomerPage,
        ConfirmInstanceThanksPage,
        ApproveInstancePage,
        ApproveInstanceThanksPage,
        RejectInstanceThanksPage)


class CreateInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                SearchPage(),
                CreateInstancePage(),
                CreateCustomerPage(),
                CreateInstanceThanksPage(),
                ]


class ProcessInstanceBody(AppBody):

    def _construct_pages(self):
        return [ProcessInstancePage()]


class ConfirmInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                ConfirmInstancePage(),
                CardCustomerPage(),
                ConfirmInstanceThanksPage(),
                ]


class ApproveInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                ApproveInstancePage(),
                ApproveInstanceThanksPage(),
                RejectInstanceThanksPage(),
                ]
