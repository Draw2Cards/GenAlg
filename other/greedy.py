import time


class Greedy:
    def __init__(self, matrix):
        self.elapsed_time = None
        self.matrix = matrix
        self.vertex_num = len(matrix)
        self.vertex = [0] * self.vertex_num

    def start(self):
        start_time = time.time()
        for vertex_index, vertex in enumerate(self.vertex):
            color = 1
            while not self.is_color_free(color, vertex_index):
                color += 1
            self.vertex[vertex_index] = color
        self.elapsed_time = time.time() - start_time

    def is_color_free(self, color_id, vertex_index):
        result = True
        if vertex_index == 0:
            return True
        for val_index, val in enumerate(self.matrix[vertex_index]):
            if vertex_index > val_index:
                if val == 1:
                    if self.vertex[val_index] == color_id:
                        result = False
                        break
            else:
                break
        return result

    def print(self):
        print('Greedy')
        print(self.vertex)
        print(max(self.vertex))
        print(self.elapsed_time)
        print('_________')
