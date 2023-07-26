class PositionComputer:
    
    def __init__(self, displayer, scale_size=1, scale_dist=1, scale_dist_satellites=1):
        self.displayer = displayer
        self.SCALE_SIZE = scale_size
        self.SCALE_DIST = scale_dist
        self.SCALE_DIST_SATELLITES = scale_dist_satellites
    
    def computePosition(self, bodyEntity):
        """Compute the position to display each frame

        :param body: the bodyEntity which have the position to be computed
        :return: the position
        """
        if bodyEntity.body.aroundBody == "Sun" or not bodyEntity.body.aroundBody: #planète classique ou astéroide
            return self.computeStandardEntityPosition(bodyEntity)
        else:
            return self.computeStalliteEntityPosition(bodyEntity)       

    def computeStandardEntityPosition(self, bodyEntity):
        """Compute the position for a standard entity

        :param bodyEntity: the entity
        :return: the position
        """
        return (bodyEntity.body.pos.normalize() * self.SCALE_DIST * bodyEntity.graphics.graphicsEntityScale(bodyEntity)).tuple()
    
    def computeStalliteEntityPosition(self, bodyEntity):
        """Compute the position for a satellite entity (we have to this, if not the display would be too horrible)

        :param bodyEntity: the entity
        :return: the position
        """
        referenceEntity = list(filter(lambda b: b.body.name == bodyEntity.body.aroundBody, self.displayer.bodyEntities))[0]
        distance = bodyEntity.body.pos - referenceEntity.body.pos
        distanceOnGraphicsBetweenBoth = distance.normalize() * self.SCALE_DIST * bodyEntity.graphics.graphicsEntityScale(bodyEntity) / self.SCALE_DIST_SATELLITES
        return (distanceOnGraphicsBetweenBoth + referenceEntity.position).tuple()