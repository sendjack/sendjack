"""
    Alpha Sign Up Bodies
    --------------------

    All the Bodies for the alpha sign up series.
    <body>

"""
from view.app.base.body import AltBody

from page import SignUpPage, NewTaskPage, ThankYouPage


class SignUpSeriesBody(AltBody):

    """The <body> with a sign up pages."""


    def _construct_pages(self):
        return [SignUpPage(), NewTaskPage(), ThankYouPage()]
