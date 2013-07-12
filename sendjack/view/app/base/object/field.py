"""
    Field Components
    ----------------

    Components that are fields or wrappers around fields and can be used for
    any theme.

"""
from jutil.errors import OverrideNotAllowedError

from view.elementary.html import Div, UL
from view.elementary.html import HiddenInput, TextInput, Label, Textarea
from view.app.base.components import DatePicker, CurrencyInput


# TODO: move this to view.elementary.components
class DataDiv(Div):

    _DASH = unicode("-")
    _UNDERSCORE = unicode("_")

    def _append_data_class(self, type, key):
        # CSS has no parent selector, so give the wrapper a class corresponding
        # to the data in it.
        raw_data_class = unicode("{}-{}").format(type, key)
        data_class = raw_data_class.replace(self._UNDERSCORE, self._DASH)
        self.append_class(data_class)


class Field(DataDiv):

    _FIELD_CLASS = unicode("field")
    _KEY_CLASS = unicode("key")
    _VALUE_CLASS = unicode("value")

    _KEY_EXPLANATION = unicode("")
    _VALUE_PLACEHOLDER = unicode("")

    _key_el = None
    _value_el = None

    def __init__(self, key, name, value="", is_explained=False):
        super(Field, self).__init__()
        self.append_class(self._FIELD_CLASS)
        self._append_data_class(self._FIELD_CLASS, name)

        self._key_el = self._construct_key(key, name)
        if self._key_el:
            self._key_el.append_class(self._KEY_CLASS)

            if is_explained:
                self._set_explanation(self._KEY_EXPLANATION)

            self.append_child(self._key_el)

        # HeadField has no value element
        if value is not None:
            self._value_el = self._construct_value(name, value)
            self._value_el.append_class(self._VALUE_CLASS)
            self._value_el.set_placeholder(self._VALUE_PLACEHOLDER)
            self.append_child(self._value_el)


    def _construct_key(self, key, name):
        return Label(key, name)


    def _construct_value(self, name, value):
        return TextInput(name, value)


    def _set_explanation(self, text):
        self._key_el.set_tail(unicode("({})".format(text)))


    def set_placeholder(self, value):
        # So we don't need to make a subclass everytime we want to override the
        # value input's placeholder.
        self._value_el.set_placeholder(value)


    def get_key_name(self):
        return self.KEY_NAME


class BigField(Field):

    _BIG_FIELD_CLASS = unicode("big-field")
    _DEFAULT_NUM_ROWS = 9

    def __init__(self, key, name, value="", is_explained=False):
        super(BigField, self).__init__(key, name, value, is_explained)

        self.append_class(self._BIG_FIELD_CLASS)


    def _construct_value(self, name, value):
        input_el = Textarea(name, value)
        input_el.set_rows(self._DEFAULT_NUM_ROWS)
        return input_el


    def set_rows(self, num_of_rows):
        # Override Element's set_rows to act on child input.
        self._value_el.set_rows(num_of_rows)


class HeadField(Field):

    _KEY_CLASS = unicode("head-key")
    _VALUE_CLASS = None

    def __init__(self, key, name, is_explained=False):
        super(HeadField, self).__init__(key, name, None, is_explained)

        # TODO: this implicitly adds a call to self._append_data_class(). does
        # that change anything about this implementation?


    def _construct_value(self, name, value):
        raise OverrideNotAllowedError("Not callable on this subclass.")


class SubField(Field):

    _FIELD_CLASS = unicode("sub-field")
    _KEY_CLASS = unicode("sub-key")
    _VALUE_CLASS = unicode("sub-value")

    # class names and disallowing the explanation parameter are the only things
    # different from the superclass, so override those and nothing else.

    def __init__(self, key, name, value=""):
        super(SubField, self).__init__(key, name, value)

        # TODO: this implicitly adds a call to self._append_data_class(). does
        # that change anything about this implementation?


