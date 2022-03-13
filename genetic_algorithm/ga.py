import random
import time

from genetic_algorithm.fitness import fitness
from genetic_algorithm.roulette_wheel_selection import RouletteWheelSelection


class GeneticAlgorithm:
    def __init__(self, matrix, population_size, max_generations, selection_algorithm, mut_probability):
        self.matrix = matrix
        self.population_size = population_size
        self.max_generations = max_generations
        self.selection_algorithm = selection_algorithm
        self.mut_probability = mut_probability

        self.elapsed_time = 0
        self.fittest_individual = 0
        self.best_fitness = -1
        self.new_population = []
        self.cur_generation = 0
        self.colors_pool_size = 0
        self.vertex_num = 0
        self.population = []

    def init(self):
        self.colors_pool_size = self.calc_max_vertex_degree() + 1
        self.vertex_num = len(self.matrix)

        if self.selection_algorithm == 0:
            self.selection_algorithm = RouletteWheelSelection

    def calc_max_vertex_degree(self):
        max_vertex_degree = 0
        for row_index, row in enumerate(self.matrix):
            cur_vertex_degree = 0
            for col_index, val in enumerate(row):
                if val == 1:
                    cur_vertex_degree += 1
            if cur_vertex_degree > max_vertex_degree:
                max_vertex_degree = cur_vertex_degree
        return max_vertex_degree

    def start(self):
        start_time = time.time()
        solution_found = True
        while solution_found and self.colors_pool_size > 0:
            self.generate_initial_population()
            while True:
                self.selection()
                self.crossover()
                self.mutation()
                self.compute_fitness()

                if self.best_fitness == 0 or self.cur_generation == self.max_generations:
                    break

            print("Using ", self.colors_pool_size, " colors : ")
            print("Generation: ", self.cur_generation, "Best_Fitness: ",
                  self.best_fitness, "Individual: ", self.fittest_individual)
            if self.best_fitness != 0:
                solution_found = False
                print("Graph is ", self.colors_pool_size + 1, " colorable")
            else:
                self.colors_pool_size -= 1
        self.elapsed_time = time.time() - start_time

    def generate_initial_population(self):
        self.population = []
        for _ in range(self.population_size):
            self.population.append(self.create_individual())
        self.cur_generation = 0

    def create_individual(self):
        individual = []
        for _ in range(self.vertex_num):
            individual.append(random.randint(1, self.colors_pool_size))
        return individual

    def crossover(self):
        random.shuffle(self.population)
        for i in range(1, self.population_size - 1, 2):
            self.new_population.extend(self.generate_children([self.population[i - 1], self.population[i]]))

    def generate_children(self, parents):
        children = [[], []]
        start_pos = random.randint(0, self.vertex_num - 2)
        end_pos = random.randint(start_pos + 1, self.vertex_num - 1)
        for i in range(self.vertex_num):
            if i < start_pos or i > end_pos:
                children[0].append(parents[0][i])
                children[1].append(parents[1][i])
            else:
                children[0].append(parents[1][i])
                children[1].append(parents[0][i])
        return children

    def mutation(self):
        for i in self.new_population:
            if self.mut_probability > random.uniform(0, 1):
                pos = random.randint(0, self.vertex_num - 1)
                i[pos] = random.randint(1, self.colors_pool_size)

    def selection(self):
        self.population = self.selection_algorithm().run(self.population, self.matrix)
        self.new_population = []
        self.cur_generation += 1

    def compute_fitness(self):
        self.population = self.new_population
        self.best_fitness = fitness(self.population[0], self.matrix)
        self.fittest_individual = self.population[0]
        for i in self.population:
            if self.best_fitness == 0:
                break
            if fitness(i, self.matrix) < self.best_fitness:
                self.best_fitness = fitness(i, self.matrix)
                self.fittest_individual = i

    def print(self):
        print('_________')
        print(self.elapsed_time)
        print('_________')
