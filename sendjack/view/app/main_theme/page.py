"""
    Pages for Main Theme
    --------------------

    The Standard Pages for the application.
    <div class="page main-page">

"""
from view.elementary.html import TextInput, SubmitButton, Textarea, HiddenInput
from view.app.base.page import Page
from view.app.base.field import FieldList, Field
from view.app.base.components import TitledGrid, DatePicker
from view.app.base.object import ObjectView, CustomerView

from .components import MainSection, MainGrid


class MainPage(Page):

    _MAIN_PAGE_CLASS = unicode("main-page")

    def __init__(self):
        super(MainPage, self).__init__()
        self.append_class(self._MAIN_PAGE_CLASS)

        main_section = MainSection(self._construct_grids())
        self.append_child(main_section)


    def _construct_grids(self):
        # TODO: should this raise an OverrideRequiredError?
        return []


class CreateCustomerPage(MainPage):

    CREATE_CUSTOMER_PAGE_ID = "create-customer-page"

    def __init__(self):
        super(CreateCustomerPage, self).__init__()
        self.set_id(self.CREATE_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CreateCustomerGrid()]


class CreateCustomerGrid(MainGrid):

    _CREATE_CUSTOMER_GRID_CLASS = unicode("create-customer-grid")

    _GRID_TITLE = unicode("Sign Up")
    _GRID_SUBTITLES = [
            unicode((
                    "Great! Now we just need your contact details. We'll"
                    "holler."
                    )),
            ]


    def __init__(self):
        super(CreateCustomerGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_CUSTOMER_GRID_CLASS)


    def _construct_form(self):
        return CustomerView()


class CreateInstancePage(MainPage):

    _CREATE_INSTANCE_PAGE_ID = unicode("create-instance-page")

    def __init__(self):
        super(CreateInstancePage, self).__init__()
        self.set_id(self._CREATE_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceGrid()]


