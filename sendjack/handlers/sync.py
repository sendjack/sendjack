"""
    sync
    ----

    Handle all sync requests through subclasses.

"""
from jutil.errors import OverrideNotAllowedError
from view.elementary.html import Element

from .base import BaseHandler


class SyncHandler(BaseHandler):

    def get(self, id=None):
        """Handle synchronous GET requests."""
        self._process_request()


    def post(self, id=None):
        """Don't handle synchronous POST requests."""
        raise OverrideNotAllowedError


    def _process_request(self):
        """Render markup and a model as a response to this request."""
        # TODO: synchronous might not exist for the CRUDHandler.
        # TODO: deal with passing constants along too.
        self.render("pre_body.html")
        self.write(Element.to_string(self._render_body_markup()))
        self.render("post_body.html")


    def _render_body_markup(self, model=None):
        """Render markup for the response <body>."""
        raise NotImplementedError()
