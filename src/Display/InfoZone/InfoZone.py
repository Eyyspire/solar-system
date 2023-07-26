from ursina import *
from Display.BodyEntity import BodyEntity
from .TextHandler import TextHandler

import Constants

HEIGHT = 0.5
WIDTH = 0.5

TRANSPARENCY = 0

class InfoZone:

    def __init__(self, displayer):


        self.rectangle_position = (window.right[0] - WIDTH/2, window.top[1] - HEIGHT/2)
        self.scale = (WIDTH, HEIGHT)
        self.starting_camera_position = camera.position

        self.button_names = ["Hide", "Show"] 
        self.index_button = 0


        self.initRectangle()
       
        self.textHandler = TextHandler(self)

        self.displayer = displayer

       
        
    def initRectangle(self):
        """Init the Inzo Zone rectangle on the displayer
        """
        self.rectangle = Entity(
            model = "quad", 
            position = self.rectangle_position,
            scale = self.scale,
            parent=camera.ui,
            color = color.rgba(100,100,100, TRANSPARENCY)
        )

        self.hide_button = Button(
            text = self.button_names[self.index_button] ,
            position = (Constants.BOX_RIGHT - 0.15, Constants.BOX_TOP - 0.1),
            scale = (0.2, 0.1),
            parent=self.rectangle,
            visible = True,
            color = color.rgba(100,100,100, 20),
            on_click = self.button_function,
        )

    def button_function(self):
        self.index_button = (self.index_button + 1 ) % 2
        self.hide_button.text = self.button_names[self.index_button] 

        self.textHandler.hide_and_show()

    def update(self):
        self.textHandler.update()


        