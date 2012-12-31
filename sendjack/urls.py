""" Module: urls

URLs for the Tornado handlers.

"""
from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler
from handlers.test import TestHandler


url_patterns = [
        (r"/", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),
        (r"/test", TestHandler),
        ]
