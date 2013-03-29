"""
    signup
    ------

A handler for the signup page.

"""
from tornado.web import RedirectHandler

from jutil.environment import Deployment

from base import BaseHandler

from model.object.user import User


class SignUpRedirectHandler(RedirectHandler):

    """ Redirect to SignUp Page (securely if not in dev). """

    def initialize(self):
        from pprint import pprint
        if Deployment.is_dev():
            pprint("DEPLOYMENT IS DEV!")
            self._url = "/search"
        else:
            self._url = "https://secure.sendjack.com/search"

        self._permanent = True


class SignUpHandler(BaseHandler):

    """ Display SignUp Page. """

    def get(self):
        """ Overload BaseHandler's HTTP GET. """
        self.render("alpha1/signup.html", xsrf_token=self.xsrf_token)


class SignUpSubmitHandler(BaseHandler):

    """ Handle form submission and respond with thank you page. """

    def post(self):
        """ Overload BaseHandler's HTTP POST. """
        parameters = self._get_arguments()

        try:
            new_user = User(parameters)
            new_user.store()

            self.render("alpha1/thankyou.html")
        except KeyError as e:
            self.render("alpha1/error.html")
        except Exception as e:
            print type(e)
            self.render("alpha1/error.html")


    def _get_arguments(self):
        """ Wrapper around getting arguments. """
        arguments = {}
        print self.request.arguments
        for k, v in self.request.arguments.items():
            arguments[k] = v[0]
        return arguments
