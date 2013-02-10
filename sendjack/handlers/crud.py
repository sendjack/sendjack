"""

    crud
    ----

    Define a CRUD handler intended to be an abstract superclass for
    authenticated reads and writes.

"""
#import tornado.web

from base import BaseHandler


class CRUDHandler(BaseHandler):

    """Provide an abstract superclass for CRUD operations.

    Attributes
    ----------
    _model_object : object

    """

    _model_object = None


    def get_current_user(self):
        return self._get_session()


    def prepare(self):
        """Override to initialize a request before post/get/put/delete."""
        self._init_model()


    def _init_model(self):
        """Construct a model object for this handler to make a CRUD call."""
        # TODO: this override is required. see example error in jackalope repo.
        raise NotImplementedError()


    def _set_model(self, model):
        """Set the model to send with the response to this request."""
        self._model = model


    def _process_request(self):
        """Return the JSON version of the model."""
        self._process_asynchronous_request()


    #@tornado.web.authenticated
    def post(self):
        """Handle a POST request by mapping it to CREATE."""
        object_dict = self._get_request_parameters()
        model = self._model_object.create(object_dict)
        self._set_model(model)
        self._process_request()


    #@tornado.web.authenticated
    def get(self, id=None):
        """Handle a GET request by mapping it to READ."""
        # TODO: raise error if id is None?
        # TODO: get parameters besides id generically?
        model = self._model_object.read(id)
        self._set_model(model)
        self._process_request()


    #@tornado.web.authenticated
    def put(self, id):
        """Handle a PUT request by mapping it to UPDATE."""
        object_dict = self._get_request_parameters()
        model = self._model_object.update(id, object_dict)
        self._set_model(model)
        self._process_request()


    #@tornado.web.authenticated
    def delete(self, id):
        """Handle a DELETE request."""
        model = self._model_object.delete(id)
        self._set_model(model)
        self._process_request()
