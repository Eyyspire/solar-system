from src.Display.BodyEntity import BodyEntity
from src.Display.Displayer import SolarSystemDisplayer
from src.SolarSystem.SolarSystem import SolarSystem
from src.Bodies.Asteroid import Asteroid

from ursina import *

class Test_BodyEntity:

    def setup_method(self):
        s = SolarSystem()
        d = SolarSystemDisplayer(s)
        self.entity = BodyEntity_Mock(Asteroid())

    def test_mass_compact_writing_works_fine(self):
        self.entity.body.mass = 25000
        self.entity.setMassCompactWriting()
        assert self.entity.massCompactWriting == "2.5 * 10^4"

        self.entity.body.mass = 1809645
        self.entity.setMassCompactWriting()
        assert self.entity.massCompactWriting == "1.81 * 10^6"

        
class BodyEntity_Mock(BodyEntity):

    def __init__(self, body):
        
        self.body = body