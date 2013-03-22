"""
    Components for Main Theme
    -------------------------

    All the reusable components for the main theme.

"""
from jutil.errors import OverrideRequiredError

from view.elementary.html import Section
from view.app.base.components import TitledGrid


class MainSection(Section):

    _MAIN_SECTION_CLASS = unicode("main-section")

    def __init__(self, grids):
        super(MainSection, self).__init__()
        self.append_class(self._MAIN_SECTION_CLASS)

        for grid in grids:
            self.append_child(grid)


class MainGrid(TitledGrid):

    _MAIN_GRID_CLASS = unicode("main-grid")

    def __init__(self, title):
        super(MainGrid, self).__init__(title)
        self.append_class(self._MAIN_GRID_CLASS)


    def _append_grid_elements(self):
        self._append_subtitles()
        self._append_form()


    def _append_form(self):
        self.append_child(self._construct_form())


    def _construct_form(self):
        raise OverrideRequiredError()
