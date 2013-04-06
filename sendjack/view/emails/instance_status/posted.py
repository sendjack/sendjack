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
        paragraphs.append(unicode(
                "We got this. You relax. take a beat. Kick back a minute."
                ))
        paragraphs.append(unicode(
                "While you're doing that, we're getting started on your task. "
                "The worker we found to get it done will reach out to you "
                "shortly."
                ))
        paragraphs.append(unicode(
                "We'll get back in touch when it's completed by sending you "
                "an email with a link to approve the work. We won't charge "
                "your card until the task is approved."
                ))
        paragraphs.append(unicode(
                "Remember, once you have been notified the task is done, if "
                "we don't hear from you for two days we will assume you "
                "approve and automatically charge your card."
                ))
        paragraphs.append(unicode(
                "Thank you for using Jackalope to get your work done!"
                ))

        return paragraphs
