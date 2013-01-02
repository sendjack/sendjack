""" Module: urls

URLs for the Tornado handlers.

"""
from tornado.web import RedirectHandler

from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler


url_patterns = [
        (r"/", RedirectHandler, {"url": "https://secure.sendjack.com/signup"}),
        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),
        ]
