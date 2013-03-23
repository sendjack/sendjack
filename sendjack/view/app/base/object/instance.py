"""
    Instance Object View
    --------------------

"""
from view.elementary.html import SubmitButton

from .base import ObjectView
from .field import TemplateIDField, CustomerTitleField
from .field import CustomerDescriptionField, TitleField, SummaryField
from .field import InstructionsField, InstructionField, PropertiesField
from .field import PropertyField, OutputTypeField, OutputMethodField
from .field import DescriptionField, MoreDetailsField, DeadlineField
from .field import PriceField, CategoryTagsField, IndustryTagsField
from .field import SkillTagsField, EquipmentTagsField


class InstanceView(ObjectView):

    _TASK_INSTANCE_VIEW_CLASS = unicode("instance-view")
    _TASK_INSTANCE_ID = unicode("instance")

    _SUBMIT_TEXT = unicode("Process")

    def __init__(self):
        super(ProcessInstanceView, self).__init__(self._TASK_INSTANCE_ID)
        self.append_class(self._TASK_INSTANCE_VIEW_CLASS)

        self.append_child(FieldList([
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
                ]))

        self.append_child(SubmitButton(self._SUBMIT_TEXT))

