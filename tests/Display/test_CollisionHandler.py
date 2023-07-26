from src.Display.BodyEntity import BodyEntity
from src.Display.Displayer import SolarSystemDisplayer
from src.SolarSystem.SolarSystem import SolarSystem
from src.Bodies.Asteroid import Asteroid

from ursina import *
import pytest

import Constants

BODIES_NUMBER = 10

# app = Ursina()

class Test_CollisionHandler:

    def setup_method(self):
        s = SolarSystem()
        self.displayer = SolarSystemDisplayer(s)
        self.collider = self.displayer.collider

    def collisions_are_detected(self):
        pass