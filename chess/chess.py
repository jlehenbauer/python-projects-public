import copy
class Board:
    BLACK = 0
    WHITE = 1
    TURN = 1

    def __init__(self):
        self.board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]]

    def set_standard(self):
        self.board = [
        [Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)],
        [Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
        [Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight(1), Rook(1)]]

    def __str__(self):
        s = '  +---+---+---+---+---+---+---+---+ \n'
        for y in range(len(self.board)):
            s += str(8 - y) + ' | '
            for x in range(len(self.board[y])):
                if self.board[y][x] is None:
                    s += '  | '
                else:
                    s += str(self.board[y][x]) + ' | '
            s += '\n  +---+---+---+---+---+---+---+---+ \n'
        s += '    a   b   c   d   e   f   g   h'
        return s

    def col(self, cha):
        return ord(cha) - 97

    def move(self, notation):
        if len(notation) == 2:
            # pawn move
            # Find appropriate pawn
            for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    piece = copy.deepcopy(self.board[y][x])
                    if self.col(notation[0]) == x and piece is not None:
                        if self.TURN == piece.color and piece.name == "Pawn":
                            print(f"moving {piece} to {notation}")
                            self.board[8 - int(notation[1])][x] = piece
                            self.board[y][x] = None
                            self.end_turn()
                            return True

        elif notation[0] == 'K':
            # King move
            pass
        elif notation[0] == 'Q':
            # Queen move
            pass
        elif notation[0] == 'R':
            # Rook move
            pass
        elif notation[0] == 'B':
            # Bishop move
            pass
        elif notation[0] == 'N':
            # Knight move
            pass


    def end_turn(self):
        if self.TURN:
            self.TURN = 0
        else:
            self.TURN = 1

class Piece:
    pass

class King(Piece):
    name = "King"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'K'
    
class Queen(Piece):
    name = "Queen"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'Q'
    
class Rook(Piece):
    name = "Rook"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'R'
    
class Bishop(Piece):
    name = "Bishop"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'B'
    
class Knight(Piece):
    name = "Knight"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'N'
    
class Pawn(Piece):
    name = "Pawn"
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'p'
