import time


def byDegree(e):
    return e[2]


class SaturationLargestFirst:
    def __init__(self, matrix):
        self.elapsed_time = None
        self.matrix = matrix
        self.vertex_num = len(matrix)
        self.vertexes_saturation_degree = self.prepare_struct()
        self.vertexes_colors = [0] * self.vertex_num

    def start(self):
        start_time = time.time()
        self.calc_vertex_degree()
        self.color_graph()
        self.elapsed_time = time.time() - start_time

    def print(self):
        print('SaturationLargestFirst')
        print(self.vertexes_colors)
        print(max(self.vertexes_colors))
        print(self.elapsed_time)
        print('_________')

    def calc_vertex_degree(self):
        for row_index, row in enumerate(self.matrix):
            for col_index, val in enumerate(row):
                if val == 1:
                    self.vertexes_saturation_degree[row_index][2] += 1

    def color_graph(self):
        is_first = True
        self.vertexes_saturation_degree = sorted(self.vertexes_saturation_degree, reverse=True,
                                                 key=lambda x: (x[1], x[2]))
        while len(self.vertexes_saturation_degree) != 0:
            color = 1
            while not self.is_color_free(color, self.vertexes_saturation_degree[0][0], is_first):
                color += 1
            self.vertexes_colors[self.vertexes_saturation_degree[0][0]] = color
            self.update_saturation(self.vertexes_saturation_degree[0][0])
            self.vertexes_saturation_degree.pop(0)
            self.vertexes_saturation_degree = sorted(self.vertexes_saturation_degree, reverse=True,
                                                     key=lambda x: (x[1], x[2]))
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
            result.append([n, 0, 0])
        return result

    def update_saturation(self, colored_index):
        for col_index, val in enumerate(self.matrix[colored_index]):
            if val == 1:
                match = next((x for x in self.vertexes_saturation_degree if x[0] == col_index), None)
                if match:
                    match[1] += 1
