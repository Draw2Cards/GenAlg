import time


def byDegree(e):
    return e[1]


class SmallestLast:
    def __init__(self, matrix):
        self.elapsed_time = None
        self.matrix = matrix
        self.vertex_num = len(matrix)
        self.vertexes_degree = self.prepare_struct()
        self.vertexes_colors = [0] * self.vertex_num

    def start(self):
        start_time = time.time()
        self.calc_vertex_degree()
        self.vertexes_degree.sort(key=byDegree)
        self.color_graph()
        self.elapsed_time = time.time() - start_time

    def print(self):
        print('SmallestLast')
        print(self.vertexes_colors)
        print(max(self.vertexes_colors))
        print(self.elapsed_time)
        print('_________')

    def calc_vertex_degree(self):
        for row_index, row in enumerate(self.matrix):
            for col_index, val in enumerate(row):
                if val == 1:
                    self.vertexes_degree[row_index][1] += 1

    def color_graph(self):
        is_first = True
        for vertex in reversed(self.vertexes_degree):
            color = 1
            while not self.is_color_free(color, vertex[0], is_first):
                color += 1
            self.vertexes_colors[vertex[0]] = color
            is_first = False

    def is_color_free(self, color_id, vertex_index, is_first):
        result = True
        if not is_first:
            for val_index, val in enumerate(self.matrix[vertex_index]):
                if val == 1:
                    if self.vertexes_colors[val_index] == color_id:
                        result = False
                        break
        return result

    def prepare_struct(self):
        result = []
        for n in range(self.vertex_num):
            result.append([n, 0])
        return result
