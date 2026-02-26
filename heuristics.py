# =============================================================
# heuristics.py
# Módulo que define la función heurística utilizada por A*.
# Se emplea la distancia Manhattan como estimación del costo
# desde cada nodo hasta la celda objetivo.
# =============================================================

def manhattan(node, goal):
    """
    Calcula la distancia Manhattan entre dos celdas del laberinto.
    Es una heurística admisible para movimientos en cuadrícula
    sin diagonales (arriba, abajo, izquierda, derecha).

    Fórmula: h(n) = |fila_n - fila_goal| + |col_n - col_goal|
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def build_heuristic(matrix, goal):
    """
    Construye la tabla heurística completa para todos los nodos
    transitables del laberinto usando la distancia Manhattan.

    Solo se calculan valores para celdas que no sean pared (valor != 1),
    ya que las paredes no forman parte del grafo de búsqueda.
    """
    N = len(matrix)
    h = {}

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 1:
                h[(i, j)] = manhattan((i, j), goal)

    return h
