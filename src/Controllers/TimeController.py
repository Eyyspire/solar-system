from .Controller import Controller

class TimeController(Controller):

    """Controller used to signal to the displayer that the dtae has changed
    """

    def __init__(self, time):
        super().__init__()
        self.observed = time

    def notify(self, subscribed, **kwargs):
        subscribed.dateChangementUpdate(self.observed.date)