"""
    Pages for Main Theme
    --------------------

    The Standard Pages for the application.
    <div class="page main-page">

"""
from view.elementary.html import TextInput, SubmitButton, Textarea, HiddenInput
from view.app.base.page import Page
from view.app.base.field import FieldList, Field
from view.app.base.components import Line, DatePicker
from view.app.base.object import ObjectView, CustomerView

from .components import MainSection, MainGrid


class MainPage(Page):

    MAIN_PAGE_CLASS = "main-page"

    def __init__(self):
        super(MainPage, self).__init__()
        self.append_class(self.MAIN_PAGE_CLASS)

        main_section = MainSection(self._construct_grids())
        self.append_child(main_section)


    def _construct_grids(self):
        return []


class CreateCustomerPage(MainPage):

    CREATE_CUSTOMER_PAGE_ID = "create-customer-page"

    def __init__(self):
        super(CreateCustomerPage, self).__init__()
        self.set_id(self.CREATE_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CreateCustomerGrid()]


class CreateCustomerGrid(MainGrid):

    CREATE_CUSTOMER_GRID_CLASS = "create-customer-grid"
    CREATE_CUSTOMER_TITLE = "Sign Up"

    LINES = [
            "Great! Now we just need your contact details. We'll holler."
            ]


    def __init__(self):
        super(CreateCustomerGrid, self).__init__(self.CREATE_CUSTOMER_TITLE)
        self.append_class(self.CREATE_CUSTOMER_GRID_CLASS)


    def _set_grid_elements(self):
        for line in self.LINES:
            line_el = Line(line)
            self.append_child(line_el)

        self.append_child(CustomerView())




class CreateInstancePage(MainPage):

    CREATE_INSTANCE_PAGE_ID = unicode("create-instance-page")

    def __init__(self):
        super(CreateInstancePage, self).__init__()
        self.set_id(self.CREATE_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceGrid()]


class CreateInstanceGrid(MainGrid):

    CREATE_INSTANCE_GRID_CLASS = unicode("create-instance-grid")
    CREATE_INSTANCE_TITLE = unicode("New Task")

    def __init__(self):
        super(CreateInstanceGrid, self).__init__(self.CREATE_INSTANCE_TITLE)
        self.append_class(self.CREATE_INSTANCE_GRID_CLASS)


    def _set_grid_elements(self):
        self.append_child(TaskInstanceView())


