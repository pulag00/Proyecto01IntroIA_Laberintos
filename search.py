# =============================================================
# search.py
# Módulo que implementa los tres algoritmos de búsqueda:
#   - DFS  (Búsqueda primero en profundidad) — búsqueda ciega
#   - BFS  (Búsqueda primero en anchura)     — búsqueda ciega
#   - A*   (A estrella)                      — búsqueda heurística
# =============================================================

from utils import reconstruct_path
import heapq



# DFS — Depth First Search (Primero en Profundidad)

def dfs(graph, start, goal):
    
    stack = [start]          # Pila LIFO para la frontera de exploración
    visited = set()          # Conjunto de nodos ya visitados
    parent = {}              # Diccionario para reconstruir el camino
    explored_order = []      # Registro del orden de exploración

    while stack:
        node = stack.pop()   # Extrae el nodo más reciente (LIFO)

        if node not in visited:
            visited.add(node)
            explored_order.append(node)

            # Se encontró la meta: reconstruir y retornar el camino
            if node == goal:
                return reconstruct_path(parent, start, goal), explored_order

            # Agregar vecinos no visitados a la pila
            for neighbor, _ in graph.adj_list.get(node, []):
                if neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)

    # No se encontró camino
    return None, explored_order


# BFS — Breadth First Search (Primero en Anchura)

def bfs(graph, start, goal):
    
    queue = [start]          # Cola FIFO para la frontera de exploración
    visited = set()          # Conjunto de nodos ya visitados
    parent = {}              # Diccionario para reconstruir el camino
    explored_order = []      # Registro del orden de exploración

    while queue:
        node = queue.pop(0)  # Extrae el nodo más antiguo (FIFO)

        if node not in visited:
            visited.add(node)
            explored_order.append(node)

            # Se encontró la meta: reconstruir y retornar el camino
            if node == goal:
                return reconstruct_path(parent, start, goal), explored_order

            # Agregar vecinos no visitados a la cola
            for neighbor, _ in graph.adj_list.get(node, []):
                if neighbor not in visited:
                    parent[neighbor] = node
                    queue.append(neighbor)

    # No se encontró camino
    return None, explored_order



# A* — A Estrella (Búsqueda Heurística)

def a_star(graph, start, goal, heuristic):
    
    # Cola de prioridad: (f_cost, nodo). Se ordena por menor f primero.
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}   # Costo g acumulado desde el inicio
    parent = {}            # Diccionario para reconstruir el camino
    closed = set()         # Conjunto de nodos ya expandidos (cerrados)
    explored_order = []    # Registro del orden de expansión

    while open_set:
        _, current = heapq.heappop(open_set)  # Nodo con menor f(n)

        # Ignorar si ya fue cerrado (puede haber duplicados en la cola)
        if current in closed:
            continue

        closed.add(current)
        explored_order.append(current)

        # Se encontró la meta: reconstruir y retornar el camino
        if current == goal:
            return reconstruct_path(parent, start, goal), explored_order

        # Expandir vecinos
        for neighbor, cost in graph.adj_list.get(current, []):
            tentative_g = g_cost[current] + cost  # Costo g tentativo

            # Actualizar si se encontró un camino más barato hacia el vecino
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]  # f = g + h
                heapq.heappush(open_set, (f, neighbor))

    # No se encontró camino
    return None, explored_order