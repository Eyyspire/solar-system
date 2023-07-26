from src.SolarSystem.SolarSystem import SolarSystem
from src.SolarSystem.Time import Time

from src.Controllers.TimeController import TimeController

from datetime import *
import src.Util.Constants as Constants

class TestTime:

    def setup_method(self):
        self.time = TimeMock(date = date(2023,3,1), scale=24) # 24 hours
        self.time.addController(TimeController(self.time))
        self.time.notified = 0

    def test_increase_increases_date(self):
        t = self.time.t
        date = self.time.date
        self.time.increase()
        assert self.time.t == t + self.time.dt
        assert self.time.date == date + timedelta(0, seconds = self.time.dt)

    def test_increase_calls_controller_only_if_needed(self):
        self.time.increase()
        assert self.time.notified == 0
        
        for _ in range (29):
            self.time.increase()
        assert self.time.notified == 0
        self.time.increase()
        assert self.time.notified == 1
        
        for _ in range (29):
            self.time.increase()
        assert self.time.notified == 1
        self.time.increase()
        assert self.time.notified == 2


class TimeMock(Time):

    def __init__(self, date, scale):

        super(TimeMock, self).__init__(date, scale=scale)
        self.notified = 0

    def checkChange(self):
        if self.month != self.date.month:
            self.notified +=1