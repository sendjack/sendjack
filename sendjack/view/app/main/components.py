"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section, HiddenInput

from view.app.base.components import Grid, Title
from view.app.base.components import Field, HeadField, BigField
from view.app.base.components import SubField, KeyedSubField


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
    NAME = unicode("id")
    CLASS = unicode("id")

    def __init__(self, value=""):
        super(IDField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class TemplateField(Field):

    LABEL = unicode("Template")
    NAME = unicode("template_id")
    CLASS = unicode("template-id")

    def __init__(self, value=""):
        super(TemplateField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CreatorField(Field):

    LABEL = unicode("Creator")
    NAME = unicode("creator_id")
    CLASS = unicode("creator-id")

    def __init__(self, value=""):
        super(CreatorField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CustomerTitleField(Field):

    LABEL = unicode("Title")
    NAME = unicode("customer_title")
    CLASS = unicode("customer-title")

    def __init__(self, value=""):
        super(CustomerTitleField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CustomerDescriptionField(BigField):

    LABEL = unicode("Steps")
    NAME = unicode("customer_description")
    CLASS = unicode("customer-description")

    def __init__(self, value=""):
        super(CustomerDescriptionField, self).__init__(
                self.LABEL,
                self.NAME,
                value)
        self.append_class(self.CLASS)


class TitleField(Field):

    LABEL = unicode("Title")
    NAME = unicode("title")
    CLASS = unicode("title")

    def __init__(self, value=""):
        super(TitleField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class StepsField(HeadField):

    LABEL = unicode("Steps")
    NAME = unicode("steps")
    CLASS = unicode("steps")

    def __init__(self, value=""):
        super(StepsField, self).__init__(self.LABEL, self.NAME)
        self.append_class(self.CLASS)
        self.append_child(HiddenInput(self.NAME, value))


class StepField(SubField):

    LABEL = unicode("Step")
    NAME = unicode("step")
    CLASS = unicode("step")

    def __init__(self, value="", include_index=False):
        super(StepField, self).__init__(
                self.LABEL,
                self.NAME,
                value,
                include_index)
        self.append_class(self.CLASS)


class CustomPropertiesField(HeadField):

    LABEL = unicode("Custom Properties")
    NAME = unicode("custom_properties")
    CLASS = unicode("custom-properties")

    def __init__(self, value=""):
        super(CustomPropertiesField, self).__init__(self.LABEL, self.NAME)
        self.append_class(self.CLASS)
        self.append_child(HiddenInput(self.NAME, value))


class CustomPropertyField(KeyedSubField):

    KEY_NAME = unicode("custom_property_key")
    VALUE_NAME = unicode("custom_property_value")
    CLASS = unicode("custom-property")

    def __init__(self, property_key="", property_value=""):
        super(CustomPropertyField, self).__init__(
                self.KEY_NAME,
                self.VALUE_NAME,
                property_key,
                property_value)
        self.append_class(self.CLASS)


class NotesField(BigField):

    LABEL = unicode("Notes")
    NAME = unicode("notes")
    CLASS = unicode("notes")
    NUM_ROWS = 4

    def __init__(self, value=""):
        super(NotesField, self).__init__(
                self.LABEL,
                self.NAME,
                value)
        self.append_class(self.CLASS)
        self._input_el.set_rows(self.NUM_ROWS)


class DeadlineField(Field):

    LABEL = unicode("Deadline")
    NAME = unicode("deadline_ts")
    CLASS = unicode("deadline-ts")

    def __init__(self, value=""):
        super(DeadlineField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class PriceField(Field):

    LABEL = unicode("Price")
    NAME = unicode("price")
    CLASS = unicode("price")

    def __init__(self, value=""):
        super(PriceField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class OutputTypeField(Field):

    LABEL = unicode("Output Type")
    NAME = unicode("output_type")
    CLASS = unicode("output-type")

    def __init__(self, value=""):
        super(OutputTypeField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class OutputMethodField(Field):

    LABEL = unicode("Output Method")
    NAME = unicode("output_method")
    CLASS = unicode("output-method")

    def __init__(self, value=""):
        super(OutputMethodField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CategoryTagsField(Field):

    LABEL = unicode("Categories")
    NAME = unicode("category_tags")
    CLASS = unicode("category-tags")

    def __init__(self, value=""):
        super(CategoryTagsField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class IndustryTagsField(Field):

    LABEL = unicode("Industries")
    NAME = unicode("industry_tags")
    CLASS = unicode("industry-tags")

    def __init__(self, value=""):
        super(IndustryTagsField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class SkillTagsField(Field):

    LABEL = unicode("Skills")
    NAME = unicode("skill_tags")
    CLASS = unicode("skill-tags")

    def __init__(self, value=""):
        super(SkillTagsField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class EquipmentTagsField(Field):

    LABEL = unicode("Equipment")
    NAME = unicode("equipment_tags")
    CLASS = unicode("equipment-tags")

    def __init__(self, value=""):
        super(EquipmentTagsField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)
