"""
    absolute
    --------

    A smallish set of absolute URL helper classes. Use these to avoid
    repetitive code, but do so knowing they may only be appropriate to use in
    certain contexts. For example, EmbeddableURL is probably only appropriate
    for the view.
"""
import settings
from jutil.environment import Deployment

from .base import URL, PROTOCOL


class AbsoluteURL(URL):

    def __init__(self, host, **kwargs):
        super(AbsoluteURL, self).__init__(
                protocol=PROTOCOL.HTTP,
                host=host,
                **kwargs)


class EmbeddableURL(AbsoluteURL):

    def __init__(self, path="", query=""):
        super(EmbeddableURL, self).__init__(
                settings.EMBEDDABLE_DOMAIN,
                path=path,
                query=query)


class SecureEmbeddableURL(EmbeddableURL):

    def __init__(self, path="", query=""):
        super(SecureEmbeddableURL, self).__init__(path, query)

        # we only own ssl certs for secure.sendjack.com. for now.
        self.set_host(settings.SSL_DOMAIN)

        # the protocol doesn't get set to https correctly in dev and
        # staging, so hack the query string to fake ssl for now.
        if Deployment.is_prod():
            self.set_protocol(PROTOCOL.HTTPS)
        else:
            self.add_query_argument(PROTOCOL.HTTPS)


class ApproveTaskURL(EmbeddableURL):

    def __init__(self, id):
        super(ApproveTaskURL, self).__init__(
                unicode("tasks/{}/approve").format(id))


class ConfirmTaskURL(EmbeddableURL):

    def __init__(self, id):
        super(ConfirmTaskURL, self).__init__(
                unicode("tasks/{}/confirm").format(id))
