"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section, HiddenInput

from view.app.base.components import Grid, Title
from view.app.base.components import Field, HeadField, SubField, BigField


class NormalSection(Section):

    NORMAL_SECTION_CLASS = unicode("normal-section")

    def __init__(self, el=None):
        super(NormalSection, self).__init__()
        self.append_class(self.NORMAL_SECTION_CLASS)

        if el:
            self.append_child(el)


class ContrastSection(Section):

    CONTRAST_SECTION_CLASS = unicode("contrast-section")

    def __init__(self, el=None):
        super(ContrastSection, self).__init__()
        self.append_class(self.CONTRAST_SECTION_CLASS)

        if el:
            self.append_child(el)


class TitledGrid(Grid):

    """A Grid with a Title at the top."""

    def __init__(self, title_str):
        super(TitledGrid, self).__init__()

        self.append_child(Title(title_str))


class IDField(Field):

    LABEL = unicode("ID")
    KEY = unicode("id")
    CLASS = unicode("id")

    def __init__(self, value=""):
        super(IDField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class CreatorField(Field):

    LABEL = unicode("Creator")
    KEY = unicode("creator_id")
    CLASS = unicode("creator-id")

    def __init__(self, value=""):
        super(CustomerTitleField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class CustomerTitleField(Field):

    LABEL = unicode("Title")
    KEY = unicode("customer_title")
    CLASS = unicode("customer-title")

    def __init__(self, value=""):
        super(CustomerTitleField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class CustomerDescriptionField(BigField):

    LABEL = unicode("Steps")
    KEY = unicode("customer_description")
    CLASS = unicode("customer-description")

    def __init__(self, value=""):
        super(CustomerDescriptionField, self).__init__(
                self.LABEL,
                self.KEY,
                value)
        self.append_class(self.CLASS)


class TitleField(Field):

    LABEL = unicode("Title")
    KEY = unicode("title")
    CLASS = unicode("title")

    def __init__(self, value=""):
        super(TitleField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class StepsField(HeadField):

    LABEL = unicode("Steps")
    KEY = unicode("steps")
    CLASS = unicode("steps")

    def __init__(self, value=""):
        super(StepsField, self).__init__(self.LABEL, self.KEY)
        self.append_class(self.CLASS)
        self.append_child(HiddenInput(self.KEY, value))


class StepField(SubField):

    LABEL = unicode("Step")
    KEY = unicode("step")
    CLASS = unicode("step")

    def __init__(self, value="", include_index=False):
        super(StepField, self).__init__(
                self.LABEL,
                self.KEY,
                value,
                include_index)
        self.append_class(self.CLASS)


class DeadlineField(Field):

    LABEL = unicode("Deadline")
    KEY = unicode("deadline_ts")
    CLASS = unicode("deadline-ts")

    def __init__(self, value=""):
        super(DeadlineField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class PriceField(Field):

    LABEL = unicode("Price")
    KEY = unicode("price")
    CLASS = unicode("price")

    def __init__(self, value=""):
        super(PriceField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class OutputTypeField(Field):

    LABEL = unicode("Output Type")
    KEY = unicode("output_type")
    CLASS = unicode("output-type")

    def __init__(self, value=""):
        super(OutputTypeField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class OutputMethodField(Field):

    LABEL = unicode("Output Method")
    KEY = unicode("output_method")
    CLASS = unicode("output-method")

    def __init__(self, value=""):
        super(OutputMethodField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class CategoryTagsField(Field):

    LABEL = unicode("Category Tags")
    KEY = unicode("category_tags")
    CLASS = unicode("category-tags")

    def __init__(self, value=""):
        super(CategoryTagsField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class IndustryTagsField(Field):

    LABEL = unicode("Industry Tags")
    KEY = unicode("industry_tags")
    CLASS = unicode("industry-tags")

    def __init__(self, value=""):
        super(IndustryTagsField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class SkillsTagsField(Field):

    LABEL = unicode("Skills Tags")
    KEY = unicode("skills_tags")
    CLASS = unicode("skills-tags")

    def __init__(self, value=""):
        super(SkillsTagsField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)


class EquipmentTagsField(Field):

    LABEL = unicode("Equipment Tags")
    KEY = unicode("equipment_tags")
    CLASS = unicode("equipment-tags")

    def __init__(self, value=""):
        super(EquipmentTagsField, self).__init__(self.LABEL, self.KEY, value)
        self.append_class(self.CLASS)
