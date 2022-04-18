class Instance:
    def __init__(self, matrix):
        self.vertex_num = len(matrix)
        self.matrix = matrix

    def gen_output(self):
        f = open('output.txt', 'w')
        f.write(str(self.vertex_num) + '\n')
        for row_index, row in enumerate(self.matrix):
            for col_index, val in enumerate(row):
                if val == 1:
                    if row_index + 1 < col_index + 1:
                        f.write(str(row_index + 1) + ' ' + str(col_index + 1) + '\n')
        f.close()
