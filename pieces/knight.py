import piece


class Knight:
    def __init__ (self, color, number):
        self.color = color

        if number == 1:
            if color == 0:
                self.initPosition = (2,1)
            elif color == 1:
                self.initPosition = (2,8)
        elif number == 2:
            if color == 0:
                self.initPosition = (7,1)
            elif color == 1:
                self.initPosition = (7,8)

        self.position = self.initPosition