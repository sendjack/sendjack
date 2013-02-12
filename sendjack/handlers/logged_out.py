"""
    logged_out
    ----------

    A handler for redirecting a logged-out user to sign up, if applicable.

"""
from signup import SignUpRedirectHandler


class LoggedOutHandler(SignUpRedirectHandler):
    pass
