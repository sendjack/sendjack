"""
    post
    ----

    A extensible handler for a series of forms.

"""
from base import BaseHandler


class PostHandler(BaseHandler):

    """Handle displaying the form (GET) and the data submission (POST)."""

    def post(self):
        """Process the form data."""
        self._process_post_request()
        self.redirect(self._NEXT_URL)


    def _process_post_request(self):
        """Render markup and a model as a response to this request."""
        raise NotImplementedError("Subclass must override.")
