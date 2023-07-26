from .Constants import *
from .Vector import Vector


def acceleration(m, force_vector) -> Vector:
    """Compute acceleration modification of a body

    :param m: the mass (kg)
    :param force_vector: the force (N)
    :return: the vector acceleration (m/s²)
    """
    return force_vector/m

# do total_acceleration
def total_acceleration(m, attractions:list) -> Vector:
    return sum(attractions, Vector(0.0 ,0.0 ,0.0)) / m


def force(mass1, mass2, dist) -> Vector:
    """force applied on mass1 by mass2

    :param mass1: body the force is applied on
    :param mass2: body which applies the force
    :return: the force represented as a vector
    """
    if dist == Vector(0, 0, 0) :
        return Vector(0, 0, 0)
    dist_mag = (dist).magnitude()
    dist_norm = dist / dist_mag
    force_mag = G * (mass1 * mass2 / dist_mag ** 2)
    force_vec = dist_norm * force_mag
    return force_vec

