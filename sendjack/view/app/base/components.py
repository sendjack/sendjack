"""
    Base Components
    ---------------

    Components that are to be reused across styles.

"""
from view.elementary.html import Section, Div, TextInput


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

    GRID = "grid"


    def __init__(self):
        super(Grid, self).__init__()

        self.append_class(self.GRID)


class Title(Div):


    TITLE = "title"


    def __init__(self, title_str):
        super(Title, self).__init__()

        self.append_class(self.TITLE)
        self.set_text(title_str)


class Line(Div):

    LINE = "line"


    def __init__(self, line_str):
        super(Line, self).__init__()
        self.append_class(self.LINE)

        self.set_text(line_str)


class DatePicker(TextInput):

    DATE_PICKER = "datepicker"


    def __init__(self, name, value=""):
        super(DatePicker, self).__init__(name, value)
        self.append_class(self.DATE_PICKER)
