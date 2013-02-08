"""
    Alpha Sign Up Components
    ------------------------

    All the reusable components for the alpha sign up series.

"""
from view.elementary.components import NonRoutingAnchor
from view.elementary.html import Div, Section
from view.app.base.components import Grid


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


class AltSection(Section):

    """Alpha Sign Up Series main container."""

    ALT_SECTION_CLASS = unicode("alt-section")

    def __init__(self, right_grid):
        super(AltSection, self).__init__()
        self.append_class(self.ALT_SECTION_CLASS)

        self.append_child(LeftGrid())
        self.append_child(right_grid)


class LeftGrid(Grid):

    LEFT_GRID_CLASS = unicode("left-grid")
    COMPUTER_IMAGE_CLASS = unicode("computer-image")

    def __init__(self):
        super(LeftGrid, self).__init__()
        self.append_class(self.LEFT_GRID_CLASS)

        computer_image = Div()
        computer_image.append_class(self.COMPUTER_IMAGE_CLASS)

        self.append_child(computer_image)


class RightGrid(Grid):

    RIGHT_GRID_CLASS = unicode("right-grid")
    TITLE_CLASS = unicode("title")

    def __init__(self):
        super(RightGrid, self).__init__()
        self.append_class(self.RIGHT_GRID_CLASS)

        title_image = Div()
        self._set_title_image_class(title_image)
        # FIXME: make this work with TitledGrid / Title
        title_image.append_class(self.TITLE_CLASS)
        self.append_child(title_image)

        self._set_grid_elements()

        self.append_child(ContactAnchor())


    def _set_title_image_class(self, title_image_div):
        raise NotImplementedError("Subclass must override.")


    def _set_grid_elements(self):
        raise NotImplementedError("Subclass must override.")
