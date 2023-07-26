from .Controller import Controller

class AsteroidCreatorController(Controller):

    """Controller used to signal that a new body has been created
    """

    def __init__(self):
        super().__init__()

    def notify(self, subscribed, **kwargs):
        subscribed.createAsteroid(**kwargs)

    def getLastAsteroidCreated(self):
        """Get the last asteroid created by the calculator

        :return: the last asteroid created by the calculator
        """
        solarsystem = self.subscribers[0]
        return solarsystem.bodies[-1]