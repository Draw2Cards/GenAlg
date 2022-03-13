class MatrixGenerator:
    def __init__(self, path):
        self.path = path

    def gen(self):
        result = []
        with open(self.path) as file:
            for line_index, line in enumerate(file):
                if line_index == 0:
                    for r in range(int(line)):
                        result.append([0] * int(line))
                else:
                    li = list(line.rstrip().split(" "))
                    result[int(li[0])-1][int(li[1])-1] = 1
                    result[int(li[1])-1][int(li[0])-1] = 1
        return result