class TaskInstanceView(ObjectView):

    TASK_INSTANCE_VIEW = "task-instance-view"
    TASK_INSTANCE_ID = "instance"

    # names
    CUSTOMER_TITLE_NAME = "customer_title"
    CUSTOMER_DESCRIPTION_NAME = "customer_description"
    TITLE_NAME = "title"
    INSTRUCTIONS_NAME = "instructions"
    PROPERTIES_NAME = "properties"
    OUTPUT_TYPE_NAME = "output_type"
    OUTPUT_METHOD_NAME = "output_method"
    DEADLINE_NAME = "deadline_ts"
    PRICE_NAME = "price"
    CATEGORY_TAGS_NAME = "category_tags"
    INDUSTRY_TAGS_NAME = "industry_tags"
    SKILL_TAGS_NAME = "skill_tags"
    EQUIPMENT_TAGS_NAME = "equipment_tags"

    # classes
    CUSTOMER_TITLE_CLASS = "customer-title"
    CUSTOMER_DESCRIPTION_CLASS = "customer-description"
    DEADLINE_CLASS = "deadline"

    # placeholder values
    CUSTOMER_TITLE_PLACEHOLDER = "Task Title"
    CUSTOMER_DESCRIPTION_PLACEHOLDER = "Enter Your Task Description"
    DEADLINE_PLACEHOLDER = "06/31/2013"

    TEXTAREA_DEFAULT_ROWS = 4
    SUBMIT_TEXT = "Post Task"

    def __init__(self):
        super(TaskInstanceView, self).__init__(self.TASK_INSTANCE_ID)
        self.append_class(self.TASK_INSTANCE_VIEW)

        # assemble customer title
        customer_title = TextInput(self.CUSTOMER_TITLE_NAME)
        customer_title.append_class(self.CUSTOMER_TITLE_CLASS)
        customer_title.set_placeholder(self.CUSTOMER_TITLE_PLACEHOLDER)

        # assemble customer description
        customer_description = Textarea(self.CUSTOMER_DESCRIPTION_NAME)
        customer_description.append_class(self.CUSTOMER_DESCRIPTION_CLASS)
        customer_description.set_placeholder(
                self.CUSTOMER_DESCRIPTION_PLACEHOLDER)
        customer_description.set_rows(self.TEXTAREA_DEFAULT_ROWS)

        # assemble hidden title, instructions, properties inputs
        title = HiddenInput(self.TITLE_NAME)
        instructions = HiddenInput(self.INSTRUCTIONS_NAME)
        properties = HiddenInput(self.PROPERTIES_NAME)
        output_type = HiddenInput(self.OUTPUT_TYPE_NAME)
        output_method = HiddenInput(self.OUTPUT_METHOD_NAME)

        # assemble deadline
        deadline = DatePicker(self.DEADLINE_NAME)
        deadline.append_class(self.DEADLINE_CLASS)
        deadline.set_placeholder(self.DEADLINE_PLACEHOLDER)

        # assemble hidden price, tags inputs
        price = HiddenInput(self.PRICE_NAME)
        category_tags = HiddenInput(self.CATEGORY_TAGS_NAME)
        industry_tags = HiddenInput(self.INDUSTRY_TAGS_NAME)
        skill_tags = HiddenInput(self.SKILL_TAGS_NAME)
        equipment_tags = HiddenInput(self.EQUIPMENT_TAGS_NAME)

        submit = SubmitButton(self.SUBMIT_TEXT)

        self.append_child(customer_title)
        self.append_child(customer_description)
        self.append_child(title)
        self.append_child(instructions)
        self.append_child(properties)
        self.append_child(output_type)
        self.append_child(output_method)
        self.append_child(deadline)
        self.append_child(price)
        self.append_child(category_tags)
        self.append_child(industry_tags)
        self.append_child(skill_tags)
        self.append_child(equipment_tags)
        self.append_child(submit)


class CreateInstanceThanksPage(MainPage):

    CREATE_INSTANCE_THANKS_PAGE_ID = unicode("create-instance-thanks-page")

    def __init__(self):
        super(CreateInstanceThanksPage, self).__init__()
        self.set_id(self.CREATE_INSTANCE_THANKS_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceThanksGrid()]


class CreateInstanceThanksGrid(MainGrid):

    CREATE_INSTANCE_THANKS_GRID_CLASS = "create-intance-thanks-grid"
    CREATE_INSTANCE_THANKS_TITLE = "Next Steps"

    # TODO: Put somewhere else
    LINES = [
            "Jackalope is on it.",
            "We're processing your task and making sure it looks great.",
            ("Then we'll email you to confirm all the details. "
            "Thanks for trying us out!")
            ]


    def __init__(self):
        super(CreateInstanceThanksGrid, self).__init__(
                self.CREATE_INSTANCE_THANKS_TITLE)
        self.append_class(self.CREATE_INSTANCE_THANKS_GRID_CLASS)


    def _set_grid_elements(self):
        for line in self.LINES:
            line_el = Line(line)
            self.append_child(line_el)


