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


class _HEADERS(object):

    @constant
    def FORWARDED_IP(self):
        """The originating client IP connecting to the Heroku router."""
        return "x-forwarded-for"

    @constant
    def FORWARDED_PROTOCOL(self):
        """Originating protocol of the client's HTTP request (ex: https)."""
        return "x-forwarded-proto"

    @constant
    def FORWARDED_PORT(self):
        """Originating port of the client's HTTP request (ex: 443)."""
        return "x-forwarded-port"

    @constant
    def REQUEST_START_TS(self):
        """Timestamp (milliseconds) when the router received the request."""
        return "x-request-start"

HEADERS = _HEADERS()


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


    def initialize(self):
        # TODO: learn something and then remove these!
        print("[X-Real-Ip] [{}]".format(self.request.remote_ip))
        print("[X-Forwarded-For] [{}]".format(
                self.request.headers.get(HEADERS.FORWARDED_IP, "")))
        print("[X-Forwarded-Port] [{}]".format(
                self.request.headers.get(HEADERS.FORWARDED_PORT, "")))
        print("[X-Forwarded-Proto] [{}]".format(
                self.request.headers.get(HEADERS.FORWARDED_PROTOCOL, "")))
        print("[protocol] [{}]".format(self.request.protocol))


    @property
    def client_ip(self):
        """When xheaders=True is set in the HTTPServer constructor, Heroku
        sends the client IP in the X-Forwarded-For header, and Tornado
        attempts to set self.request.remote_ip to X-Real-Ip. However, they
        don't necessarily play well together, so just rely on Heroku."""
        return self.request.headers.get(HEADERS.FORWARDED_IP, "")


    @property
    def client_port(self):
        """When xheaders=True is set in the HTTPServer constructor, Heroku
        sends the client port in the X-Forwarded-Port header, but Tornado
        request objects have no notion of port. This may be vestigial, but it's
        valuable at least for documentation purposes."""
        return self.request.headers.get(HEADERS.FORWARDED_PORT, "")


    @property
    def start_ts(self):
        """When xheaders=True is set in the HTTPServer constructor, Heroku
        sends a UNIX timestamp (in milliseconds) for the request start time."""
        return self.request.headers.get(HEADERS.REQUEST_START_TS, None)


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
