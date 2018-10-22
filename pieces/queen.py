import piece


class Queen:
    def __init__(self, color):
        self.color = color

        if color == 0:
            self.initPosition = (5,1)
        elif color == 1:
            self.initPosition = (5,8)
