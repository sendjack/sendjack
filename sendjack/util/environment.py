"""
    Environmental Variables Utility
    -------------------------------

    A utility module for interacting with environmental variables.

"""

import os

from base_type import to_unicode, to_integer, UnicodeError


def get_unicode(key):
    """Look up a environmental variable by key and return a unicode string by
    decoding the byte string to unicode with utf8."""
    if type(key) is not unicode:
        raise UnicodeError()
    byte_string = os.environ.get(str(key))
    return to_unicode(byte_string)


def get_integer(key):
    """Look up an environmental variable by key and return an int."""
    if type(key) is not unicode:
        raise UnicodeError()
    byte_string = os.environ.get(str(key))
    return to_integer(byte_string)
