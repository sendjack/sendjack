"""
    Base <body> framework
    ---------------------

    Provide several body structures to subclass from.

"""
from view.elementary.html import Body, Div, Header

from view.app.base.components import ContactAnchor


class AppBody(Body):

    """The standard <body>.

    Attributes
    ----------
    page_container : Element

    """


    def __init__(self):
        super(AppBody, self).__init__()

        self.set_header()

        self.append_child(PageContainer(self._construct_pages()))

        self.set_footer()


    def _construct_pages(self):
        return []

    def set_header(self):
        self.append_child(AppHeader())


    def set_footer(self):
        pass


class AppHeader(Header):

    """The standard <header> section."""

    APP_HEADER_ID = unicode("app-header")
    APP_LOGO_CLASS = unicode("app-logo")

    def __init__(self):
        super(AppHeader, self).__init__()
        self.set_id(self.APP_HEADER_ID)

        # inner_wrapper = InnerWrapper()

        main_logo = Div()
        main_logo.append_class(self.APP_LOGO_CLASS)

        # inner_wrapper.append_child(main_logo)
        #inner_wrapper.append_child(contact_link)
        # self.append_child(inner_wrapper)
        self.append_child(main_logo)
        self.append_child(AppMenu())


class AppMenu(Div):

    """A menu for the app header."""

    APP_MENU_ID = unicode("app-menu")
    CONTACT_US_LINK = unicode("mailto:contact@sendjack.com")
    CONTACT_US_TEXT = unicode("Contact Us")

    def __init__(self):
        super(AppMenu, self).__init__()
        self.set_id(self.APP_MENU_ID)

        self.append_child(ContactAnchor())


class PageContainer(Div):

    """A generic <div id="page-container" class="content"> section.

    Attributes
    ----------
    pages : list

    """

    PAGE_CONTAINER_ID = unicode("page-container")
    CONTENT_CLASS = unicode("content")

    def __init__(self, pages):
        super(PageContainer, self).__init__()
        self.pages = pages
        self.set_id(self.PAGE_CONTAINER_ID)

        self.append_class(self.CONTENT_CLASS)

        for page in self.pages:
            self.append_child(page)


class HeadlessBody(Body):

    """The alternative <body> section."""

    def set_header(self):
        # Don't use a header.
        pass
