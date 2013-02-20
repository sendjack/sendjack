"""
    Main Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section, HiddenInput

from view.app.base.components import Grid, Title, HeadField, SubField


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


class StepsField(HeadField):

    STEPS_LABEL = unicode("Steps")
    STEPS_KEY = unicode("steps")
    STEPS_CLASS = unicode("steps")

    def __init__(self, value=""):
        super(StepsField, self).__init__(self.STEPS_LABEL, self.STEPS_KEY)
        self.append_class(self.STEPS_CLASS)
        self.append_child(HiddenInput(self.STEPS_KEY))


class StepField(SubField):

    STEP_LABEL = unicode("Step")
    STEP_KEY = unicode("step")
    STEP_CLASS = unicode("step")

    def __init__(self, value="", include_index=False):
        super(StepField, self).__init__(
                self.STEP_LABEL,
                self.STEP_KEY,
                value,
                include_index)
        self.append_class(self.STEP_CLASS)
