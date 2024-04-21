class Heuristics:
    def __init__(self):
        pass

    @staticmethod
    def h1(board, symbol):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == symbol:
                    neighbors_b = Heuristics.__check_neighbors__(board, symbol)
                    neighbors_c = Heuristics.__check_neighborsc__(board, symbol)
        return neighbors_b - neighbors_c
        

    @staticmethod
    def is_valid_move(board, x, y):        
        return (0 <= x < len(board) and 0 <= y < len(board))


    @staticmethod
    def __check_neighbors__(self, board, symbol, x, y):
        cont = 0
        movements = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for mov in movements:
            new_x = x + mov[0]
            new_y = y + mov[0]
            if self.is_valid_move(board, new_x, new_y):
                if board[new_x][new_y] != 0 and board[new_x][new_y] != symbol :
                    cont += 1
        return cont
    
    @staticmethod
    def __check_neighbors__(self, board, symbol, x, y):
        cont = 0
        movements = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for mov in movements:
            new_x = x + mov[0]
            new_y = y + mov[0]
            if self.is_valid_move(board, new_x, new_y):
                if board[new_x][new_y] == symbol :
                    cont += 1
        return cont