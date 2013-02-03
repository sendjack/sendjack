"""
    test handler
    ------------

    A test handler.

"""
#from model.data.test import Test
from base import BaseHandler
from crud import CRUDHandler


class TestHandler(BaseHandler):


    def _init_markup(self):
        self._markup_path = "app/test.html"


class BackboneHandler(CRUDHandler):

    def _init_model(self):
        # TODO: Connect this function to an actual model.
        # TODO: remove this when connected to model:
        if not hasattr(self, '_id'):
            self._id = 666

        self._model_object = {
                "id": self._id,
                "name": "yes",
                "age": 24
                }
