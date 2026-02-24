class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node, neighbor, cost=1):
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].append((neighbor, cost))


def matrix_to_graph(matrix):
    N = len(matrix)
    graph = Graph()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 1:
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < N and 0 <= nj < N:
                        if matrix[ni][nj] != 1:
                            graph.add_edge((i, j), (ni, nj), 1)

    return graph
