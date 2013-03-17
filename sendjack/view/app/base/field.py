"""
    Field Components
    ----------------

    Components that are fields or wrappers around fields and can be used for
    any theme.

"""
from view.elementary.html import Div, UL
from view.elementary.html import HiddenInput, TextInput, Label, Textarea
from view.app.base.components import DatePicker


class Field(Div):

    FIELD_CLASS = unicode("field")
    KEY_CLASS = unicode("key")
    VALUE_CLASS = unicode("value")

    _label_el = None
    _input_el = None

    def __init__(self, label, name, value=""):
        super(Field, self).__init__()
        self.append_class(self.FIELD_CLASS)

        self._label_el = self._construct_label(label, name)
        self._label_el.append_class(self.KEY_CLASS)
        self.append_child(self._label_el)

        self._input_el = self._construct_input(name, value)
        self._input_el.append_class(self.VALUE_CLASS)
        self.append_child(self._input_el)


    def _construct_label(self, label, name):
        return Label(label, name)


    def _construct_input(self, name, value):
        return TextInput(name, value)


    def set_placeholder(self, placeholder):
        # Override Element's set_placeholder to act on child input.
        self._input_el.set_placeholder(placeholder)


class BigField(Field):

    BIG_FIELD_CLASS = unicode("big-field")
    DEFAULT_NUM_ROWS = 9

    _label_el = None
    _input_el = None

    def __init__(self, label, name, value=""):
        super(BigField, self).__init__(label, name, value)
        self.append_class(self.BIG_FIELD_CLASS)


    def _construct_input(self, name, value):
        input_el = Textarea(name, value)
        input_el.set_rows(self.DEFAULT_NUM_ROWS)
        return input_el


    def set_rows(self, num_of_rows):
        # Override Element's set_rows to act on child input.
        self._input_el.set_rows(num_of_rows)


class HeadField(Div):

    FIELD_CLASS = unicode("field")
    KEY_CLASS = unicode("head-key")

    _label_el = None

    def __init__(self, label, name):
        super(HeadField, self).__init__()
        self.append_class(self.FIELD_CLASS)

        # assemble label
        self._label_el = Label(label, name)
        self._label_el.append_class(self.KEY_CLASS)

        self.append_child(self._label_el)


class SubField(Div):

    FIELD_CLASS = unicode("sub-field")
    KEY_CLASS = unicode("sub-key")
    VALUE_CLASS = unicode("sub-value")

    _label_el = None
    _input_el = None

    def __init__(self, label, name, value="", include_index=False):
        super(SubField, self).__init__()
        self.append_class(self.FIELD_CLASS)

        if include_index:
            label = unicode("{} 1".format(label))

        # TODO: can this be <subfield-name>[]?
        #name = unicode("{}[]".format(name))

        # assemble label
        self._label_el = Label(label, name)
        self._label_el.append_class(self.KEY_CLASS)

        # assemble input
        self._input_el = TextInput(name, value)
        self._input_el.append_class(self.VALUE_CLASS)

        self.append_child(self._label_el)
        self.append_child(self._input_el)


class KeyedSubField(Div):

    FIELD_CLASS = unicode("sub-field")
    KEY_CLASS = unicode("sub-key")
    VALUE_CLASS = unicode("sub-value")

    _label_el = None
    _input_el = None

    def __init__(self, key_name, value_name, key_value="", value_value=""):
        super(KeyedSubField, self).__init__()
        self.append_class(self.FIELD_CLASS)

        # TODO: can this be <subfield-name>[]?
        #key_name = unicode("{}[]".format(key_name))
        #value_name = unicode("{}[]".format(value_name))

        # assemble key input
        self._label_el = TextInput(key_name, key_value)
        self._label_el.append_class(self.KEY_CLASS)

        # assemble value input
        self._input_el = TextInput(value_name, value_value)
        self._input_el.append_class(self.VALUE_CLASS)

        self.append_child(self._label_el)
        self.append_child(self._input_el)


class FieldList(UL):

    FIELD_LIST_CLASS = unicode("field-list")

    def __init__(self, fields):
        super(FieldList, self).__init__(fields)
        self.append_class(self.FIELD_LIST_CLASS)


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


    def _construct_input(self, name, value):
        # Overwrite Field's _set_input to use DatePicker.
        return DatePicker(name, value)


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


class EmailField(Field):

    LABEL = unicode("Email")
    NAME = unicode("email")
    CLASS = unicode("email")

    def __init__(self, value=""):
        super(EmailField, self).__init__(self.LABEL, self.NAME, value)
        self.append_class(self.CLASS)
