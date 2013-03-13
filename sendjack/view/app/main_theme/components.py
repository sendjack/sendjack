"""
    Components for Main Theme
    -------------------------

    All the reusable components for the main theme.

"""
from view.elementary.html import Section
from view.app.base.components import TitledGrid


class MainSection(Section):

    MAIN_SECTION_CLASS = unicode("main-section")

    def __init__(self, grids):
        super(MainSection, self).__init__()
        self.append_class(self.MAIN_SECTION_CLASS)

        for grid in grids:
            self.append_child(grid)


class MainGrid(TitledGrid):

    MAIN_GRID_CLASS = unicode("main-grid")

    def __init__(self, title_str):
        super(MainGrid, self).__init__(title_str)
        self.append_class(self.MAIN_GRID_CLASS)
