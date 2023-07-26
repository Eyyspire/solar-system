from ursina import *

SCALE_POS_RATIO = 0.15
#Sun : scale = 1, pos at border : 0.06 

class CollisionHandler:

    def __init__(self, display):

        self.display = display
        self.deletionController = display.solarsystem.deletionController

    def handle_collisions(self):
        """Check if there are collisions on the displayer side
        Takes the position and the size_scale into consideration
        """
        for i, entityA in enumerate(self.display.bodyEntities):
            for entityB in self.display.bodyEntities[i+1:]:
                if (entityA.position - entityB.position).length() - abs(entityA.graphics.size_scale - entityB.graphics.size_scale) * SCALE_POS_RATIO < 0:
                    self.deletionController.collision(entityA.body, entityB.body)


