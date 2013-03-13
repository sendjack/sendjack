"""
    Alpha Sign Up Bodies
    --------------------

    All the Bodies for the alpha sign up series.
    <body>

"""
from view.app.base.body import AltBody

from page import CreateInstancePage, CreateCustomerPage
from page import CreateInstanceThanksPage


class CreateInstanceBody(AltBody):

    def _construct_pages(self):
        return [
                CreateInstancePage(),
                CreateCustomerPage(),
                CreateInstanceThanksPage()
                ]
