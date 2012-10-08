""" Module: deck

The investor deck.

"""
from base import BaseHandler


class DeckHandler(BaseHandler):

    """ Display our investor Deck. """


    def get(self):
        """ Overload BaseHandler's HTTP GET. """
        self.render("deck.html")
