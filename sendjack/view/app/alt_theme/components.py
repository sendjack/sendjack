"""
    Alt Components
    ---------------

    All the reusable components for the main views.

"""
from view.elementary.html import Section


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
