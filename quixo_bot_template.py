import numpy as np
from solver import Quixo

class QuixoBot:
    # symbol sera un numero representando el simbolo con el que me
    # toca jugar. Puede tener el valor 1 o -1;
    def __init__(self, symbol):
        # define a name for your bot to appear during the log printing.
        self.name = "CC"
        self.symbol = symbol
        pass

    # board es el estado actual del tablero. Sera una matriz de 5x5 que contiene
    # los siguientes numeros enteros.
    #  0 - blank cubit
    #  1 - X cubit
    # -1 - O cubit
    def play_turn(self, board):
        # Esta funcion debe tomar el tablero actual, simular el movimiento deseado
        board = Quixo(self.symbol).initialize_board(board)
        bot = Quixo(self.symbol)
        updated_board = bot.bot_move(board)
        return updated_board

    # Esta funcion sera llamada antes de empezar una nueva partida,
    # por lo que su proposito es resetear cualquier estado que sea necesario
    # para empezar desde 0.
    # Tambien recibe el nuevo simbolo con el que empezara la partida.
    def reset(self, symbol):
        pass

# Ejemplo de uso

# Creamos el tablero inicial
board = np.zeros((5, 5), dtype=int)
custom_board_1 = [
    [0, 1, -1, 1, 0],
    [-1, 0, 1, 0, -1],
    [1, -1, 0, -1, 1],
    [0, 1, -1, 0, 1],
    [1, 0, 1, -1, 0]
]
# Inicializamos el bot 
bot = QuixoBot(1)

# Jugamos un turno con este bot y recibimos el nuevo estado del tablero.
new_board = bot.play_turn(custom_board_1)
print(new_board)

