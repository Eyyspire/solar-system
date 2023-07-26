from src.Bodies.Star import Star 
from tests.Bodies.test_Body import TestBody
from src.Util.Vector import Vector


class TestStar(TestBody):

    __test__ = True

    def createBody(self):
        return Star('Sun', radius=10, mass=40, pos=Vector(-10, -50, 30), velocity=Vector(0,0,0))

