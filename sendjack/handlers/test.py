"""
    test handler
    ------------

    A test handler.

"""
#from model.data.test import TestTable
from base import BaseHandler
from crud import CRUDHandler


class TestHandler(BaseHandler):


    MARKUP_PATH = "app/test.html"


    def get_model(self):
        return None


    def get(self):
        self.process_request()


    def process_request(self):
        if self.is_asynchronous_request():
            self.process_asynchronous_request()
        else:
            self.process_synchronous_request()


    def process_synchronous_request(self):
        """Return the HTML page of an empty form."""
        self.render_jinja(self.MARKUP_PATH, model=self.get_model())
        #self.render(self.MARKUP_PATH, model=self.get_model())


class BackboneHandler(CRUDHandler):

    def get_model(self):
        # TODO: Connect this function to an actual model.
        # TODO: remove this when connected to model:
        if not hasattr(self, '_id'):
            self._id = 666

        fake_model = {
                "id": self._id,
                "name": "yes",
                "age": 24
                }

        return fake_model
