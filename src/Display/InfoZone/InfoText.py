from ursina import *
from Display.BodyEntity import BodyEntity

class InfoText:
    
    def __init__(self, x, y, handler, info, updateFunction, parent, unit="", size=0.05):
        """constructor of an info text

        :param x: x pos
        :param y: y pos
        :param handler: the object's text handler
        :param info: the body's info the text is displaying
        :param updateFunction: the function used to know what is displayed
        :param parent: the parent entity
        :param unit: the info's unit, defaults to ""
        :param size: the text size, defaults to 0.05
        """
        
        self.x = x
        self.y = y
        self.handler = handler
        self.info = info
        self.unit = unit
        self.updateFunction = updateFunction
        self.parent = parent
        self.size = size
        self.text = Text(x=x, y=y, parent=parent, size=size)
        self.body = None
        self.hide = False

    def erase(self):
        self.text.text = ""

    def displayText(self, object):
        
        self.text.text = f" {self.info} : {self.updateFunction(object)}"
        if self.unit:
            self.text.text += f" {self.unit}"
        