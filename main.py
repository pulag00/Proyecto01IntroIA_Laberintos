# =============================================================
# main.py
# Punto de entrada principal del proyecto.
# Orquesta la carga del laberinto, la construcción del grafo,
# la ejecución de los algoritmos de búsqueda y la visualización
# de los resultados.
# =============================================================

from maze import Maze
from graph import matrix_to_graph
from search import dfs, bfs, a_star
from heuristics import build_heuristic
from visualization import draw_graph, draw_matrix_with_path


def main():

     # Definición del laberinto (matriz N*N)
    # Convención: 0=libre, 1=pared, 2=inicio, 3=meta
    matrix = [
        [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Inicialización del laberinto y localización de inicio/meta
    maze = Maze(matrix)
    start = maze.find_value(2)  # Celda marcada con 2 es el inicio
    goal = maze.find_value(3)   # Celda marcada con 3 es la meta

    # Construcción del grafo a partir de la matriz
    graph = matrix_to_graph(matrix)

    print("Inicio:", start)
    print("Meta:", goal)

    
    # DFS — Búsqueda Primero en Profundidad
   
    print("\n===== DFS =====")
    path_dfs, explored_dfs = dfs(graph, start, goal)

    print("Ruta:", path_dfs)
    print("Nodos explorados:", len(explored_dfs))

    # Visualizar resultados de DFS
    draw_graph(graph, path_dfs, explored_dfs)
    draw_matrix_with_path(matrix, path_dfs, explored_dfs)

    # BFS — Búsqueda Primero en Anchura
    print("\n===== BFS =====")
    path_bfs, explored_bfs = bfs(graph, start, goal)

    print("Ruta:", path_bfs)
    print("Nodos explorados:", len(explored_bfs))

    # Visualizar resultados de BFS
    draw_graph(graph, path_bfs, explored_bfs)
    draw_matrix_with_path(matrix, path_bfs, explored_bfs)

     # A* — Búsqueda Heurística A Estrella
    print("\n===== A* =====")
    # Construir la tabla heurística (distancia Manhattan a la meta)
    heuristic = build_heuristic(matrix, goal)
    path_astar, explored_astar = a_star(graph, start, goal, heuristic)

    print("Ruta:", path_astar)
    print("Nodos explorados:", len(explored_astar))

     # Visualizar resultados de A*
    draw_graph(graph, path_astar, explored_astar)
    draw_matrix_with_path(matrix, path_astar, explored_astar)


if __name__ == "__main__":
    main()
