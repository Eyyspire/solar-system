from ursina import *

LEFT = -0.5
RIGHT = 0.5
UP = 0.5

PADDING_LEFT = 0.3
PADDING_UP = -0.2

SLIDER_GAP = 0.2

DEFAULT_RADIUS = 500
DEFAULT_MASS = 10

class AsteroidParameters(Entity):

    def __init__(self, zone, displayer):

        super().__init__()

        self.visible = False

        self.zone = zone
        self.parent = zone.rectangle

        self.displayer = displayer 

        self.sliders = {}
        self.sliders["radius"] = Slider(1, 2000, step=1, default = DEFAULT_RADIUS, dynamic=False, on_value_changed = lambda : self.asteroid_parameter_changement("radius"), position=(LEFT + PADDING_LEFT, UP + PADDING_UP), scale=1.2, background = True,thumb_texture='slider_thumb', bar_texture='slider_bar', parent=self)
        self.sliders["mass"] = Slider(1, 31, dynamic=False, default = DEFAULT_MASS, on_value_changed = lambda : self.asteroid_parameter_changement("mass"), position=(LEFT + PADDING_LEFT, UP + PADDING_UP- SLIDER_GAP), scale=1.2, background = True,thumb_texture='slider_thumb', bar_texture='slider_bar', parent=self)

        self.sliders["radius"].label = Text(parent=self.sliders["radius"], origin=(-0.6, 0), y=-0.05, text="radius in kilometers", visible = True, scale=1)
        self.sliders["mass"].label = Text(parent=self.sliders["mass"], origin=(-0.5, 0), y=-0.05, text="mass exponent : 10 powered to the slider value (kg)", visible = True, scale=1)
        
        self.default_values = {
            "radius" : DEFAULT_RADIUS,
            "mass" : DEFAULT_MASS,
        }

        self.params = {
            "radius" : self.default_values["radius"],
            "mass" : self.default_values["mass"],
        }

        self.text_info = Text(parent=self, scale = 1.5, position=(LEFT + PADDING_LEFT, UP), text="press ALT + mouse click to send an asteroid")


    def asteroid_parameter_changement(self, param):
        """sliders changement function. It updates the future asteroid parameters

        :param param: the parameter to update
        """
        self.params[param] = self.sliders[param].value
