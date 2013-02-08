"""
    post
    ----

    A extensible handler for a series of forms.

"""
from base import BaseHandler


class PostHandler(BaseHandler):

    """Handle displaying the form (GET) and the data submission (POST)."""


    def get(self):
        self.render("pre_body.html")
        self._render_body()
        self.render("post_body.html")


    def _render_body():
        raise NotImplementedError("Subclass must override.")


    def _process_request(self):
        """Process the form data."""
        self._process_synchronous_request()
        print "EVAN", self._NEXT_URL
        self.redirect(self._NEXT_URL)


    def _process_synchronous_request(self):
        """Render markup and a model as a response to this request."""
        raise NotImplementedError("Subclass must override.")
