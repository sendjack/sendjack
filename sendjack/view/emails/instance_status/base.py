"""
    instance_status.base
    --------------------

    Base instance status email to subclass from.

"""
from view.emails.status_message import StatusMessage


class InstanceStatusMessage(StatusMessage):

    """Create an instance triggered message.

    Attributes
    ----------
    _instance_id : id

    """

    def __init__(self, customer_model, instance_model=None):
        super(InstanceStatusMessage, self).__init__(customer_model)
        self._instance_id = instance_model.id
