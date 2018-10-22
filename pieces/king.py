import piece


class King:
    def __init__(self, color):

        self.color = color

        if color == 0:
            self.initPosition = (4, 1)
        else:
            self.initPosition = (4, 8)

        self.position = self.initPosition