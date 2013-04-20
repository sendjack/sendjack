"""
    instance_status.completed
    -------------------------

    Email customer after their task instance has been completed.

"""
from url.absolute import ApproveTaskURL

from .base import InstanceStatusMessage


class CompletedInstanceMessage(InstanceStatusMessage):


    @property
    def subject(self):
        return unicode("Your task is done!")

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "Your task is done!"
                ))
        paragraphs.append(unicode(
                "Now it's up to you to check out the results (files attached, "
                "content posted, packages delivered, etc.)."
                ))
        paragraphs.append(unicode(
                "If you are satisfied, simply visit the link below to give "
                "the work your stamp of approval. Once this is done, your "
                "card will be charged."
                ))
        paragraphs.append(unicode(
                "If you do nothing for two days, we will assume you approve, "
                "and your card will be charged automatically."
                ))
        paragraphs.append(ApproveTaskURL(self._instance_id).render())
        paragraphs.append(unicode(
                "Thank you for using Jackalope to get your work done!"
                ))

        return paragraphs
