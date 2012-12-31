"""

    crud
    ----

    Define a CRUD handler intended to be an abstract superclass for
    authenticated reads and writes.

"""
import tornado.web

from base import BaseHandler


class CRUDHandler(BaseHandler):


    def get_current_user(self):
        return self.get_session()


    @tornado.web.authenticated
    def get(self):
        self.process_request()


    @tornado.web.authenticated
    def post(self):
        self.process_request()


    def process_request(self):
        if self.is_asynchronous_request():
            self.process_asynchronous_request()
        else:
            self.process_synchronous_request()


    def process_asynchronous_request(self):
        self.write({
                "markup": self.markup_path(),
                "model": self.content_model(),
                })


    def process_synchronous_request(self):
        self.render(self.markup_path(), self.content_model())
