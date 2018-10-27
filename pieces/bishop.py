from piece import piece
from parameters import board_length
from board.board import Board


class Bishop (piece):
    def __init__(self, color, initPosition):
        piece.__init__(self, color, initPosition)

    def validMoves (self):
        position = self.position
        x = position[0]
        y = position[1]
        xDirection = [-1, 1]
        yDirection = [-1,1]