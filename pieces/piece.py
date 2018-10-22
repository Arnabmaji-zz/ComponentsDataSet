class piece:
    def __init__(self, color):
        self.color = color

    def updatePosition (self, position):
        self.position = position

    def legalmoves(self, position):
        return