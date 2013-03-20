"""
    Pages for Main Theme
    --------------------

    The Standard Pages for the application.
    <div class="page main-page">

"""
from view.elementary.html import SubmitButton, HiddenInput
from view.app.base.page import Page
from view.app.base.field import FieldList, Field
from view.app.base.components import TitledGrid
from view.app.base.field import CustomerTitleField, CustomerDescriptionField
from view.app.base.field import DeadlineField, PriceField, TitleField
from view.app.base.field import DescriptionField, MoreDetailsField
from view.app.base.field import SummaryField
from view.app.base.object import ObjectView, CustomerView, ProcessInstanceView

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


class CreateInstancePage(MainPage):

    _CREATE_INSTANCE_PAGE_ID = unicode("create-instance-page")

    def __init__(self):
        super(CreateInstancePage, self).__init__()
        self.set_id(self._CREATE_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceGrid()]


class CreateInstanceGrid(MainGrid):

    _CREATE_INSTANCE_GRID_CLASS = unicode("create-instance-grid")

    _GRID_TITLE = unicode("Add Task Details")
    _GRID_SUBTITLES = [
            unicode("We're excited to get started on your task. Let's dig a "
                    "little deeper...tell us more about the work you need "
                    "done."
                    ),
            unicode("Your task will be matched with similar work that has "
                    "gone well in the past to make sure we write clear "
                    "instructions, set the right price, and find the best "
                    "worker to get it done on time."
                    ),
            ]

    def __init__(self):
        super(CreateInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return CreateInstanceView()


class CreateInstanceView(ObjectView):

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

    _TEXTAREA_DEFAULT_ROWS = 4
    _SUBMIT_TEXT = unicode("Create")


    def __init__(self):
        super(CreateInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        self.append_child(CustomerTitleField())
        self.append_child(CustomerDescriptionField())
        self.append_child(DeadlineField())

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


class CreateCustomerPage(MainPage):

    _CREATE_CUSTOMER_PAGE_ID = unicode("create-customer-page")

    def __init__(self):
        super(CreateCustomerPage, self).__init__()
        self.set_id(self._CREATE_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CreateCustomerGrid()]


class CreateCustomerGrid(MainGrid):

    _CREATE_CUSTOMER_GRID_CLASS = unicode("create-customer-grid")

    _GRID_TITLE = unicode("Add Contact Information")
    _GRID_SUBTITLES = [
            unicode("Thank you for using Jackalope to get your work done!"),
            unicode("We've started looking into your task. Now we just need "
                    "to know how to get in touch with you to confirm the "
                    "details, like description and price. It won't be long."
                    ),
            ]


    def __init__(self):
        super(CreateCustomerGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_CUSTOMER_GRID_CLASS)


    def _construct_form(self):
        return CustomerView()


class CreateInstanceThanksPage(MainPage):

    _CREATE_INSTANCE_THANKS_PAGE_ID = unicode("create-instance-thanks-page")

    def __init__(self):
        super(CreateInstanceThanksPage, self).__init__()
        self.set_id(self._CREATE_INSTANCE_THANKS_PAGE_ID)


    def _construct_grids(self):
        return [CreateInstanceThanksGrid()]


class CreateInstanceThanksGrid(TitledGrid):

    _CREATE_INSTANCE_THANKS_GRID_CLASS = unicode("create-instance-thanks-grid")

    _GRID_TITLE = unicode("Best. Decision. Ever.")
    _GRID_SUBTITLES = [
            unicode("You're about to be a whole lot more productive. And "
                    "awesome. Tell your friends."
                    ),
            unicode("Watch your inbox. Soon you will get an email with a link "
                    "to confirm the details. It shouldn't be long."
                    ),
            unicode("In the meantime, maybe read about the mythical jackalope "
                    "for fun. Or do other work. You're very important!"
                    ),
            ]


    def __init__(self):
        super(CreateInstanceThanksGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_INSTANCE_THANKS_GRID_CLASS)


class ProcessInstancePage(MainPage):

    _PROCESS_INSTANCE_PAGE_ID = unicode("process-instance-page")

    def __init__(self):
        super(ProcessInstancePage, self).__init__()
        self.set_id(self._PROCESS_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [ProcessInstanceGrid()]


class ProcessInstanceGrid(MainGrid):

    _PROCESS_INSTANCE_GRID_CLASS = unicode("process-instance-grid")

    _GRID_TITLE = unicode("Process A Task")
    _GRID_SUBTITLES = [
            unicode("Enter a Template ID and copy overlapping fields from "
                    "that Template into this task."
                    ),
            unicode("Title = Vendor Title"),
            unicode("Summary = Vendor Description"),
            unicode("Description + More Details = Vendor Private Description"),
            unicode("Deadline = Vendor Deadline"),
            unicode("Price = Vendor Price"),
            ]

    def __init__(self):
        super(ProcessInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._PROCESS_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return ProcessInstanceView()


class ConfirmInstancePage(MainPage):

    _CONFIRM_INSTANCE_PAGE_ID = unicode("confirm-instance-page")

    def __init__(self):
        super(ConfirmInstancePage, self).__init__()
        self.set_id(self._CONFIRM_INSTANCE_PAGE_ID)


    def _construct_grids(self):
        return [ConfirmInstanceGrid()]


class ConfirmInstanceGrid(MainGrid):

    _CONFIRM_INSTANCE_GRID_CLASS = unicode("confirm-instance-grid")

    _GRID_TITLE = unicode("Confirm the Details")
    _GRID_SUBTITLES = [
            unicode("We're almost ready to get to work on your task, but we "
                    "need you to confirm a few things."
                    ),
            unicode("Jackalope turns every successful task into a reusable "
                    "recipe for getting work done. We checked out tasks just "
                    "like yours that went really well in order to fine-tune "
                    "the description and suggest a price."
                    ),
            unicode("Our suggestions are included below. Edit and confirm the "
                    "details of the task, and we'll get to work right away."
                    ),
            ]

    def __init__(self):
        super(ConfirmInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CONFIRM_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return ConfirmInstanceView()


class ConfirmInstanceView(ObjectView):

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

    _TEXTAREA_DEFAULT_ROWS = 4
    _SUBMIT_TEXT = unicode("Create")

    def __init__(self):
        super(ConfirmInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        title = TitleField()
        summary = SummaryField()
        description = DescriptionField()
        more_details = MoreDetailsField()
        deadline = DeadlineField()
        price = PriceField()

        self.append_child(title)
        self.append_child(summary)
        self.append_child(description)
        self.append_child(more_details)
        self.append_child(deadline)
        self.append_child(price)

        self.append_child(HiddenInput(self._CUSTOMER_TITLE_NAME))
        self.append_child(HiddenInput(self._CUSTOMER_DESCRIPTION_NAME))

        self.append_child(HiddenInput(self._INSTRUCTIONS_NAME))
        self.append_child(HiddenInput(self._PROPERTIES_NAME))
        self.append_child(HiddenInput(self._OUTPUT_TYPE_NAME))
        self.append_child(HiddenInput(self._OUTPUT_METHOD_NAME))
        self.append_child(HiddenInput(self._CATEGORY_TAGS_NAME))
        self.append_child(HiddenInput(self._INDUSTRY_TAGS_NAME))
        self.append_child(HiddenInput(self._SKILL_TAGS_NAME))
        self.append_child(HiddenInput(self._EQUIPMENT_TAGS_NAME))

        self.append_child(SubmitButton(self._SUBMIT_TEXT))


class CardCustomerPage(MainPage):

    _CARD_CUSTOMER_PAGE_ID = unicode("card-customer-page")

    def __init__(self):
        super(CardCustomerPage, self).__init__()
        self.set_id(self._CARD_CUSTOMER_PAGE_ID)


    def _construct_grids(self):
        return [CardCustomerGrid()]


class CardCustomerGrid(MainGrid):

    _CARD_CUSTOMER_GRID_CLASS = unicode("card-customer-grid")

    _GRID_TITLE = unicode("One More Thing...")
    _GRID_SUBTITLES = [
            unicode("Before we get to work, please enter your credit card "
                    "details so that we know how to charge you when all is "
                    "said and done."
                    ),
            unicode("To be clear, you will not be charged until the work is "
                    "done and you've had an opportunity to review it."
                    ),
            unicode("Jackalope processes credit card information securely "
                    "using Stripe."
                    ),
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
                    unicode("CVC"),
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

    _GRID_TITLE = unicode("We're On It!")
    _GRID_SUBTITLES = [
            unicode("Thank you for using Jackalope to get your work done."),
            unicode("We got this. You relax. Take a beat. Kick back a "
                    "minute."
                    ),
            unicode("While you're doing that, we're getting started on your "
                    "task. We'll let you know when it's finished by sending "
                    "you an email with a link to approve the work. We won't "
                    "charge your card until the task is approved."
                    ),
            unicode("Remember, once you have been notified the task is done, "
                    "if we don't hear from you for two days, we will assume "
                    "you approve and automatically charge your card."
                    ),
            unicode("Email ask@sendjack.com with questions."),
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
            unicode("All done!"),
            unicode("Now it's up to you to check out the results (files "
                    "attached, content posted, packages delivered, etc.)."
                    ),
            unicode("If you are satisfied, simply give the work your stamp of "
                    "approval. If you do nothing for two days, we will assume "
                    "you approve. Once this is done, your card will be "
                    "charged."
                    ),
            unicode("If you are not satisfied, please let us know by "
                    "rejecting the work."),
            ]

    def __init__(self):
        super(ApproveInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._APPROVE_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return ApproveInstanceView()


class ApproveInstanceView(ObjectView):

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

    _TEXTAREA_DEFAULT_ROWS = 4
    _SUBMIT_TEXT = unicode("Approve")

    def __init__(self):
        super(ApproveInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        title = TitleField()
        summary = SummaryField()
        description = DescriptionField()
        more_details = MoreDetailsField()
        deadline = DeadlineField()
        price = PriceField()

        self.append_child(title)
        self.append_child(summary)
        self.append_child(description)
        self.append_child(more_details)
        self.append_child(deadline)
        self.append_child(price)

        self.append_child(HiddenInput(self._CUSTOMER_TITLE_NAME))
        self.append_child(HiddenInput(self._CUSTOMER_DESCRIPTION_NAME))

        self.append_child(HiddenInput(self._INSTRUCTIONS_NAME))
        self.append_child(HiddenInput(self._PROPERTIES_NAME))
        self.append_child(HiddenInput(self._OUTPUT_TYPE_NAME))
        self.append_child(HiddenInput(self._OUTPUT_METHOD_NAME))
        self.append_child(HiddenInput(self._CATEGORY_TAGS_NAME))
        self.append_child(HiddenInput(self._INDUSTRY_TAGS_NAME))
        self.append_child(HiddenInput(self._SKILL_TAGS_NAME))
        self.append_child(HiddenInput(self._EQUIPMENT_TAGS_NAME))

        self.append_child(SubmitButton(self._SUBMIT_TEXT))


class ApproveInstanceThanksPage(MainPage):

    _APPROVE_INSTANCE_THANKS_PAGE_ID = unicode("approve-instance-thanks-page")

    def __init__(self):
        super(ApproveInstanceThanksPage, self).__init__()
        self.set_id(self._APPROVE_INSTANCE_THANKS_PAGE_ID)


    def _construct_grids(self):
        return [ApproveInstanceThanksGrid()]


class ApproveInstanceThanksGrid(TitledGrid):

    _APPROVE_INSTANCE_THANKS_GRID_CLASS = unicode(
            "approve-instance-thanks-grid")

    _GRID_TITLE = unicode("Thank You!")
    _GRID_SUBTITLES = [
            unicode("Bitte! Arigato! Prego! Ha mea iki! If you're happy, "
                    "we're happy."
                    ),
            unicode("Now that your task is done and you're satisfied with the "
                    "results, it's time for us to charge your card. You "
                    "should be receiving an email receipt shortly. We hope "
                    "you will continue using Jackalope to get your work done."
                    ),
            unicode("Jackalope gets better with your help. Please fill out a "
                    "short survey if you have a free minute. We're pretty "
                    "sure you do, since you just saved all that time "
                    "outsourcing your work. That's not working hard, that's "
                    "working smart!"
                    ),
            ]

    def __init__(self):
        super(ApproveInstanceThanksGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._APPROVE_INSTANCE_THANKS_GRID_CLASS)
