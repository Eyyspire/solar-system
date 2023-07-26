from Bodies.Body import Body
from Util.Vector import Vector

class Star(Body):

    def __init__(self, name="Sun", radius=1, mass=1, pos=Vector(0,0,0), velocity=Vector(0,0,0), sideralRotation = Vector(0,0,0)):
        super().__init__(name, radius, mass, pos, velocity, sideralRotation)