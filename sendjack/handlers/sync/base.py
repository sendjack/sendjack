"""
    base
    ----

    Define a base synchronous handler for subclassing.

"""
from jutil.errors import OverrideNotAllowedError, OverrideRequiredError
from view.elementary.html import Element
from handlers.base import BaseHandler


class SyncHandler(BaseHandler):

    """Provide an abstract superclass for synchronous requests.

    Attributes
    ----------
    _markup_class : class
    _id : id

    """

    def initialize(self):
        self._set_markup_class()


    def _set_markup_class(self):
        """Set the markup class to use."""
        raise OverrideRequiredError()


    def get(self, id=None):
        """Handle synchronous GET requests."""
        self._id = id

        self._pre_process_request()
        self._send_response()


    def post(self, id=None):
        """Don't handle synchronous POST requests."""
        raise OverrideNotAllowedError


    def _send_response(self):
        """Render markup and a model as a response to this request."""
        # TODO: synchronous might not exist for the CRUDHandler.
        # TODO: deal with passing constants along too.
        self.render("pre_body.html")
        self.write(Element.to_string(self._markup_class()))
        self.render("post_body.html")


    def _pre_process_request(self):
        """Do any class specific pre processing."""
        pass


class SecureSyncHandler(SyncHandler):

    """Provide an abstract superclass for synchronous requests requiring https.

    Attributes
    ----------
    _markup_class : class
    _id : id
    """
    pass
