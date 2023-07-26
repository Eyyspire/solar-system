import Constants
from datetime import *

from Controllers.TimeController import TimeController

class Time:

    """Represents the time of our system : the amount of time that has passed, and the scale between each movement
    """

    def __init__(self, date, hour="00:01", scale=Constants.DEFAULT_SCALE):

        self.changeDate(date)
        self.hour = hour
        self._dt = scale * Constants.SECHOUR
        self.t = 0  
        self.month = self.date.month

    def changeDate(self, date):
        self.date = datetime(date.year, date.month, date.day, 0, 0, 1)

    def addController(self, timeController):
        self.timeController = timeController

    @property
    def dt(self):
        return self._dt
    
    @dt.setter
    def dt(self, scale):
        self._dt = scale * Constants.SECHOUR

    def increase(self):
        self.t += self.dt
        self.month = self.date.month
        self.date += timedelta(0, seconds = self.dt)
        self.checkChange()

    def checkChange(self):
        if self.month != self.date.month:
            self.timeController.notify_all()
