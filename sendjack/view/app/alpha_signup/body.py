"""
    Alpha Sign Up Bodies
    --------------------

    All the Pages for the alpha sign up series.
    <body>

"""
from view.app.base.body import AltBody
from view.app.alpha_signup.page import SignUpPage, NewTaskPage, ThankYouPage


class SignUpBody(AltBody):

    """The <body> with a sign up page."""


    def _construct_pages(self):
        return [SignUpPage()]


class NewTaskBody(AltBody):

    """The <body> with a new task page."""


    def _construct_pages(self):
        return [NewTaskPage()]


class ThankYouBody(AltBody):

    """The <body> with a thank you page."""


    def _construct_pages(self):
        return [ThankYouPage()]
