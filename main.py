from board import Board
from solver import Solver

game = Board()
print()

game.print_b()

# Crear una instancia de la clase Solver y resolver el juego
solver = Solver(game)
winner_board = solver.bfs()

print("\nTablero ganador:")
winner_board.print_b()