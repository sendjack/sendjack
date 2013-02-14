"""
    Alpha Sign Up Pages
    -------------------

    All the Pages for the alpha sign up series.
    <div class="page">

"""
from view.elementary.html import TextInput, SubmitButton, Textarea, HiddenInput
from view.app.base.page import Page
from view.app.base.components import Line, DatePicker, ObjectView

from components import AltSection, RightGrid


class SignUpPage(Page):

    SIGN_UP_PAGE = "sign-up-page"


    def __init__(self):
        super(SignUpPage, self).__init__()
        self.append_class(self.SIGN_UP_PAGE)

        sign_up_section = AltSection(SignUpGrid())

        self.append_child(sign_up_section)


class SignUpGrid(RightGrid):

    SIGN_UP_GRID = "sign-up-grid"
    SIGN_UP_TITLE = "sign-up-title"

    LINES = [
            "Jackalope is the easiest way to outsource work.",
            ("Send us a task you need done. "
            "We'll source and price it for you for free.")
            ]


    def __init__(self):
        super(SignUpGrid, self).__init__()
        self.append_class(self.SIGN_UP_GRID)


    def _set_title_image_class(self, title_image_div):
        title_image_div.append_class(self.SIGN_UP_TITLE)


    def _set_grid_elements(self):
        for line in self.LINES:
            line_el = Line(line)
            self.append_child(line_el)

        self.append_child(CustomerView())


class CustomerView(ObjectView):

    CUSTOMER_VIEW_CLASS = "customer-view"
    SUBMIT_TEXT = "Take Jack for a Test Drive"
    CUSTOMER_ID = "customer"

    FIRST_NAME_PLACEHOLDER = "First Name"
    LAST_NAME_PLACEHOLDER = "Last Name"
    EMAIL_PLACEHOLDER = "Email"

    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    EMAIL = "email"
    STATUS = "status"
    STATUS_REQUESTED = "requested"

    def __init__(self):
        super(CustomerView, self).__init__(self.CUSTOMER_ID)
        self.append_class(self.CUSTOMER_VIEW_CLASS)

        first_name = TextInput(self.FIRST_NAME)
        last_name = TextInput(self.LAST_NAME)
        email = TextInput(self.EMAIL)
        status = HiddenInput(self.STATUS, self.STATUS_REQUESTED)
        submit = SubmitButton(self.SUBMIT_TEXT)

        first_name.append_class(self.FIRST_NAME)
        last_name.append_class(self.LAST_NAME)
        email.append_class(self.EMAIL)

        first_name.set_placeholder(self.FIRST_NAME_PLACEHOLDER)
        last_name.set_placeholder(self.LAST_NAME_PLACEHOLDER)
        email.set_placeholder(self.EMAIL_PLACEHOLDER)

        self.append_child(first_name)
        self.append_child(last_name)
        self.append_child(email)
        self.append_child(status)
        self.append_child(submit)


class NewTaskPage(Page):

    NEW_TASK_PAGE = "new-task-page"


    def __init__(self):
        super(NewTaskPage, self).__init__()
        self.append_class(self.NEW_TASK_PAGE)

        new_task_section = AltSection(NewTaskGrid())

        self.append_child(new_task_section)


class NewTaskGrid(RightGrid):

    NEW_TASK_GRID = "new-task-grid"
    NEW_TASK_TITLE = "new-task-title"

    def __init__(self):
        super(NewTaskGrid, self).__init__()
        self.append_class(self.NEW_TASK_GRID)


    def _set_title_image_class(self, title_image_div):
        title_image_div.append_class(self.NEW_TASK_TITLE)


    def _set_grid_elements(self):
        self.append_child(TaskInstanceView())


class TaskInstanceView(ObjectView):

    TASK_INSTANCE_VIEW = "task-instance-view"
    SUBMIT_TEXT = "Post Task"
    TASK_INSTANCE_ID = "instance"

    TASK_TITLE_PLACEHOLDER = "Task Title"
    TASK_DESCRIPTION_PLACEHOLDER = "Enter Your Task Description"
    TASK_DEADLINE_PLACEHOLDER = "06/31/2013"

    TASK_TITLE = "customer_title"
    TASK_DESCRIPTION = "customer_description"
    TASK_DEADLINE = "deadline_ts"


    def __init__(self):
        super(TaskInstanceView, self).__init__(self.TASK_INSTANCE_ID)
        self.append_class(self.TASK_INSTANCE_VIEW)

        task_title = TextInput(self.TASK_TITLE)
        task_description = Textarea(self.TASK_DESCRIPTION)
        task_deadline = DatePicker(self.TASK_DEADLINE)
        submit = SubmitButton(self.SUBMIT_TEXT)

        task_title.append_class(self.TASK_TITLE)
        task_description.append_class(self.TASK_DESCRIPTION)
        task_deadline.append_class(self.TASK_DEADLINE)

        task_title.set_placeholder(self.TASK_TITLE_PLACEHOLDER)
        task_description.set_placeholder(self.TASK_DESCRIPTION_PLACEHOLDER)
        task_deadline.set_placeholder(self.TASK_DEADLINE_PLACEHOLDER)

        task_description.set_rows(4)

        self.append_child(task_title)
        self.append_child(task_description)
        self.append_child(task_deadline)
        self.append_child(submit)


class ThankYouPage(Page):

    THANK_YOU_PAGE = "thank-you-page"


    def __init__(self):
        super(ThankYouPage, self).__init__()
        self.append_class(self.THANK_YOU_PAGE)

        thank_you_section = AltSection(ThankYouGrid())

        self.append_child(thank_you_section)


class ThankYouGrid(RightGrid):

    THANK_YOU_GRID = "thank-you-grid"
    THANK_YOU_TITLE = "thank-you-title"

    # TODO: Put somewhere else
    LINES = [
            "Jackalope is on it.",
            "We're processing your task and making sure it looks great.",
            ("Then we'll email you to confirm all the details. "
            "Thanks for trying us out!")
            ]


    def __init__(self):
        super(ThankYouGrid, self).__init__()
        self.append_class(self.THANK_YOU_GRID)


    def _set_title_image_class(self, title_image_div):
        title_image_div.append_class(self.THANK_YOU_TITLE)


    def _set_grid_elements(self):
        for line in self.LINES:
            line_el = Line(line)
            self.append_child(line_el)
