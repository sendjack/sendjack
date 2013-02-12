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


class TaskTemplatePage(Page):

    TEMPLATE_NEW_PAGE_CLASS = unicode("template-new-page")
    TEMPLATE_ID = "template"

    def __init__(self):
        super(TaskTemplatePage, self).__init__()
        self.append_class(self.TEMPLATE_NEW_PAGE_CLASS)
        self.set_id(self.TEMPLATE_ID)

        self.append_child(TaskNormalSection())
        self.append_child(TaskContrastSection())


class TaskNormalSection(NormalSection):

    def __init__(self):
        super(TaskNormalSection, self).__init__()

        self.append_child(MainGrid())
        self.append_child(PostGrid())


class TaskInstancePage(Page):

    #INSTANCE_NEW_PAGE_CLASS = unicode("instance-new-page")
    INSTANCE_ID = unicode("instance")

    def __init__(self):
        super(TaskInstancePage, self).__init__()
        #self.append_class(self.INSTANCE_NEW_PAGE_CLASS)
        self.set_id(self.INSTANCE_ID)

        self.append_child(TaskNormalSection())
        self.append_child(TaskContrastSection())


class MainGrid(TitledGrid):

    MAIN_GRID_CLASS = unicode("main-grid")
    MAIN_TITLE = unicode("New Template")

    def __init__(self):
        super(MainGrid, self).__init__(self.MAIN_TITLE)
        self.append_class(self.MAIN_GRID_CLASS)

        fields = [
                Field(
                        "ID",
                        "id",
                        ""),
                Field(
                        "Name",
                        "name",
                        ""),

                Field(
                        "Creator",
                        "creator_id",
                        ""),
                Field(
                        "Steps",
                        "steps",
                        ""),
                Field(
                        "Custom Prop",
                        "custom_properties",
                        ""),
                Field(
                        "Output Type",
                        "output_type",
                        ""),
                Field(
                        "Output Method",
                        "output_method",
                        "")
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


class TaskContrastSection(ContrastSection):

    def __init__(self):
        super(TaskContrastSection, self).__init__()

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
                        "Min Price",
                        "min_price",
                        ""),
                Field(
                        "Max Price",
                        "max_price",
                        ""),
                Field(
                        "Min Overhead",
                        "min_overhead",
                        ""),
                Field(
                        "Max Overhead",
                        "max_overhead",
                        ""),
                Field(
                        "Min Interactions",
                        "min_interactions",
                        ""),
                Field(
                        "Max Interactions",
                        "max_interactions",
                        ""),
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
                        "",
                        "James Marsh"),
                Field(
                        "Rating",
                        "All of Stars",
                        ""),
                Field(
                        "Details / Notes",
                        "",
                        "This Grid isn't hooked up to anything."),
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
                        "category_tags",
                        ""),
                Field(
                        "Industry",
                        "industry_tags",
                        ""),
                Field(
                        "Skills",
                        "skills_tags",
                        ""),
                Field(
                        "Equipment",
                        "equipment_tags",
                        ""),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)
