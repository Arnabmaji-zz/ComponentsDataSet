from pieces import *


class Board:
    def __init__(self):
        pieces = []
        colors = [0, 1]

        for i in colors:
            pieces.append(king.King(i))
            pieces.append(queen.Queen(i))
            for j in range(1,3):
                pieces.append(bishop.Bishop(i, j))
                pieces.append(rook.Rook(i))
                pieces.append(knight.Knight(i, j))
            for j in range(1, 9):
                pieces.append(pawn.Pawn(i, j))

        self.pieces = pieces
        self.initPieces = pieces