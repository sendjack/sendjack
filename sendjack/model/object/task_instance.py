"""
    task_instance
    -------------

    Define the TaskInstance object.

"""
from model.data.task_instance import TaskInstanceModel


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
