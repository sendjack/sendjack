"""
    urls
    ----

    URLs for the Tornado handlers.

"""
from handlers.signup import SignUpHandler, SignUpSubmitHandler

from handlers.sync.task_template import TaskTemplateSyncHandler
from handlers.sync.task_instance import (
        CreateInstanceSyncHandler,
        ProcessInstanceSyncHandler,
        ConfirmInstanceSyncHandler,
        ApproveInstanceSyncHandler)

from handlers.crud.task_template import TaskTemplateCRUDHandler
from handlers.crud.task_instance import TaskInstanceCRUDHandler
from handlers.crud.customer import CustomerCRUDHandler
from handlers.crud.comment import CommentCRUDHandler


url_patterns = [
        (r"/signup", SignUpHandler),
        (r"/thankyou", SignUpSubmitHandler),

        (r"/", CreateInstanceSyncHandler),
        (r"/search", CreateInstanceSyncHandler),
        (r"/tasks/create", CreateInstanceSyncHandler),
        (r"/users/create", CreateInstanceSyncHandler),
        (r"/tasks/create/thanks", CreateInstanceSyncHandler),

        (r"/tasks/([0-9]+)/confirm", ConfirmInstanceSyncHandler),
        (r"/users/([0-9]+)/card", ConfirmInstanceSyncHandler),
        (r"/tasks/([0-9]+)/confirm/thanks", ConfirmInstanceSyncHandler),

        (r"/tasks/([0-9]+)/process", ProcessInstanceSyncHandler),

        (r"/tasks/([0-9]+)/approve", ApproveInstanceSyncHandler),
        (r"/tasks/([0-9]+)/approve/thanks", ApproveInstanceSyncHandler),
        (r"/tasks/([0-9]+)/reject/thanks", ApproveInstanceSyncHandler),

        (r"/templates/?([0-9]+)?", TaskTemplateSyncHandler),

        (r"/a/customers/?([0-9]+)?", CustomerCRUDHandler),
        (r"/a/instances/?([0-9]+)?", TaskInstanceCRUDHandler),
        (r"/a/templates/?([0-9]+)?", TaskTemplateCRUDHandler),
        (r"/a/comments/?([0-9]+)?", CommentCRUDHandler),
        ]
