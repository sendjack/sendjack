"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from handlers.signup import SignUpHandler, SignUpSubmitHandler
from handlers.logged_out import LoggedOutHandler

from handlers.sync.alpha import SignUpSeriesHandler
from handlers.sync.task_instance import TaskInstanceSyncHandler
from handlers.sync.task_template import TaskTemplateSyncHandler

from handlers.crud.customer import CustomerCRUDHandler
from handlers.crud.task_instance import TaskInstanceCRUDHandler
from handlers.crud.task_template import TaskTemplateCRUDHandler
from handlers.crud.comment import CommentCRUDHandler


url_patterns = [
        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),

        (r"/posting/signup", SignUpSeriesHandler),

        (r"/", LoggedOutHandler),

        (r"/task/?([0-9]+)?", TaskInstanceSyncHandler),
        (r"/template/?([0-9]+)?", TaskTemplateSyncHandler),

        (r"/a/customer/?([0-9]+)?", CustomerCRUDHandler),
        (r"/a/task/?([0-9]+)?", TaskInstanceCRUDHandler),
        (r"/a/template/?([0-9]+)?", TaskTemplateCRUDHandler),
        (r"/a/comment/?([0-9]+)?", CommentCRUDHandler),
        ]
