from Bodies.Body import Body
from Util.Vector import Vector

class Satellite(Body):

    def __init__(self, name="", radius=1, mass=1, pos=Vector(0,0,0), velocity=Vector(0,0,0), sideralRotation = Vector(0,0,0), aroundBody = None):
        super().__init__(name, radius, mass, pos, velocity, sideralRotation, aroundBody)