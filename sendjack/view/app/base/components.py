"""
    Base Components
    ---------------

    Components that are to be reused across styles.

"""
from view.elementary.html import Section, Div, TextInput, Label, UL


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

    def __init__(self, label, key, value=""):
        super(Field, self).__init__()
        self.append_class(self.FIELD_CLASS)

        key = Label(label, key)
        value = TextInput(key, value)

        key.append_class(self.KEY_CLASS)
        value.append_class(self.VALUE_CLASS)

        self.append_child(key)
        self.append_child(value)


class FieldList(UL):

    FIELD_LIST_CLASS = unicode("field-list")

    def __init__(self, fields):
        super(FieldList, self).__init__(fields)
        self.append_class(self.FIELD_LIST_CLASS)
