from piece import *

class Game:
    def __init__(self, playerColor):
        self.pieces = dict()
        for i in range(8,16):
            self.pieces[i] = Pawn(-1, i, self)
        for i in range(48,56):
            self.pieces[i] = Pawn(1, i, self)
        self.pieces[0] = Rook(-1, 0, self)
        self.pieces[7] = Rook(-1, 7, self)
        self.pieces[56] = Rook(1, 56, self)
        self.pieces[63] = Rook(1, 63, self)

        self.playerColor = playerColor
        self.lastMove = (None, -1, -1)
        self.turn = 1