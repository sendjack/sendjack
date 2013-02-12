"""
    alpha
    -----

    A set of landing/posting pages for our alpha test.

"""
from view.app.alpha_signup.body import SignUpSeriesBody

from post import PostHandler


class SignUpSeriesHandler(PostHandler):

    _NEXT_URL = "/posting/newtask"

    def _render_body_markup(self, model=None):
        return SignUpSeriesBody()


    def _process_post_request(self):
        """Process the form data."""
        pass
