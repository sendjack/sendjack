"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section

from view.app.base.components import Grid, Title


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


class TitledGrid(Grid):

    """A Grid with a Title at the top."""

    def __init__(self, title_str):
        super(TitledGrid, self).__init__()

        self.append_child(Title(title_str))
