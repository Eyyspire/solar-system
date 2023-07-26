from ursina import *
from .BodyEntity import BodyEntity
from SolarSystem.SolarSystem import SolarSystem
from .CameraHandler import CameraHandler
from datetime import date
from Bodies import Satellite
from Display.InfoZone.InfoZone import InfoZone
from .SliderHandler import Slider_dt
from .DateInput.DateInputHandler import DateInputHandler
from Display.AsteroidZone.AsteroidZone import AsteroidZone
from .BodyGraphics import BodyGraphics
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from .CollisionHandler import CollisionHandler
from .PositionComputer import PositionComputer
 
import Constants

"""
ORDRE : 

Sun

Mercury
Venus
Earth
Mars
Jupiter
Saturne
Uranus
Neptune

Moon
"""

SIZE_SCALES = [1, 0.2, 0.25, 0.3, 0.25, 0.8, 0.6, 0.6, 0.6, 0.08]
ASTEROID_SCALE = 0.2

ROTATION_X = 0
ROTATION_Y = 0.1

LEFT_POS_X = - (Constants.WINDOW_SIZE + 0.15)

DATE_INPUT_POS = (LEFT_POS_X, Constants.WINDOW_SIZE - 0.1)
DATE_INPUT_SCALE = (0.5, 0.2)

SLIDER_DATE_INPUT_POS = (-0.85, 0.2)

SCALE_DISPLAY = 1/ 10**10.5

ASTEROID_SCALE_DISPLAY = 12**10.5


class SolarSystemDisplayer(Entity):

    def __init__(self, solarsystem:SolarSystem = SolarSystem(), scale_size=1, scale_dist=1, scale_dist_satellites=10):
        super().__init__()
        self.solarsystem = solarsystem
        self.bodies = solarsystem.bodies
        self.positionComputer = PositionComputer(self, scale_size, scale_dist, scale_dist_satellites)
        self.initCamera()
        self.initSky()
        self.initEntities()
        self.sliderHandler = Slider_dt(self, pos = SLIDER_DATE_INPUT_POS, scale_x = DATE_INPUT_SCALE[1] * 3.1)
        self.infos = InfoZone(self)


        self.asteroidZone = AsteroidZone(self)

        # additional infos should be updated
        self.frozen = False

        self.dateInputHandler = DateInputHandler(self, pos = DATE_INPUT_POS, scale = DATE_INPUT_SCALE)

        self.solarEntity = Entity()

        self.solarsystem.deletionController.subscribe(self)

        self.collisionHandler = CollisionHandler(self)

        self.asteroidCreatorController = self.solarsystem.asteroidCreatorController




    def initCamera(self):
        """ init the app's camera
        """
        self.camera = CameraHandler(self)

    def initSky(self):
        """ init the app's background
        """
        self.sky = Sky(texture='Stars')

    def initEntities(self):
        """b.graphics.scale -> proportoinnal to sun scale
        """
        self.bodyEntities = []
        for (index, b) in enumerate(self.bodies):
            self.initEntity(b, SIZE_SCALES[index]) 
        self.basicBodyEntities =[]
        self.basicBodyEntities.extend(self.bodyEntities)

    def initEntity(self, body, size_scale, textureName=None):
        """init an entity

        :param body: body
        :param distance_scale: the distance scale on the graphics
        :param size_scale: the entity scale on the graphics
        """
        if not textureName : textureName = body.name 
        graphics = BodyGraphics(textureName, size_scale)
        bodyEntity = BodyEntity(self, name = body.name, model='sphere', color = color.white, body = body, graphics = graphics)
        graphics.bodyEntity = bodyEntity
        bodyEntity.position = self.positionComputer.computePosition(bodyEntity)
        self.bodyEntities.append(bodyEntity)
        return bodyEntity

    def createAsteroid(self, name, radius, mass, pos, velocity, entity=False):
        """Create an asteroid with some attributes

        :param name: name
        :param name: radius
        :param mass: mass
        :param pos: asteroid position
        :param velocity: asteroid velocity
        """
        if entity:
            pos=[e * ASTEROID_SCALE_DISPLAY for e in pos]


        self.asteroidCreatorController.notify_all(name = name, radius=radius, mass=mass, pos=pos, velocity=velocity)
        asteroid = self.asteroidCreatorController.getLastAsteroidCreated()
        self.initEntity(asteroid, ASTEROID_SCALE * math.sqrt(radius)/50, textureName="Moon")
            
    
    def newDateEntered(self):
        """delete the additional bodies to init a new date
        """
        to_delete = [] 
        for e in self.bodyEntities:
                if e not in self.basicBodyEntities:
                    to_delete.append(self.deleteBodyEntity(e))
        self.bodyEntities = [e for e in self.bodyEntities if e not in to_delete] 

        

    def deleteBody(self, body):
        """delete a body, looking for its bodyEntity. Function called by the deletion controller

        :param body: the body to delete
        """
        try:
            bodyEntity = self.findBodyEntityAccordingToBody(body)
            to_delete = self.deleteBodyEntity(bodyEntity)
            if to_delete in self.bodyEntities:
                self.bodyEntities.remove(to_delete)
        except:
            print("already deleted")
        

    def deleteBodyEntity(self, bodyEntity):
        """delete a bodyEntity

        :param body: the bodyEntity to delete
        """
        bodyEntity.visible = False
        return bodyEntity

    def findBodyEntityAccordingToBody(self, body):
        """find the bodyEntity matching with the body

        :param body: the body
        :raises Exception: Exception if the bodyEntity does not exist
        :return: the bodyentity
        """
        bodyEntity = list(filter(lambda bodyEntity : bodyEntity.body == body, self.bodyEntities))
        if len(bodyEntity) == 0:
            raise Exception("body already deleted")
        else:
            return bodyEntity[0]
    
    def update(self):
        """update function that triggers each frame
        """
        self.solarsystem.move()
        for e in self.bodyEntities:
            if not self.frozen:
                e.position = self.positionComputer.computePosition(e)
                e.rotation_y += ROTATION_Y * self.sliderHandler.value
                e.rotation_x += ROTATION_X * self.sliderHandler.value
                self.collisionHandler.handle_collisions()
        self.camera.camera_update()
        self.infos.update()
        self.asteroidZone.update()

  

    
        
    







    

            



