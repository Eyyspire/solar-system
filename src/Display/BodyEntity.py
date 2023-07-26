from ursina import *

class BodyEntity(Entity):

    def __init__(self, displayer, name, model, color, body, graphics):
        self.body = body
        self.graphics = graphics
        self.displayer = displayer
        self.name = body.name
        super().__init__(model=model, scale=graphics.size_scale, texture=graphics.texture, color=color, collider='sphere')
        self.setMassCompactWriting()

    def setMassCompactWriting(self):
        """set the string that will be used to display the mass of the body.
        For example, 1809645 will set 1.92 * 10^6
        """
        scale = 0
        mass_copy = self.body.mass
        while mass_copy >= 10:
            mass_copy /= 10
            scale += 1
        unit = round((self.body.mass / 10**scale), 3)
        self.massCompactWriting = f"{unit} * 10^{scale}"
        

        