# TODO: work this into the Field subclass hierarchy. maybe.
class KeyedSubField(DataDiv):

    """Field has a more natural but less abstract notion of a field being a
    key/value pair. Meaning, it forces keys to be label elements, which they
    nearly always will be. In order to properly treat this as a special case,
    just don't subclass Field and instead mimic it's logic.
    """

    _FIELD_CLASS = unicode("sub-field")
    _KEY_CLASS = unicode("sub-key")
    _VALUE_CLASS = unicode("sub-value")

    _KEY_PLACEHOLDER = unicode("")
    _VALUE_PLACEHOLDER = unicode("")

    _key_el = None
    _value_el = None

    # TODO: make Field abstract enough to accommodate non-Label key elements.

    def __init__(self, key_name, value_name, key_value="", value_value=""):
        super(KeyedSubField, self).__init__()
        self.append_class(self._FIELD_CLASS)

        # also of note: KeyedSubField has no explanation parameter.

        # TODO: do we want to bother with data class?
        #self._append_data_class(self._FIELD_CLASS, value_name)

        self._key_el = self._construct_key(key_name, key_value)
        self._key_el.set_placeholder(self._KEY_PLACEHOLDER)
        self._key_el.append_class(self._KEY_CLASS)

        self._value_el = self._construct_value(value_name, value_value)
        self._value_el.set_placeholder(self._VALUE_PLACEHOLDER)
        self._value_el.append_class(self._VALUE_CLASS)

        self.append_child(self._key_el)
        self.append_child(self._value_el)


    def _construct_key(self, key, name):
        # this override abuses the superclass signature slightly. key is
        # key_name and name is key_value.
        return TextInput(key, name)


    def _construct_value(self, key, name):
        return self._construct_key(key, name)


    def _set_explanation(self, text):
        raise OverrideNotAllowedError("Not callable on this subclass.")


    def set_placeholder(self, value):
        # So we don't need to make a subclass everytime we want to override the
        # value input's placeholder.
        self._value_el.set_placeholder(value)


class FieldList(UL):

    FIELD_LIST_CLASS = unicode("field-list")

    def __init__(self, fields):
        super(FieldList, self).__init__(fields)
        self.append_class(self.FIELD_LIST_CLASS)


class IDField(Field):

    LABEL = unicode("ID")
    NAME = unicode("id")

    def __init__(self):
        super(IDField, self).__init__(self.LABEL, self.NAME)


class TemplateIDField(Field):

    LABEL = unicode("Template ID")
    NAME = unicode("template_id")

    def __init__(self):
        super(TemplateIDField, self).__init__(self.LABEL, self.NAME)


class CreatorField(Field):

    LABEL = unicode("Creator")
    NAME = unicode("creator_id")

    def __init__(self):
        super(CreatorField, self).__init__(self.LABEL, self.NAME)


class CustomerIDField(Field):

    LABEL = unicode("Customer")
    NAME = unicode("customer_id")

    def __init__(self):
        super(CustomerIDField, self).__init__(self.LABEL, self.NAME)


class CustomerTitleField(Field):

    LABEL = unicode("Title")
    NAME = unicode("customer_title")

    _KEY_EXPLANATION = NAME
    _VALUE_PLACEHOLDER = unicode("Enter a title for your task...")

    def __init__(self, is_explained=False):
        super(CustomerTitleField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)


class CustomerDescriptionField(BigField):

    LABEL = unicode("Instructions")
    NAME = unicode("customer_description")

    _KEY_EXPLANATION = NAME
    _VALUE_PLACEHOLDER = unicode("Describe your task...")

    def __init__(self, is_explained=False):
        super(CustomerDescriptionField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)


class TitleField(Field):

    LABEL = unicode("Title")
    NAME = unicode("title")

    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(TitleField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)


class SummaryField(BigField):

    LABEL = unicode("Summary")
    NAME = unicode("summary")

    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(SummaryField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)


class InstructionsField(HeadField):

    LABEL = unicode("Instructions")
    NAME = unicode("instructions")

    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(InstructionsField, self).__init__(
                self.LABEL,
                self.NAME,
                is_explained)
        self.append_child(HiddenInput(self.NAME))


class InstructionField(SubField):

    LABEL = unicode("Step")
    NAME = unicode("instruction")
    CLASS = unicode("instruction")

    def __init__(self):
        super(InstructionField, self).__init__(self.LABEL, self.NAME)
        self.append_class(self.CLASS)


class PropertiesField(HeadField):

    LABEL = unicode("Properties")
    NAME = unicode("properties")

    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(PropertiesField, self).__init__(
                self.LABEL,
                self.NAME,
                is_explained)
        self.append_child(HiddenInput(self.NAME))


class PropertyField(KeyedSubField):

    KEY_NAME = unicode("property_key")
    VALUE_NAME = unicode("property_value")
    CLASS = unicode("property")

    def __init__(self):
        super(PropertyField, self).__init__(self.KEY_NAME, self.VALUE_NAME)
        self.append_class(self.CLASS)


