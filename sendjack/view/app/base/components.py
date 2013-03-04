"""
    Base Components
    ---------------

    Components that are to be reused across styles.

"""
from view.elementary.html import Section, Div, TextInput, Label, UL, Textarea
from view.elementary.html import Form


class InnerWrapper(Div):

    """An Inner Wrapper that can we used to align margins between elements."""

    INNER_WRAPPER = "inner-wrapper"

    def __init__(self):
        super(InnerWrapper, self).__init__()

        self.append_class(self.INNER_WRAPPER)


class InnerWrapperSection(Section):

    """The Standard Jackalope Section, which has an inner wrapper to do
    something clever with page margins."""

    # TODO: Investigate why this is necessary.

    def __init__(self, el=None):
        super(InnerWrapperSection, self).__init__()

        inner_wrapper = InnerWrapper()
        if el:
            inner_wrapper.append_child(el)

        self.append_child(inner_wrapper)


class Grid(Div):

    """Grid imitates bootstrap grid -- think of it like a layout cellblock."""

    GRID_CLASS = "grid"

    def __init__(self):
        super(Grid, self).__init__()
        self.append_class(self.GRID_CLASS)


class Title(Div):

    TITLE_CLASS = "title"

    def __init__(self, title_str):
        super(Title, self).__init__()
        self.append_class(self.TITLE_CLASS)

        self.set_text(title_str)


class Line(Div):

    LINE_CLASS = "line"

    def __init__(self, line_str):
        super(Line, self).__init__()
        self.append_class(self.LINE_CLASS)

        self.set_text(line_str)


class DatePicker(TextInput):

    DATE_PICKER_CLASS = "datepicker"

    def __init__(self, name, value=""):
        super(DatePicker, self).__init__(name, value)
        self.append_class(self.DATE_PICKER_CLASS)


class Field(Div):

    FIELD_CLASS = unicode("field")
    KEY_CLASS = unicode("key")
    VALUE_CLASS = unicode("value")

    _label_el = None
    _input_el = None

    def __init__(self, label, name, value=""):
        super(Field, self).__init__()
        self.append_class(self.FIELD_CLASS)

        # assemble label
        self._label_el = Label(label, name)
        self._label_el.append_class(self.KEY_CLASS)

        # assemble input
        self._input_el = TextInput(name, value)
        self._input_el.append_class(self.VALUE_CLASS)

        self.append_child(self._label_el)
        self.append_child(self._input_el)


class BigField(Div):

    BIG_FIELD_CLASS = unicode("big-field")
    FIELD_CLASS = unicode("field")
    KEY_CLASS = unicode("key")
    VALUE_CLASS = unicode("value")
    DEFAULT_NUM_ROWS = 7

    _label_el = None
    _input_el = None

    def __init__(self, label, name, value=""):
        super(BigField, self).__init__()
        self.append_class(self.FIELD_CLASS)
        self.append_class(self.BIG_FIELD_CLASS)

        # assemble label
        self._label_el = Label(label, name)
        self._label_el.append_class(self.KEY_CLASS)

        # assemble input
        self._input_el = Textarea(name, value)
        self._input_el.append_class(self.VALUE_CLASS)
        self._input_el.set_rows(self.DEFAULT_NUM_ROWS)

        self.append_child(self._label_el)
        self.append_child(self._input_el)


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


class Paragraph(Div):

    PARAGRAPH_CLASS = unicode("paragraph")

    def __init__(self):
        super(Paragraph, self).__init__()
        self.append_class(self.PARAGRAPH_CLASS)


class ObjectView(Form):

    """Provide a view that corresponds to a model object. Provide a framework
    for coordinating the javascript Model/View classes."""

    OBJECT_VIEW_CLASS = "object-view"

    def __init__(self, object_id):
        super(ObjectView, self).__init__(object_id)
        self.append_class(self.OBJECT_VIEW_CLASS)

        self.set_id(object_id)
