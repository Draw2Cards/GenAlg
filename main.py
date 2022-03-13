from genetic_algorithm.ga import GeneticAlgorithm
from matrix.matrix_generator import MatrixGenerator

if __name__ == '__main__':
    # instance = Instance(matrix)
    # instance.gen_output()
    # matrix_gen = MatrixGenerator('D:\\ez.txt')
    matrix_gen = MatrixGenerator('D:\\test.txt')
    matrix = matrix_gen.gen()

    print("tour")
    for _ in range(25):
        ga = GeneticAlgorithm(matrix, 200, 500, 1, 0.2)
        ga.init()
        ga.start()
        ga.print()
    print("rws")
    for _ in range(25):
        ga = GeneticAlgorithm(matrix, 200, 500, 0, 0.2)
        ga.init()
        ga.start()
        ga.print()
