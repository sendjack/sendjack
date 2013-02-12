"""
    Mailgun Mailer
    --------------

    Send outgoing mail using requests and mailgun. This is a basic
    implementation to test integration.

"""

import requests

from jutil.decorators import constant
from jutil.environment import get_unicode, Deployment

MAILGUN_API_KEY = get_unicode(unicode("MAILGUN_API_KEY"))
MAILGUN_DOMAIN = get_unicode(unicode("MAILGUN_DOMAIN"))
MAILGUN_API_URL = unicode("https://api.mailgun.net/v2")
MAILGUN_MESSAGES_SUFFIX = unicode("messages")


class _Mail(object):

    """Mail constants for interacting with incoming mail from MailGun.

    http://documentation.mailgun.net/user_manual.html#receiving-messages

    """

    @constant
    def RECIPIENT(self):
        return "recipient"

    @constant
    def SENDER(self):
        return "sender"

    @constant
    def FROM(self):
        return "from"

    @constant
    def TO(self):
        return "to"

    @constant
    def SUBJECT(self):
        return "subject"

    @constant
    def BODY_TEXT(self):
        return "body-plain"

    @constant
    def BODY_HTML(self):
        return "body-html"

    @constant
    def BODY_TEXT_STRIPPED(self):
        return "stripped-text"

    @constant
    def BODY_HTML_STRIPPED(self):
        return "stripped-html"

    @constant
    def STRIPPED_SIGNATURE(self):
        return "stripped-signature"

    @constant
    def ATTACHMENT_COUNT(self):
        return "attachment-count"

    @constant
    def ATTACHMENT_X(self):
        return "attachment-x"

    @constant
    def TIMESTAMP(self):
        return "timestamp"

    @constant
    def TOKEN(self):
        return "token"

    @constant
    def SIGNATURE(self):
        return "signature"

    @constant
    def MESSAGE_HEADERS(self):
        return "message-headers"

    @constant
    def CONTENT_ID_MAP(self):
        return "content-id-map"

    @constant
    def TEXT(self):
        return "text"

    @constant
    def API(self):
        return "api"

MAIL = _Mail()


def default_sender_name():
    name = ""

    if Deployment.is_prod():
        name = "Jack Lope"
    elif Deployment.is_staging():
        name = "Jack Staging"
    elif Deployment.is_dev():
        name = "Jack Dev"

    return unicode(name)


def default_sender():
    return unicode("{} <{}>").format(
            default_sender_name(),
            get_unicode(unicode("JACKS_EMAIL")))


def send_message_from_jack(recipient, subject, body):
    """Send a smtp message using Mailgun's API with 'Jack Lope' as the sender
    and return the response dict.

    Parameters
    ----------
    recipient : `str`
        Formatted as "Name <email@domain.com>"
    subject : `str`
    body : `str`

    """
    sender = default_sender()
    return send_message(sender, recipient, subject, body)


def send_message_as_jack(sender_email, recipient, subject, body):
    """Send a smtp mesage using Mailgun's API with 'Jack Lope' as
    the name and the sender_email as the email, and return the response dict.

    Parameters
    ----------
    sender_email `str`
    recipient : `str`
        Formatted as "Name <email@domain.com>"
    subject : `str`
    body : `str`

    """
    sender_name = default_sender_name()
    sender = unicode("{} <{}>").format(sender_name, sender_email)
    return send_message(sender, recipient, subject, body)


def send_message(sender, recipient, subject, body):
    """Send a smtp message using Mailgun's API and return the response dict.

    Parameters
    ----------
    sender : `str`
        Formatted as "Name <email@domain.com>"
    recipient : `str`
        Formatted as "Name <email@domain.com>"
    subject : `str`
    body : `str`

    """
    data_dict = {
            MAIL.FROM: sender,
            MAIL.TO: [recipient],
            MAIL.SUBJECT: subject,
            MAIL.TEXT: body
            }
    url = unicode("{}/{}/{}").format(
            MAILGUN_API_URL,
            MAILGUN_DOMAIN,
            MAILGUN_MESSAGES_SUFFIX)
    response = requests.post(
            url,
            auth=(MAIL.API, MAILGUN_API_KEY),
            data=data_dict)

    return response.text
