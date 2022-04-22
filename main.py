from genetic_algorithm.ga import GeneticAlgorithm
from matrix.graph_gen import GraphGenerator
from matrix.instance import Instance
from matrix.matrix_generator import MatrixGenerator
from other.greedy import Greedy
from other.largest_first import LargestFirst
from other.saturation_largest_first import SaturationLargestFirst
from other.smallest_last import SmallestLast

if __name__ == '__main__':

    #graph_gen = GraphGenerator(4, 0.75)
    #matrix = graph_gen.gen_rand_graph()
    #instance = Instance(matrix)
    #instance.gen_output()
    # matrix_gen = MatrixGenerator('D:\\ez.txt')
    #matrix_gen = MatrixGenerator('D:\\gc_1000.txt')
    matrix_gen = MatrixGenerator('D:\\gc500.txt')
    matrix = matrix_gen.gen()

    greedy = Greedy(matrix)
    greedy.start()
    greedy.print()

    lf = LargestFirst(matrix)
    lf.start()
    lf.print()

    slf = SaturationLargestFirst(matrix)
    slf.start()
    slf.print()

    sl = SmallestLast(matrix)
    sl.start()
    sl.print()

    # print("tour")
    # for _ in range(25):
    #     ga = GeneticAlgorithm(matrix, 200, 500, 1, 0.2)
    #     ga.init()
    #     ga.start()
    #     ga.print()
    # print("rws")
    # for _ in range(25):
    #     ga = GeneticAlgorithm(matrix, 200, 500, 0, 0.2)
    #     ga.init()
    #     ga.start()
    #     ga.print()
