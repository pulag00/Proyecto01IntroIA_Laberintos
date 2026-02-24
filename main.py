from maze import Maze
from graph import matrix_to_graph
from search import dfs, bfs, a_star
from heuristics import build_heuristic
from visualization import draw_graph, draw_matrix_with_path


def main():

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

    maze = Maze(matrix)
    start = maze.find_value(2)
    goal = maze.find_value(3)

    graph = matrix_to_graph(matrix)

    print("Inicio:", start)
    print("Meta:", goal)

    # ==============================
    # DFS
    # ==============================
    print("\n===== DFS =====")
    path_dfs, explored_dfs = dfs(graph, start, goal)

    print("Ruta:", path_dfs)
    print("Nodos explorados:", len(explored_dfs))

    draw_graph(graph, path_dfs, explored_dfs)
    draw_matrix_with_path(matrix, path_dfs, explored_dfs)

    # ==============================
    # BFS
    # ==============================
    print("\n===== BFS =====")
    path_bfs, explored_bfs = bfs(graph, start, goal)

    print("Ruta:", path_bfs)
    print("Nodos explorados:", len(explored_bfs))

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

    draw_graph(graph, path_astar, explored_astar)
    draw_matrix_with_path(matrix, path_astar, explored_astar)


if __name__ == "__main__":
    main()
