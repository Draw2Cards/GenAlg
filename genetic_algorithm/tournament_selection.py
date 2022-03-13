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
                if t == 0:
                    fitness1 = fitness(population[i - 1], matrix)
                    population_with_fitness.append([population[i - 1], fitness1])
                    fitness2 = fitness(population[i], matrix)
                    population_with_fitness.append([population[i], fitness2])
                    if fitness1 < fitness2:
                        new_population.append(population[i - 1])
                    else:
                        new_population.append(population[i])
                else:
                    if population_with_fitness[i - 1][1] < population_with_fitness[i][1]:
                        new_population.append(population_with_fitness[i - 1][0])
                    else:
                        new_population.append(population_with_fitness[i][0])

        return new_population
