"""
    absolute
    --------

    A smallish set of absolute URL helper classes. Use these to avoid
    repetitive code, but do so knowing they may only be appropriate to use in
    certain contexts. For example, EmbeddableURL is probably only appropriate
    for the view.
"""
import settings

from .base import URL, PROTOCOL


class AbsoluteURL(URL):

    def __init__(self, host, port="", **kwargs):
        super(AbsoluteURL, self).__init__(
                protocol=PROTOCOL.HTTP,
                host=host,
                port=port,
                **kwargs)


class EmbeddableURL(AbsoluteURL):

    def __init__(self, path="", query=""):
        super(EmbeddableURL, self).__init__(
                settings.EMBEDDABLE_DOMAIN,
                settings.PORT,
                path=path,
                query=query)


class SecureEmbeddableURL(EmbeddableURL):

    def __init__(self, path="", query=""):
        super(SecureEmbeddableURL, self).__init__(path, query)
        self.set_protocol(PROTOCOL.HTTPS)

        # TODO: is this necessary? if not, remove it!
        #if not Deployment.is_prod():
        #    self.add_query_argument(PROTOCOL.HTTPS)


class ApproveTaskURL(EmbeddableURL):

    def __init__(self, id):
        super(EmbeddableURL, self).__init__(
                unicode("tasks/{}/approve").format(id))


class ConfirmTaskURL(EmbeddableURL):

    def __init__(self, id):
        super(EmbeddableURL, self).__init__(
                unicode("tasks/{}/confirm").format(id))
