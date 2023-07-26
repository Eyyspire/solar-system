from ursina import *
from datetime import date
from Controllers.DateEnteredController import DateEnteredController
import Constants

TRANSPARENCY = 20

class Slider_dt(Slider) : 

    def __init__(self, displayer, pos, scale_x):
        self.displayer = displayer
        super().__init__(
            0, Constants.HOURDAY/2 , default=Constants.DEFAULT_SCALE, on_value_changed = self.slider_dt_change, dynamic=True, position=pos, scale=0.8, length=0.5, color=color.blue)
        
        self.initSlider() 
      

    def initSlider(self):
        """ init the slider the user may use in the app
        """
        self.label = Text(parent=self, origin=(-0.6, 0), y=-0.07, text="time interval in hours", visible = True)
        self.memory = self.value
        
    def slider_dt_change(self):
        """change the differential time value
        """
        self.displayer.solarsystem.time.dt = self.value 
        self.displayer.frozen = (self.value == 0)

    def update(self):
        super().update()

        self.visible_label()
        self.freeze()
        self.memorize()

    def visible_label(self):
        """Change the visibility of the slider
        """
        if mouse.hovered_entity in (self.knob, self.bg, self.label) :
            self.label.visible = True
        else:
            self.label.visible = False


    def freeze(self):
        if held_keys['f']:
            self.value = 0

        elif held_keys['r']:
            self.value = self.memory

    def memorize(self):
        if self.value != 0: self.memory = self.value

