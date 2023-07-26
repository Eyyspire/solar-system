from src.SolarSystem.SolarSystem import SolarSystem
from src.SolarSystem.MovementHandler import MovementHandler, COLLISION_SCOPE

import pytest

# change radius after


def test_collisions_are_detected():

    s = SolarSystem()
    a1 = s.createAsteroid(pos=(500,500,500), velocity=(50,50,50))
    a2 = s.createAsteroid(pos=(500 + (a1.radius + 1) + COLLISION_SCOPE - 1,500,500), velocity=(50,50,50))
    a3 = s.createAsteroid(pos=(500 + (a1.radius + 1) + COLLISION_SCOPE + 1,500,500), velocity=(50,50,50))
    assert s.movementHandler.detect_collision(a1,a2) == True
    assert s.movementHandler.detect_collision(a1,a3) == False


def test_smaller_bodies_are_destroyed():
    
    s = SolarSystem()
    a1 = s.createAsteroid(mass=200, pos=(5000,500,5 * 10**30), velocity=(0,0,0))
    a2 = s.createAsteroid(mass=1, pos=(5000 + COLLISION_SCOPE - 1 + a1.radius,500,5 * 10**30), velocity=(0,0,0))

    assert a1 in s.bodies
    assert a2 in s.bodies

    s.move()

    assert a1 in s.bodies
    assert a2 not in s.bodies