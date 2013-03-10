"""
    Main Bodies
    -----------

    All the Bodies for the main series.
    <body>

"""
from view.app.base.body import MainBody

from page import TaskTemplatePage, TaskInstancePostPage
from page import TaskInstanceApprovePage


class TaskTemplateBody(MainBody):

    """The <body> for the template new Page."""

    def _construct_pages(self):
        return [TaskTemplatePage()]


class ConfirmInstanceBody(MainBody):

    def _construct_pages(self):
        return [TaskInstancePostPage()]


class ApproveInstanceBody(MainBody):

    def _construct_pages(self):
        return [TaskInstanceApprovePage()]
