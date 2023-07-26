class BodyGraphics:

    DISTANCE_SCALE = 1/ 10**10.5
    
    def __init__(self, texture, scale=1, bodyEntity = None):
        self.texture = texture
        self.size_scale = scale
        self.bodyEntity = bodyEntity

    def graphicsEntityScale(self, bodyEntity):
        return bodyEntity.body.pos.magnitude() * getattr(BodyGraphics, 'DISTANCE_SCALE')

    

    

