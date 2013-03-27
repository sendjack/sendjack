"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions for a task instance.

"""
from model.object.task_instance import TaskInstance
from model.object.task_template import TaskTemplate

from .base import CRUDHandler


# TODO: should we create a factory to churn out subclasses of
# TaskInstanceCRUDHandler, or is this giant if/elif block sufficient?

class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance


    def _trigger_created_action(self):
        if self._is_create_request():
            # TODO: we want a created task email too but for now it's just a
            # sign up email.
            pass

        elif self._is_update_request():
            # the task wasn't just created, but rather a change was made
            # without advancing it to the processed state.

            # TODO: get the diff and check that instead of self._model.
            if self._model.template_id:
                # TODO: write copy() into model.data.crud or
                # model.data.task_instance. if this isn't the right call, then
                # at least programmatically get the common columns to construct
                # the fields dict below.
                self._model = self._copy_from_task_template()

            #if self._model.price:
            #    # TODO: add a second button to be more clear about this.
            #    self._change_state("processed")


    def _copy_from_task_template(self):
        """Copy common TaskTemplate fields into this TaskInstance."""
        # TODO: figure out how to skip this when self._model.template_id was
        # not changed by this request.

        task_template = TaskTemplate.read(self._model.template_id)

        fields = {
                "title": task_template.title,
                "instructions": task_template.instructions,
                "properties": task_template.properties,
                "output_type": task_template.output_type,
                "output_method": task_template.output_method,
                "category_tags": task_template.category_tags,
                "industry_tags": task_template.industry_tags,
                "skill_tags": task_template.skill_tags,
                "equipment_tags": task_template.equipment_tags,
                }

        return TaskInstance.update(self._model.id, fields)


    def _change_state(self, to_status):
        return TaskInstance.update(self._model.id, {"status": to_status})
