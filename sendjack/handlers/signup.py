"""
    signup
    ------

A handler for the signup page.

"""
from base import BaseHandler


class SignUpHandler(BaseHandler):

    """ Display SignUp Page. """


    def get(self):
        """ Overload BaseHandler's HTTP GET. """
        self.render("signup.html", xsrf_token=self.xsrf_token)
