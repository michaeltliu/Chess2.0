from game import *

class Piece:
    def __init__(self, color, loc, game):
        self.color = color
        self.loc = loc
        self.game = game
        self.pieces = game.pieces

    def moveTo(self, dest):
        temp = self.loc
        self.pieces.pop(self.loc)
        self.loc = dest
        self.pieces[dest] = self
        
        self.game.lastMove = (self, temp, dest)
        self.game.turn *= -1

class Pawn(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 1
        self.hasMoved = False

    def validMoves():
        moves = set()
        x = self.loc % 8
        y = self.loc // 8

        if self.color == 1:
            if self.loc > 7:
                if self.pieces.get(self.loc - 8) == None:
                    moves.add(self.loc - 8)
                if self.pieces.get(self.loc - 7) != None and onBoard(x + 1, y - 1):
                    moves.add(self.loc - 7)
                if self.pieces.get(self.loc - 9) != None and onBoard(x - 1, y - 1):
                    moves.add(self.loc - 9)
            if not self.hasMoved and self.pieces.get(self.loc - 16) == None:
                moves.add(self.loc - 16)
            if y == 3:
                lastMove = self.game.lastMove
                #if type(lastMove[0]) == Pawn and lastMove[1] 
                

        elif self.color == -1:
            if self.loc < 56:
                if self.pieces.get(self.loc + 8) == None:
                    moves.add(self.loc + 8)
                if self.pieces.get(self.loc + 7) != None and onBoard(x - 1, y + 1):
                    moves.add(self.loc + 7)
                if self.pieces.get(self.loc + 9) != None and onBoard(x + 1, y + 1):
                    moves.add(self.loc + 9)
            if not self.hasMoved and self.pieces.get(self.loc + 16) == None:
                moves.add(self.loc + 16)
            if y == 4:
                # En passant
                pass

    def moveTo(self, dest):
        super().moveTo(self, dest)
        self.hasMoved = True

class Bishop(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 3

    def validMoves():
        pass

class Knight(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 3

class Rook(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 5

class Queen(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 9

class King(Piece):
    def __init__(self, color, loc, game):
        super().__init__(color, loc, game)
        self.val = 999

def onBoard(x,y):
    return 0 <= x and x <= 7 and 0 <= y and y <= 7

def convertTo2D(loc):
    return 