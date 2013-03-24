"""
    Base Object View
    ----------------

    Base ObjectView and Field for subclassing.

"""
from jutil.errors import OverrideRequiredError
from view.elementary.html import Form, SubmitButton

from .field import FieldList, Field


class ObjectView(Form):

    """Provide a view that corresponds to a model object. Provide a framework
    for coordinating the javascript Model/View classes."""

    _OBJECT_VIEW_CLASS = unicode("object-view")
    _SUBMIT_TEXT = unicode("Submit")

    allowed_fields = []

    def __init__(
            self,
            object_type_class,
            object_view_id=None,
            submit_text=None):
        super(ObjectView, self).__init__(
                self._get_object_view_id(object_view_id))
        self.append_class(self._OBJECT_VIEW_CLASS)

        self.append_class(object_type_class)
        if submit_text is None:
            submit_text = self._SUBMIT_TEXT

        self.append_child(FieldList(self._construct_fields()))
        self.append_child(self._construct_submit_button(submit_text))


    def _get_object_view_id(self, object_view_id):
        if object_view_id is None:
            object_view_id = self._OBJECT_VIEW_ID
        return object_view_id


    def _construct_fields(self):
        """Return list of Fields."""
        raise OverrideRequiredError()


    def _construct_submit_button(self, submit_text):
        return SubmitButton(submit_text)


    def append_child(self, element):
        if not self._is_child_allowed(element):
            raise ObjectFieldNotAllowedError(element)

        super(ObjectView, self).append_child(element)


    def insert_child(self, element, index=0):
        if self._is_child_allowed(element):
            self.insert_child(element, index)
        else:
            raise ObjectFieldNotAllowedError(element)


    def _is_child_allowed(self, element):
        """Return True if child and descendents that are fields are allowed by
        object view."""
        is_allowed = True

        child_and_descendants = [element]
        child_and_descendants.extend(element.descendants())

        for e in child_and_descendants:
            if isinstance(e, Field):
                is_allowed = self._is_field_allowed(e)

        return is_allowed


    def _is_field_allowed(self, field):
        is_field_allowed = False
        if field in self.allowed_fields:
            is_field_allowed = True
        return is_field_allowed


class ObjectFieldNotAllowedError(Exception):

    """Throw error if field is not allowed by object view."""

    _REASON = unicode("This field is not allowed with this object.")

    def __init__(self, field):
        super(ObjectFieldNotAllowedError, self).__init__(
                unicode("{}: {}").format(self._REASON, field.get_key_name()))
