from board import Board
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
            score -= self.evaluate_line_c(board[i])
            score += self.evaluate_line([board[j][i] for j in range(5)])
            score -= self.evaluate_line_c([board[j][i] for j in range(5)])
        diagonal1 = [board[i][i] for i in range(5)]
        diagonal2 = [board[i][4-i] for i in range(5)]
        score += self.evaluate_line(diagonal1)
        score -= self.evaluate_line_c(diagonal1)
        score += self.evaluate_line(diagonal2)
        score -= self.evaluate_line_c(diagonal2)
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
        
    def evaluate_line_c(self, line):
        # Contar fichas en línea
        count = line.count(self.symbol * -1)
        if count == 5:
            return 10000
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
        moves = []
        for i in range(5):
            for j in [0, 4]:  # Check left and right edges
                if board[i][j] != self.opponent_symbol:
                    moves.append((i, j))
        for j in range(5):
            for i in [0, 4]:  # Check top and bottom edges
                if board[i][j] != self.opponent_symbol:
                    moves.append((i, j))
        return moves

    def apply_move(self, board, move):
        new_board = copy.deepcopy(board)
        x, y = move
        game = Board(new_board)
        game.move(x, y, self.symbol)
        game.print_b()
        return game.board

# Ejemplo de uso
# Tablero de ejemplo
example_board = [
    [1, 0, 0, 1, -1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [-1, 0, 0, 0, -1],
    [1, 0, 0, 1, 0]
]

# Símbolo del bot
bot_symbol = 1

# Crear el bot
bot = QuixoBot(bot_symbol)

# Realizar una jugada
next_move = bot.make_move(example_board)
print("El bot elige mover la ficha en la posición:", next_move)
