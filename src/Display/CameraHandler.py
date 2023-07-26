from ursina import *
from .BodyEntity import BodyEntity

ZOOM_SPEED = 0.5; 

class CameraHandler:

    def __init__(self, displayer):

        self.displayer = displayer
    
    def camera_update(self):
        """the keys and commands to use the camera
        """
        if held_keys['up arrow']:
            camera.position += (0, 0.1, 0)
        if held_keys['down arrow']:
            camera.position -= (0, 0.1, 0)
        if held_keys['left arrow']:
            camera.position -= (0.1, 0, 0)
        if held_keys['right arrow']:
            camera.position += (0.1, 0, 0)
        if held_keys['g']:
            camera.position += camera.forward * ZOOM_SPEED
        if held_keys['h']:
            camera.position -= camera.forward * ZOOM_SPEED

        for (index, element) in enumerate(self.displayer.bodyEntities):
            if held_keys[str(index)] and held_keys['alt']:
                camera.position = (element.position.x, element.position.y, camera.position.z)
                

        
