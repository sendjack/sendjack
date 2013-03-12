"""

    task_template
    -------------

    Define the TaskTemplate object.

"""
from model.data.task_template import TaskTemplateModel


class TaskTemplate(TaskTemplateModel):

    @property
    def price_range(self):
        return (self.min_price, self.max_price)

    @property
    def price_range_str(self):
        # TODO: convert to float.
        return "${} to ${} per hour".format(
                self.min_price / 100,
                self.max_price / 100)

    @property
    def overhead_range(self):
        return (self.min_overhead, self.max_overhead)

    @property
    def overhead_range_str(self):
        return "{} to {} hours".format(
                self.min_overhead / 3600,
                self.max_overhead / 3600)

    @property
    def interactions_range(self):
        return (self.min_interactions, self.max_interactions)

    @property
    def interactions_range_str(self):
        return "{} to {} messages".format(
                self.min_interactions,
                self.max_interactions)

    @property
    def score_range(self):
        return (self.min_score, self.max_score)

    @property
    def score_range_str(self):
        return "{} to {} rating".format(self.min_score, self.max_score)

    @property
    def location_range_str(self):
        return "within {} miles of {}".format(
                self.location_radius,
                self.location)

    @property
    def output_str(self):
        return "{} via {}".format(self.output_type, self.output_method)

    @property
    def category_str(self):
        return ", ".join(self.category_tags)

    @property
    def industry_str(self):
        return ", ".join(self.industry_tags)

    @property
    def skill_str(self):
        return ", ".join(self.skill_tags)

    @property
    def equipment_str(self):
        return ", ".join(self.equipment_tags)
