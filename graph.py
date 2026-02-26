# =============================================================
# graph.py
# Módulo encargado de representar el grafo y transformar
# la matriz del laberinto en una lista de adyacencia.
# =============================================================
class Graph:
    def __init__(self):
         # Diccionario: nodo -> lista de (vecino, costo)
        self.adj_list = {}

    def add_edge(self, node, neighbor, cost=1):
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].append((neighbor, cost))


def matrix_to_graph(matrix):
    """
    Convierte una matriz NxN del laberinto en un grafo de adyacencia.

    Convención de la matriz:
        0 -> espacio libre
        1 -> pared (no transitable)
        2 -> celda de salida (inicio)
        3 -> celda meta (objetivo)

    Para cada celda no pared se generan aristas hacia sus vecinos
    (arriba, abajo, izquierda, derecha) que tampoco sean pared,
    con costo uniforme de 1.
    """
    N = len(matrix)
    graph = Graph()

    # Las cuatro direcciones posibles de movimiento (sin diagonales)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):
            # Solo se procesan celdas transitables (distinto de pared)
            if matrix[i][j] != 1:
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    # Verificar que el vecino esté dentro de los límites
                    # y que también sea transitable
                    if 0 <= ni < N and 0 <= nj < N:
                        if matrix[ni][nj] != 1:
                            graph.add_edge((i, j), (ni, nj), 1)

    return graph
