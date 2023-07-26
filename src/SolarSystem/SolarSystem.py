import math
import itertools  
from datetime import date
from Api.Api import planets, sun, moon
from Bodies.Body import Body
from Bodies.Satellite import Satellite
from Bodies.Planet import Planet
from Bodies.Star import Star
from Bodies.Asteroid import Asteroid
from Util.Vector import Vector
from .Time import Time
from .MovementHandler import MovementHandler
from .InitialConditions import InitialConditions
from Display.BodyGraphics import BodyGraphics
from Controllers.TimeController import TimeController
from Controllers.DateEnteredController import DateEnteredController
from Controllers.DeletionController import DeletionController
from Controllers.AsteroidCreatorController import AsteroidCreatorController

import threading

class SolarSystem:

    def __init__(self, startingDate:date = date(1800, 7, 1)):
        # init bodies
        self.bodies  = []
        self.create_bodies()
         # init time
        self.time = Time(startingDate)  
        self.init_date(startingDate)
        # init pairs
        self.all_pairs()
        

        self.timeController = TimeController(self.time)
        self.time.addController(self.timeController)

        self.newDateEnteredController = DateEnteredController()
        self.newDateEnteredController.subscribe(self)

        self.deletionController = DeletionController()
        self.deletionController.subscribe(self)

        self.asteroidCreatorController = AsteroidCreatorController()
        self.asteroidCreatorController.subscribe(self)

        # init movement handler
        self.movementHandler = MovementHandler(self)

        self.created_asteroids_number = 0


    def create_bodies(self):
        """create all the bodies of the solar system
        """
        self.bodies.append(Star('Sun', sun['meanRadius']*1000, sun['mass']['massValue']*10**sun['mass']['massExponent'], Vector(0,0,0), Vector(0,0,0), sun['sideralRotation']))
        i = 0
        for e in planets:
            self.bodies.append(Planet(e['englishName'], e['meanRadius']*1000, e['mass']['massValue']*10**e['mass']['massExponent'], Vector((e['aphelion'] + e['perihelion'])/2*1000,0,0), Vector(0,e['velocity'],0), e['sideralRotation']))
            i+=1
        self.bodies.append(Satellite('Moon', radius = moon['meanRadius']*1000, mass = moon['mass']['massValue']*10**moon['mass']['massExponent'], pos = Vector((moon['aphelion'] + moon['perihelion'])/2*1000,0,0), velocity = Vector(0,moon['velocity'],0), sideralRotation = moon['sideralRotation'], aroundBody = "Earth"))
        self.basicBodies = self.bodies.copy()

    def createAsteroid(self, name="", radius=1, mass=1, pos=Vector(0,0,0), velocity=Vector(0,0,0)):
        """Create an asteroid with essential attributes

        :param name: name
        :param radius: radius
        :param mass: mass
        :param pos: position
        :param velocity: velocity
        :return: the newly created asteroid
        """
        if not name:
            name = f"asteroid_{self.created_asteroids_number}"
        asteroid = Asteroid(name, radius = radius, mass = mass, pos = Vector(pos[0], pos[1], pos[2]), velocity = Vector(velocity[0], velocity[1], velocity[2]))
        self.bodies.append(asteroid)
        self.all_pairs()
        self.created_asteroids_number += 1
        return asteroid


    def init_date(self, startingDate:date):
        """init the date attributes and all the elements directly depending on the date (the initial conditions of each body)

        :param startingDate: the startingDate
        """
        self.date = startingDate
        
        # threads = []
        # met à jour les conditions initiales 
        # for e in self.basicBodies:
        #     t = threading.Thread(target=self.init_initialConditions, args=(e,))
        #     threads.append(t)
        #     t.start()
        # for t in threads:
        #     t.join()   

        for e in self.basicBodies:
            self.init_initialConditions(e)
            
    def init_initialConditions(self, body): 
        """init the initial conditions for a given body : position and velocity. This will be set according to the date

        :param e: body
        """
        initialConditions = InitialConditions(body.name, self.date)
        body.pos = initialConditions.computePosition()
        body.velocity = initialConditions.computeVeclocity() 

    def changeDate(self, newDate):
        """Do all the necessary operations when the date is changed

        :param newDate: the new date (date_format)
        """
        self.date = newDate
        self.time.changeDate(newDate)
        self.bodies = self.basicBodies.copy()
        self.all_pairs()

    def move(self):
        """Call the movementHandler to move all the solarsytem bodies, and increase the value of time
        """
        self.movementHandler.move_all()
        self.time.increase()

    def all_pairs(self):
        """Compute all unique possible pairs among the bodies
        let a and b be two bodies, we consider the pairs (a,b) and (b,a) to be the sames.
        """
        self.pairs=[]
        for e in self.bodies:
            for f in self.bodies[self.bodies.index(e)+1:]:
                self.pairs.append((e,f))

    def distance(self, body1:Body, body2:Body) -> Vector:
        """give a vector representing the distance on each axis between two bodies
        a distance is here meant like the difference of coordinates between body1 and body2. Thus, it can be negative on any axis.

        :param body1: first body
        :param body2: second body
        :return: vector representing how to go from body1 to body2
        """
        return body1.distance(body2.pos)
    
    def newDateEntered(self, date):
        self.changeDate(date)
        self.init_date(date)

    def deleteBody(self, body):
        if body in self.bodies:
            self.bodies.remove(body)
            for e in self.bodies:
                if e.aroundBody == body.name:
                    e.aroundBody = None
            self.all_pairs()

    
    

        


    


    