class CreateInstanceGrid(MainGrid):

    _CREATE_INSTANCE_GRID_CLASS = unicode("create-instance-grid")

    _GRID_TITLE = unicode("Create A Task")
    _GRID_SUBTITLES = [
            unicode((
                    "I'll find something to put here that makes lots of sense."
                    )),
            unicode((
                    "This proves there can be more than one of me!"
                    )),
            ]


    def __init__(self):
        super(CreateInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return TaskInstanceView()


class TaskInstanceView(ObjectView):

    _TASK_INSTANCE_VIEW_CLASS = unicode("task-instance-view")
    _TASK_INSTANCE_ID = unicode("instance")

    # names
    _CUSTOMER_TITLE_NAME = unicode("customer_title")
    _CUSTOMER_DESCRIPTION_NAME = unicode("customer_description")
    _TITLE_NAME = unicode("title")
    _SUMMARY_NAME = unicode("summary")
    _DEADLINE_NAME = unicode("deadline_ts")

    _INSTRUCTIONS_NAME = unicode("instructions")
    _PROPERTIES_NAME = unicode("properties")
    _OUTPUT_TYPE_NAME = unicode("output_type")
    _OUTPUT_METHOD_NAME = unicode("output_method")
    _PRICE_NAME = unicode("price")
    _CATEGORY_TAGS_NAME = unicode("category_tags")
    _INDUSTRY_TAGS_NAME = unicode("industry_tags")
    _SKILL_TAGS_NAME = unicode("skill_tags")
    _EQUIPMENT_TAGS_NAME = unicode("equipment_tags")

    # classes
    _CUSTOMER_TITLE_CLASS = unicode("customer-title")
    _CUSTOMER_DESCRIPTION_CLASS = unicode("customer-description")
    _DEADLINE_CLASS = unicode("deadline")

    # placeholder values
    _CUSTOMER_TITLE_PLACEHOLDER = unicode("Enter a title for your task...")
    _CUSTOMER_DESCRIPTION_PLACEHOLDER = unicode("Describe your task...")
    _DEADLINE_PLACEHOLDER = unicode("06/31/2013")

    _TEXTAREA_DEFAULT_ROWS = 4
    _SUBMIT_TEXT = unicode("Create")


    def __init__(self):
        super(TaskInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        # assemble customer title
        customer_title = TextInput(self._CUSTOMER_TITLE_NAME)
        customer_title.append_class(self._CUSTOMER_TITLE_CLASS)
        customer_title.set_placeholder(self._CUSTOMER_TITLE_PLACEHOLDER)

        # assemble customer description
        customer_description = Textarea(self._CUSTOMER_DESCRIPTION_NAME)
        customer_description.append_class(self._CUSTOMER_DESCRIPTION_CLASS)
        customer_description.set_placeholder(
                self._CUSTOMER_DESCRIPTION_PLACEHOLDER)
        customer_description.set_rows(self._TEXTAREA_DEFAULT_ROWS)

        # assemble deadline
        deadline = DatePicker(self._DEADLINE_NAME)
        deadline.append_class(self._DEADLINE_CLASS)
        deadline.set_placeholder(self._DEADLINE_PLACEHOLDER)

        self.append_child(customer_title)
        self.append_child(customer_description)
        self.append_child(deadline)

        self.append_child(HiddenInput(self._TITLE_NAME))
        self.append_child(HiddenInput(self._SUMMARY_NAME))

        self.append_child(HiddenInput(self._INSTRUCTIONS_NAME))
        self.append_child(HiddenInput(self._PROPERTIES_NAME))
        self.append_child(HiddenInput(self._OUTPUT_TYPE_NAME))
        self.append_child(HiddenInput(self._OUTPUT_METHOD_NAME))
        self.append_child(HiddenInput(self._PRICE_NAME))
        self.append_child(HiddenInput(self._CATEGORY_TAGS_NAME))
        self.append_child(HiddenInput(self._INDUSTRY_TAGS_NAME))
        self.append_child(HiddenInput(self._SKILL_TAGS_NAME))
        self.append_child(HiddenInput(self._EQUIPMENT_TAGS_NAME))

        self.append_child(SubmitButton(self._SUBMIT_TEXT))


class CreateInstanceThanksPage(MainPage):

    _CREATE_INSTANCE_THANKS_PAGE_ID = unicode("create-instance-thanks-page")

    def __init__(self):
        super(CreateInstanceThanksPage, self).__init__()
        self.set_id(self._CREATE_INSTANCE_THANKS_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceThanksGrid()]


class CreateInstanceThanksGrid(TitledGrid):

    _CREATE_INSTANCE_THANKS_GRID_CLASS = unicode("create-instance-thanks-grid")

    _GRID_TITLE = unicode("Next Steps")
    _GRID_SUBTITLES = [
            unicode((
                    "Jackalope is on it.",
                    )),
            unicode((
                    "We're processing your task to make sure it looks great.",
                    )),
            unicode((
                    "Then we'll email you to confirm all the details. Thanks "
                    "for trying us out!"
                    )),
            ]

    def __init__(self):
        super(CreateInstanceThanksGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_INSTANCE_THANKS_GRID_CLASS)


class ConfirmInstancePage(MainPage):

    _CONFIRM_INSTANCE_PAGE_ID = unicode("confirm-instance-page")

    def __init__(self):
        super(ConfirmInstancePage, self).__init__()
        self.set_id(self._CONFIRM_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [ConfirmInstanceGrid()]


class ConfirmInstanceGrid(MainGrid):

    _CONFIRM_INSTANCE_GRID_CLASS = unicode("confirm-instance-grid")

    _GRID_TITLE = unicode("Task Details")
    _GRID_SUBTITLES = [
            unicode((
                    "We checked out a number of tasks like yours that went "
                    "well, and fine-tuned your description. We've also "
                    "suggested a price below."
                    )),
            ]

    def __init__(self):
        super(ConfirmInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CONFIRM_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        self.append_child(TaskInstanceView())


class CardCustomerPage(MainPage):

    _CARD_CUSTOMER_PAGE_ID = unicode("card-customer-page")

    def __init__(self):
        super(CardCustomerPage, self).__init__()
        self.set_id(self._CARD_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CardCustomerGrid()]


class CardCustomerGrid(MainGrid):

    _CARD_CUSTOMER_GRID_CLASS = unicode("card-customer-grid")

    _GRID_TITLE = unicode("Payment")
    _GRID_SUBTITLES = [
            unicode((
                    "Great! Now all we need is your payment details. You'll "
                    "never be charged until your task is done and you have "
                    "approved the work."
                    )),
            ]

    def __init__(self):
        super(CardCustomerGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CARD_CUSTOMER_GRID_CLASS)


    def _construct_form(self):
        return CardCustomerView()


class CardCustomerView(ObjectView):

    _CARD_CUSTOMER_VIEW_CLASS = unicode("card-customer-view")
    _CARD_CUSTOMER_ID = unicode("customer")

    _SUBMIT_TEXT = unicode("Save")

    def __init__(self):
        super(CardCustomerView, self).__init__(self._CARD_CUSTOMER_ID)
        self.append_class(self._CARD_CUSTOMER_VIEW_CLASS)

        fields = [
                Field(
                    unicode("First Name"),
                    unicode("first_name")),
                Field(
                    unicode("Last Name"),
                    unicode("last_name")),
                Field(
                    unicode("Email"),
                    unicode("email")),
                Field(
                    unicode("Credit Card"),
                    unicode("card_number")),
                Field(
                    unicode("Exp Month"),
                    unicode("card_expiry_month")),
                Field(
                    unicode("Exp Year"),
                    unicode("card_expiry_year")),
                Field(
                    unicode("CVC:"),
                    unicode("card_cvc")),
                ]

        self.append_child(FieldList(fields))
        self.append_child(SubmitButton(self._SUBMIT_TEXT))


class ConfirmInstanceThanksPage(MainPage):

    _CONFIRM_INSTANCE_THANKS_PAGE_ID = unicode("confirm-instance-thanks-page")

    def __init__(self):
        super(ConfirmInstanceThanksPage, self).__init__()
        self.set_id(self._CONFIRM_INSTANCE_THANKS_PAGE_ID)

    def _construct_grids(self):
        return [ConfirmInstanceThanksGrid()]


class ConfirmInstanceThanksGrid(TitledGrid):

    _CONFIRM_INSTANCE_THANKS_GRID_CLASS = unicode(
            "confirm-instance-thanks-grid")

    _GRID_TITLE = unicode("Fill this in.")
    _GRID_SUBTITLES = [
            unicode((
                    "We're on it. We'll let you know when it's done."
                    )),
            ]

    def __init__(self):
        super(ConfirmInstanceThanksGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CONFIRM_INSTANCE_THANKS_GRID_CLASS)


class ApproveInstancePage(MainPage):

    _APPROVE_INSTANCE_PAGE_ID = unicode("approve-instance-page")

    def __init__(self):
        super(ApproveInstancePage, self).__init__()
        self.set_id(self._APPROVE_INSTANCE_PAGE_ID)

    def _construct_grids(self):
        return [ApproveInstanceGrid()]


class ApproveInstanceGrid(MainGrid):

    _APPROVE_INSTANCE_GRID_CLASS = unicode("approve-task-grid")

    _GRID_TITLE = unicode("Approve Work")
    _GRID_SUBTITLES = [
            unicode("Your Task Is Complete!"),
            unicode("Hi, your task has been completed and your file is in "
                    "your email inbox."),
            unicode("Once you review your work, please approve the work below "
                    "so that we can pay your worker."),
            unicode("Thanks!"),
            ]

    def __init__(self):
        super(ApproveInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._APPROVE_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return ApproveInstanceView()


class ApproveInstanceView(ObjectView):

    _APPROVE_INSTANCE_VIEW_CLASS = unicode("approve-instance-view")
    _APPROVE_INSTANCE_ID = unicode("instance")

    _SUBMIT_TEXT = unicode("Approve")

    def __init__(self):
        super(ApproveInstanceView, self).__init__(self._APPROVE_INSTANCE_ID)
        self.append_class(self._APPROVE_INSTANCE_VIEW_CLASS)

        self.append_child(SubmitButton(self._SUBMIT_TEXT))
