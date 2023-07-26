from src.Display.BodyEntity import BodyEntity
from src.Display.Displayer import SolarSystemDisplayer
from src.Display.PositionComputer import PositionComputer
from src.SolarSystem.SolarSystem import SolarSystem
from src.Bodies.Asteroid import Asteroid

from ursina import *
import pytest

import Constants

class Test_PositionComputer:

    def setup_method(self):
        self.displayer = SolarSystemDisplayer()
        self.positionComputer = PositionComputer(self.displayer)


    def test_compute_standard_entity_position(self):
        mercuryEntity = self.displayer.bodyEntities[1]
        pos = self.positionComputer.computePosition(mercuryEntity)
        assert pos == (mercuryEntity.body.pos.normalize() * self.positionComputer.SCALE_DIST * mercuryEntity.graphics.graphicsEntityScale(mercuryEntity)).tuple()


    def test_compute_satellite_entity_position(self):
        moonEntity = self.displayer.bodyEntities[9]
        moon = moonEntity.body
        earthEntity = self.displayer.bodyEntities[3]
        earth = self.displayer.bodyEntities[3].body
        distance = moon.pos - earth.pos
        distanceOnGraphicsBetweenBoth = distance.normalize() * self.positionComputer.SCALE_DIST * moonEntity.graphics.graphicsEntityScale(moonEntity) / self.positionComputer.SCALE_DIST_SATELLITES
        assert self.positionComputer.computePosition(moonEntity) == (distanceOnGraphicsBetweenBoth + earthEntity.position).tuple()
