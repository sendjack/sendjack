"""
    Pages for Main Theme
    --------------------

    The Standard Pages for the application.
    <div class="page main-page">

"""
from view.elementary.html import TextInput, SubmitButton, Div

from view.app.base.page import Page
from view.app.base.components import TitledGrid, GridText

# instance fields
from view.app.base.object.instance import InstanceView
from view.app.base.object.field import TitleField, SummaryField
from view.app.base.object.field import CustomerTitleField
from view.app.base.object.field import CustomerDescriptionField
from view.app.base.object.field import DeadlineField, PriceField
from view.app.base.object.field import DescriptionField, MoreDetailsField
from view.app.base.object.field import TemplateIDField
from view.app.base.object.field import InstructionsField, InstructionField
from view.app.base.object.field import PropertiesField, PropertyField
from view.app.base.object.field import OutputTypeField, OutputMethodField
from view.app.base.object.field import CategoryTagsField, IndustryTagsField
from view.app.base.object.field import SkillTagsField, EquipmentTagsField

# customer fields
from view.app.base.object.customer import CustomerView
from view.app.base.object.field import FirstNameField, LastNameField
from view.app.base.object.field import EmailField, CreditCardField, CVCField
from view.app.base.object.field import ExpiryMonthField, ExpiryYearField

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
            unicode("We're excited to get to work. Tell us more about what "
                    "you need done."
                    ),
            unicode("Jackalope examines tasks just like yours that went "
                    "really well in order to fine-tune the description, "
                    "suggest a price, and find the best worker to get the "
                    "work done on time."
                    ),
            ]

    def __init__(self):
        super(CreateInstanceGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._CREATE_INSTANCE_GRID_CLASS)


    def _construct_form(self):
        return CreateInstanceView()


class CreateInstanceView(InstanceView):

    _OBJECT_VIEW_ID = unicode("create-instance")
    _SUBMIT_TEXT = unicode("Create")


    def __init__(self):
        super(CreateInstanceView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                CustomerTitleField(),
                CustomerDescriptionField(),
                DeadlineField(),
                ]


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
        return CreateCustomerView()


class CreateCustomerView(CustomerView):

    _OBJECT_VIEW_ID = unicode("create-customer")
    _SUBMIT_TEXT = unicode("Sign Up and Continue")

    def __init__(self):
        super(CreateCustomerView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                EmailField()
                ]


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


class ProcessInstanceView(InstanceView):

    _OBJECT_VIEW_ID = unicode("process-instance")
    _SUBMIT_TEXT = unicode("Process")

    def __init__(self):
        super(ProcessInstanceView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                TemplateIDField(),
                #CustomerField(),
                CustomerTitleField(True),
                CustomerDescriptionField(True),
                TitleField(True),
                SummaryField(True),
                InstructionsField(True),
                InstructionField(),
                PropertiesField(True),
                PropertyField(),
                OutputTypeField(),
                OutputMethodField(),
                DescriptionField(True),
                MoreDetailsField(True),
                DeadlineField(),
                PriceField(),
                CategoryTagsField(),
                IndustryTagsField(),
                SkillTagsField(),
                EquipmentTagsField(),
                ]


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


class ConfirmInstanceView(InstanceView):

    _OBJECT_VIEW_ID = unicode("confirm-instance")
    _SUBMIT_TEXT = unicode("Create")


    def __init__(self):
        super(ConfirmInstanceView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                TitleField(),
                SummaryField(),
                DescriptionField(),
                MoreDetailsField(),
                DeadlineField(),
                PriceField(),
                ]


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


class CardCustomerView(CustomerView):

    _OBJECT_VIEW_ID = unicode("card-customer")
    _SUBMIT_TEXT = unicode("Save")

    def __init__(self):
        super(CardCustomerView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                FirstNameField(),
                LastNameField(),
                EmailField(),
                CreditCardField(),
                ExpiryMonthField(),
                ExpiryYearField(),
                CVCField(),
                ]


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
            unicode("We got this. You relax. Take a beat. Kick back a "
                    "minute."
                    ),
            unicode("While you're doing that, we're getting started on your "
                    "task. The worker we found to get it done will reach out "
                    "to you shortly."
                    ),
            unicode("We'll get back in touch when it's completed by sending "
                    "you an email with a link to approve the work. We won't "
                    "charge your card until the task is approved."
                    ),
            unicode("Remember, once you have been notified the task is done, "
                    "if we don't hear from you for two days, we will assume "
                    "you approve and automatically charge your card."
                    ),
            unicode("Thank you for using Jackalope to get your work done."),
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


class ApproveInstanceView(InstanceView):

    _OBJECT_VIEW_ID = unicode("approve-instance")
    _SUBMIT_TEXT = unicode("Approve")


    def __init__(self):
        super(ApproveInstanceView, self).__init__(
                self._OBJECT_VIEW_ID,
                self._SUBMIT_TEXT)


    def _construct_fields(self):
        return [
                TitleField(),
                SummaryField(),
                DescriptionField(),
                MoreDetailsField(),
                DeadlineField(),
                PriceField()
                ]


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


class SearchPage(MainPage):

    # TODO: Make this page link to a different theme
    _SEARCH_PAGE_ID = unicode("search-page")

    def __init__(self):
        super(SearchPage, self).__init__()
        self.set_id(self._SEARCH_PAGE_ID)

    def _construct_grids(self):
        return [SearchGrid()]


class SearchGrid(MainGrid):

    _SEARCH_GRID_CLASS = unicode("search-grid")
    _SEARCH_TEXT_CLASS = unicode("search-text")
    _SEARCH_TEXT = unicode(
            "Getting your work done is as simple as search.")

    _GRID_TITLE = unicode("Jackalope Beta")
    _GRID_SUBTITLES = [
            unicode("The most reliable way to find contact information."),
            ]


    def __init__(self):
        super(SearchGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._SEARCH_GRID_CLASS)

        grid_text = GridText(self._SEARCH_TEXT)
        grid_text.append_class(self._SEARCH_TEXT_CLASS)
        self.append_child(grid_text)


    def _construct_form(self):
        return SearchInstanceView()


class SearchInstanceView(InstanceView):

    _OBJECT_VIEW_ID = unicode("search-instance")
    _CUSTOMER_TITLE_PLACEHOLDER = unicode(
            "Enter your task to find contact information...")


    def __init__(self):
        super(SearchInstanceView, self).__init__(self._OBJECT_VIEW_ID)


    def _construct_fields(self):
        return []

    def _construct_submit_button(self, submit_text):
        customer_title_input = TextInput(CustomerTitleField.NAME)
        customer_title_input.set_placeholder(self._CUSTOMER_TITLE_PLACEHOLDER)
        return SearchButton(customer_title_input)


class SearchButton(Div):

    _SEARCH_BUTTON_CLASS = unicode("search-button")
    _SUBMIT_TEXT = unicode("j")

    def __init__(self, input_el):
        super(SearchButton, self).__init__()
        self.append_class(self._SEARCH_BUTTON_CLASS)

        submit_button = SubmitButton(self._SUBMIT_TEXT)

        input_div = Div()
        input_div.append_child(input_el)

        input_el.set_tabindex(1)
        submit_button.set_tabindex(2)

        # Needs to be in this order for overflow: hidden in CSS
        self.append_child(submit_button)
        self.append_child(input_div)
