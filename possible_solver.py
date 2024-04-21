import copy

class QuixoBot:
    def __init__(self, symbol, depth_limit=3):
        self.symbol = symbol
        self.depth_limit = depth_limit

    def make_move(self, board):
        _, move = self.minimax(board, 0, True)
        return move

    def minimax(self, board, depth, maximizing_player):
        if depth == self.depth_limit or self.is_terminal_node(board):
            return self.evaluate(board), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_possible_moves(board):
                new_board = self.apply_move(board, move)
                eval, _ = self.minimax(new_board, depth + 1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_possible_moves(board):
                new_board = self.apply_move(board, move)
                eval, _ = self.minimax(new_board, depth + 1, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def evaluate(self, board):
        score = 0
        for i in range(5):
            score += self.evaluate_line(board[i])
            score += self.evaluate_line([board[j][i] for j in range(5)])
        diagonal1 = [board[i][i] for i in range(5)]
        diagonal2 = [board[i][4-i] for i in range(5)]
        score += self.evaluate_line(diagonal1)
        score += self.evaluate_line(diagonal2)
        return score

    def evaluate_line(self, line):
        # Contar fichas en línea
        count = line.count(self.symbol)
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

    def is_terminal_node(self, board):
        # Comprobar si el juego ha terminado
        for row in board:
            if ' ' in row:
                return False
        return True

    def get_possible_moves(self, board):
        # Obtener todas las posibles jugadas
        moves = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def apply_move(self, board, move):
        # Aplicar una jugada al tablero
        new_board = copy.deepcopy(board)
        x, y = move
        new_board[x][y] = self.symbol
        return new_board

# Ejemplo de uso
# Tablero de ejemplo
example_board = [
    ['X', ' ', ' ', 'O', 'X'],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', 'O'],
    ['X', ' ', ' ', 'X', ' ']
]

# Símbolo del bot
bot_symbol = 'O'

# Crear el bot
bot = QuixoBot(bot_symbol)

# Realizar una jugada
next_move = bot.make_move(example_board)
print("El bot elige mover la ficha en la posición:", next_move)
