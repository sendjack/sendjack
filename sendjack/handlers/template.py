"""
    TemplateHandler
    ---------------

    Handle all CRUD interactions for a Template.

"""
from model.object.task_template import TaskTemplate

from view.app.main.body import TemplateBody

from base import BaseHandler
from crud import CRUDHandler


class TemplateCRUDHandler(CRUDHandler):

    """Initialize markup and model for a Template CRUD request."""


    def _init_model(self):
        self._model_object = TaskTemplate()


class TemplateSyncHandler(BaseHandler):

    """Initialize markup for a CRUD request to create a new Template."""

    def _render_body_markup(self, model=None):
        return TemplateBody()
