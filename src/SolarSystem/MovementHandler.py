from Util.Vector import Vector
from Util.Laws import acceleration, force, total_acceleration

COLLISION_SCOPE = 1.92 * 10 **8 # moitié de la distance terre lune

class MovementHandler:

    """Handles the movements of the bodies in a given solar system
    """

    def __init__(self, system):
        self.system = system
        self.deletionController = system.deletionController

    def move_all(self):
        """Move all the objects of the system. Computes its acceleration according to the forces applied to it, and move the 
        objects according to the period of time given in the time class
        """
        self.all_attractions()
        for e in self.system.bodies:
            self.move(e)
        self.detect_collisions()

    def move(self, body):
        """Move a body. Computes its acceleration according to the forces applied to it, and move the 
        object according to the period of time given in the time class

        :param body: the body to move
        """
        a = Vector(0,0,0)
        a += total_acceleration(body.mass, self.attractions[body].values()) 
        body.velocity +=  a * self.system.time.dt
        body.move(self.system.time.dt)
        

    def all_attractions(self):
        """For each body, give a list that gives the attraction forces with each other body in the system
        """
        self.attractions = {}
        for e in self.system.bodies : 
            self.attractions[e] = {}
        for (a,b) in self.system.pairs:
            self.compute_attraction(a, b)

    def compute_attraction(self, a, b):
        """compute attraction force between two object

        :param a: body1
        :param b: body2
        """
        attraction = force(a.mass,b.mass, self.system.distance(a,b))
        # forced applied on a by b
        self.attractions[a][b] = attraction
        # forced applied on b by a
        self.attractions[b][a] = -attraction

    def detect_collisions(self):
        """detect the collision in the system
        """
        for a in self.system.bodies:
            for b in self.system.bodies[self.system.bodies.index(a)+1:]:
                is_there_collision = self.detect_collision(a,b)
                if (is_there_collision):
                    self.deletionController.collision(a, b)

    def detect_collision(self, a, b):
        """detect if there is a collision between the two bodies"""
        return a.distance(b.pos).magnitude() - (a.radius + b.radius) < COLLISION_SCOPE
        

    

    