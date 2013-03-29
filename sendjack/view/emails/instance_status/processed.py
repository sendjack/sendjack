"""
    instance_status.process
    -----------------------

    Email customer that their task has been processed and is ready to confirm.

"""
from .base import InstanceStatusMessage


class ProcessedInstanceMessage(InstanceStatusMessage):


    @property
    def subject(self):
        return unicode("Your task is prepared and ready to post.")


    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "We checked out a number of tasks like yours that went well, "
                "and Jack is ready to get started."
                ))
        paragraphs.append(unicode(
                "We've also fine-tuned your description to fit a format that "
                "has worked well for similar tasks. This should help Jack get "
                "your work done better and faster, but let us know if "
                "anything is off."
                ))
        paragraphs.append(unicode(
                "Please check out our write up and confirm the price:"
                ))
        paragraphs.append(unicode("http://{}/tasks/{}/confirm").format(
                self._domain,
                self._instance_id))

        return paragraphs
