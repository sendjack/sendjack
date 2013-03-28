"""
    event factory
    -------------

    Event Factory for initializing all events.

"""
from .customer import CustomerEventFactory
from .instance import InstanceEventFactory
#import template
from .base import EventManager


def initialize():
    manager = EventManager()
    CustomerEventFactory(manager)
    InstanceEventFactory(manager)
    #template.initialize_events(manager)
