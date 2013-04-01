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
import tornado
import tornado.web

from jutil.decorators import constant
from jutil.errors import OverrideRequiredError

import settings


class _PROTOCOL(object):

    @constant
    def HTTP(self):
        return "http"

    @constant
    def HTTPS(self):
        return "https"

PROTOCOL = _PROTOCOL()


class _HOST(object):

    @constant
    def BASE(self):
        return "sendjack.com"

    @constant
    def SECURE(self):
        return "secure.sendjack.com"

HOST = _HOST()


class _COOKIE(object):

    @constant
    def SESSION(self):
        return "session"

COOKIE = _COOKIE()


class BaseHandler(tornado.web.RequestHandler):

    """Handle all requests through subclasses."""


    def get_current_user(self):
        """Return current user from cookie or return None.

        Only override when authentication is required by a subclass.

        """
        return None


    def _set_session(self, cookie):
        # TODO: Sessions are not being used.
        self.set_secure_cookie(
                COOKIE.SESSION,
                tornado.escape.json_encode(cookie))


    def _get_session(self):
        # TODO: Sessions are not being used.
        session = self.get_secure_cookie(COOKIE.SESSION)
        return tornado.escape.json_decode(session) if session else None


    def _end_session(self):
        # TODO: Sessions are not being used.
        session = self._get_session()
        self.clear_cookie(COOKIE.SESSION)
        return session


    def _process_request(self):
        """Execute a request and send a response as JSON or markup."""
        raise OverrideRequiredError()


    def _get_request_body(self):
        """Return the request body (POST / PUT data) as a dict."""
        return json.loads(self.request.body)


    def render(self, markup_path, **kwargs):
        """Render jinja markup with given arguments as the response."""
        template = settings.JINJA2_ENVIRONMENT.get_template(markup_path)
        self.write(template.render(**kwargs))
