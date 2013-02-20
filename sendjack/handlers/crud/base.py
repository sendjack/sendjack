"""
    base
    ----

    Define a base CRUD handler intended to be an abstract superclass for
    authenticated reads and writes.

"""
#import tornado.web
import json

from jutil.errors import OverrideRequiredError
from jutil.decorators import constant

from handlers.base import BaseHandler


class _RequestType(object):

    @constant
    def CREATE(self):
        return "create"

    @constant
    def READ(self):
        return "read"

    @constant
    def UPDATE(self):
        return "update"

    @constant
    def DELETE(self):
        return "delete"

REQUEST_TYPE = _RequestType()


class CRUDHandler(BaseHandler):

    """Provide an abstract superclass for CRUD operations.

    Attributes
    ----------
    _request_type : str
    _model_class : class
    _model : object

    """

    def get_current_user(self):
        return self._get_session()


    def initialize(self):
        self._set_model_class()


    def _set_model_class(self):
        """Set the model class to use."""
        raise OverrideRequiredError()


    #@tornado.web.authenticated
    def post(self, id=None):
        """Handle a POST request by mapping it to CREATE."""
        # FIXME: we need the id parameter here although we should be able to
        # change the RegEx in urls.py so it won't post if it doesn't hit.
        self._request_type = REQUEST_TYPE.CREATE
        self._pre_process_request()

        object_dict = self._get_request_body()
        self._model = self._model_class.create(object_dict)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def get(self, id=None):
        """Handle a GET request by mapping it to READ."""
        self._request_type = REQUEST_TYPE.READ
        # TODO: raise error if id is None?
        # TODO: get parameters besides id generically?
        self._pre_process_request()

        self._model = self._model_class.read(id)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def put(self, id):
        """Handle a PUT request by mapping it to UPDATE."""
        self._request_type = REQUEST_TYPE.UPDATE
        self._pre_process_request()

        object_dict = self._get_request_body()
        self._model = self._model_class.update(id, object_dict)

        self._post_process_request()
        self._send_response()


    #@tornado.web.authenticated
    def delete(self, id):
        """Handle a DELETE request."""
        self._request_type = REQUEST_TYPE.DELETE
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


    def _is_create(self):
        return self._request_type == REQUEST_TYPE.CREATE


    def _is_read(self):
        return self._request_type == REQUEST_TYPE.READ


    def _is_update(self):
        return self._request_type == REQUEST_TYPE.UPDATE


    def _is_delete(self):
        return self._request_type == REQUEST_TYPE.DELETE
