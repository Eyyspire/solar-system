from src.Display.BodyEntity import BodyEntity
from src.Display.Displayer import SolarSystemDisplayer
from src.SolarSystem.SolarSystem import SolarSystem
from src.Bodies.Asteroid import Asteroid

from ursina import *
import pytest

import Constants

BODIES_NUMBER = 10

# app = Ursina()

class Test_SolarSystemDisplayer:

    def setup_method(self):
        s = SolarSystem()
        self.displayer = SolarSystemDisplayer(s)

    def test_initEntities_creates_good_number_of_entities(self):
        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER
        assert len(self.displayer.basicBodyEntities) == Constants.BODIES_NUMBER

    def test_initEntity_adds_new_body(self):
        asteroid = Asteroid()
        self.displayer.initEntity(asteroid, 1)
        assert len(self.displayer.basicBodyEntities) == Constants.BODIES_NUMBER
        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER + 1
        assert asteroid == self.displayer.bodyEntities[Constants.BODIES_NUMBER].body

    def test_delete_bodyEntity(self):

        sun = self.displayer.bodyEntities[0].body
        neptune = self.displayer.bodyEntities[8].body
        mercury = self.displayer.bodyEntities[1].body
        moon = self.displayer.bodyEntities[9].body

        assert len(self.displayer.solarsystem.bodies) == Constants.BODIES_NUMBER
        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER

        self.displayer.deleteBody(sun)

        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER -1

        self.displayer.deleteBody(neptune)

        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER -2

        assert mercury == self.displayer.bodyEntities[0].body
        assert moon == self.displayer.bodyEntities[Constants.BODIES_NUMBER -3].body




    def test_delete_bodyEntity_does_nothing_if_not_in_list(self):
        asteroid = Asteroid()
        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER
        self.displayer.deleteBody(asteroid)
        assert len(self.displayer.bodyEntities) == Constants.BODIES_NUMBER

    def test_find_body_works(self):
        mercury = self.displayer.bodyEntities[1].body
        moon = self.displayer.bodyEntities[9].body
        mercuryEntity = self.displayer.findBodyEntityAccordingToBody(mercury)
        moonEntity = self.displayer.findBodyEntityAccordingToBody(moon)
        assert mercuryEntity.body == mercury
        assert moonEntity.body == moon


    def test_find_body_raises_error_if_not_in_bodies(self):
        asteroid = Asteroid()
        with pytest.raises(Exception):
            asteroidEntity = self.displayer.findBodyEntityAccordingToBody(asteroid)