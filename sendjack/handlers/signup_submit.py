""" Module: signup_submit

The signup form submission handler.

"""
from model.api.user import User

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

        try:
            new_user = User(parameters)
            new_user.store()

            self.render("thankyou.html")
        except KeyError as e:
            self.render("error.html")
        except Exception as e:
            print type(e)
            self.render("error.html")


    def _get_arguments(self):
        """ Wrapper around getting arguments. """
        arguments = {}
        print self.request.arguments
        for k, v in self.request.arguments.items():
            arguments[k] = v[0]
        return arguments
