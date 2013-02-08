"""
    Alpha Sign Up Components
    ------------------------

    All the reusable components for the alpha sign up series.

"""
from view.elementary.components import NonRoutingAnchor
from view.elementary.html import Div, Section
from view.app.base.components import Grid


class ContactAnchor(Div):

    CONTACT_ANCHOR = "contact-anchor"

    # FIXME: Put this somewhere else.
    ANCHOR_TEXT = "Contact Us"
    MAIL_TO_LINK = "mailto:alpha@sendjack.com"


    def __init__(self):
        super(ContactAnchor, self).__init__()

        self.append_class(self.CONTACT_ANCHOR)

        anchor = NonRoutingAnchor(
                {"href": self.MAIL_TO_LINK},
                self.ANCHOR_TEXT)
        self.append_child(anchor)


class AltSection(Section):

    """Alpha Sign Up Series main container."""

    ALT_SECTION = "alt-section"


    def __init__(self, right_grid):
        super(AltSection, self).__init__()
        self.append_class(self.ALT_SECTION)

        self.append_child(LeftGrid())
        self.append_child(right_grid)


class LeftGrid(Grid):

    LEFT_GRID = "left-grid"
    COMPUTER_IMAGE = "computer-image"


    def __init__(self):
        super(LeftGrid, self).__init__()
        self.append_class(self.LEFT_GRID)

        computer_image = Div()
        computer_image.append_class(self.COMPUTER_IMAGE)

        self.append_child(computer_image)


class RightGrid(Grid):

    RIGHT_GRID = "right-grid"
    TITLE = "title"


    def __init__(self):
        super(RightGrid, self).__init__()
        self.append_class(self.RIGHT_GRID)

        title_image = Div()
        self._set_title_image_class(title_image)
        # FIXME: make this work with TitledGrid / Title
        title_image.append_class(self.TITLE)
        self.append_child(title_image)

        self._set_grid_elements()

        self.append_child(ContactAnchor())


    def _set_title_image_class(self, title_image_div):
        raise NotImplementedError("Subclass must override.")


    def _set_grid_elements(self):
        raise NotImplementedError("Subclass must override.")
