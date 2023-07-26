from ursina import *
from datetime import date
import Constants

TRANSPARENCY = 20
SCALE = (0.2, 0.4)
TEXT_SCALE = 10

class DateField(InputField):

    def __init__(self, **kwargs):
        super().__init__(
                         position = kwargs['position'],
                         parent = kwargs['parent'],
                         character_limit= kwargs['character_limit']
        )
        self.scale = SCALE
        self.text_field.scale = TEXT_SCALE

        self.color = color.rgba(100,100,100, TRANSPARENCY)
        self.limit_content_to = kwargs['limit_content_to']

        self.on_submit = print("ok")

        self.text_entity = Text(
            parent=self
        )

