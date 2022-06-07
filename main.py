import os

from genetic_algorithm.ga import GeneticAlgorithm
from matrix.matrix_generator import MatrixGenerator

if __name__ == '__main__':

    file_name = 'miles250.txt'

    matrix_gen = MatrixGenerator('D:\\Graphs\\' + file_name)
    matrix = matrix_gen.gen()
    ga = GeneticAlgorithm(matrix, 500, 500, 0, 0.2, file_name, 300)
    ga.init()
    ga.start()
    ga.print()
