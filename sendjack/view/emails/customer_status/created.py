"""
    customer_status.created
    -----------------------

    Sign up and created task instance email.

"""
from jutil.errors import OverrideRequiredError

from view.emails.status_message import StatusMessage


class CreatedCustomerMessage(StatusMessage):


    @property
    def subject(self):
        return unicode("Welcome to Jackalope!")

    @property
    def paragraphs(self):
        raise OverrideRequiredError()


class ControlCreatedCustomerMessage(CreatedCustomerMessage):

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "Best. Decision. Ever."
                ))
        paragraphs.append(unicode(
                "Thank you for using Jackalope to get your work done!"
                ))
        paragraphs.append(unicode(
                "We're checking out tasks just like yours that went really "
                "well in order to suggest a price and find the right worker."
                ))
        paragraphs.append(unicode(
                "Watch your inbox. Soon we will send you an email with a link "
                "to confirm the details. It shouldn't be long."
                ))
        paragraphs.append(unicode(
                "You're about to be a whole lot more productive. And awesome. "
                "Tell your friends."
                ))

        return paragraphs


class TestCreatedCustomerMessage(CreatedCustomerMessage):

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "Best. Decision. Ever."
                ))
        paragraphs.append(unicode(
                "Thank you for using Jackalope to get your work done!"
                ))
        paragraphs.append(unicode(
                "We're checking out tasks just like yours that went really "
                "well in order to fine-tune the description and suggest a "
                "price."
                ))
        paragraphs.append(unicode(
                "Watch your inbox. Soon we will send you an email with a link "
                "to confirm the details. It shouldn't be long."
                ))
        paragraphs.append(unicode(
                "You're about to be a whole lot more productive. And awesome. "
                "Tell your friends."
                ))

        return paragraphs
