"""
    Main Bodies
    -----------

    All the Bodies for the main series.
    <body>

"""
from view.app.base.body import AppBody

from page import TaskTemplatePage


class TaskTemplateBody(AppBody):

    """The <body> for the template new Page."""

    def _construct_pages(self):
        return [TaskTemplatePage()]
