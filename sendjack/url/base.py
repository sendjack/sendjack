"""
    base
    ----

    Generic and widely applicable URL class for generating URLs which are
    internal/external, relative/absolute, dev/staging/prod, etc.

"""
from urlparse import urlsplit, urlunsplit, urljoin, parse_qs
from urllib import urlencode

from jutil.decorators import constant
from jutil.environment import Deployment


class _PROTOCOL(object):

    @constant
    def HTTP(self):
        return "http"

    @constant
    def HTTPS(self):
        return "https"

PROTOCOL = _PROTOCOL()


class _HOST(object):

    @constant
    def DELIMITER(self):
        return ":"

HOST = _HOST()


class URL(object):

    """Provide a relatively thin wrapper around python's urlparse library to
    include an implicit understanding of the sendjack environment and to be a
    little bit smart about whether to produce a relative or absolute URL.

    Typically, an absolute URL is needed for an external URL, an internal URL
    with a different protocol (such as https), or an internal URL to be
    rendered out of context (such as in an email).

    Attributes
    ----------
    base : str
        Typically used to generate an absolute URL or test the current URI.
        When other URL parts are not specified, access is granted to the base
        parts through the protocol, host, path, query, and fragment properties.
        Once set, base cannot be modified in part using mutators for protocol,
        host, port, path, query, query_dict or fragment, but it can be replaced
        in its entirety using set_base. When other URL parts are specified,
        render urlparse.urljoin()s them with base.
    protocol : str
        Default "", which retains current request's protocol for relative URLs.
    host : str
        Default "", which retains current request's host for relative URLs.
    port : str
        With a leading ":" delimiter when present, this is appended to host. It
        is not stored as a member. Not supported for base because base cannot
        be modified in part once set.
    path : str
        Default "".
    query : str
        Default "".
    query_dict : dict
        An alternate way to specify query. Not stored as a member, but is
        returned as a property. Not supported for base because base cannot be
        modified in part once set.
    fragment : str
        Default "". For now, this is pretty much unused.
    """

    _base = ""
    _protocol = ""
    _host = ""
    _path = ""
    _query = ""
    _fragment = ""

    def __init__(self, **kwargs):
        self.set_protocol(kwargs.get("protocol", ""))
        self.set_host(kwargs.get("host", ""))
        self.set_path(kwargs.get("path", ""))
        self.set_query(kwargs.get("query", ""))
        self.set_fragment(kwargs.get("fragment", ""))

        # default None avoids appending ":" to path when port is empty.
        self.set_port(kwargs.get("port", ""))

        # default None avoids overwriting query with empty query_dict.
        self.set_query_dict(kwargs.get("query_dict", {}))

        # default None allows for explicit (but worthless) use of "" as base.
        self.set_base(kwargs.get("base", ""))


    def render(self):
        """Return the URL as a string either by urlparse.urlunsplit()ing the
        URL parts or, when a base URI is present, by urlparse.urljoin()ing the
        base URI and the unsplit URL parts. The former is meant for rendering
        relative URLs and the latter for rendering absolute URls, but each is
        capable of either. See the urlunsplit and urljoin docstrings."""
        url = urlunsplit([
                self._protocol,
                self._host,
                self._path,
                self._query,
                self._fragment,
                ])

        base = self._base.geturl()

        return urljoin(base, url) if base else url


    @property
    def protocol(self):
        if self._protocol:
            protocol = self._protocol
        elif self._base.geturl():
            protocol = self._base.scheme
        else:
            protocol = ""

        return protocol


    @property
    def host(self):
        if self._host:
            host = self._host
        elif self._base.geturl():
            host = self._base.netloc
        else:
            host = ""

        return host


    @property
    def path(self):
        if self._path:
            path = self._path
        elif self._base.geturl():
            path = self._base.path
        else:
            path = ""

        return path


    @property
    def query(self):
        if self._query:
            query = self._query
        elif self._base.geturl():
            query = self._base.query
        else:
            query = ""

        return query


    @property
    def query_dict(self):
        # keep_blank_values=True allows for boolean query strings with keys and
        # no values, like http://sendjack.com/tasks/1/confirm?secure.
        return parse_qs(self._query, True)


    @property
    def fragment(self):
        if self._fragment:
            fragment = self._fragment
        elif self._base.geturl():
            fragment = self._base.fragment
        else:
            fragment = ""

        return fragment


    @property
    def base(self):
        return self._base.geturl()


    def set_protocol(self, protocol):
        self._protocol = protocol


    def set_host(self, host):
        self._set_netloc(host, None)


    def set_port(self, port):
        self._set_netloc(None, port)


    def _set_netloc(self, host, port):
        parts = self._host.split(HOST.DELIMITER)

        if host:
            parts[0] = unicode(host)

        if port:
            if len(parts) > 1:
                parts.pop(1)
            parts.insert(1, unicode(port))

        self._host = HOST.DELIMITER.join(parts)


    def set_path(self, path):
        self._path = path


    def set_query(self, query):
        self._query = query


    def set_query_dict(self, query_dict):
        if query_dict:
            # doseq=True ensures query parameters from the original url are
            # preserved correctly after parse_qs returns them as tuples.
            self.set_query(urlencode(query_dict, True))


    def add_query_argument(self, key, value=""):
        query_dict = self.query_dict
        query_dict.update({key: value})
        self.set_query_dict(query_dict)


    def remove_query_argument(self, key):
        query_dict = self.query_dict
        query_dict.pop(key, None)
        self.set_query_dict(query_dict)


    def get_query_argument(self, key):
        return self.query_dict.get(key, None)


    def has_query_argument(self, key):
        return key in self.query_dict


    def set_fragment(self, fragment):
        self._fragment = fragment


    def set_base(self, uri):
        self._base = urlsplit(uri)


    def is_secure(self):
        # the protocol doesn't get set to https correctly in dev and
        # staging, so hack the query string to fake ssl for now.
        if Deployment.is_prod():
            return self.protocol == PROTOCOL.HTTPS
        else:
            return self.has_query_argument(PROTOCOL.HTTPS)
