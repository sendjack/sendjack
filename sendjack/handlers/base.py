"""
    base
    ----

    Provide our base class for all Handlers in the Controller. In reality,
    this subclasses tornado.web.RequestHandler to get all of Tornado's
    Controller functionality.

    Think of this as the one-stop shop for all the basic cookie, request
    argument, user, etc. functionality that any handler in our ecosystem
    would want access to.

    Also included:

    Simple class hierarchy for the controller's cookie functionality so that
    handlers don't have to repeat work and can take advantage of a good API.

"""
import json
import tornado.web

from jutil.decorators import constant


class _Argument(object):

    @constant
    def ASYNCHRONOUS(self):
        return "asynchronous"

    @constant
    def PARAMETERS(self):
        return "parameters"

ARGUMENT = _Argument()


class _COOKIE(object):

    @constant
    def SESSION(self):
        return "session"

COOKIE = _COOKIE()


class BaseHandler(tornado.web.RequestHandler):

    """Collect common handler methods.

    All handlers should be subclasses.

    """


    def get_current_user(self):
        """Return current user from cookie or return None.

        Only override when authentication is required by a subclass.

        """
        return None


    def process_request(self):
        # TODO: grab errors subclassing this from jackalope and raise those.
        raise NotImplementedError()


    def process_asynchronous_request(self):
        # TODO: grab errors subclassing this from jackalope and raise those.
        raise NotImplementedError()


    def process_synchronous_request(self):
        # TODO: grab errors subclassing this from jackalope and raise those.
        raise NotImplementedError()


    def markup_path(self):
        # TODO: grab errors subclassing this from jackalope and raise those.
        raise NotImplementedError()


    def content_model(self):
        # TODO: grab errors subclassing this from jackalope and raise those.
        raise NotImplementedError()


    def is_asynchronous_request(self):
        return bool(self.get_argument(ARGUMENT.ASYNCHRONOUS, False))


    def get_request_parameters(self):
        return json.loads(self.get_argument(ARGUMENT.PARAMETERS, None))


    def set_session(self, cookie):
        self.set_secure_cookie(
                COOKIE.SESSION,
                tornado.escape.json_encode(cookie))


    def get_session(self):
        session = self.get_secure_cookie(COOKIE.SESSION)
        return tornado.escape.json_decode(session) if session else None


    def end_session(self):
        session = self.get_session()
        self.clear_cookie(COOKIE.SESSION)
        return session
