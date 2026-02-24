def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        if node == start:
            break
        node = parent.get(node)
    if not path or path[-1] != start:
        return None
    path.reverse()
    return path
