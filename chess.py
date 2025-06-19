from pieces import *

class Board():
    def __init__(self):
        self.rows_cords = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7
            }
        self.pieces = []
        self.board= [[None for _ in range(8)] for _ in range(8)]

    def update_board(self):
        self.board= [[None for _ in range(8)] for _ in range(8)]
        for peca in self.pieces:
            l, c = peca.position
            self.board[l][c] = peca

    def init_board(self):
            for i in range(8):
                #self.pieces.append(Pawn('white', (1, i)))
                self.pieces.append(Pawn('black', (6, i)))
            self.pieces.append(Queen('white',(0,3)))
            self.pieces.append(King('white',(0,4)))
            self.pieces.append(Knight('white',(0,1)))
            self.pieces.append(Knight('white',(0,6)))
            self.pieces.append(Rook('white',(0,0)))
            self.pieces.append(Rook('white',(0,7)))
            self.pieces.append(Bishop('white',(0,2)))
            self.pieces.append(Bishop('white',(0,5)))

            #black
            self.pieces.append(Queen('black',(7,3)))
            self.pieces.append(King('black',(7,4)))
            self.pieces.append(Knight('black',(7,1)))
            self.pieces.append(Knight('black',(7,6)))
            self.pieces.append(Rook('black',(7,0)))
            self.pieces.append(Rook('black',(7,7)))
            self.pieces.append(Bishop('black',(7,2)))
            self.pieces.append(Bishop('black',(7,5)))

            
    def show(self):
        self.update_board()
        c=1
        for row in self.board:
            print(c, end='.|')
            for square in row:
                if square:
                    print(f'{str(square)} |', end="")
                else: 
                    print('  |', end='') 
            
            c+=1
            print()
            print("---------------------------")

        print("  |A |B |C |D |E |F |G |H |")

    def isValid(self, piecePos, move):
        
        piece = None
        if self.board[piecePos[0]][piecePos[1]]:
            piece = self.board[piecePos[0]][piecePos[1]]
        if piece:
            if piece.name == "N":
                directions = [
                    (-2, 1), (-2, -1),
                    (-1, -2), (-1, 2),
                    (1, -2), (1, 2),
                    (2, -1), (2, 1)
                    ]
                movements = []
                row, column = piece.position
                for i in directions:
                    new_pos = (row + i[0], column + i[1])
                    if 0 <= new_pos[0] < 8 and 0<= new_pos[1] < 8:
                        movements.append(new_pos)

                for i in self.pieces:
                    if i.position in movements:
                        if i.color == piece.color:
                            movements.remove(i.position)

                if move not in movements:
                    return False
                return True

            if piece.name == "Q":
                directions = [(-1,-1),(-1,1),(1,-1),(1,1),(-1, 0), (1,0), (0,1), (0,-1)]
                row, column = piece.position
                movements = []

                for dr, dc in directions:
                    for i in range(1, 8):
                        new_pos = (row + dr*i, column + dc*i)
                        if 0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7:
                            blocked = False

                            for i in self.pieces:
                                if i.position == new_pos:
                                    if piece.color != i.color:
                                        movements.append(new_pos)
                                        blocked = True
                                    elif piece.color == i.color:
                                        blocked = True
                                    break
                                

                            if blocked:
                                break
                            movements.append(new_pos)
                if move not in movements:
                    return False
                return True

            if piece.name == "K":
                movements = []
                row, column = piece.position
                for i in range(-1, 2):
                    for j in range(-1,2):
                        new_pos = (row + i, column + j)

                        if new_pos == (row, column):
                            pass
                        
                        if 0<= new_pos[0] < 8 and 0<= new_pos[1] < 8:
                            movements.append(new_pos)
                for i in pieces:
                    if i.position in movements:
                        if i.color == piece.color:
                            movements.remove(i.position)
                if move not in movements:
                    return False
                return True



            if piece.name == "B":
                directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
                row, column = piece.position
                movements = []

                #to do
                for dr, dc in directions:
                    for i in range(1, 8):
                        new_pos = (row + dr*i, column + dc*i)
                        if 0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7:
                            blocked = False

                            for i in self.pieces:
                                if i.position == new_pos:
                                    if i.color != piece.color:
                                        movements.append(new_pos)
                                        blocked = True
                                    elif i.color == piece.color:
                                        blocked = True
                                    break
                                

                            if blocked:
                                break
                            movements.append(new_pos)
                if move not in movements:
                    return False
                return True
                
            if piece.name == "R":
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                row, column = piece.position
                movements = []

                #to do
                for dr, dc in directions:
                    for i in range(1, 8):
                        new_pos = (row + dr*i, column + dc*i)
                        if 0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7:
                            blocked = False

                            for i in self.pieces:
                                if i.position == new_pos:
                                    if piece.color != piece.color:
                                        movements.append(new_pos)
                                        blocked = True
                                    elif i.color == piece.color:
                                        blocked = True
                                    break
                                

                            if blocked:
                                break
                            movements.append(new_pos)
                if move not in movements:
                    return False
                return True
                
            if piece.name == "p":
                direction = 1 if piece.color == 'white' else -1
                row, column = piece.position
                movements = []

                new_row = row + direction
                if 0 <= new_row < 8:
                    movements.append((new_row, column))
                
                if (piece.first_move):
                    new_row = row + 2 * direction
                    movements.append((new_row, column)) 
                for piece in self.pieces:
                    if piece.position == (new_row, column):
                        movements.remove(piece.position)

                #captura
                capture = [-1,1]

                for dc in capture:
                    capture_pos = (row+direction, column + dc)
                    if 0 <= capture_pos[0] < 8 and 0 <= capture_pos[1] < 8: 
                        for piece in self.pieces:
                            if piece.position == capture_pos and piece.color != piece.color:
                                movements.append(capture_pos)
                if move not in movements:
                    return False
                return True
        return False


tab = Board()

tab.init_board()
tab.show()
print(tab.isValid((0,3), (1,3)))


