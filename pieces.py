RESET = '\033[0m'
WHITE = '\033[97m'
BLACK = '\033[30m'


class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def possible_moves(self, board):
        return []

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.first_move = True
        self.name = 'p'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    def possible_moves(self, pieces):
        direction = 1 if self.color == 'white' else -1
        row, column = self.position
        movements = []

        new_row = row + direction
        if 0 <= new_row < 8:
            movements.append((new_row, column))
        
        if (self.first_move):
            new_row = row + 2 * direction
            movements.append((new_row, column)) 
        for piece in pieces:
            if piece.position == (new_row, column):
                movements.remove(piece.position)

        #captura
        capture = [-1,1]

        for dc in capture:
            capture_pos = (row+direction, column + dc)
            if 0 <= capture_pos[0] < 8 and 0 <= capture_pos[1] < 8: 
                for piece in pieces:
                    if piece.position == capture_pos and piece.color != self.color:
                        movements.append(capture_pos)

        return movements

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = 'N'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    def possible_moves(self,pieces):
        directions = [
            (-2, 1), (-2, -1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
            ]
        movements = []
        row, column = self.position
        for i in directions:
            new_pos = (row + i[0], column + i[1])
            if 0 <= new_pos[0] < 8 and 0<= new_pos[1] < 8:
                movements.append(new_pos)

        for i in pieces:
            if i.position in movements:
                if i.color == self.color:
                    movements.remove(i.position)
        return movements
#to do
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = 'B'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    def possible_moves(self, pieces):
        directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
        row, column = self.position
        movements = []

        #to do
        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + dr*i, column + dc*i)
                if 0 < new_pos[0] <= 7 and 0 < new_pos[1] <= 7:
                    blocked = False

                    for piece in pieces:
                        if piece.position == new_pos:
                            if piece.color != self.color:
                                movements.append(new_pos)
                                blocked = True
                            elif piece.color == self.color:
                                blocked = True
                            break
                        

                    if blocked:
                        break
                    movements.append(new_pos)
        

        return movements
                        
#to do
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.first_move = True
        self.name = 'R'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    #to do
    def possible_moves(self):

        for i in pieces:
            if i.position in movements:
                movements.remove(i.position)
        return movements

#to do
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.name = 'Q'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    def possible_moves(self,pieces):
        for i in pieces:
            if i.position in movements:
                movements.remove(i.position)
        return movements

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.first_move = True
        self.name = 'K'

    def get_symbol(self):
        if self.color == 'white':
            return WHITE + self.name + RESET
        else:
            return BLACK + self.name + RESET

    def __str__(self):
        return self.get_symbol()

    def possible_moves(self, pieces):
        movements = []
        row, column = self.position
        for i in range(-1, 2):
            for j in range(-1,2):
                new_pos = (row + i, column + j)

                if new_pos == (row, column):
                    pass
                
                if 0<= new_pos[0] < 8 and 0<= new_pos[1] < 8:
                    movements.append(new_pos)
        for i in pieces:
            if i.position in movements:
                if i.color == self.color:
                    movements.remove(i.position)
        return movements

        return movements