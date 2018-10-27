from piece import piece
from parameters import board_length


class King(piece):
    def __init__(self, color, initPosition):
        piece.__init__(self, color, initPosition)