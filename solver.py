import numpy as np

# Constantes del juego
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
MAX_DEPTH = 3  # Profundidad máxima del árbol de búsqueda

class QuixoBot:
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
            return -1000
        elif count == 4:
            return -100
        elif count == 3:
            return -10
        elif count == 2:
            return -1
        else:
            return 0

def initialize_board(custom_board=None):
    if custom_board is not None:
        return np.array(custom_board, dtype=int)
    return np.zeros((5, 5), dtype=int)

def print_board(board):
    symbols = {EMPTY: ".", PLAYER_X: "X", PLAYER_O: "O"}
    for row in board:
        print(" ".join(symbols[cell] for cell in row))
    print()

def get_valid_moves(board, player):
    moves = []
    for i in range(5):
        for j in range(5):
            if (i == 0 or i == 4 or j == 0 or j == 4) and (board[i, j] == EMPTY or board[i, j] == player):
                if i == 0:
                    moves.append((i, j, 'down'))
                if i == 4:
                    moves.append((i, j, 'up'))
                if j == 0:
                    moves.append((i, j, 'right'))
                if j == 4:
                    moves.append((i, j, 'left'))
    return moves

def make_move(board, move, player):
    x, y, direction = move
    if board[x, y] == EMPTY or board[x, y] == player:
        if direction == 'up':
            board[1:x+1, y] = np.roll(board[1:x+1, y], shift=1)
            board[0, y] = player
        elif direction == 'down':
            board[x:, y] = np.roll(board[x:, y], shift=-1)
            board[4, y] = player
        elif direction == 'left':
            board[x, 1:y+1] = np.roll(board[x, 1:y+1], shift=1)
            board[x, 0] = player
        elif direction == 'right':
            board[x, y:] = np.roll(board[x, y:], shift=-1)
            board[x, 4] = player
    else:
        raise ValueError("Movimiento inválido")

def minimax(board, depth, maximizing_player, bot):
    player = bot.symbol
    opponent = PLAYER_O if player == PLAYER_X else PLAYER_X
    
    if depth == 0:
        return bot.evaluate(board)
    
    player_score = bot.evaluate(board)
    if abs(player_score) == 1000:
        return player_score - depth if maximizing_player else depth - player_score

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_valid_moves(board, player):
            board_copy = board.copy()
            make_move(board_copy, move, player)
            eval = minimax(board_copy, depth - 1, False, bot)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board, opponent):
            board_copy = board.copy()
            make_move(board_copy, move, opponent)
            eval = minimax(board_copy, depth - 1, True, bot)
            min_eval = min(min_eval, eval)
        return min_eval

def bot_move(board, bot):
    best_score = float('-inf')
    best_move = None
    for move in get_valid_moves(board, bot.symbol):
        board_copy = board.copy()
        make_move(board_copy, move, bot.symbol)
        score = minimax(board_copy, MAX_DEPTH, False, bot)
        print(f"Evaluando movimiento: {move}, Puntuación: {score}")  # Añadido para depuración
        if score > best_score:
            best_score = score
            best_move = move
    print(f"Mejor movimiento: {best_move}, Mejor puntuación: {best_score}")  # Añadido para depuración
    make_move(board, best_move, bot.symbol)
    return board

# Define tu tablero personalizado aquí
custom_board = [
    [0, 1, 0, -1, 1],
    [0, 0, 1, 1, -1],
    [1, -1, 1, 1, 0],
    [1, 0, -1, 0, 1],
    [1, 0, 0, 0, 0]
]

# Inicializar el tablero con el tablero personalizado
board = initialize_board(custom_board)
print("Tablero inicial:")
print_board(board)

# Inicializar el bot para el jugador X
bot = QuixoBot(PLAYER_X)

# Obtener el tablero con el mejor movimiento ya hecho
updated_board = bot_move(board, bot)

print("Tablero después del mejor movimiento:")
print_board(updated_board)
