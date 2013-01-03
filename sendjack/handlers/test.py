"""
    test handler
    ------------

    A test handler.

"""
from base import BaseHandler
from model.data.test import TestTable


class TestHandler(BaseHandler):


    def get(self):

        test = TestTable.read(6)
        self.write("ID: {}<br />".format(test.id))
        self.write("NAME: {}\n".format(test.stop))
