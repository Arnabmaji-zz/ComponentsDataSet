from piece import piece
from parameters import board_length


class Pawn(piece):
    def __init__(self, color, initPosition):
        piece.__init__(self, color, initPosition)