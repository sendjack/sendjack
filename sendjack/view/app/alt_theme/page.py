"""
    Main Pages
    ----------

    All the Pages for the Main series.
    <div class="page">

"""
from view.elementary.html import SubmitButton

from view.app.base.page import Page
from view.app.base.components import TitledGrid, Grid
from view.app.base.field import Field, FieldList
from view.app.base.field import IDField, TitleField, SummaryField
#from components import CreatorField
from view.app.base.field import InstructionsField, InstructionField
from view.app.base.field import PropertiesField, PropertyField
from view.app.base.field import OutputTypeField, OutputMethodField
from view.app.base.field import CategoryTagsField, IndustryTagsField
from view.app.base.field import SkillTagsField, EquipmentTagsField
from view.app.base.object import ObjectView

from .components import NormalSection, ContrastSection


class AltPage(Page):

    _ALT_PAGE_CLASS = unicode("alt-page")

    def __init__(self):
        super(AltPage, self).__init__()
        self.append_class(self._ALT_PAGE_CLASS)


class TaskTemplatePage(AltPage):

    _TEMPLATE_PAGE_ID = unicode("template-page")
    _TEMPLATE_ID = unicode("template")

    def __init__(self):
        super(TaskTemplatePage, self).__init__()
        self.set_id(self._TEMPLATE_PAGE_ID)

        template_view = ObjectView(self._TEMPLATE_ID)
        template_view.append_child(TaskTemplateNormalSection())
        template_view.append_child(TaskTemplateContrastSection())

        self.append_child(template_view)


class TaskTemplateNormalSection(NormalSection):

    def __init__(self):
        super(TaskTemplateNormalSection, self).__init__()

        self.append_child(MainTemplateGrid())
        self.append_child(PostGrid())


class MainFieldsGrid(TitledGrid):

    def __init__(self, title):
        super(MainFieldsGrid, self).__init__(title)


    def _append_grid_elements(self):
        self._append_fields()


    def _append_fields(self):
        self.append_child(self._construct_fields())


    def _construct_fields(self):
        pass


class MainTemplateGrid(MainFieldsGrid):

    _MAIN_TEMPLATE_GRID_CLASS = unicode("main-grid")
    _MAIN_TEMPLATE_TITLE = unicode("New Template")

    def __init__(self):
        super(MainFieldsGrid, self).__init__(self._MAIN_TEMPLATE_TITLE)
        self.append_class(self._MAIN_TEMPLATE_GRID_CLASS)


    def _construct_fields(self):
        return FieldList([
                IDField(),
                #CreatorField(),
                TitleField(True),
                SummaryField(True),
                InstructionsField(True),
                InstructionField(),
                PropertiesField(True),
                PropertyField(),
                OutputTypeField(),
                OutputMethodField(),
                #CategoryTagsField(),
                #IndustryTagsField(),
                #SkillTagsField(),
                #EquipmentTagsField(),
                ])


class PostGrid(Grid):

    _POST_GRID_CLASS = unicode("post-grid")
    _SUBMIT_TEXT = unicode("Create Template")

    def __init__(self):
        super(PostGrid, self).__init__()
        self.append_class(self._POST_GRID_CLASS)


    def _append_grid_elements(self):
        self.append_child(SubmitButton(self._SUBMIT_TEXT))


class TaskTemplateContrastSection(ContrastSection):

    def __init__(self):
        super(TaskTemplateContrastSection, self).__init__()

        self.append_child(DetailsGrid())
        self.append_child(WorkerGrid())
        self.append_child(TagsGrid())


class DetailsGrid(TitledGrid):

    _DETAILS_GRID_CLASS = unicode("details-grid")
    _GRID_TITLE = unicode("Details")

    def __init__(self):
        super(DetailsGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._DETAILS_GRID_CLASS)


    def _construct_fields(self):
        return FieldList([
                Field(
                    unicode("Min Price"),
                    unicode("min_price")),
                Field(
                    unicode("Max Price"),
                    unicode("max_price")),
                Field(
                    unicode("Min Overhead"),
                    unicode("min_overhead")),
                Field(
                    unicode("Max Overhead"),
                    unicode("max_overhead")),
                Field(
                    unicode("Min Interactions"),
                    unicode("min_interactions")),
                Field(
                    unicode("Max Interactions"),
                    unicode("max_interactions")),
                ])


class WorkerGrid(TitledGrid):

    _WORKER_GRID_CLASS = unicode("worker-grid")
    _GRID_TITLE = unicode("Worker")

    def __init__(self):
        super(WorkerGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._WORKER_GRID_CLASS)


    def _construct_fields(self):
        return FieldList([
                Field(
                    unicode("Name"),
                    unicode("name")),
                Field(
                    unicode("Rating"),
                    unicode("rating")),
                Field(
                    unicode("Details / Notes"),
                    unicode("notes")),
                ])


class TagsGrid(TitledGrid):

    _TAGS_GRID_CLASS = unicode("tags-grid")
    _GRID_TITLE = unicode("Tags")

    def __init__(self):
        super(TagsGrid, self).__init__(self._GRID_TITLE)
        self.append_class(self._TAGS_GRID_CLASS)


    def _construct_fields(self):
        return FieldList([
                CategoryTagsField(),
                IndustryTagsField(),
                SkillTagsField(),
                EquipmentTagsField(),
                ])
