"""
    customer_status.created
    -----------------------

    Sign up and created task instance email.

"""
from view.emails.status_message import StatusMessage


class CreatedCustomerMessage(StatusMessage):


    @property
    def subject(self):
        return unicode("Welcome to Jackalope!")

    @property
    def paragraphs(self):
        paragraphs = []
        paragraphs.append(unicode(
                "Thank you for signing up to use Jackalope to get your work "
                "done!"
                ))
        paragraphs.append(unicode(
                "We're looking into your task. We'll email you when it's "
                "ready to post."
                ))
        paragraphs.append(unicode(
                "If you have questions, comments, or concerns about this "
                "task, just reply to this email thread. Jack will do the same."
                ))

        return paragraphs
