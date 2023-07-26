from ursina import *
from .InfoText import InfoText
from Display.BodyEntity import BodyEntity


LEFT = -0.5
UP = 0.5
RIGHT = 0.5
DOWN = -0.5

SIZE = 0.06
PADDING = SIZE + 0.01


class TextHandler:
    
    def __init__(self, infoZone):

        self.texts = {} 
        self.texts["name"] = InfoText(x= LEFT + PADDING, y= UP - PADDING, handler=self, info="name", updateFunction=lambda b : b.body.name, parent=infoZone.rectangle, size=SIZE)
        self.texts["radius"] = InfoText(x= LEFT + PADDING, y= UP - 2* PADDING, handler=self, info="radius", unit="km", updateFunction=lambda b : int(b.body.radius), parent=infoZone.rectangle, size=SIZE)
        self.texts["mass"] = InfoText(x= LEFT + PADDING, y= UP - 3* PADDING, handler=self, info="mass", unit="kg", updateFunction=lambda b : b.massCompactWriting, parent=infoZone.rectangle, size=SIZE)
        self.texts["velocity"] = InfoText(x= LEFT + PADDING, y= UP - 4* PADDING, handler=self, info="velocity", unit="km/s", updateFunction=lambda b : round(b.body.velocity.magnitude() / 1000, 2)  , parent=infoZone.rectangle, size=SIZE)

        self.default_text = "Survolez une entité pour obtenir ses informations"
        self.infoZone = infoZone

        self.body = None
        self.visible_texts = True
        
    def update(self):
        """Update all the infoText contained in the textHandler
        """
        for text in self.texts.values() :
            if isinstance(mouse.hovered_entity, BodyEntity):
                self.body = mouse.hovered_entity

            for (index, entity) in enumerate(self.infoZone.displayer.bodyEntities):
                if held_keys[str(index)] and held_keys['alt'] :
                    self.body = self.infoZone.displayer.bodyEntities[index] 

            if held_keys['e'] :
                self.body = None
                self.erase()

            if self.body :
                self.displayInfos()

    def displayInfos(self):
        """display all the infos about an entity in the differents info text zones
        """
        for e in self.texts.values():
            e.displayText(self.body)

    def hide_and_show(self):
        self.visible_texts = not self.visible_texts
        for e in self.texts.values():
            e.text.visible = self.visible_texts

    def erase(self):
        for e in self.texts.values():
            e.erase()


    

        


