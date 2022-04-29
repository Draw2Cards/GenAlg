import os

from genetic_algorithm.ga import GeneticAlgorithm
from matrix.matrix_generator import MatrixGenerator

if __name__ == '__main__':

    directory = 'D:\\Graphs'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            matrix_gen = MatrixGenerator(f)
            matrix = matrix_gen.gen()
            ga = GeneticAlgorithm(matrix, 200, 500, 1, 0.2)
            ga.init()
            ga.start()
            ga.print()
