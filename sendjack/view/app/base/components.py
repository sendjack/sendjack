"""
    Base Components
    ---------------

    Components that are to be reused across styles.

"""
from jutil.errors import OverrideRequiredError

from view.elementary.html import Div, TextInput
from view.elementary.components import NonRoutingAnchor


class Grid(Div):

    """Grid imitates bootstrap grid -- think of it like a layout cellblock."""

    _GRID_CLASS = unicode("grid")

    def __init__(self):
        super(Grid, self).__init__()
        self.append_class(self._GRID_CLASS)

        self._append_grid_elements()


    def _append_grid_elements(self):
        raise OverrideRequiredError()


class TitledGrid(Grid):

    _GRID_SUBTITLES = []

    def __init__(self, title):
        super(TitledGrid, self).__init__()

        # because super() appends all the other child grid elements first, use
        # insert_child() to ensure the title is at the top.
        self.insert_child(GridTitle(title))


    def _append_grid_elements(self):
        self._append_subtitles()


    def _append_subtitles(self):
        for subtitle in self._GRID_SUBTITLES:
            self.append_child(GridText(subtitle))


class ContactAnchor(Div):

    _CONTACT_ANCHOR_CLASS = unicode("contact-anchor")

    # TODO: Put this somewhere else.
    _ANCHOR_TEXT = unicode("Contact Us")
    _MAIL_TO_LINK = unicode("mailto:alpha@sendjack.com")


    def __init__(self):
        super(ContactAnchor, self).__init__()
        self.append_class(self._CONTACT_ANCHOR_CLASS)

        # TODO: create subclass MailToAnchor
        anchor = NonRoutingAnchor(
                {"href": self._MAIL_TO_LINK},
                self._ANCHOR_TEXT)
        self.append_child(anchor)


class GridTitle(Div):

    _GRID_TITLE_CLASS = unicode("grid-title")

    def __init__(self, text):
        super(GridTitle, self).__init__()
        self.append_class(self._GRID_TITLE_CLASS)

        self.set_text(text)


class GridText(Div):

    _GRID_TEXT_CLASS = unicode("grid-text")

    def __init__(self, text):
        super(GridText, self).__init__()
        self.append_class(self._GRID_TEXT_CLASS)

        self.set_text(text)


class DatePicker(TextInput):

    _DATE_PICKER_CLASS = "date-picker"

    def __init__(self, name, value=""):
        super(DatePicker, self).__init__(name, value)
        self.append_class(self._DATE_PICKER_CLASS)
