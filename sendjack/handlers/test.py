"""
    test handler
    ------------

    A test handler.

"""
#from model.data.test import Test
from base import BaseHandler


class TestHandler(BaseHandler):


    def _init_markup(self):
        self._markup_path = "app/test.html"
