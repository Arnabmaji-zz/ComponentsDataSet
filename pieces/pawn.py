import piece


class Pawn:
    def __init__(self, color, number):
        self.color = color

        if color == 0:
            self.initPosition = (2, number)
        elif color == 1:
            self.initPosition = (7, number)