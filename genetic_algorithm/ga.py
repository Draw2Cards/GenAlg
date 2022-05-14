import random
import time

from genetic_algorithm.fitness import fitness
from genetic_algorithm.roulette_wheel_selection import RouletteWheelSelection
from genetic_algorithm.tournament_selection import TournamentSelection
from other.greedy import Greedy


def find_best_fitness(population):
    best_fitness = population[0][1]
    for i in population:
        if best_fitness == 0:
            break
        if i[1] < best_fitness:
            best_fitness = i[1]
    print(best_fitness)
    return best_fitness


def combine(old_pop, new_pop):
    new_best_fitness = new_pop[0]
    for i in new_pop:
        if new_best_fitness[1] == 0:
            break
        if i[1] < new_best_fitness[1]:
            new_best_fitness = i

    pos = 0
    old_least_fitness = old_pop[0]
    for cur_pos, i in enumerate(old_pop):
        if i[1] > old_least_fitness[1]:
            old_least_fitness = i
            pos = cur_pos

    if new_best_fitness[1] < old_least_fitness[1]:
        print(f'{old_least_fitness[1]}->{new_best_fitness[1]}')
        old_pop[pos] = new_best_fitness


class GeneticAlgorithm:
    def __init__(self, matrix, population_size, max_generations, selection_algorithm, mut_probability):
        self.matrix = matrix
        self.population_size = population_size
        self.max_generations = max_generations
        self.selection_algorithm = selection_algorithm
        self.mut_probability = mut_probability

        self.elapsed_time = 0
        self.best_fitness = -1
        self.new_population = []
        self.population_for_crossover = []
        self.cur_generation = 0
        self.colors_pool_size = 0
        self.vertex_num = 0
        self.population = []

        self.file_output = None

    def init(self):
        self.colors_pool_size = self.calc_max_vertex_degree() + 1
        self.vertex_num = len(self.matrix)

        if self.selection_algorithm == 0:
            self.selection_algorithm = RouletteWheelSelection
        elif self.selection_algorithm == 1:
            self.selection_algorithm = TournamentSelection

        self.file_output = open("le450_5a.csv", "a")

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

        greedy = Greedy(self.matrix)
        greedy.start()
        self.colors_pool_size = max(greedy.vertex) - 1
        print(f'init colors pool size: {self.colors_pool_size}')

        while solution_found and self.colors_pool_size > 0:
            self.generate_initial_population()
            while True:
                self.selection()
                self.new_population = self.crossover(self.population_for_crossover)
                self.mutation(self.population)
                combine(self.population, self.new_population)
                self.best_fitness = find_best_fitness(self.population)

                self.file_output.write(f'{time.time() - start_time};{self.best_fitness};{self.colors_pool_size}\n')
                print(f'T: {time.time() - start_time} - '
                      f'current generation: {self.cur_generation}/{self.max_generations} '
                      f'(best fitness: {self.best_fitness})')
                if self.best_fitness == 0 or self.cur_generation == self.max_generations:
                    break

            if self.best_fitness != 0:
                solution_found = False
                self.colors_pool_size += 1
            else:
                self.colors_pool_size -= 1
                print(f'current colors pool size: {self.colors_pool_size}')
        self.elapsed_time = time.time() - start_time
        self.file_output.close()

    def validate_population(self):
        for i, pop in enumerate(self.population):
            for j, color in enumerate(pop):
                if color > self.colors_pool_size:
                    self.population[i][j] = random.randint(1, self.colors_pool_size)

    def generate_initial_population(self):
        self.population = []
        for i in range(self.population_size):
            individual = self.create_individual()
            individual_fitness = fitness(individual, self.matrix)
            self.population.append([individual, individual_fitness])
        self.cur_generation = 0

    def create_individual(self):
        individual = []
        for _ in range(self.vertex_num):
            individual.append(random.randint(1, self.colors_pool_size))
        return individual

    def crossover(self, population):
        new_population = []
        random.shuffle(population)
        for i in range(1, self.population_size, 2):
            children = self.generate_children([self.population[i - 1], self.population[i]])
            children1_fittness = fitness(children[0], self.matrix)
            children2_fittness = fitness(children[1], self.matrix)

            if children1_fittness < children2_fittness:
                new_population.append([children[0], children1_fittness])
            else:
                new_population.append([children[1], children2_fittness])
        return new_population

    def generate_children(self, parents):
        children = [[], []]
        start_pos = random.randint(0, self.vertex_num - 2)
        end_pos = random.randint(start_pos + 1, self.vertex_num - 1)
        for i in range(self.vertex_num):
            if i < start_pos or i > end_pos:
                children[0].append(parents[0][0][i])
                children[1].append(parents[1][0][i])
            else:
                children[0].append(parents[1][0][i])
                children[1].append(parents[0][0][i])
        return children

    def mutation(self, population):
        for i_index, i in enumerate(population):
            rand = random.uniform(0, 1)
            if self.mut_probability > rand:
                ind_index = random.randint(0, len(i) - 1)
                uniq_list = [*range(1, self.colors_pool_size + 1)]
                result = False
                for row_index, row in enumerate(self.matrix[ind_index]):
                    if row_index > ind_index:
                        if row == 1:
                            if i[0][row_index] in uniq_list:
                                uniq_list.remove(i[0][row_index])
                            if i[0][ind_index] == i[0][row_index]:
                                result = True
                if result and len(uniq_list) > 0:
                    i[0][ind_index] = random.choice(uniq_list)
                    i[1] = fitness(i[0], self.matrix)

    def selection(self):
        self.population_for_crossover = self.selection_algorithm().run(self.population, self.matrix)
        self.cur_generation += 1

    def print(self):
        print('_________')
        print(self.colors_pool_size)
        print(self.elapsed_time)
        print('_________')
