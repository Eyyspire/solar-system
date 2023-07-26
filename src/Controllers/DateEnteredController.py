from .Controller import Controller

class DateEnteredController(Controller):

    """Controller used to signal that a new date has been entered by a user
    """

    def __init__(self):
        super().__init__()

    def notify(self, subscribed, **kwargs):
        subscribed.newDateEntered(kwargs['date'])