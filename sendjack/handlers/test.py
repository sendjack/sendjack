"""
    test handler
    ------------

    A test handler.

"""
from base import BaseHandler
from model.test import Test


class TestHandler(BaseHandler):


    def get(self):

        test = Test.read(6)
        self.write("ID: {}<br />".format(test.id))
        self.write("NAME: {}\n".format(test.stop))
