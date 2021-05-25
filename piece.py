class Piece:
    def __init__(self, color, loc, pieces):
        self.color = color
        self.loc = loc
        self.pieces = pieces

    def moveTo(self, dest):
        self.pieces.pop(self.loc)
        self.loc = dest
        self.pieces[dest] = self

class Pawn(Piece):
    def __init__(self, color, loc, pieces):
        super().__init__(self, color, loc, pieces)
        self.val = 1
        self.hasMoved = False

    def validMoves():
        

    def validCaptures():
        pass

class Bishop(Piece):
    def __init__(self, color, loc, pieces):
        super().__init__(self, color, loc, pieces)
        self.val = 3

    def validMoves():
        pass

class Knight(Piece):
    def __init__(self, color, loc, pieces):
        super().__init__(self, color, loc, pieces)
        self.val = 3
