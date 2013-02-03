"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from tornado.web import RedirectHandler

from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler
from handlers.template import TemplateHandler, TemplateNewHandler

from handlers.test import TestHandler, BackboneHandler


url_patterns = [
        (r"/", RedirectHandler, {"url": "https://secure.sendjack.com/signup"}),
        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),
        (r"/test", TestHandler),
        (r"/backbone", BackboneHandler),
        (r"/template/([0-9]+)", TemplateHandler),
        (r"/template", TemplateNewHandler),
        (r"/template/new", TemplateNewHandler),
        ]
