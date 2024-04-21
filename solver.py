from queue import Queue
from copy import deepcopy
class Solver:
    def __init__(self, board):
        self.board = board
        self.symbol = None
        self.plau = deepcopy(board)
        self.dic = {
            'derecha': self.derecha,
            'izquierda': self.izquierda,
            'abajo': self.abajo,
            'arriba': self.arriba,
        }
    
    def bfs(self):
        queue = Queue()
        queue.put(self.board)

        while not queue.empty():
            current_board = queue.get()
            if current_board.check_win():
                return current_board

            for x in range(len(current_board.board)):
                for y in range(len(current_board.board[x])):
                    if current_board.board[x][y] == 0:
                        for move_name, move_func in self.dic.items():
                            new_board = deepcopy(current_board)
                            move_func(new_board, x, y, move_name)
                            queue.put(new_board)

    def derecha(self, board, x, y, move_name):
        board.move(x, y, move_name, self.symbol)

    def izquierda(self, board, x, y, move_name):
        board.move(x, y, move_name, self.symbol)

    def abajo(self, board, x, y, move_name):
        board.move(x, y, move_name, self.symbol)

    def arriba(self, board, x, y, move_name):
        board.move(x, y, move_name, self.symbol)
