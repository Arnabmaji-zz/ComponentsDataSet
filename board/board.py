from pieces import *


class Board:
    def __init__(self):
        self.pieceMap = {}

    def addPiece(self, piece, position):
        self.pieceMap[position] = piece