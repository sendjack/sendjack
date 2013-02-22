"""
    Main Pages
    ----------

    All the Pages for the Main series.
    <div class="page">

"""
from view.elementary.html import SubmitButton, Div, Img

from view.app.base.page import Page
from view.app.base.components import Field, FieldList, Grid, ObjectView, Title
from view.app.base.components import BigField

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
                        "name",
                        "James Marsh"),
                Field(
                        "Rating",
                        "rating",
                        "All of Stars"),
                Field(
                        "Details / Notes",
                        "notes",
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


    def __init__(self):
        super(TaskInstancePostContrastSection, self).__init__()

        self.append_child(TaskInstanceGrid())
        self.append_child(CreditCardGrid())
        self.append_child(ThankYouGrid())


class TaskInstanceGrid(Grid):

    TASK_INSTANCE_GRID_CLASS = unicode("task-instance-grid")
    TASK_INSTANCE_GRID_ID = unicode("task-instance-grid")
    TASK_INSTANCE_ID = unicode("instance")
    WELCOME_TEXT = unicode(
            "We checked out a number of tasks like yours that went "
            "well, and fine-tuned your description. We've also suggested a "
            "price below.")
    POST_TASK_TEXT = unicode("Save")
    POST_TITLE = unicode("Post Your Task")

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
                        "customer_title",
                        ""),
                BigField(
                        "Steps:",
                        "customer_description",
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

        task_instance_view.append_child(Title(self.POST_TITLE))
        task_instance_view.append_child(welcome_div)
        task_instance_view.append_child(FieldList(fields))
        task_instance_view.append_child(SubmitButton(self.POST_TASK_TEXT))
        self.append_child(task_instance_view)


class CreditCardGrid(Grid):

    CREDIT_CARD_GRID_CLASS = unicode("credit-card-grid")
    CREDIT_CARD_GRID_ID = unicode("credit-card-grid")
    CUSTOMER_ID = "customer"
    WELCOME_TEXT = unicode(
            "Register your credit card to finish signing up for "
            "Jackalope. You will not be charged until you're satisfied "
            "with the work.")
    POST_TASK_TEXT = unicode("Send Jack")
    POST_TITLE = unicode("Post Your Task")

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
                        "card_number",
                        ""),
                Field(
                        "Exp Month",
                        "card_expiry_month",
                        ""),
                Field(
                        "Exp Year",
                        "card_expiry_year",
                        ""),
                Field(
                        "CVC:",
                        "card_cvc",
                        "")
                ]

        customer_view.append_child(Title(self.POST_TITLE))
        customer_view.append_child(welcome_div)
        customer_view.append_child(FieldList(fields))
        customer_view.append_child(SubmitButton(self.POST_TASK_TEXT))
        self.append_child(customer_view)


class ThankYouGrid(Grid):
    THANK_YOU_GRID_CLASS = unicode("thank-you-grid")
    THANK_YOU_GRID_ID = unicode("thank-you-grid")
    MAIN_TITLE = unicode("Thanks!")
    SUB_TEXT = unicode("We're on it. We'll let you know when it's done.")
    IMG_SOURCE = "/static/images/jackalope.jpg"

    def __init__(self):
        super(ThankYouGrid, self).__init__()
        self.append_class(self.THANK_YOU_GRID_CLASS)

        self.set_id(self.THANK_YOU_GRID_ID)

        main_title = Title(self.MAIN_TITLE)

        sub_div = Div()
        sub_div.set_text(self.SUB_TEXT)

        img = Img(self.IMG_SOURCE, "")

        self.append_child(main_title)
        self.append_child(sub_div)
        self.append_child(img)