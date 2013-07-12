"""
    Pages for Simple Series
    -----------------------

    <div class="page simple-page">

"""
from view.elementary.html import Div, Section, UL

from view.app.base.page import Page

from view.app.base.object.customer import CustomerView
from view.app.base.object.field import EmailField


class SimplePage(Page):

    _SIMPLE_PAGE_CLASS = unicode("simple-page")

    def __init__(self):
        super(SimplePage, self).__init__()
        self.append_class(self._SIMPLE_PAGE_CLASS)


class LandingPage(SimplePage):

    _LANDING_PAGE_ID = unicode("landing-page")
    _MARKETING_SECTION_ID = unicode("marketing-section")
    _DELIVERABLES_SECTION_ID = unicode("deliverables-section")
    _MAIN_COLUMN_ID = unicode("main-column")
    _DETAILS_COLUMN_ID = unicode("details-column")

    _TITLE_TEXT = unicode("We do your research and administrative tasks.")
    BENEFITS_TITLE = unicode("Benefits:")
    BENEFITS_BULLETS = [
            unicode("No hiring"),
            unicode("No marketplaces"),
            unicode("No contracts"),
            unicode("Guaranteed work"),
            ]
    TASKS_TITLE = unicode("Common Tasks:")
    TASKS_BULLETS = [
            unicode("Web Research"),
            unicode("Data Entry"),
            unicode("Lead Generation"),
            unicode("Market Research & Reports"),
            unicode("Document Creation"),
            unicode("Transcription"),
            unicode("Translation"),
            ]
    DELIVERABLES_TITLE = unicode("Deliverables:")
    DELIVERABLES_BULLETS = [
            unicode("Spreadsheets"),
            unicode("Documents"),
            unicode("Powerpoints"),
            unicode("Salesforce"),
            unicode("Custom Databases"),
            ]

    def __init__(self):
        super(LandingPage, self).__init__()
        self.set_id(self._LANDING_PAGE_ID)

        self.append_child(self._construct_marketing_section())
        self.append_child(self._construct_deliverables_section())


    def _construct_marketing_section(self):
        section = Section()
        section.set_id(self._MARKETING_SECTION_ID)

        main_column = Div()
        main_column.set_id(self._MAIN_COLUMN_ID)
        main_column.append_child(LandingTitle(self._TITLE_TEXT))
        main_column.append_child(Separator())
        main_column.append_child(LandingCustomerView())

        section.append_child(main_column)

        details_column = Div()
        details_column.set_id(self._DETAILS_COLUMN_ID)
        details_column.append_child(LandingList(
                self.BENEFITS_BULLETS,
                self.BENEFITS_TITLE))
        details_column.append_child(LandingList(
                self.TASKS_BULLETS,
                self.TASKS_TITLE))
        details_column.append_child(LandingList(
                self.DELIVERABLES_BULLETS,
                self.DELIVERABLES_TITLE))
        section.append_child(details_column)

        return section



    def _construct_deliverables_section(self):
        section = Section()
        section.set_id(self._DELIVERABLES_SECTION_ID)

        return section


class LandingTitle(Div):

    _LANDING_TITLE_CLASS = unicode("landing-title")

    def __init__(self, title):
        super(LandingTitle, self).__init__()
        self.append_class(self._LANDING_TITLE_CLASS)

        self.set_text(title)


class LandingList(Div):

    _LANDING_LIST_CLASS = unicode("landing-list")

    def __init__(self, items, title):
        super(LandingList, self).__init__()
        self.append_class(self._LANDING_LIST_CLASS)

        self.append_child(LandingListTitle(title))
        self.append_child(UL(items))


class LandingListTitle(Div):

    _LANDING_LIST_TITLE_CLASS = unicode("landing-list-title")

    def __init__(self, title):
        super(LandingListTitle, self).__init__()
        self.append_class(self._LANDING_LIST_TITLE_CLASS)

        self.set_text(title)


class Separator(Div):

    _SEPARATOR_CLASS = unicode("separator")

    def __init__(self):
        super(Separator, self).__init__()
        self.append_class(self._SEPARATOR_CLASS)


class LandingCustomerView(CustomerView):

    _OBJECT_VIEW_ID = unicode("create-customer")
    _SUBMIT_TEXT = unicode("Sign Up")
    _SIGNUP_TEXT = unicode("Try us out or join our mailing list:")
    _EMAIL_PLACEHOLDER = unicode("Email address")

    def __init__(self):
        super(LandingCustomerView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)

    def _construct_fields(self):
        signup_text = Div()
        signup_text.set_text(self._SIGNUP_TEXT)
        email_input = LandingEmailField()
        email_input.set_placeholder(self._EMAIL_PLACEHOLDER)
        return [
                signup_text,
                email_input
                ]


class LandingEmailField(EmailField):

    def _construct_key(self, key, name):
        return None
