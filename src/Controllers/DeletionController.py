from .Controller import Controller

class DeletionController(Controller):

    """Controller used when bodies should be deleted
    """

    def __init__(self):
        super().__init__()

    def collision(self, bodyA, bodyB):
        self.notify_all(body = self.lightestBody(bodyA, bodyB))

    def notify(self, subscribed, **kwargs):
        subscribed.deleteBody(kwargs['body'])

    def lightestBody(self, bodyA, bodyB):
        """Returns the lightest body. It compares their mass attribute

        :param bodyA: first body
        :param bodyB: second body
        :return: the lightest body
        """
        if bodyA.mass <= bodyB.mass : 
            return bodyA
        else:
            return bodyB