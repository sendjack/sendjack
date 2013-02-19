"""
    crud
    ----

    Define a CRUD handler intended to be an abstract superclass for
    authenticated reads and writes.

"""
#import tornado.web
import json

from jutil.errors import OverrideRequiredError

from .base import BaseHandler


class CRUDHandler(BaseHandler):

    """Provide an abstract superclass for CRUD operations.

    Attributes
    ----------
    _model_class : class
    _model : object

    """

    def get_current_user(self):
        return self._get_session()


    def initialize(self):
        self._set_model_class()


    def _set_model_class(self):
        """Construct a model object for this handler to make a CRUD call."""
        raise OverrideRequiredError()


    #@tornado.web.authenticated
    def post(self):
        """Handle a POST request by mapping it to CREATE."""
        self._pre_process_request()

        object_dict = self._get_request_body()
        self._model = self._model_class.create(object_dict)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def get(self, id=None):
        """Handle a GET request by mapping it to READ."""
        # TODO: raise error if id is None?
        # TODO: get parameters besides id generically?
        self._pre_process_request()

        self._model = self._model_class.read(id)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def put(self, id):
        """Handle a PUT request by mapping it to UPDATE."""
        self._pre_process_request()

        object_dict = self._get_request_body()
        self._model = self._model_class.update(id, object_dict)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def delete(self, id):
        """Handle a DELETE request."""
        self._pre_process_request()

        self._model = self._model_class.delete(id)

        self._post_process_request()
        self._send_response()


    def _pre_process_request(self):
        """Override to take action before db/model interaction."""
        pass


    def _post_process_request(self):
        """Override to take action after db/model interaction."""
        pass


    def _send_response(self):
        """Send response to client."""
        self.write(json.dumps(self._model.to_dict()))
        self.finish()
