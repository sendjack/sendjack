"""
    task_instance
    -------------

    Handle all asynchronous CRUD interactions for a task instance.

"""
from redflag import redflag

import settings
from model.object.task_instance import TaskInstance
from model.object.task_template import TaskTemplate

from .base import CRUDHandler


class TaskInstanceCRUDHandler(CRUDHandler):

    def _set_model_class(self):
        self._model_class = TaskInstance


    def _post_process_request(self):
        if self._model.is_new():
            self._trigger_new_action()

        elif self._model.is_created():
            self._trigger_created_action()

        elif self._model.is_processed():
            self._trigger_processed_action()

        elif self._model.is_confirmed():
            self._trigger_confirmed_action()

        elif self._model.is_posted():
            self._trigger_posted_action()

        elif self._model.is_assigned():
            self._trigger_assigned_action()

        elif self._model.is_completed():
            self._trigger_completed_action()

        elif self._model.is_approved():
            self._trigger_approved_action()

        elif self._model.is_expired():
            self._trigger_expired_action()

        elif self._model.is_canceled():
            self._trigger_canceled_action()


    def _trigger_new_action(self):
        pass


    def _trigger_created_action(self):
        if self._is_create_request():
            # TODO: email the customer with a canned response that mixes in the
            # message from two of our canned responses: Welcome to Jackalope;
            # and Re: <YourNewTask>. Depending on how we want to manage the
            # control group, we might transition some tasks directly to
            # created. If so, it might be appropriate to do nothing, since the
            # created-to-posted transition would contact the customer.
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


    def _trigger_processed_action(self):
        # TODO: email test group customers with a canned response a la "Re:
        # <YourPricedTask>" and include a link to confirm and create the task.
        pass


    def _trigger_confirmed_action(self):
        # trigger an email to our jackalope service to attempt to post the task
        # to a vendor. do not message the user.
        if not self._is_read_request():
            email = unicode("{}-{}@{}").format(
                    "sendjack",
                    self._model.id,
                    settings.MAILGUN_DOMAIN)

            redflag.send_email_from_jack(
                    email,
                    "POST THIS TASK",
                    "neither the messsage nor subject make a difference")


    def _trigger_posted_action(self):
        # TODO: email the customer with a canned response a la "Re:
        # <YourConfirmedTask>" and make it clear that a worker is not yet
        # assigned.
        pass


    def _trigger_assigned_action(self):
        # this is a no-op, probably because this is likely to be unreachable
        # code. any messaging we would want to happen here should probably just
        # be mixed into the first communication that comes from the worker
        # through our system.
        pass


    def _trigger_completed_action(self):
        # TODO: email the customer with a canned response a la "Re:
        # <YourCompletedTask>" and make the approval process clear.
        pass


    def _trigger_approved_action(self):
        # TODO: email the customer with a canned response a la "Re:
        # <YourApprovedTask>" or "Re: <YourTacitlyApprovedTask>" and make it
        # clear how and why the work was approved.
        pass


    def _trigger_expired_action(self):
        pass


    def _trigger_canceled_action(self):
        pass


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
