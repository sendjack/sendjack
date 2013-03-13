"""
    Main Bodies
    -----------

    All the Bodies for the main series.
    <body>

"""
from view.app.base.body import MainBody

from page import ConfirmInstancePage, CardCustomerPage
from page import ConfirmInstanceThanksPage, ProcessInstancePage

from page import TaskTemplatePage
from page import ApproveInstancePage


class TaskTemplateBody(MainBody):

    """The <body> for the template new Page."""

    def _construct_pages(self):
        return [TaskTemplatePage()]


class ProcessInstanceBody(MainBody):

    def _construct_pages(self):
        return [ProcessInstancePage()]


class ConfirmInstanceBody(MainBody):

    def _construct_pages(self):
        return [
                ConfirmInstancePage(),
                CardCustomerPage(),
                ConfirmInstanceThanksPage()
                ]


class ApproveInstanceBody(MainBody):

    def _construct_pages(self):
        return [ApproveInstancePage()]
