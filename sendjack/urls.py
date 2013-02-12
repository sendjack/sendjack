"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from tornado.web import RedirectHandler

from handlers.signup import SignUpHandler
from handlers.signup_submit import SignUpSubmitHandler
from handlers.customer import CustomerCRUDHandler
from handlers.task_template import TaskTemplateCRUDHandler
from handlers.task_template import TaskTemplateSyncHandler
from handlers.task_instance import TaskInstanceCRUDHandler
from handlers.task_instance import TaskInstanceSyncHandler
from handlers.alpha import SignUpSeriesHandler
from handlers.test import TestHandler


url_patterns = [
        (r"/test", TestHandler),

        (r"/", RedirectHandler, {"url": "https://secure.sendjack.com/signup"}),

        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),

        (r"/a/customer", CustomerCRUDHandler),
        (r"/a/customer/([0-9]+)", CustomerCRUDHandler),

        (r"/a/template", TaskTemplateCRUDHandler),
        (r"/a/template/([0-9]+)", TaskTemplateCRUDHandler),
        (r"/template", TaskTemplateSyncHandler),
        (r"/template/([0-9]+)", TaskTemplateSyncHandler),

        (r"/a/task", TaskInstanceCRUDHandler),
        (r"/a/task/([0-9]+)", TaskInstanceCRUDHandler),
        (r"/task", TaskInstanceSyncHandler),
        (r"/task/([0-9]+)", TaskInstanceSyncHandler),

        (r"/posting/signup", SignUpSeriesHandler),
        ]
