"""
    Base <body> framework
    ---------------------

    Provide several body structures to subclass from.

"""
from view.elementary.html import Body, Div, Header

from components import InnerWrapper


class MainBody(Body):

    """The standard <body> layout."""

    MAIN_CONTENT = "main-content"


    def __init__(self):
        super(MainBody, self).__init__()

        header = MainHeader()
        content = ContentDiv()
        content.append_class(self.MAIN_CONTENT)

        for page in self._construct_pages():
            content.append_child(page)

        self.append_child(header)
        self.append_child(content)


    def _construct_pages(self):
        return []


class MainHeader(Header):

    """The standard <header> section."""

    MAIN_LOGO = unicode("main-logo")
    MAIN_LETTERING = unicode("main-lettering")


    def __init__(self):
        super(MainHeader, self).__init__()

        inner_wrapper = InnerWrapper()

        main_logo = Div()
        main_logo.append_class(self.MAIN_LOGO)

        main_lettering = Div()
        main_lettering.append_class(self.MAIN_LETTERING)

        inner_wrapper.append_child(main_logo)
        inner_wrapper.append_child(main_lettering)
        self.append_child(inner_wrapper)


class AltBody(Body):

    """The alternative <body> section."""

    ALT_CONTENT = "alt-content"


    def __init__(self):
        super(AltBody, self).__init__()

        content = ContentDiv()
        content.append_class(self.ALT_CONTENT)

        for page in self._construct_pages():
            content.append_child(page)

        self.append_child(content)


    def _construct_pages(self):
        return []


class ContentDiv(Div):

    """A generic <div class="content"> section."""

    CONTENT = unicode("content")

    def __init__(self):
        super(ContentDiv, self).__init__()

        self.append_class(self.CONTENT)
