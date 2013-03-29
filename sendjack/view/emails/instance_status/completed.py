"""
    instance_status.completed
    -------------------------

    Email customer after their task instance has been completed.

"""
from .base import InstanceStatusMessage


class CompletedInstanceMessage(InstanceStatusMessage):


    @property
    def subject(self):
        return unicode("Your task is done!")

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "You'll never guess what just happened...just kidding, you "
                "probably already figured it out. Your task is done!"
                ))
        paragraphs.append(unicode(
                "Now it's up to you to check out the results (files attached, "
                "content posted, packages delivered, etc.). As always, if you "
                "have questions, comments, or concerns about this task, just "
                "reply to this email thread. Jack will continue doing the "
                "same."
                ))
        paragraphs.append(unicode(
                "If you are satisfied, simply approve your task at the link "
                "below. Once this is done, your card will be charged."
                ))
        paragraphs.append(unicode("http://{}/tasks/{}/approve").format(
                self._domain,
                self._instance_id))

        return paragraphs
