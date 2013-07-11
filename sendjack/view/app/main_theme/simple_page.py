"""
    Pages for Simple Series
    -----------------------

    <div class="page simple-page">

"""
from view.elementary.html import Div, Section, UL

from view.app.base.page import Page


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

    _HEADER_TEXT = unicode("We do your research and administrative tasks.")
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
        header = Div()
        header.set_text(self._HEADER_TEXT)
        main_column.append_child(header)

        # TODO: Insert any other text and email sign up

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
