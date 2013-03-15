"""
    Object Views
    ------------

    All object views. Subclass if you need to make use specific modifications.

"""
from view.elementary.html import Form, TextInput, HiddenInput, SubmitButton

from .field import FieldList, TemplateField
#from components import CreatorField, CustomerField
from .field import CustomerTitleField, CustomerDescriptionField
from .field import TitleField, SummaryField, DescriptionField
from .field import InstructionsField, InstructionField
from .field import PropertiesField, PropertyField, MoreDetailsField
from .field import DeadlineField, PriceField
from .field import OutputTypeField, OutputMethodField
from .field import CategoryTagsField, IndustryTagsField
from .field import SkillTagsField, EquipmentTagsField


class ObjectView(Form):

    """Provide a view that corresponds to a model object. Provide a framework
    for coordinating the javascript Model/View classes."""

    OBJECT_VIEW_CLASS = "object-view"

    def __init__(self, object_id):
        super(ObjectView, self).__init__(object_id)
        self.append_class(self.OBJECT_VIEW_CLASS)

        self.set_id(object_id)


class CustomerView(ObjectView):

    CUSTOMER_VIEW_CLASS = "customer-view"
    SUBMIT_TEXT = "Post Task"
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


class TaskInstanceInternalView(ObjectView):

    TASK_INSTANCE_VIEW_CLASS = "instance-view"
    SUBMIT_TEXT = "Save"
    TASK_INSTANCE_ID = unicode("instance")

    def __init__(self):
        super(TaskInstanceInternalView, self).__init__(self.TASK_INSTANCE_ID)
        self.append_class(self.TASK_INSTANCE_VIEW_CLASS)

        fields = [
                TemplateField(),
                #CustomerField(),
                CustomerTitleField(),
                CustomerDescriptionField(),
                TitleField(),
                SummaryField(),
                InstructionsField(),
                InstructionField(),
                PropertiesField(),
                PropertyField(),
                OutputTypeField(),
                OutputMethodField(),
                DescriptionField(),
                MoreDetailsField(),
                DeadlineField(),
                PriceField(),
                CategoryTagsField(),
                IndustryTagsField(),
                SkillTagsField(),
                EquipmentTagsField(),
                ]
        self.append_child(FieldList(fields))
        self.append_child(SubmitButton(self.SUBMIT_TEXT))
