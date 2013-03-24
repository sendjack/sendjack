"""
    Instance Object View
    --------------------

"""
from .base import ObjectView
from .field import TemplateIDField, CustomerIDField, CustomerTitleField
from .field import CustomerDescriptionField, TitleField, SummaryField
from .field import InstructionsField, InstructionField, PropertiesField
from .field import PropertyField, OutputTypeField, OutputMethodField
from .field import DescriptionField, MoreDetailsField, DeadlineField
from .field import PriceField, CategoryTagsField, IndustryTagsField
from .field import IDField, SkillTagsField, EquipmentTagsField


class InstanceView(ObjectView):

    _OBJECT_VIEW_ID = unicode("instance")
    _OBJECT_TYPE_CLASS = unicode("instance-view")

    allowed_fields = [
            IDField,
            TitleField,
            SummaryField,
            InstructionsField,
            InstructionField,
            OutputTypeField,
            OutputMethodField,
            PropertiesField,
            PropertyField,
            CategoryTagsField,
            IndustryTagsField,
            SkillTagsField,
            EquipmentTagsField,
            TemplateIDField,
            CustomerIDField,
            #WorkerIDField,
            CustomerTitleField,
            CustomerDescriptionField,
            DescriptionField,
            MoreDetailsField,
            #StatusField,
            DeadlineField,
            #IsUrgentField,
            PriceField,
            #OverheadField,
            #InteractionsField,
            #ScoreField
            ]


    def __init__(self, object_view_id=None, submit_text=None):
        super(InstanceView, self).__init__(
                self._OBJECT_TYPE_CLASS,
                self._get_object_view_id(object_view_id),
                self._SUBMIT_TEXT)
