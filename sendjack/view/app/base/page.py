"""
    Base <div class="page"> framework
    ---------------------------------

    Provide basic page to subclass from.

"""
from view.elementary.html import Div


class Page(Div):

    PAGE = unicode("page")

    def __init__(self):
        super(Page, self).__init__()

        self.append_class(self.PAGE)
