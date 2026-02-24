from utils import reconstruct_path
import heapq


# =========================
# DFS
# =========================
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {}
    explored_order = []   # ← lista de nodos recorridos

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            explored_order.append(node)

            if node == goal:
                return reconstruct_path(parent, start, goal), explored_order

            for neighbor, _ in graph.adj_list.get(node, []):
                if neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)

    return None, explored_order


# =========================
# BFS
# =========================
def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    parent = {}
    explored_order = []

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            explored_order.append(node)

            if node == goal:
                return reconstruct_path(parent, start, goal), explored_order

            for neighbor, _ in graph.adj_list.get(node, []):
                if neighbor not in visited:
                    parent[neighbor] = node
                    queue.append(neighbor)

    return None, explored_order


# =========================
# A*
# =========================
def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}
    parent = {}
    closed = set()
    explored_order = []

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in closed:
            continue

        closed.add(current)
        explored_order.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), explored_order

        for neighbor, cost in graph.adj_list.get(current, []):
            tentative_g = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f, neighbor))

    return None, explored_order
