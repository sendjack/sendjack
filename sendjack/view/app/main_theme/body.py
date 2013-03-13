"""
    Alpha Sign Up Bodies
    --------------------

    All the Bodies for the alpha sign up series.
    <body>

"""
from view.app.base.body import AppBody

from page import CreateInstancePage, CreateCustomerPage
from page import CreateInstanceThanksPage


class CreateInstanceBody(AppBody):

    def _construct_pages(self):
        return [
                CreateInstancePage(),
                CreateCustomerPage(),
                CreateInstanceThanksPage()
                ]
