from src.SolarSystem.SolarSystem import SolarSystem

from datetime import date

def test_venus_jupiter_align():
    s = SolarSystem()
    s.newDateEntered(date(2023,3,1))
    earth = s.bodies[3]
    venus = s.bodies[2]
    jupiter = s.bodies[5] 

    venus_jupiter_dist = venus.distance(jupiter.pos)
    earth_venus_dist =  earth.distance(venus.pos)

    venus_jupiter_dist_norm = venus_jupiter_dist.normalize()
    earth_venus_dist_norm = earth_venus_dist.normalize()

    assert venus_jupiter_dist_norm.x - earth_venus_dist_norm.x < 0.1
    assert venus_jupiter_dist_norm.y - earth_venus_dist_norm.y < 0.1
    assert venus_jupiter_dist_norm.z - earth_venus_dist_norm.z < 0.1