from board import Board
from solver import Solver

game = Board()

game.izquierda(4, 2, 'z')
game.izquierda(4, 1, 'o')
print()
# Imprimir el tablero
game.arriba(3, 0, 'a')
game.print_b()

# Crear una instancia de la clase Solver y resolver el juego
solver = Solver(game)
winner_board = solver.bfs()

print("\nTablero ganador:")
winner_board.print_b()