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

    _MARKUP_PATH = "app/page/new_template.html"
