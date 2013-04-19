"""
    instance_status.process
    -----------------------

    Email customer that their task has been processed and is ready to confirm.

"""
from jutil.errors import OverrideRequiredError

from url.absolute import ConfirmTaskURL

from .base import InstanceStatusMessage


class ProcessedInstanceMessage(InstanceStatusMessage):


    @property
    def subject(self):
        return unicode("Confirm Your Task Details")


    @property
    def paragraphs(self):
        raise OverrideRequiredError()


class ControlProcessedInstanceMessage(ProcessedInstanceMessage):


    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "We're almost ready to get to work on your task, but we need "
                "you to confirm a few things."
                ))
        paragraphs.append(unicode(
                "Please confirm the task details, including price, so we can "
                "get to work right away."
                ))
        paragraphs.append(ConfirmTaskURL(self._instance_id))

        return paragraphs


class TestProcessedInstanceMessage(ProcessedInstanceMessage):


    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "We're almost ready to get to work on your task, but we need "
                "you to confirm a few things."
                ))
        paragraphs.append(unicode(
                "Jackalope turns every successful task into a reusable recipe "
                "for getting work done. We checked out tasks just like yours "
                "that went really well in order to fine-tune the description "
                "and suggest a price."
                ))
        paragraphs.append(unicode(
                "Please check out our suggestions, make necessary edits, and "
                "confirm the task details so we can get to work right away."
                ))
        paragraphs.append(ConfirmTaskURL(self._instance_id))

        return paragraphs
