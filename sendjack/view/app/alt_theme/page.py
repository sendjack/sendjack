"""
    Main Pages
    ----------

    All the Pages for the Main series.
    <div class="page">

"""
from view.elementary.html import SubmitButton

from view.app.base.page import Page
from view.app.base.components import TitledGrid, Grid, GridText
from view.app.base.field import Field, FieldList
from view.app.base.field import IDField, TitleField, SummaryField
#from components import CreatorField
from view.app.base.field import InstructionsField, InstructionField
from view.app.base.field import PropertiesField, PropertyField
from view.app.base.field import OutputTypeField, OutputMethodField
from view.app.base.field import CategoryTagsField, IndustryTagsField
from view.app.base.field import SkillTagsField, EquipmentTagsField
from view.app.base.object import ObjectView, TaskInstanceView

from .components import NormalSection, ContrastSection


class AltPage(Page):

    ALT_PAGE_CLASS = "alt-page"

    def __init__(self):
        super(AltPage, self).__init__()
        self.append_class(self.ALT_PAGE_CLASS)


class TaskTemplatePage(AltPage):

    TEMPLATE_PAGE_ID = unicode("template-page")
    TEMPLATE_ID = "template"

    def __init__(self):
        super(TaskTemplatePage, self).__init__()
        self.set_id(self.TEMPLATE_PAGE_ID)

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

    def _set_grid_elements(self):
        fields = [
                IDField(),
                #CreatorField(),
                TitleField(),
                SummaryField(),
                InstructionsField(),
                InstructionField(),
                PropertiesField(),
                PropertyField(),
                OutputTypeField(),
                OutputMethodField(),
                #CategoryTagsField(),
                #IndustryTagsField(),
                #SkillTagsField(),
                #EquipmentTagsField(),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)


class PostGrid(Grid):

    POST_GRID_CLASS = unicode("post-grid")
    CREATE_TEMPLATE = unicode("Create Template")

    def __init__(self):
        super(PostGrid, self).__init__()
        self.append_class(self.POST_GRID_CLASS)

    def _set_grid_elements(self):
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

    def _set_grid_elements(self):
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

    def _set_grid_elements(self):
        fields = [
                Field(
                        "Name",
                        "name",
                        ""),
                Field(
                        "Rating",
                        "rating",
                        ""),
                Field(
                        "Details / Notes",
                        "notes",
                        ""),
                ]

        field_list = FieldList(fields)
        self.append_child(field_list)


class TagsGrid(TitledGrid):

    TAGS_GRID_CLASS = unicode("tags-grid")
    TAGS_TITLE = unicode("Tags")

    def __init__(self):
        super(TagsGrid, self).__init__(self.TAGS_TITLE)
        self.append_class(self.TAGS_GRID_CLASS)

    def _set_grid_elements(self):
        fields = [
                CategoryTagsField(),
                IndustryTagsField(),
                SkillTagsField(),
                EquipmentTagsField(),
                ]

        self.append_child(FieldList(fields))


class ProcessInstancePage(AltPage):

    PROCESS_INSTANCE_PAGE_ID = unicode("process-instance-page")

    def __init__(self):
        super(ProcessInstancePage, self).__init__()
        self.set_id(self.PROCESS_INSTANCE_PAGE_ID)

        contrast_section = ContrastSection()
        contrast_section.append_child(ProcessInstanceGrid())

        self.append_child(contrast_section)


class ProcessInstanceGrid(Grid):

    TASK_INSTANCE_GRID_CLASS = unicode("task-instance-grid")

    WELCOME_TEXT = unicode(
            "We checked out a number of tasks like yours that went "
            "well, and fine-tuned your description. We've also suggested a "
            "price below.")
    POST_TITLE = unicode("Post Your Task")

    def __init__(self):
        super(ProcessInstanceGrid, self).__init__()
        self.append_class(self.TASK_INSTANCE_GRID_CLASS)


    def _set_grid_elements(self):
        self.append_child(GridText(self.WELCOME_TEXT))
        self.append_child(TaskInstanceView())
