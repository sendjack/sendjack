""" Module: urls

URLs for the Tornado handlers.

"""
from handlers.signup import SignUpHandler

url_patterns = [
        (r"/", SignUpHandler),
        ]
