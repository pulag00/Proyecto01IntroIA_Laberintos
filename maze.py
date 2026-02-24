class Maze:
    def __init__(self, matrix):
        self.matrix = matrix
        self.N = len(matrix)

    def find_value(self, value):
        for i in range(self.N):
            for j in range(self.N):
                if self.matrix[i][j] == value:
                    return (i, j)
        return None
