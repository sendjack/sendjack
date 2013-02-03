"""
    TemplateHandler
    ---------------

    Handle all CRUD interactions for a Template.

"""
from model.object.task_template import TaskTemplate

from base import BaseHandler
from crud import CRUDHandler


class TemplateHandler(CRUDHandler):

    """Initialize markup and model for a Template CRUD request."""


    def _init_model(self):
        self._model_object = TaskTemplate()


class TemplateNewHandler(BaseHandler):

    """Initialize markup for a CRUD request to create a new Template."""


    def _init_markup(self):
        self._markup_path = "app/page/new_template.html"
