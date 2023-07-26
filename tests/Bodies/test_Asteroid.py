from src.Bodies.Asteroid import Asteroid 
from tests.Bodies.test_Body import TestBody
from src.Util.Vector import Vector


class TestAsteroid(TestBody):

    __test__ = True

    def createBody(self):
        return Asteroid('Cérès', radius=10, mass=40, pos=Vector(-50, 40, 20), velocity=Vector(10,-20,30))

