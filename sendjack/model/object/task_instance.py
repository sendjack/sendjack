"""
    task_instance
    -------------

    Define the TaskInstance object.

"""
from model.data.task_instance import TaskInstanceModel, TASK_INSTANCE


class TaskInstance(TaskInstanceModel):

    @property
    def deadline(self):
        # TODO: convert DateTime to string.
        pass

    @property
    def price_str(self):
        # TODO: convert to float.
        return "${}".format(self.price / 100)

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
