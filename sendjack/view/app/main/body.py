"""
    Main Bodies
    -----------

    All the Bodies for the main series.
    <body>

"""
from view.app.base.body import MainBody

from page import TemplateNewPage


class TemplateNewBody(MainBody):

    """The <body> for the template new Page."""

    def _construct_pages(self):
        return [TemplateNewPage()]
