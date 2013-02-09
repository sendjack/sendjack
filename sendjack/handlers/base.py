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
from view.elementary.html import Element
import settings


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

    _model = None


    def get_current_user(self):
        """Return current user from cookie or return None.

        Only override when authentication is required by a subclass.

        """
        return None


    def _set_session(self, cookie):
        self.set_secure_cookie(
                COOKIE.SESSION,
                tornado.escape.json_encode(cookie))


    def _get_session(self):
        session = self.get_secure_cookie(COOKIE.SESSION)
        return tornado.escape.json_decode(session) if session else None


    def _end_session(self):
        session = self._get_session()
        self.clear_cookie(COOKIE.SESSION)
        return session


    def get(self):
        """Handle a GET request by mapping it to READ."""
        self._process_request()


    def post(self):
        """Handle a POST request."""
        self._process_request()


    def _process_request(self):
        """Execute a request and send a response as JSON or markup."""
        if self._is_asynchronous_request():
            self._process_asynchronous_request()
        else:
            self._process_synchronous_request()


    def _process_asynchronous_request(self):
        """Send a JSON response to this request containing a model."""
        # TODO: deal with passing constants along too.
        self.write(json.dumps(self._model.to_dict()))


    def get_request_arguments(self):
        arguments = {}
        print self.request.arguments
        for k, v in self.request.arguments.items():
            arguments[k] = v[0]
        return arguments


    def _process_synchronous_request(self):
        """Render markup and a model as a response to this request."""
        # TODO: synchronous might not exist for the CRUDHandler.
        # TODO: deal with passing constants along too.
        self.render("pre_body.html")
        self.write(Element.to_string(self._render_body_markup(self._model)))
        self.render("post_body.html")


    def _render_body_markup(self, model=None):
        """Render markup for the response <body>."""
        raise NotImplementedError()


    def _is_asynchronous_request(self):
        return bool(self.get_argument(ARGUMENT.ASYNCHRONOUS, False))


    def _init_model(self):
        """Construct a model object for this handler to make a CRUD call."""
        # TODO: intentionally no override here, but the crud subclass requires
        # it. others should raise errors. see example error in jackalope repo.
        raise NotImplementedError()


    def _get_request_parameters(self):
        return json.loads(self.request.body)


    def render(self, markup_path, **kwargs):
        """Render jinja markup with given arguments as the response."""
        template = settings.JINJA2_ENVIRONMENT.get_template(markup_path)
        self.write(template.render(**kwargs))
