""" Module: urls

URLs for the Tornado handlers.

"""
from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler


url_patterns = [
        (r"/", SignUpHandler),
        (r"/signup/submit", SignUpSubmitHandler)
        ]