class ConfirmInstancePage(MainPage):

    CONFIRM_INSTANCE_PAGE_ID = unicode("confirm-instance-page")

    def __init__(self):
        super(ConfirmInstancePage, self).__init__()
        self.set_id(self.CONFIRM_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [ConfirmInstanceGrid()]


class ConfirmInstanceGrid(MainGrid):

    CONFIRM_INSTANCE_GRID_CLASS = unicode("confirm-instance-grid")

    WELCOME_TEXT = unicode(
            "We checked out a number of tasks like yours that went "
            "well, and fine-tuned your description. We've also suggested a "
            "price below.")
    CONFIRM_INSTANCE_GRID_TITLE = unicode("Task Details")

    def __init__(self):
        super(ConfirmInstanceGrid, self).__init__(
                self.CONFIRM_INSTANCE_GRID_TITLE)
        self.append_class(self.CONFIRM_INSTANCE_GRID_CLASS)


    def _set_grid_elements(self):
        self.append_child(Line(self.WELCOME_TEXT))
        self.append_child(TaskInstanceView())


class CardCustomerPage(MainPage):

    CARD_CUSTOMER_PAGE_ID = unicode("card-customer-page")

    def __init__(self):
        super(CardCustomerPage, self).__init__()
        self.set_id(self.CARD_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CardCustomerGrid()]


class CardCustomerGrid(MainGrid):

    CARD_CUSTOMER_GRID_CLASS = unicode("card-customer-grid")
    CARD_CUSTOMER_TITLE = unicode("Payment")

    CUSTOMER_ID = "customer"
    WELCOME_TEXT = unicode(
            "Great! Now all we need is your payment details. You'll never be "
            "charged until your task is done and you have approved the work.")
    POST_TASK_TEXT = unicode("Post Task")

    def __init__(self):
        super(CardCustomerGrid, self).__init__(self.CARD_CUSTOMER_TITLE)
        self.append_class(self.CARD_CUSTOMER_GRID_CLASS)


    def _set_grid_elements(self):
        customer_view = ObjectView(self.CUSTOMER_ID)
        welcome_line = Line(self.WELCOME_TEXT)

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

        customer_view.append_child(welcome_line)
        customer_view.append_child(FieldList(fields))
        customer_view.append_child(SubmitButton(self.POST_TASK_TEXT))
        self.append_child(customer_view)


class ConfirmInstanceThanksPage(MainPage):

    CONFIRM_INSTANCE_THANKS_PAGE_ID = unicode("confirm-instance-thanks-page")

    def __init__(self):
        super(ConfirmInstanceThanksPage, self).__init__()
        self.set_id(self.CONFIRM_INSTANCE_THANKS_PAGE_ID)

    def _construct_grids(self):
        return [ConfirmInstanceThanksGrid()]


class ConfirmInstanceThanksGrid(MainGrid):

    CONFIRM_INSTANCE_THANKS_GRID_CLASS = unicode(
            "confirm-instance-thanks-grid")

    CONFIRM_INSTANCE_THANKS_TITLE = unicode("Fill this in.")
    TEXT = unicode("We're on it. We'll let you know when it's done.")

    def __init__(self):
        super(ConfirmInstanceThanksGrid, self).__init__(
                self.CONFIRM_INSTANCE_THANKS_TITLE)
        self.append_class(self.CONFIRM_INSTANCE_THANKS_GRID_CLASS)


    def _set_grid_elements(self):
        self.append_child(Line(self.TEXT))


class ApproveInstancePage(MainPage):

    APPROVE_INSTANCE_PAGE_ID = unicode("approve-instance-page")

    def __init__(self):
        super(ApproveInstancePage, self).__init__()
        self.set_id(self.APPROVE_INSTANCE_PAGE_ID)

    def _construct_grids(self):
        return [ApproveTaskGrid()]


class ApproveTaskGrid(MainGrid):

    APPROVE_TASK_GRID_CLASS = unicode("approve-task-grid")

    TASK_INSTANCE_ID = unicode("instance")
    LINES = [
            unicode("Your Task Is Complete!"),
            unicode("Hi, your task has been completed and your file is in "
                    "your email inbox."),
            unicode("Once you review your work, please approve the work below "
                    "so that we can pay your worker."),
            unicode("Thanks!")
            ]

    APPROVE_TASK_TEXT = unicode("Approve Work")

    def __init__(self):
        super(ApproveTaskGrid, self).__init__()
        self.append_class(self.APPROVE_TASK_GRID_CLASS)

        self.set_id(self.APPROVE_TASK_GRID_ID)

        for line in self.LINES:
            self.append_child(Line(line))

        task_instance_view = ObjectView(self.TASK_INSTANCE_ID)
        task_instance_view.append_child(SubmitButton(self.APPROVE_TASK_TEXT))
        self.append_child(task_instance_view)
