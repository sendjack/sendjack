"""
    Main Pages
    ----------

    All the Pages for the Main series.
    <div class="page">

"""
from view.elementary.html import SubmitButton

from view.app.base.page import Page
from view.app.base.components import Field, FieldList, Grid

from components import NormalSection, ContrastSection, TitledGrid


class TemplateNewPage(Page):

    TEMPLATE_NEW_PAGE_CLASS = unicode("template-new-page")

    def __init__(self):
        super(TemplateNewPage, self).__init__()
        self.append_class(self.TEMPLATE_NEW_PAGE_CLASS)

        self.append_child(TemplateNewNormalSection())
        self.append_child(TemplateNewContrastSection())


class TemplateNewNormalSection(NormalSection):

    def __init__(self):
        super(TemplateNewNormalSection, self).__init__()

        self.append_child(MainGrid())
        self.append_child(PostGrid())


class MainGrid(TitledGrid):

    MAIN_GRID_CLASS = unicode("main-grid")
    MAIN_TITLE = unicode("New Template")

    def __init__(self):
        super(MainGrid, self).__init__(self.MAIN_TITLE)
        self.append_class(self.MAIN_GRID_CLASS)

        fields = [
                Field(
                        "Name",
                        "title",
                        "Find me 20 CEOs."),
                Field(
                        "Creator",
                        "creator",
                        "Cassandra Orion"),
                Field(
                        "Steps",
                        "steps",
                        "Make a list of steps"),
                Field(
                        "Custom Prop",
                        "custom-prop",
                        "TODO"),
                Field(
                        "Output Type",
                        "output-type",
                        "xls"),
                Field(
                        "Output Method",
                        "output-method",
                        "Email")
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)


class PostGrid(Grid):

    POST_GRID_CLASS = unicode("post-grid")
    CREATE_TEMPLATE = unicode("Create Template")

    def __init__(self):
        super(PostGrid, self).__init__()
        self.append_class(self.POST_GRID_CLASS)

        self.append_child(SubmitButton(self.CREATE_TEMPLATE))


class TemplateNewContrastSection(ContrastSection):

    def __init__(self):
        super(TemplateNewContrastSection, self).__init__()

        self.append_child(DetailsGrid())
        self.append_child(WorkerGrid())
        self.append_child(TagsGrid())


class DetailsGrid(TitledGrid):

    DETAILS_GRID_CLASS = unicode("details-grid")
    DETAILS_TITLE = unicode("Details")

    def __init__(self):
        super(DetailsGrid, self).__init__(self.DETAILS_TITLE)
        self.append_class(self.DETAILS_GRID_CLASS)

        fields = [
                Field(
                        "Price",
                        "price",
                        "$15-$25"),
                Field(
                        "Overhead",
                        "overhead",
                        "5 Minutes"),
                Field(
                        "Interactions",
                        "interactions",
                        "1 Email"),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)


class WorkerGrid(TitledGrid):

    WORKER_GRID_CLASS = unicode("worker-grid")
    WORKER_TITLE = unicode("Worker")

    def __init__(self):
        super(WorkerGrid, self).__init__(self.WORKER_TITLE)
        self.append_class(self.WORKER_GRID_CLASS)

        fields = [
                Field(
                        "Name",
                        "worker-name",
                        "Jame Marsh"),
                Field(
                        "Rating",
                        "rating",
                        ""),
                Field(
                        "Details / Notes",
                        "details",
                        ""),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)


class TagsGrid(TitledGrid):

    TAGS_GRID_CLASS = unicode("tags-grid")
    TAGS_TITLE = unicode("Tags")

    def __init__(self):
        super(TagsGrid, self).__init__(self.TAGS_TITLE)
        self.append_class(self.TAGS_GRID_CLASS)

        fields = [
                Field(
                        "Category",
                        "category",
                        "Market Research"),
                Field(
                        "Industry",
                        "industry",
                        "Finance, Health Care"),
                Field(
                        "Skills",
                        "skills",
                        "Internet Research"),
                Field(
                        "Equipment",
                        "equipment",
                        "Camera"),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)
