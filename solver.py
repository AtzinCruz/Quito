import numpy as np

# Constantes del juego
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
MAX_DEPTH = 2  # Profundidad máxima del árbol de búsqueda

class Quixo:
    def __init__(self, symbol):
        self.symbol = symbol

    def evaluate(self, board):
        score = 0
        for i in range(5):
            score += self.evaluate_line(board[i])
            score -= self.evaluate_line_c(board[i])
            score += self.evaluate_line(board[:, i])
            score -= self.evaluate_line_c(board[:, i])
        diagonal1 = np.array([board[i, i] for i in range(5)])
        diagonal2 = np.array([board[i, 4 - i] for i in range(5)])
        score += self.evaluate_line(diagonal1)
        score -= self.evaluate_line_c(diagonal1)
        score += self.evaluate_line(diagonal2)
        score -= self.evaluate_line_c(diagonal2)
        return score

    def evaluate_line(self, line):
        count = np.sum(line == self.symbol)
        if count == 5:
            return 1000
        elif count == 4:
            return 100
        elif count == 3:
            return 10
        elif count == 2:
            return 1
        else:
            return 0

    def evaluate_line_c(self, line):
        count = np.sum(line == self.symbol * -1)
        if count == 5:
            return 1000
        elif count == 4:
            return 100
        elif count == 3:
            return 10
        elif count == 2:
            return 1
        else:
            return 0

    def initialize_board(self, custom_board=None):
        if custom_board is not None:
            return np.array(custom_board, dtype=int)
        return np.zeros((5, 5), dtype=int)

    def print_board(self, board):
        symbols = {EMPTY: ".", PLAYER_X: "X", PLAYER_O: "O"}
        for row in board:
            print(" ".join(symbols[cell] for cell in row))
        print()

    def get_valid_moves(self, board, player):
        moves = []
        for i in range(5):
            for j in range(5):
                if (i == 0 or i == 4 or j == 0 or j == 4) and (board[i, j] == EMPTY or board[i, j] == player):
                    if i == 0 and j != 4:
                        moves.append((i, j, 'down'))
                    if i == 4 and j != 0:
                        moves.append((i, j, 'up'))
                    if j == 0 and i != 4:
                        moves.append((i, j, 'right'))
                    if j == 4 and i != 0:
                        moves.append((i, j, 'left'))
        return moves

    def make_move(self, board, move, player):
        x, y, direction = move
        if board[x, y] == EMPTY or board[x, y] == player:
            if direction == 'up':
                for i in range(x, 0, -1):
                    board[i, y] = board[i - 1, y]
                board[0, y] = player
            elif direction == 'down':
                for i in range(x, 4):
                    board[i, y] = board[i + 1, y]
                board[4, y] = player
            elif direction == 'left':
                for i in range(y, 0, -1):
                    board[x, i] = board[x, i - 1]
                board[x, 0] = player
            elif direction == 'right':
                for i in range(y, 4):
                    board[x, i] = board[x, i + 1]
                board[x, 4] = player
        else:
            raise ValueError("Movimiento inválido")

    def minimax(self, board, depth, maximizing_player):
        player = self.symbol
        opponent = PLAYER_O if player == PLAYER_X else PLAYER_X
        
        if depth == 0:
            return self.evaluate(board)
        
        player_score = self.evaluate(board)
        if abs(player_score) == 1000:
            return player_score - depth if maximizing_player else depth - player_score

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_valid_moves(board, player):
                board_copy = board.copy()
                self.make_move(board_copy, move, player)
                eval = self.minimax(board_copy, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_valid_moves(board, opponent):
                board_copy = board.copy()
                self.make_move(board_copy, move, opponent)
                eval = self.minimax(board_copy, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def bot_move(self, board):
        best_score = float('-inf')
        best_move = None
        for move in self.get_valid_moves(board, self.symbol):
            board_copy = board.copy()
            self.make_move(board_copy, move, self.symbol)
            score = self.minimax(board_copy, MAX_DEPTH, False)
            if score > best_score:
                best_score = score
                best_move = move
        self.make_move(board, best_move, self.symbol)
        return board

    def check_winner(self, board):
        for symbol in [PLAYER_X, PLAYER_O]:
            for i in range(5):
                if np.all(board[i, :] == symbol) or np.all(board[:, i] == symbol):
                    return symbol
            if np.all(np.diagonal(board) == symbol) or np.all(np.diagonal(np.fliplr(board)) == symbol):
                return symbol
        return None

# Define tu tablero personalizado aquí
custom_board = [
    [-1, 1, 0, 1, -1],
    [1, 0, 1, -1, -1],
    [1, -1, 1, -1, 0],
    [1, 0, -1, -1, 1],
    [1, 1, 1, -1, 1]
]

custom_board_1 = [
    [0, 1, -1, 1, 0],
    [-1, 0, 1, 0, -1],
    [1, -1, 0, -1, 1],
    [0, 1, -1, 0, 1],
    [1, 0, 1, -1, 0]
]

custom_board_2 = [
    [-1, -1, 0, 1, 1],
    [1, 0, -1, 1, 0],
    [0, 1, -1, 0, 1],
    [1, -1, 0, 1, -1],
    [-1, 1, 1, 0, -1]
]

custom_board_3 = [
    [1, 0, 1, -1, -1],
    [-1, 1, 0, 1, -1],
    [1, -1, 1, 1, 1],
    [-1, 0, -1, 0, 0],
    [1, 1, -1, 0, 1]
]

'''
# Inicializar el tablero con el tablero personalizado

board = Quixo(PLAYER_X).initialize_board(custom_board_2)
print("Tablero inicial:")
Quixo(PLAYER_X).print_board(board)

# Inicializar el bot para el jugador X
bot = Quixo(PLAYER_X)

# Obtener el tablero con el mejor movimiento ya hecho
updated_board = bot.bot_move(board)

print("Tablero después del mejor movimiento:")
Quixo(PLAYER_X).print_board(updated_board)

# Verificar si hay un ganador
winner = bot.check_winner(updated_board)
if winner == PLAYER_X:
    print("Jugador X ha ganado!")
elif winner == PLAYER_O:
    print("Jugador O ha ganado!")

'''