# =============================================================
# utils.py
# Módulo de utilidades compartidas por los algoritmos de búsqueda.
# =============================================================


def reconstruct_path(parent, start, goal):
    """
    Reconstruye el camino desde el nodo inicio hasta el nodo meta
    siguiendo el diccionario de padres generado durante la búsqueda.

    El diccionario 'parent' guarda, para cada nodo visitado, el nodo
    desde el cual fue alcanzado. La reconstrucción comienza en 'goal'
    y sigue hacia atrás hasta llegar a 'start'.
    """
    path = []
    node = goal

    # Recorre hacia atrás desde la meta hasta el inicio
    while node is not None:
        path.append(node)
        if node == start:
            break
        node = parent.get(node)

    # Si el último nodo reconstruido no es el inicio, no hay camino válido
    if not path or path[-1] != start:
        return None

    # Invertir para obtener el camino en orden start -> goal
    path.reverse()
    return path