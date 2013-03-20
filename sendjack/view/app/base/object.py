"""
    Object Views
    ------------

    All object views. Subclass if you need to make use specific modifications.

"""
from view.elementary.html import Form, HiddenInput, SubmitButton

from .field import FieldList, TemplateField
#from components import CreatorField, CustomerField
from .field import CustomerTitleField, CustomerDescriptionField
from .field import TitleField, SummaryField, DescriptionField
from .field import InstructionsField, InstructionField
from .field import PropertiesField, PropertyField, MoreDetailsField
from .field import DeadlineField, PriceField
from .field import OutputTypeField, OutputMethodField
from .field import CategoryTagsField, IndustryTagsField
from .field import SkillTagsField, EquipmentTagsField, EmailField


class ObjectView(Form):

    """Provide a view that corresponds to a model object. Provide a framework
    for coordinating the javascript Model/View classes."""

    _OBJECT_VIEW_CLASS = unicode("object-view")

    def __init__(self, object_id):
        super(ObjectView, self).__init__(object_id)
        self.append_class(self._OBJECT_VIEW_CLASS)

        self.set_id(object_id)


class CustomerView(ObjectView):

    _CUSTOMER_VIEW_CLASS = unicode("customer-view")
    _SUBMIT_TEXT = unicode("Sign Up and Continue")
    _CUSTOMER_ID = unicode("customer")

    #_FIRST_NAME_PLACEHOLDER = unicode("First Name")
    #_LAST_NAME_PLACEHOLDER = unicode("Last Name")
    _EMAIL_PLACEHOLDER = unicode("Enter your email address")

    _FIRST_NAME = unicode("first_name")
    _LAST_NAME = unicode("last_name")
    _EMAIL = unicode("email")
    _STATUS = unicode("status")
    _STATUS_REQUESTED = unicode("requested")

    def __init__(self):
        super(CustomerView, self).__init__(self._CUSTOMER_ID)
        self.append_class(self._CUSTOMER_VIEW_CLASS)

        first_name = HiddenInput(self._FIRST_NAME)
        last_name = HiddenInput(self._LAST_NAME)
        email = EmailField()
        status = HiddenInput(self._STATUS, self._STATUS_REQUESTED)
        submit = SubmitButton(self._SUBMIT_TEXT)

        first_name.append_class(self._FIRST_NAME)
        last_name.append_class(self._LAST_NAME)
        email.append_class(self._EMAIL)

        #first_name.set_placeholder(self._FIRST_NAME_PLACEHOLDER)
        #last_name.set_placeholder(self._LAST_NAME_PLACEHOLDER)
        email.set_placeholder(self._EMAIL_PLACEHOLDER)

        self.append_child(first_name)
        self.append_child(last_name)
        self.append_child(email)
        self.append_child(status)
        self.append_child(submit)


class ProcessInstanceView(ObjectView):

    _TASK_INSTANCE_VIEW_CLASS = unicode("task-instance-view")
    _TASK_INSTANCE_ID = unicode("instance")

    _SUBMIT_TEXT = unicode("Process")

    def __init__(self):
        super(ProcessInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        self.append_child(FieldList([
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
                ]))

        self.append_child(SubmitButton(self._SUBMIT_TEXT))
