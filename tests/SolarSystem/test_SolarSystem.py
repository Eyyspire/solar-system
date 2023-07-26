from src.SolarSystem.SolarSystem import SolarSystem
from datetime import *
import src.Util.Constants as Constants
import src.Util.Vector as Vector
import src.Bodies.Asteroid as Asteroid

import Constants

class TestSolarSystem:

    def setup_method(self):
        self.solarSystem = SolarSystem()

    def test_bodies_are_well_created(self):
        assert len(self.solarSystem.bodies) == Constants.BODIES_NUMBER
        names_list = list(map(lambda body : body.name, self.solarSystem.bodies))
        names = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Moon"]
        assert names_list == names

    def test_create_Asteroid_creates_a_new_body(self):
        length = len(self.solarSystem.bodies)
        created = self.solarSystem.created_asteroids_number
        asteroid = self.solarSystem.createAsteroid("test", radius=5, mass=10)
        assert len(self.solarSystem.bodies) == length + 1
        assert self.solarSystem.created_asteroids_number == created + 1

    def test_delete_body(self):
        self.solarSystem.deleteBody(self.solarSystem.bodies[1])
        assert len(self.solarSystem.bodies) == Constants.BODIES_NUMBER - 1
        assert self.solarSystem.bodies[1].name != "Mercury"

    def test_delete_body_does_nothing_if_not_in_bodies(self):
        body = Asteroid.Asteroid()
        self.solarSystem.deleteBody(body)
        assert len(self.solarSystem.bodies) == Constants.BODIES_NUMBER 

    def test_delete_body_updates_around_body(self):
        moon = self.solarSystem.bodies[9]
        earth = self.solarSystem.bodies[3]
        assert moon.aroundBody == earth.name
        self.solarSystem.deleteBody(earth) 
        assert len(self.solarSystem.bodies) == Constants.BODIES_NUMBER - 1
        assert self.solarSystem.bodies[8].aroundBody == None



        


