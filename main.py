import os

from genetic_algorithm.ga import GeneticAlgorithm
from matrix.matrix_generator import MatrixGenerator

if __name__ == '__main__':

    matrix_gen = MatrixGenerator('D:\\Graphs\\gc_1000.txt')
    matrix = matrix_gen.gen()
    ga = GeneticAlgorithm(matrix, 500, 2000, 0, 0.2)
    ga.init()
    ga.start()
    ga.print()
