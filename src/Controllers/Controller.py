class Controller:

    """Define the controller architecture
    It uses the classical observer pattern"""

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_all(self, **kwargs):
        for e in self.subscribers:
            self.notify(e, **kwargs)

    def notify(self, e, **kwargs):
        pass
