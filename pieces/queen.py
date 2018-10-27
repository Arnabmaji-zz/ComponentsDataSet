from piece import piece
from parameters import board_length


class Queen(piece):
    def __init__(self, color, initPosition):
        piece.__init__(self, color, initPosition)
