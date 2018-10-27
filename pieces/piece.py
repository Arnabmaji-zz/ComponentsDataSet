class piece:
    def __init__(self, color, initPosition):
        self.color = color
        self.position = initPosition

    def updatePosition (self, position):
        self.position = position