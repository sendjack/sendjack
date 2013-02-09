"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from tornado.web import RedirectHandler

from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler
from handlers.template import TemplateCRUDHandler, TemplateSyncHandler
from handlers.alpha import SignUpPostingHandler
from handlers.alpha import NewTaskPostingHandler
from handlers.alpha import ThankYouPostingHandler
from handlers.test import TestHandler


url_patterns = [
        (r"/", RedirectHandler, {"url": "https://secure.sendjack.com/signup"}),

        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),

        (r"/test", TestHandler),

        (r"/a/template/([0-9]+)", TemplateCRUDHandler),
        (r"/a/template", TemplateCRUDHandler),
        (r"/template/([0-9]+)", TemplateSyncHandler),
        (r"/template", TemplateSyncHandler),

        (r"/posting/signup", SignUpPostingHandler),
        (r"/posting/signup/submit", SignUpPostingHandler),
        (r"/posting/newtask", NewTaskPostingHandler),
        (r"/posting/newtask/submit", NewTaskPostingHandler),
        (r"/posting/thankyou", ThankYouPostingHandler)
        ]
