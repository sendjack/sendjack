"""
    instance_status.posted
    ----------------------

    Email customer after they confirm a task to let them know what to expect.

"""
from .base import InstanceStatusMessage


class PostedInstanceMessage(InstanceStatusMessage):


    @property
    def subject(self):
        return unicode("We're on it.")

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode("We'll take it from here."))
        paragraphs.append(unicode(
                "The awesome worker we've found for you will reach out "
                "shortly. And we'll get back in touch when the work is "
                "completed."
                ))
        paragraphs.append(unicode(
                "If you have any questions, feel free to write back."
                ))

        return paragraphs
