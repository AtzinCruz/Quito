class Board:
    def __init__(self):
        self.board = [[0 for _ in range(5)] for _ in range(5)]
        self.symbol = None

        self.dic = {
            'derecha': self.derecha,
            'izquierda': self.izquierda,
            'abajo': self.abajo,
            'arriba': self.arriba,
        }
    
    def print_b(self):
        for row in self.board:
            print(" ".join(map(str, row)))

    def move(self, x, y, w, symbol):
        if self.check_move(x, y):
            self.dic[w](x, y, symbol)

    def derecha(self, x, y, symbol):
        for i in range(y, len(self.board[x]) - 1):
            self.board[x][i] = self.board[x][i + 1]
        self.board[x][len(self.board) - 1] = symbol

    def izquierda(self, x, y, symbol):
        for i in range(y, 0, -1):
            self.board[x][i] = self.board[x][i - 1]
        self.board[x][0] = symbol

    def abajo(self, x, y, symbol):
        for i in range(x, len(self.board) - 1):
            self.board[i][y] = self.board[i + 1][y]
        self.board[len(self.board) - 1
                   ][y] = symbol

    
    def arriba(self, x, y, symbol):
        for i in range(x, 0, -1):
            self.board[i][y] = self.board[i - 1][y]
        self.board[0][y] = symbol
    
    def check_move(self, x, y):
        return self.board[x][y] == 0
    
    def check_win(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                symbol = self.board[x][y]
                if symbol != 0:
                    # Verificar horizontalmente
                    if y + 4 < len(self.board[x]):
                        if all(self.board[x][y+i] == symbol for i in range(5)):
                            return True
                    # Verificar verticalmente
                    if x + 4 < len(self.board):
                        if all(self.board[x+i][y] == symbol for i in range(5)):
                            return True
                    # Verificar diagonalmente \
                    if x + 4 < len(self.board) and y + 4 < len(self.board[x]):
                        if all(self.board[x+i][y+i] == symbol for i in range(5)):
                            return True
                    # Verificar diagonalmente /
                    if x + 4 < len(self.board) and y - 4 >= 0:
                        if all(self.board[x+i][y-i] == symbol for i in range(5)):
                            return True
        return False

# Crear una instancia de la clase Board
game = Board()
# Llamar al método derecha
game.izquierda(2, 2, 'z')
print()
# Imprimir el tablero

game.arriba(3, 0, 'a')
game.print_b()

