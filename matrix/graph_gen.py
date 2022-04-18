import random


class GraphGenerator:
    def __init__(self, vertex_num, edge_prec):
        self.vertex_num = vertex_num
        self.edge_prec = edge_prec

    def gen_rand_graph(self):
        matrix = []

        for r in range(self.vertex_num):
            matrix.append([0] * self.vertex_num)

        for row in range(self.vertex_num):
            single_edge_created = False
            for column in range(self.vertex_num):
                if column > row:
                    if self.edge_prec > random.uniform(0, 1):
                        single_edge_created = True
                        matrix[row][column] = 1
                        matrix[column][row] = 1
            if not single_edge_created and (column != row):
                single_edge = random.randint(row + 1, self.vertex_num - 1)
                matrix[row][single_edge] = 1
                matrix[single_edge][row] = 1
        return matrix
