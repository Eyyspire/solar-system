from src.Bodies.Planet import Planet 
from tests.Bodies.test_Body import TestBody
from src.Util.Vector import Vector


class TestPlanet(TestBody):

    __test__ = True

    def createBody(self):
        return Planet('Tatooine', radius=10, mass=40, pos=Vector(10, 50, 30), velocity=Vector(10,20,0))

