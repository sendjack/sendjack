"""
    status
    ------

    Template for status response emails.

"""
from jutil.errors import OverrideRequiredError


class StatusMessage(object):

    """Create an email message.

    Attributes
    ----------
    _domain : str
    _customer_first_name: str

    """

    def __init__(self, domain, customer_model):
        self._domain = domain
        self._customer_first_name = customer_model.first_name


    @property
    def subject(self):
        raise OverrideRequiredError()


    @property
    def body_text(self):
        return unicode("{}\n\n{}\n\n{}").format(
                self.salutation,
                self.construct_body_text_blob(),
                self.signature)


    #@property
    #def body_html(self):
    #    return unicode("")


    @property
    def salutation(self):
        salutation = unicode("Hi,")
        if self._customer_first_name is not None:
            salutation = unicode("Hi {},").format(self._customer_first_name)
        return salutation


    @property
    def valediction(self):
        return unicode("Let's get to work,")


    @property
    def signature(self):
        return unicode("{}\nJack\njack@sendjack.com").format(self.valediction)


    @property
    def paragraphs(self):
        raise OverrideRequiredError()


    def construct_body_text_blob(self):
        return unicode("\n\n").join(self.paragraphs)
