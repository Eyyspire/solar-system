from src.Bodies.Star import Star
from src.Bodies.Planet import Planet
from src.Util.Vector import Vector
from src.Util.Laws import force, acceleration, total_acceleration
from src.Util.Constants import G

body1 = Star('Sun', 10, 100, Vector(0,0,0), Vector(0,0,0))
body2 = Planet('Daggobah', 10, 40, Vector(10, 50, 30), Vector(0,0,0))
body3 = Planet('Hot', 10, 50, Vector(20,-10,-50), Vector(0,0,0))

bodies = [body1, body2, body3] 
forces = [[force(bodies[i].mass, bodies[j].mass, bodies[i].distance(bodies[j].pos)) for j in range(len(bodies))] for i in range(len(bodies))] 

def test_force():
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            res = force(bodies[i].mass, bodies[j].mass, bodies[i].distance(bodies[j].pos))
            if i!=j:
                assert res == bodies[i].distance(bodies[j].pos).normalize() * (G * (bodies[i].mass *  bodies[j].mass / bodies[i].distance(bodies[j].pos).magnitude() ** 2))
            else:
                assert res == Vector(0,0,0)

def test_acceleration():
    for i in range(len(forces)):
        for j in range(len(forces)):
            assert acceleration(bodies[i].mass, forces[i][j]) == forces[i][j] / bodies[i].mass 

def test_total_acceleration():
    for i in range(len(bodies)):
        assert (total_acceleration(bodies[i].mass, forces[i]) - sum(forces[i], Vector(0,0,0)) / bodies[i].mass).round(10) == sum([acceleration(bodies[i].mass, forces[i][j]) for j in range(len(bodies))], Vector(0,0,0)).round(10)


