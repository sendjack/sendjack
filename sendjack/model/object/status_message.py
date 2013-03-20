"""
    status
    ------

"""
from jutil.errors import OverrideRequiredError


# XXX: FINISH THIS!


class StatusMessage(object):

    _status = None
    _model = None

    def __init__(self, status, model):
        self._status = status
        self._model = model

    def subject(self):
        raise OverrideRequiredError()

    def body(self):
        raise OverrideRequiredError()


class TaskStatus(StatusMessage):

    @property
    def subject(self):
        # XXX: FILL ME IN!
        return "SUBJECT!"


    @property
    def body(self):
        # XXX: FILL ME IN!
        return "BODY!"
