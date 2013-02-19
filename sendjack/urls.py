"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from handlers.test import TestHandler
from handlers.signup import SignUpHandler, SignUpSubmitHandler
from handlers.alpha import SignUpSeriesHandler
from handlers.logged_out import LoggedOutHandler

from handlers.task_instance import TaskInstanceSyncHandler
from handlers.task_template import TaskTemplateSyncHandler

from handlers.customer import CustomerCRUDHandler
from handlers.task_instance import TaskInstanceCRUDHandler
from handlers.task_template import TaskTemplateCRUDHandler


url_patterns = [
        (r"/test", TestHandler),

        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),

        (r"/posting/signup", SignUpSeriesHandler),

        (r"/", LoggedOutHandler),

        (r"/task/?([0-9]+)?", TaskInstanceSyncHandler),
        (r"/template/?([0-9]+)?", TaskTemplateSyncHandler),

        (r"/a/customer/?([0-9]+)?", CustomerCRUDHandler),
        (r"/a/task/?([0-9]+)?", TaskInstanceCRUDHandler),
        (r"/a/template/?([0-9]+)?", TaskTemplateCRUDHandler),
        ]
