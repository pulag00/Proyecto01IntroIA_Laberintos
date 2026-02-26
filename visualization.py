import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



# Dibujar grafo con camino y explorados

def draw_graph(graph, path=None, explored=None):

    G = nx.Graph()

    for node in graph.adj_list:
        for neighbor, cost in graph.adj_list[node]:
            G.add_edge(node, neighbor, weight=cost)

    pos = {node: (node[1], -node[0]) for node in G.nodes()}

    plt.figure(figsize=(8, 8))

    # Colores por defecto
    node_colors = []

    for node in G.nodes():
        if path and node in path:
            node_colors.append("red")           # camino final
        elif explored and node in explored:
            node_colors.append("yellow")        # explorados
        else:
            node_colors.append("lightblue")     # normales

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=300,
        node_color=node_colors,
        font_size=6
    )

    # Resaltar aristas del camino
    if path:
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges_in_path,
            edge_color="red",
            width=3
        )

    plt.title("Grafo del Laberinto")
    plt.show()


# ==========================================
# Dibujar matriz con camino y explorados
# ==========================================
def draw_matrix_with_path(matrix, path=None, explored=None):

    N = len(matrix)
    display_matrix = np.array(matrix)

    # Marcar explorados
    if explored:
        for (i, j) in explored:
            if display_matrix[i][j] == 0:
                display_matrix[i][j] = 5  # valor para explorado

    # Marcar camino final (encima de explorado)
    if path:
        for (i, j) in path:
            if display_matrix[i][j] == 0 or display_matrix[i][j] == 5:
                display_matrix[i][j] = 4  # valor para camino

    plt.figure(figsize=(6, 6))

     # Mapa de colores personalizado para los 6 valores posibles (0 a 5)
    cmap = plt.cm.colors.ListedColormap([
        "white",    # 0 espacio
        "black",    # 1 pared
        "green",    # 2 inicio
        "blue",     # 3 meta
        "red",      # 4 camino
        "yellow"    # 5 explorado
    ])

    plt.imshow(display_matrix, cmap=cmap)
    plt.grid(True)
    plt.xticks(range(N))
    plt.yticks(range(N))
    plt.title("Exploración y Ruta Final")
    plt.show()
