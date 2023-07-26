from astropy.coordinates import SkyCoord
from sunpy.coordinates import get_body_heliographic_stonyhurst
import matplotlib.pyplot as plt
import numpy as np
import math


from Util.Constants import AU, DAYSEC
from Util.Vector import Vector
from datetime import date
import astropy.units as u

from Api.NasaApi import NasaApi

from Bodies.Planet import *


class InitialConditions:
    """Use the Api to get, convert in good units, and return the initial conditions of bodies : the initial positions and velocities
    """

    def __init__(self, name, date:date):
        self.date = date
        self.api = NasaApi(name, date)
        self.initial_conditions = self.api.initial_conditions_request()

    def computePosition(self):
        """Compute the position of the planet to a given date

        :return: the position
        """
        self.position = Vector(self.initial_conditions['x'][0], self.initial_conditions['y'][0], self.initial_conditions['z'][0])* AU 
        return self.position

    def computeVeclocity(self):
        """Compute the velocity to a given date

        :return: the velocity
        """
        self.velocity = Vector(self.initial_conditions['vx'][0], self.initial_conditions['vy'][0], self.initial_conditions['vz'][0]) * AU / DAYSEC #numbers of sec per day
        return self.velocity


