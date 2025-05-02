from pieces import *
import re



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
                self.pieces.append(Pawn('white', (1, i)))
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
        for row in self.board:
            for column in row:
                if column:
                    print(str(column), end=' ')
                else: 
                    print(' ', end=' ') 
            print()

    def show_possibles(self, position):
        return self.board[position[0]][position[1]].possible_moves(self.pieces)

    # def parser(self,lance):
    #     if lance == "O-O" or lance == "O-O-O":
    #         print("Roque detectado, ainda não implementado.")
    #         return

    #     match = re.match(r'^([RQBNK])?([a-h1-8]?)([a-h1-8]))$', lance)
    #     tipo, origem, destino = match.group() 
    #     tipo = tipo or 'p'

# muito dificil para fazer agora

    #to do 
    def valid_moves(self):
        pass
    def move(self, piece, coord):    
        #to do: create a parser to move the pieces
        pass




                     



tab = Board()

tab.init_board()
tab.show()
print(tab.show_possibles((0,6)))
