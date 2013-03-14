"""
    Base Components
    ---------------

    Components that are to be reused across styles.

"""
from view.elementary.html import Div, TextInput
from view.elementary.components import NonRoutingAnchor


class Grid(Div):

    """Grid imitates bootstrap grid -- think of it like a layout cellblock."""

    GRID_CLASS = "grid"

    def __init__(self):
        super(Grid, self).__init__()
        self.append_class(self.GRID_CLASS)

        self._set_grid_elements()


    def _set_grid_elements(self):
        raise NotImplementedError("Subclass must override.")


class TitledGrid(Grid):

    def __init__(self, title_str):
        super(TitledGrid, self).__init__()
        self.insert_child(Title(title_str))


class ContactAnchor(Div):

    CONTACT_ANCHOR_CLASS = unicode("contact-anchor")

    # FIXME: Put this somewhere else.
    ANCHOR_TEXT = unicode("Contact Us")
    MAIL_TO_LINK = unicode("mailto:alpha@sendjack.com")


    def __init__(self):
        super(ContactAnchor, self).__init__()

        self.append_class(self.CONTACT_ANCHOR_CLASS)

        anchor = NonRoutingAnchor(
                {"href": self.MAIL_TO_LINK},
                self.ANCHOR_TEXT)
        self.append_child(anchor)


class Title(Div):

    TITLE_CLASS = unicode("title")

    def __init__(self, title_str):
        super(Title, self).__init__()
        self.append_class(self.TITLE_CLASS)

        self.set_text(title_str)


class Line(Div):

    LINE_CLASS = unicode("line")

    def __init__(self, line_str):
        super(Line, self).__init__()
        self.append_class(self.LINE_CLASS)

        self.set_text(line_str)


class DatePicker(TextInput):

    DATE_PICKER_CLASS = "datepicker"

    def __init__(self, name, value=""):
        super(DatePicker, self).__init__(name, value)
        self.append_class(self.DATE_PICKER_CLASS)
