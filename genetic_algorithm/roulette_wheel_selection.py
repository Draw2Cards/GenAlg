import random

from genetic_algorithm.fitness import fitness
from genetic_algorithm.selection_algorithm import SelectionAlgorith


class RouletteWheelSelection(SelectionAlgorith):
    def run(self, population, matrix):
        total_fitness = 0
        ratios = []
        for individual in population:
            ratio = 1 / (1 + fitness(individual, matrix))
            total_fitness += ratio
            ratios.append(ratio)
        cumulative_fitness = []
        cumulative_fitness_sum = 0
        for i in range(len(population)):
            cumulative_fitness_sum += ratios[i] / total_fitness
            cumulative_fitness.append(cumulative_fitness_sum)

        new_population = []
        for i in range(len(population)):
            roulette = random.uniform(0, 1)
            for j in range(len(population)):
                if roulette <= cumulative_fitness[j]:
                    new_population.append(population[j])
                    break
        return new_population
