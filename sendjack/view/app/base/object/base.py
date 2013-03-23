"""
    Base Object View
    ----------------

    Base ObjectView and Field for subclassing.

"""
from view.elementary.html import Form


class ObjectView(Form):

    """Provide a view that corresponds to a model object. Provide a framework
    for coordinating the javascript Model/View classes."""

    _OBJECT_VIEW_CLASS = unicode("object-view")

    def __init__(self, object_id):
        super(ObjectView, self).__init__(object_id)
        self.append_class(self._OBJECT_VIEW_CLASS)

        self.set_id(object_id)
