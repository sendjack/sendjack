"""
    Main Bodies
    -----------

    All the Bodies for the main series.
    <body>

"""
from view.app.base.body import AppBody

from page import ConfirmInstancePage, CardCustomerPage
from page import ConfirmInstanceThanksPage, ProcessInstancePage

from page import TaskTemplatePage
from page import ApproveInstancePage


class TaskTemplateBody(AppBody):

    """The <body> for the template new Page."""

    def _construct_pages(self):
        return [TaskTemplatePage()]


class ProcessInstanceBody(AppBody):

    def _construct_pages(self):
        return [ProcessInstancePage()]


class ConfirmInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                ConfirmInstancePage(),
                CardCustomerPage(),
                ConfirmInstanceThanksPage()
                ]


class ApproveInstanceBody(AppBody):

    def _construct_pages(self):
        return [ApproveInstancePage()]
