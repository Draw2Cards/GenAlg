def fitness(individual, matrix):
    result = 0
    for ind_index, ind in enumerate(individual):
        for row_index, row in enumerate(matrix[ind_index]):
            if row_index > ind_index:
                if row == 1:
                    if individual[ind_index] == individual[row_index]:
                        result += 1
    return result