class DescriptionField(BigField):

    LABEL = unicode("Instructions")
    NAME = unicode("description")

    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(DescriptionField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)


class MoreDetailsField(BigField):

    LABEL = unicode("More Details")
    NAME = unicode("more_details")

    _DEFAULT_NUM_ROWS = 5
    _KEY_EXPLANATION = NAME

    def __init__(self, is_explained=False):
        super(MoreDetailsField, self).__init__(
                self.LABEL,
                self.NAME,
                "",
                is_explained)

        # XXX: does this work? if so, explanation can probably be set some
        # other simpler way [ebh: by 'this' do you mean num rows or
        # 'is_explained'?]
        self.set_rows(self._DEFAULT_NUM_ROWS)


class DeadlineField(Field):

    LABEL = unicode("Deadline")
    NAME = unicode("deadline_ts")

    _VALUE_PLACEHOLDER = unicode("06/31/2013")

    def __init__(self):
        super(DeadlineField, self).__init__(self.LABEL, self.NAME)


    def _construct_value(self, name, value):
        # Overwrite Field's _construct_value to use DatePicker.
        return DatePicker(name, value)


class PriceField(Field):

    LABEL = unicode("Price ($)")
    NAME = unicode("price")

    _VALUE_PLACEHOLDER = unicode("US$")

    def __init__(self):
        super(PriceField, self).__init__(self.LABEL, self.NAME)


    def _construct_value(self, name, value):
        # Overwrite Field's _construct_value to use CurrencyInput.
        return CurrencyInput(name, value)


class OutputTypeField(Field):

    LABEL = unicode("Output Type")
    NAME = unicode("output_type")

    def __init__(self):
        super(OutputTypeField, self).__init__(self.LABEL, self.NAME)


class OutputMethodField(Field):

    LABEL = unicode("Output Method")
    NAME = unicode("output_method")

    def __init__(self):
        super(OutputMethodField, self).__init__(self.LABEL, self.NAME)


class CategoryTagsField(Field):

    LABEL = unicode("Categories")
    NAME = unicode("category_tags")

    def __init__(self):
        super(CategoryTagsField, self).__init__(self.LABEL, self.NAME)


class IndustryTagsField(Field):

    LABEL = unicode("Industries")
    NAME = unicode("industry_tags")

    def __init__(self):
        super(IndustryTagsField, self).__init__(self.LABEL, self.NAME)


class SkillTagsField(Field):

    LABEL = unicode("Skills")
    NAME = unicode("skill_tags")

    def __init__(self):
        super(SkillTagsField, self).__init__(self.LABEL, self.NAME)


class EquipmentTagsField(Field):

    LABEL = unicode("Equipment")
    NAME = unicode("equipment_tags")

    def __init__(self):
        super(EquipmentTagsField, self).__init__(self.LABEL, self.NAME)


class FirstNameField(Field):

    LABEL = unicode("First Name")
    NAME = unicode("first_name")

    def __init__(self):
        super(FirstNameField, self).__init__(self.LABEL, self.NAME)


class LastNameField(Field):

    LABEL = unicode("Last Name")
    NAME = unicode("last_name")

    def __init__(self):
        super(LastNameField, self).__init__(self.LABEL, self.NAME)


class EmailField(Field):

    LABEL = unicode("Email")
    NAME = unicode("email")

    _VALUE_PLACEHOLDER = unicode("Enter a valid email address...")

    def __init__(self):
        super(EmailField, self).__init__(self.LABEL, self.NAME)


class CreditCardField(Field):

    LABEL = unicode("Credit Card")
    NAME = unicode("card_number")

    def __init__(self):
        super(CreditCardField, self).__init__(self.LABEL, self.NAME)


class ExpiryMonthField(Field):

    LABEL = unicode("Exp Month")
    NAME = unicode("card_expiry_month")

    def __init__(self):
        super(ExpiryMonthField, self).__init__(self.LABEL, self.NAME)


class ExpiryYearField(Field):

    LABEL = unicode("Exp Year")
    NAME = unicode("card_expiry_year")

    def __init__(self):
        super(ExpiryYearField, self).__init__(self.LABEL, self.NAME)


class CVCField(Field):

    LABEL = unicode("CVC")
    NAME = unicode("card_cvc")

    def __init__(self):
        super(CVCField, self).__init__(self.LABEL, self.NAME)
