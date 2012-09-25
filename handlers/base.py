""" Module: base

Provide our base class for all Handlers in the Controller. In reality,
this subclasses tornado.web.RequestHandler to get all of Tornado's
Controller functionality.

Think of this as the one-stop shop for all the basic cookie, request
argument, user, etc. functionality that any handler in our ecosystem
would want access to.

Also included:

Simple class hierarchy for the controller's cookie functionality so that
handlers don't have to repeat work and can take advantage of a good API.

"""
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    """ Collect common handler methods.

    All handlers should be subclasses.

    """


    def get_current_user(self):
        """ Return current user from cookie or return None.

        Only override when authentication is required by a subclass.

        """
        return None
