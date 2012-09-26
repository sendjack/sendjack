""" Module: signup_submit

The signup form submission handler.

"""
import re
from base import BaseHandler


FIRST_NAME = "first-name"
LAST_NAME = "last-name"
EMAIL = "email"
TOKEN = "token"


class SignUpSubmitHandler(BaseHandler):

    """ Handle form submission and respond with thank you page. """


    def post(self):
        """ Overload BaseHandler's HTTP POST. """
        parameters = self._get_arguments()

        # FIXME put this in model
        first_name = parameters[FIRST_NAME]
        last_name = parameters[LAST_NAME]
        email = parameters[EMAIL]
        credit_card_token = parameters[TOKEN]

        print FIRST_NAME, first_name
        print LAST_NAME, last_name
        print EMAIL, email
        print TOKEN, credit_card_token

        self.render("thankyou.html")


    def _get_arguments(self):
        """ Wrapper around getting arguments. """
        arguments = {}
        print self.request.arguments
        for k, v in self.request.arguments.items():
            arguments[k] = v[0]
        return arguments
