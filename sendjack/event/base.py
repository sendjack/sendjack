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
        changed_objects = session.new.union(session.dirty)
        for object_ in changed_objects:
            self._trigger_attribute_change_events(object_)


    def _trigger_attribute_change_events(self, object_):
        for mapper_property in object_mapper(object_).iterate_properties:
            if isinstance(mapper_property, ColumnProperty):
                key = mapper_property.key
                attribute_state = inspect(object_).attrs.get(key)
                history = attribute_state.history

                if history.has_changes():
                    value = attribute_state.value
                    # old_value is None for session.new objects
                    old_value = self._get_old_value(attribute_state)
                    event = self._attribute_change_registry.get(
                            mapper_property)
                    if event:
                        handler = event.get_handler()
                        handler(object_, value, old_value)


    def _get_old_value(self, attribute_state):
        """Return old value for updated objects and None for new objects."""
        history = attribute_state.history
        return history.deleted[0] if history.deleted else None
