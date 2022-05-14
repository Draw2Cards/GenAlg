import random

from genetic_algorithm.fitness import fitness
from genetic_algorithm.selection_algorithm import SelectionAlgorith


class TournamentSelection(SelectionAlgorith):
    def run(self, population, matrix):
        new_population = []
        population_with_fitness = []
        for t in range(2):
            if t == 0:
                random.shuffle(population)
            else:
                random.shuffle(population_with_fitness)
            for i in range(1, len(population), 2):
                if population[i - 1][1] < population[i][1]:
                    new_population.append(population[i - 1][0])
                else:
                    new_population.append(population[i][0])

        return new_population
