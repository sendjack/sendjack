"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.app.base.components import InnerWrapperSection, Grid, Title


class NormalSection(InnerWrapperSection):


    NORMAL_SECTION = "normal-section"


    def __init__(self, el=None):
        super(NormalSection, self).__init__(el)

        self.append_class(self.NORMAL_SECTION)


class ContrastSection(InnerWrapperSection):


    NORMAL_SECTION = "contrast-section"


    def __init__(self, el=None):
        super(NormalSection, self).__init__(el)

        self.append_class(self.CONTRAST_SECTION)


class TitledGrid(Grid):

    """A Grid with a Title at the top."""


    def __init__(self, title_str):
        super(TitledGrid, self).__init__()

        self.append_child(Title(title_str))
