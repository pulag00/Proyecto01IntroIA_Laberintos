# =============================================================
# maze.py
# Módulo que encapsula la lectura y consulta del laberinto
# representado como una matriz NxN.
# =============================================================

class Maze:
    """
    Clase que representa el laberinto como una matriz NxN.

    Convención de valores:
        0 -> espacio libre
        1 -> pared
        2 -> celda de salida / inicio
        3 -> celda meta / objetivo
    """

    def __init__(self, matrix):
        self.matrix = matrix
        # Se asume que la matriz es cuadrada; N es el número de filas
        self.N = len(matrix)

    def find_value(self, value):
        """
        Busca la primera celda cuyo valor coincida con el indicado.
        Se usa principalmente para encontrar el inicio (2) y la meta (3).
        """
        for i in range(self.N):
            for j in range(self.N):
                if self.matrix[i][j] == value:
                    return (i, j)
        return None