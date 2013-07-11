"""

    Simple Landing Bodies
    ---------------------

    All the bodies for the simple landing series.
    <body>

"""
from view.app.base.body import AppBody

from .simple_page import LandingPage


class SimpleBody(AppBody):

    def _construct_pages(self):
        return [
                LandingPage(),
                ]
