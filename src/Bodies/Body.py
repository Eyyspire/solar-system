import math

from Util.Vector import Vector

class Body:

    def __init__(self, name:str, radius:float, mass:float, pos, velocity, sideralRotation = None, aroundBody = "Sun"):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.velocity = velocity
        self.pos = pos
        self.sideralRotation = sideralRotation
        self.aroundBody = aroundBody

    def move(self, time=1):
        """Move the body according to a given period of time. Actualizes the body pos after the computing.

        :param time: the time in seconds, defaults to 1
        """
        self.pos = self.pos + (self.velocity * time)

    def distance(self, pos2=Vector(0,0,0)): 
        return pos2 - self.pos
    
    def findReferenceEntity(self, bodies):
        return list(filter(lambda b: b.name == self.aroundBody, bodies))[0]
    
    def findReferenceBodyAmongEntities(self, entities):
        return list(filter(lambda b: b.body.name == self.aroundBody, entities))[0]


