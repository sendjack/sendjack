"""
    simple
    -------

    Handle synchronous requests for the simple landing series.

"""
from view.app.main_theme.simple_body import SimpleBody

from .base import SyncHandler


class SimpleSyncHandler(SyncHandler):

    """Handle simple landing series.

    Note: landing --> survey --> credit card --> thanks

    """

    def _set_markup_class(self):
        self._markup_class = SimpleBody
