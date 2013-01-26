"""
    TemplateHandler
    ---------------

    Define a TemplateHandler that handles all CRUD interactions for a Template.

"""
from base import BaseHandler
from crud import CRUDHandler


class TemplateCRUDHandler(CRUDHandler):

    """Handle all CRUD requests for a Template.

    Attributes
    ----------
    MARKUP_PATH : string

    """

    MARKUP_PATH = "crud/template/base.html"


    def get_model(self):
        # TODO: Connect this function to an actual model.
        # TODO: remove this when connected to model:
        if not hasattr(self, '_id'):
            self._id = 666

        fake_model = {
                "id": self._id,
                "name": "yes"
                }

        return fake_model


class TemplateNewHandler(BaseHandler):

    """Handle the non-CRUD new template request, as CRUD doesn't provide a form
    to submit a new Template.

    Attributes
    ----------
    MARKUP_PATH : string

    """

    MARKUP_PATH = "crud/template/new.html"

    def get_model(self):
        # TODO: Perhaps this function should return an empty TemplateModel
        fake_model = {
                "id": "",
                "name": ""
                }

        return fake_model


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
