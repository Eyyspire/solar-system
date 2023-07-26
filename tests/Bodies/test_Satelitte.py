from src.Bodies.Satellite import Satellite 
from tests.Bodies.test_Body import TestBody
from src.Util.Vector import Vector


class TestSatellite(TestBody):

    __test__ = True

    def createBody(self):
        return Satellite('Moon', radius=10, mass=40, pos=Vector(10, 50, 30), aroundBody=None, velocity=Vector(10,20,0))

