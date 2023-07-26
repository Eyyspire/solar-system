from src.Bodies.Body import Body 
from src.Bodies.Planet import Planet 
from src.Bodies.Star import Star 
from src.Util.Vector import Vector

from abc import ABC

# factory test 

class TestBody(ABC):

    __test__ = False

    def setup_method(self):
        self.body = self.createBody()
        self.initBodies()

    def createBody(self):
        pass

    def initBodies(self):
        self.body1 = Star('Sun', radius=10, mass=100,pos= Vector(0,0,0), velocity = Vector(0,0,0))
        self.body2 = Planet('Daggobah', radius=10, mass=40, pos=Vector(10, 50, 30), velocity = Vector(0,0,0))
        self.body3 = Planet('Hot', radius=10, mass=50, pos=Vector(20,-10,-50), velocity = Vector(0,0,0))
        self.list = [self.body1, self.body2, self.body3]

    def test_move(self):
        for i in range (20):
            pos = self.body.pos
            self.body.move(i)
            assert self.body.pos == pos + self.body.velocity * i

    def test_distance(self):
        for b in self.list:
            assert self.body.distance(b.pos) == b.pos - self.body.pos
