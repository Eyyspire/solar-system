from ursina import *
from .AsteroidParameters import AsteroidParameters

import threading
import time


HEIGHT = 0.5
WIDTH = 0.5

TRANSPARENCY_FULL = 0
TRANSPARENCY = 20

BUTTON_POSITION = (0,-0.23)
BUTTON_SIZE = 5
BUTTON_SCALE = (0.46, 0.2)

class AsteroidZone:

    def __init__(self, displayer):


        self.rectangle_position = (-window.right[0] + WIDTH/3, window.bottom[1] + HEIGHT/2)
        self.scale = (WIDTH, HEIGHT)
        self.starting_camera_position = camera.position

        self.initRectangle()
        self.displayer = displayer

        self.asteroid_infos = AsteroidParameters(self, self.displayer)

        self.launcher_mode = False

        self.position = (0,0,0)
        self.velocity = (0,0,0)

        
    def initRectangle(self):

        self.rectangle = Entity(
            model = "quad", 
            position = self.rectangle_position,
            scale = self.scale,
            visibility = True,
            parent=camera.ui,
            color = color.rgba(100,100,100, TRANSPARENCY_FULL)
        )

        self.button = Button(
            position = BUTTON_POSITION,
            parent = self.rectangle,
            size = BUTTON_SCALE,
            scale = BUTTON_SCALE,
            text = "Asteroid launcher" ,
            on_click = self.launch_mode,
        )

    def launch_mode(self):
        self.activate_asteroid_infos()
        t = threading.Thread(target = self.activate_launcher, args =())
        t.start()

    def activate_launcher(self):
        time.sleep(1/5)
        self.launcher_mode = not self.launcher_mode
        return
    
    def activate_asteroid_infos(self):
        self.asteroid_infos.visible = not self.asteroid_infos.visible
        if self.asteroid_infos.visible:
            self.button.text_color = color.green
        else:
            self.button.text_color = color.white



    def update(self):
        if self.launcher_mode and (held_keys["alt"] or held_keys["right mouse"]):
            if mouse.delta_drag[0] != 0 and mouse.delta_drag[1] != 0:
                self.position = [(mouse.position[i] - mouse.delta_drag[i]) for i in range(3)]
                self.velocity = [int(e * 3 * 10**5) for e in mouse.delta_drag]
                self.launch_asteroid()
                mouse.delta_drag = (0,0,0)


    def launch_asteroid(self):
        self.displayer.createAsteroid("", radius = self.asteroid_infos.params["radius"], mass = 10 ** self.asteroid_infos.params["mass"], pos = self.position, velocity = self.velocity, entity=True)



        