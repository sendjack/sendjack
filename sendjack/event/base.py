"""
    base
    ----

    All model events that should trigger actions.

"""
from sqlalchemy import event as sqlalchemy_event
from sqlalchemy import inspect
from sqlalchemy.orm import object_mapper
from sqlalchemy.orm.properties import ColumnProperty

from jutil.errors import AlreadySetError

from model.data.database import db


class EventFactory(object):

    def __init__(self, manager):
        self._event_manager = manager


class Event(object):

    def __init__(self, key, handler):
        self._key = key
        self._handler = handler


    def get_key(self):
        return self._key


    def get_handler(self):
        return self._handler


class AttributeChangeEvent(Event):

    def __init__(self, attribute, handler):
        super(AttributeChangeEvent, self).__init__(attribute.property, handler)


class EventManager(object):

    """Manage all Object Events.

    Attributes
    ----------
    _attribute_change_registry: dict
        Key: attribute_property, Value: handler

    """

    def __init__(self):
        self._initialize_registries()

        session = db().session()
        sqlalchemy_event.listen(session, "after_flush", self.on_after_flush)

        # TODO: Do certain properties need active_history=True?


    def _initialize_registries(self):
        self._attribute_change_registry = {}


    def add_attribute_change_handler(self, event):
        self._add_event_to_registry(
                event,
                self._attribute_change_registry)


    def remove_attribute_change_handler(self, event):
        # TODO: allow for handlers to be removed
        pass


    def _add_event_to_registry(self, event, registry):
        key = event.get_key()
        if key in registry.keys():
            raise AlreadySetError()

        registry[key] = event


    def on_after_flush(self, session, flush_context):
        """ Trigger registered events for each changed object."""
        for changed_object in session.new.union(session.dirty):
            self._trigger_attribute_change_events(changed_object)


    def _trigger_attribute_change_events(self, changed_object):
        """ Trigger registered events for an object's changed attributes."""
        for property in object_mapper(changed_object).iterate_properties:
            # sanity check: does this property match a database column?
            if isinstance(property, ColumnProperty):
                self._trigger_attribute_change_event(changed_object, property)


    def _trigger_attribute_change_event(self, object_, property):
        """If an attribute has changed, trigger a registered event."""
        attribute_state = self._get_attribute_state(object_, property)

        if self._attribute_has_changed(attribute_state):
            self._invoke_attribute_change_event(
                    object_,
                    attribute_state,
                    self._get_attribute_change_event(property))


    def _invoke_attribute_change_event(self, object_, attribute_state, event):
        """Given a valid Event, get and execute its handler."""
        if event:
            event.get_handler()(
                    object_,
                    self._get_new_attribute_value(attribute_state),
                    self._get_old_attribute_value(attribute_state))


    def _get_attribute_state(self, object_, property):
        """Inspect an object for and return the state of an attribute."""
        return inspect(object_).attrs.get(property.key)


    def _attribute_has_changed(self, attribute_state):
        """Determine and return whether an attribute has changed."""
        return attribute_state.history.has_changes()


    def _get_attribute_change_event(self, property):
        """Return an AttributeChangeEvent object from the registry."""
        return self._attribute_change_registry.get(property)


    def _get_new_attribute_value(self, attribute_state):
        """Return current value for new and updated objects."""
        return attribute_state.value


    def _get_old_attribute_value(self, attribute_state):
        """Return old value for updated objects and None for new objects."""
        history = attribute_state.history
        return history.deleted[0] if history.deleted else None
