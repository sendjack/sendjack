"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section, HiddenInput

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


class CustomerField(Field):

    LABEL = unicode("Customer")
    NAME = unicode("customer_id")
    CLASS = unicode("customer-id")

    def __init__(self, value=""):
        super(CustomerField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CustomerTitleField(Field):

    LABEL = unicode("Title")
    NAME = unicode("customer_title")
    CLASS = unicode("customer-title")

    def __init__(self, value=""):
        super(CustomerTitleField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class CustomerDescriptionField(BigField):

    LABEL = unicode("Instructions")
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


class SummaryField(BigField):

    LABEL = unicode("Summary")
    NAME = unicode("summary")
    CLASS = unicode("summary")

    def __init__(self, value=""):
        super(SummaryField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)


class InstructionsField(HeadField):

    LABEL = unicode("Instructions")
    NAME = unicode("instructions")
    CLASS = unicode("instructions")

    def __init__(self, value=""):
        super(InstructionsField, self).__init__(self.LABEL, self.NAME)
        self.append_class(self.CLASS)
        self.append_child(HiddenInput(self.NAME, value))


class InstructionField(SubField):

    LABEL = unicode("Instruction")
    NAME = unicode("instruction")
    CLASS = unicode("instruction")

    def __init__(self, value="", include_index=False):
        super(InstructionField, self).__init__(
                self.LABEL,
                self.NAME,
                value,
                include_index)
        self.append_class(self.CLASS)


class PropertiesField(HeadField):

    LABEL = unicode("Properties")
    NAME = unicode("properties")
    CLASS = unicode("properties")

    def __init__(self, value=""):
        super(PropertiesField, self).__init__(self.LABEL, self.NAME)
        self.append_class(self.CLASS)
        self.append_child(HiddenInput(self.NAME, value))


class PropertyField(KeyedSubField):

    KEY_NAME = unicode("property_key")
    VALUE_NAME = unicode("property_value")
    CLASS = unicode("property")

    def __init__(self, property_key="", property_value=""):
        super(PropertyField, self).__init__(
                self.KEY_NAME,
                self.VALUE_NAME,
                property_key,
                property_value)
        self.append_class(self.CLASS)


class DescriptionField(BigField):

    LABEL = unicode("Description")
    NAME = unicode("description")
    CLASS = unicode("description")

    def __init__(self, value=""):
        super(DescriptionField, self).__init__(
                self.LABEL,
                self.NAME,
                value)
        self.append_class(self.CLASS)


class MoreDetailsField(BigField):

    LABEL = unicode("More Details")
    NAME = unicode("more_details")
    CLASS = unicode("more-details")
    NUM_ROWS = 4

    def __init__(self, value=""):
        super(MoreDetailsField, self).__init__(
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
