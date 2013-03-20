"""
    task_instance
    -------------

    Define the TaskInstance object.

"""
from model.data.task_instance import TaskInstanceModel, TASK_INSTANCE
from model.object.status_message import TaskStatusMessage


class TaskInstance(TaskInstanceModel):

    def __str__(self):
        fields = {
                "id": self.id,
                "status": self.status,
                "customer_id": self.customer_id,
                "customer_title": self.customer_title,
                "customer_description": self.customer_description,
                "template_id": self.template_id,
                "title": self.title,
                "instructions": self.instructions,
                "properties": self.properties,
                "more_details": self.more_details,
                "summary": self.summary,
                "description": self.description,
                "deadline_ts": self.deadline_ts,
                "price": self.price,
                "output_type": self.output_type,
                "output_method": self.output_method,
                "category_tags": self.category_tags,
                "industry_tags": self.industry_tags,
                "skill_tags": self.skill_tags,
                "equipment_tags": self.equipment_tags,
                }

        return "\n".join(
                ["{} : {}".format(k, v) for k, v in fields.items()]
                )

    @property
    def deadline(self):
        # TODO: convert DateTime to string.
        pass

    @property
    def price_str(self):
        # TODO: convert to float.
        # TODO: store 100*price
        #return "${}".format(self.price / 100)
        pass

    @property
    def overhead_str(self):
        return "{} hours".format(self.overhead / 3600)

    @property
    def interactions_str(self):
        return "{} messages".format(self.interactions)

    @property
    def score_str(self):
        return "{} rating".format(self.score)

    @property
    def location_range_str(self):
        return "within {} miles of {}".format(
                self.location_radius,
                self.location)

    @property
    def status_message(self):
        return TaskStatusMessage(self.status, self)

    def is_new(self):
        return self.status == TASK_INSTANCE.NEW


    def is_created(self):
        return self.status == TASK_INSTANCE.CREATED


    def is_processed(self):
        return self.status == TASK_INSTANCE.PROCESSED


    def is_confirmed(self):
        return self.status == TASK_INSTANCE.CONFIRMED


    def is_posted(self):
        return self.status == TASK_INSTANCE.POSTED


    def is_assigned(self):
        return self.status == TASK_INSTANCE.ASSIGNED


    def is_completed(self):
        return self.status == TASK_INSTANCE.COMPLETED


    def is_approved(self):
        return self.status == TASK_INSTANCE.APPROVED


    def is_expired(self):
        return self.status == TASK_INSTANCE.EXPIRED


    def is_canceled(self):
        return self.status == TASK_INSTANCE.CANCELED
