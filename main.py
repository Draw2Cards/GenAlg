import os

from genetic_algorithm.ga import GeneticAlgorithm
from matrix.matrix_generator import MatrixGenerator

if __name__ == '__main__':

    matrix_gen = MatrixGenerator('D:\\Graphs\\le450_5a.txt')
    matrix = matrix_gen.gen()
    ga = GeneticAlgorithm(matrix, 1000, 2000, 1, 0.4)
    ga.init()
    ga.start()
    ga.print()
