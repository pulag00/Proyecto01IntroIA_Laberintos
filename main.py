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
import ast


def leer_laberinto():
    print("Pegue la matriz del laberinto en formato Python.")
    print("Ejemplo:")
    print("[[2,1,1],[0,0,1],[1,3,0]]\n")

    entrada = input("Ingrese la matriz: ")

    try:
        matrix = ast.literal_eval(entrada)

        # Validar que sea lista de listas
        if not isinstance(matrix, list) or not all(isinstance(fila, list) for fila in matrix):
            print("Error: Formato inválido.")
            return None, None

        N = len(matrix)

        # Validar que sea NxN
        for fila in matrix:
            if len(fila) != N:
                print("Error: La matriz no es NxN.")
                return None, None

        return matrix, N

    except:
        print("Error: Entrada inválida.")
        return None, None


def main():

    matrix, N = leer_laberinto()

    if matrix is None:
        return

    maze = Maze(matrix)

    start = maze.find_value(2)
    goal = maze.find_value(3)

    if start is None or goal is None:
        print("Error: No se encontró inicio (2) o meta (3).")
        return

    graph = matrix_to_graph(matrix)

    print("\nDimensión:", N)
    print("Inicio:", start)
    print("Meta:", goal)

    # ==============================
    # DFS
    # ==============================
    print("\n===== DFS =====")
    path_dfs, explored_dfs = dfs(graph, start, goal)

    print("Ruta:", path_dfs)
    print("Nodos explorados:", len(explored_dfs))
    print("Orden exploración:", explored_dfs)

    draw_graph(graph, path_dfs, explored_dfs)
    draw_matrix_with_path(matrix, path_dfs, explored_dfs)

    # ==============================
    # BFS
    # ==============================
    print("\n===== BFS =====")
    path_bfs, explored_bfs = bfs(graph, start, goal)

    print("Ruta:", path_bfs)
    print("Nodos explorados:", len(explored_bfs))
    print("Orden exploración:", explored_bfs)

    draw_graph(graph, path_bfs, explored_bfs)
    draw_matrix_with_path(matrix, path_bfs, explored_bfs)

    # ==============================
    # A*
    # ==============================
    print("\n===== A* =====")
    heuristic = build_heuristic(matrix, goal)
    path_astar, explored_astar = a_star(graph, start, goal, heuristic)

    print("Ruta:", path_astar)
    print("Nodos explorados:", len(explored_astar))
    print("Orden exploración:", explored_astar)

    draw_graph(graph, path_astar, explored_astar)
    draw_matrix_with_path(matrix, path_astar, explored_astar)


if __name__ == "__main__":
    main()
