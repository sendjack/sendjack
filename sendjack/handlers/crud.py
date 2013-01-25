"""

    crud
    ----

    Define a CRUD handler intended to be an abstract superclass for
    authenticated reads and writes.

"""
import json
import tornado.web

from base import BaseHandler


class CRUDHandler(BaseHandler):

    """Provide an abstract superclass for CRUD operations.

    Attributes:
    _id : int

    """


    def get_current_user(self):
        return self.get_session()


    #@tornado.web.authenticated
    def post(self):
        """Handle POST -- create -- request."""
        # TODO: Each request should be able to get generic parameters.
        self.process_request()


    #@tornado.web.authenticated
    def get(self, id=None):
        """Handle GET -- read -- request."""
        # TODO: Each request should be able to get generic parameters.
        self._id = id
        self.process_request()


    #@tornado.web.authenticated
    def put(self, id):
        """Handle PUT -- update -- request."""
        # TODO: Each request should be able to get generic parameters.
        self._id = id
        # FIXME: This won't work with Forms (forms only use GET and POST). WE'd
        # have to use AJAX.
        print "HAHA", id
        pass


    #@tornado.web.authenticated
    def delete(self, id):
        """Handle DELETE -- delete -- request."""
        # TODO: Each request should be able to get generic parameters.
        self._id = id
        pass


    def process_request(self):
        if self.is_asynchronous_request():
            self.process_asynchronous_request()
        else:
            self.process_synchronous_request()


    def process_asynchronous_request(self):
        """Return the JSON version of the model."""
        self.write(json.dumps(self.model()))


    def process_synchronous_request(self):
        """Return the HTML page of the model."""
        # TODO: This might not exist for the CRUDHandler.
        self.render(self.markup_path(), model=self.get_model())


    def get_model(self):
        """Return the model."""
        # TODO: perhaps this should be load_model()
        raise NotImplementedError()


    def markup_path(self):
        """Return the markup path."""
        return self.MARKUP_PATH
