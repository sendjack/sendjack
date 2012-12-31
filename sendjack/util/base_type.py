"""
    base_type
    ---------

    A all-purpose module for working with base types.

"""

# Don't import constant because of circular dependencies.

UTF8 = unicode("utf8")


def to_unicode(anything, encoding=UTF8):
    """Convert *anything* to a unicode string using `unicode()` but return an
    empty unicode string if None."""
    new_unicode = unicode("")
    if anything is not None:
        if type(anything) is unicode:
            new_unicode = anything
        else:
            byte_string = str(anything)
            new_unicode = unicode(byte_string, encoding=encoding)

    return new_unicode


def to_integer(anything):
    """Convert *anything* to a string using `int()` but return None if
    None."""
    new_integer = None
    if anything is not None and anything != unicode(""):
        new_integer = int(anything)
    return new_integer


class UnicodeError(Exception):

    REASON = unicode("Expected unicode string but received byte string.")

    def __init__(self):
        super(UnicodeError, self).__init__(self.REASON)


class ByteError(Exception):

    REASON = unicode("Expected byte string but received unicode string.")

    def __init(self):
        super(ByteError, self).__init__(self.REASON)
