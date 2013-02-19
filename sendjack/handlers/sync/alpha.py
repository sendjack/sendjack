"""
    alpha
    -----

    A set of landing/posting pages for our alpha test.

"""
from view.app.alpha_signup.body import SignUpSeriesBody

from .base import SyncHandler


class SignUpSeriesHandler(SyncHandler):

    """Handle alpha signup pages (user --> task --> thank you)."""

    def _set_markup_class(self):
        self._markup_class = SignUpSeriesBody
