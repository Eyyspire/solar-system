from ursina import *
from dateutil.parser import parse
from dateutil.parser import ParserError
from datetime import date

from .DateField import DateField

import Constants

TRANSPARENCY = 20

BUTTON_SCALE = (0.5, 0.25)
BUTTON_Y = .26
BUTTON_TEXT_SCALE = 8


class DateInputHandler(Entity):

    def __init__(self, displayer, pos, scale):
        self.displayer = displayer

        super().__init__(position = pos, 
                         scale = scale,
                         model="quad",
                         parent = camera.ui,
                         color = color.rgba(100,100,100, 1)
                         )

        self.year = DateField(
            position=(-0.25, 0.2),
            parent= self,
            character_limit = 4,
            limit_content_to = '0123456789'
        )

        self.month = DateField(
            position=(0.1, 0.2),
            parent= self,
            character_limit = 2,
            limit_content_to = list(str(i) for i in range(13))
        )

        self.initButton()

        self.initFields()
        self.displayer.solarsystem.timeController.subscribe(self)

        self.newDateEnteredController = self.displayer.solarsystem.newDateEnteredController

    def initFields(self):
        """init the fields with the starting values
        """
        year = self.displayer.solarsystem.time.date.year
        month = self.displayer.solarsystem.time.date.month
        self.updateFields(year, month)

    def initButton(self):
        """Init the change date button, its button, and its legend
        """
        self.validate = Button('Change the date', 
                               scale= BUTTON_SCALE, 
                               highlight_scale = 1.2,
                               color = color.rgba(100,100,100, TRANSPARENCY),
                               position = (self.year.position[0]/2 + self.month.position[0]/2, self.year.position[1]/2 + self.month.position[1]/2),
                               y=-BUTTON_Y, 
                               on_click=self.submit, 
                               parent = self)
    
        self.validate.text_entity.text_scale = BUTTON_TEXT_SCALE
        self.validate.on_mouse_enter = self.button_on_mouse_enter
        self.validate.on_mouse_exit = self.button_on_mouse_exit

        self.button_legend = Text(text = 'This might takes a few seconds...',
              color = color.gray,
              position = (2 * Constants.BOX_LEFT / 3, Constants.BOX_BOTTOM),
              parent = self, 
              size = 50,
              scale = (1.5, 4),
              visible = False)

    def updateFields(self, year, month):
        """update the input fields with the given values

        :param year: current year
        :param month: current month
        """
        self.year.text = str(year)
        self.month.text = str(month)

        self.year.fit_to_text()
        self.month.fit_to_text()

    def dateChangementUpdate(self, date):
        """Time observer update
        """
        self.updateFields(date.year, date.month)

    def button_on_mouse_enter(self):
        self.button_legend.visible = True

    def button_on_mouse_exit(self):
        self.button_legend.visible = False
        
    def submit(self):
        """Updates the system with the date corresponding to the inputs
        """
        try:
            year = min(Constants.MAX_YEAR, max(int(self.year.text), Constants.MIN_YEAR))
            new_date = date(year, int(self.month.text), 1)
            self.year.text = str(year)
            self.newDateEnteredController.notify_all(date = new_date)
            self.displayer.updateCondition = True
            self.displayer.newDateEntered()
        except:
            print("Mauvaise date rentrée")
        