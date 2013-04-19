"""
    base
    ----

    Define a base synchronous handler for subclassing.

"""
from jutil.errors import OverrideNotAllowedError, OverrideRequiredError
from view.elementary.html import Element

from url.base import URL
from url.absolute import SecureEmbeddableURL

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

    def prepare(self):
        """Before we enter get/post/put/delete(), perform any last-minute
        setup. Or decide to leave and redirect elsewhere for security reasons.
        It is imperative to wait until after initialize() to redirect(), or
        else we won't be able to finish() properly, since we won't have been
        completely set up."""
        if not self._is_request_secure():
            self.secure_redirect()


    def secure_redirect(self):
        """Redirect to the same URL, but use https and the subdomain "secure."
        For dev and staging, keep http and keep the host but add a GET argument
        to prove we are functionally secure. When we have an SSL certificate
        for a wildcard subdomain, we can drop the GET argument hack."""
        # build an absolute url to redirect internally to https.
        url = SecureEmbeddableURL(self.request.path, self.request.query)

        # permanent=True also implicitly means status=301.
        self.redirect(url.render(), True)


    def _is_request_secure(self):
        """Determine whether or not the current request is secure by checking
        whether it is using https (in production). In the dev and staging
        environments, rely instead on a GET argument for testing purposes. When
        we have an SSL certificate for a wildcard subdomain, we can drop the
        GET argument hack."""
        return URL(base=self.request.uri).is_secure()
