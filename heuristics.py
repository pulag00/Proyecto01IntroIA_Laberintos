def manhattan(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def build_heuristic(matrix, goal):
    N = len(matrix)
    h = {}

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 1:
                h[(i, j)] = manhattan((i, j), goal)

    return h
