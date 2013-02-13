"""
    Main Pages
    ----------

    All the Pages for the Main series.
    <div class="page">

"""
from view.elementary.html import SubmitButton, Div

from view.app.base.page import Page
from view.app.base.components import Field, FieldList, Grid, ObjectView, Title

from components import NormalSection, ContrastSection, TitledGrid


class TaskTemplatePage(Page):

    TEMPLATE_NEW_PAGE_CLASS = unicode("template-new-page")
    TEMPLATE_ID = "template"

    def __init__(self):
        super(TaskTemplatePage, self).__init__()
        self.append_class(self.TEMPLATE_NEW_PAGE_CLASS)

        template_view = ObjectView(self.TEMPLATE_ID)
        template_view.append_child(TaskTemplateNormalSection())
        template_view.append_child(TaskTemplateContrastSection())

        self.append_child(template_view)


class TaskTemplateNormalSection(NormalSection):

    def __init__(self):
        super(TaskTemplateNormalSection, self).__init__()

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
                        "ID",
                        "id",
                        ""),
                Field(
                        "Title",
                        "title",
                        ""),

                #Field(
                #        "Creator",
                #        "creator_id",
                #        ""),
                Field(
                        "Steps",
                        "steps",
                        ""),
                #Field(
                #        "Custom Prop",
                #        "custom_properties",
                #        ""),
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


class TaskTemplateContrastSection(ContrastSection):

    def __init__(self):
        super(TaskTemplateContrastSection, self).__init__()

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

        self.append_child(FieldList(fields))


class TaskInstancePostPage(Page):

    TASK_INSTANCE_POST_PAGE_CLASS = unicode("task-instance-post-page")

    def __init__(self):
        super(TaskInstancePostPage, self).__init__()
        self.append_class(self.TASK_INSTANCE_POST_PAGE_CLASS)

        self.append_child(TaskInstancePostContrastSection())


class TaskInstancePostContrastSection(ContrastSection):

    POST_TITLE = unicode("Post your Task")
    POST_TASK_TEXT = unicode("Post Task")
    GRID_CONTAINER = unicode("grid-container")

    def __init__(self):
        super(TaskInstancePostContrastSection, self).__init__()

        grid_container = Div()
        grid_container.append_class(self.GRID_CONTAINER)

        grid_container.append_child(TaskInstanceGrid())
        grid_container.append_child(CreditCardGrid())

        self.append_child(Title(self.POST_TITLE))
        self.append_child(grid_container)
        self.append_child(SubmitButton(self.POST_TASK_TEXT))


class TaskInstanceGrid(Grid):

    TASK_INSTANCE_GRID_CLASS = unicode("task-instance-grid")
    TASK_INSTANCE_GRID_ID = unicode("task-instance-grid")
    TASK_INSTANCE_ID = unicode("instance")
    WELCOME_TEXT = unicode("Hi! Here's your task details and pricing.")

    def __init__(self):
        super(TaskInstanceGrid, self).__init__()
        self.append_class(self.TASK_INSTANCE_GRID_CLASS)

        self.set_id(self.TASK_INSTANCE_GRID_ID)

        task_instance_view = ObjectView(self.TASK_INSTANCE_ID)
        welcome_div = Div()
        welcome_div.set_text(self.WELCOME_TEXT)
        fields = [
                Field(
                        "Task:",
                        "steps",
                        ""),
                Field(
                        "Deadline:",
                        "deadline_ts",
                        ""),
                Field(
                        "Price:",
                        "price",
                        "")
                ]

        task_instance_view.append_child(welcome_div)
        task_instance_view.append_child(FieldList(fields))
        self.append_child(task_instance_view)


class CreditCardGrid(Grid):

    CREDIT_CARD_GRID_CLASS = unicode("credit-card-grid")
    CREDIT_CARD_GRID_ID = unicode("credit-card-grid")
    CUSTOMER_ID = "customer"
    WELCOME_TEXT = unicode(
            "Now we just need your Billing Info and we're all set!")

    def __init__(self):
        super(CreditCardGrid, self).__init__()
        self.append_class(self.CREDIT_CARD_GRID_CLASS)

        self.set_id(self.CREDIT_CARD_GRID_ID)

        customer_view = ObjectView(self.CUSTOMER_ID)
        welcome_div = Div()
        welcome_div.set_text(self.WELCOME_TEXT)

        fields = [
                Field(
                        "First Name:",
                        "first_name",
                        ""),
                Field(
                        "Last Name:",
                        "last_name",
                        ""),
                Field(
                        "Email:",
                        "email",
                        ""),
                Field(
                        "Credit Card:",
                        "credit-card",
                        ""),
                Field(
                        "Exp:",
                        "expiration-date",
                        ""),
                Field(
                        "CVC:",
                        "cvc",
                        "")
                ]

        customer_view.append_child(welcome_div)
        customer_view.append_child(FieldList(fields))
        self.append_child(customer_view)
