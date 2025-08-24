import numpy as np
import math
import random

# Define the objective function
def objective_function(x1, x2):
    return 20 + x1**2 + x2**2 - 10*(math.cos(2*math.pi*x1) + math.cos(2*math.pi*x2))

def get_fitness(pop):
    fit = np.zeros(population_size)
    for i in range(population_size):
        x1 = convert_bin_t_real(pop[i][:bits_var])
        x2 = convert_bin_t_real(pop[i][bits_var:])
        fit[i] = objective_function(x1, x2)
    return fit

# Define the initial population
def initialize_population(population_size):
    # Generate a population of binary strings
    population = []
    # Repeat the process for each individual in the population
    for _ in range(population_size):
        population = [''.join(np.random.choice(['0', '1']) for _ in range(bits_var * 2)) for _ in range(population_size)]
        return population

# Convert a binary string to a decimal value within the given range
def convert_bin_t_real(binary, lower=-5.0, upper=5.0):
    return lower + (upper - lower) * int(binary, 2) / (2**bits_var - 1)

def find_probabilities_range(fitness_values, sum_fit):
    probabilities = []
    for fitness in fitness_values:
        prob = (float) (fitness/sum_fit)
        probabilities.append(prob)
    
    probabilities_range_sum = []
    sum = 0.0
    for prob in probabilities:
        probabilities_range_sum.append(sum + prob)
        sum+=prob

    return probabilities_range_sum

def select_atoms(fitness_scores, population):
    # Normalize fitness scores to probabilities
    probabilities_sum = []
    probabilities_sum.append(0.0)
    sum = 0
    for fit in fitness_scores:
        sum+=fit

    for i in range(population_size):
        probabilities_sum.append(probabilities_sum[i] + (fitness_scores[i]/sum))
    #print(probabilities_sum)
    atoms_index = []
    for i in range(population_size):
        rand = random.random()
        for i in range(1, len(probabilities_sum)):
            if(rand >= probabilities_sum[i-1] and rand <probabilities_sum[i]):
                atoms_index.append(i-1)
    selected_atoms = []
    for index in atoms_index:
        selected_atoms.append(population[index])

    return selected_atoms


# Perform crossover
def crossover(population):
    cross_atoms_index = []
    for i in range(population_size):
        if random.random() < crossover_rate:
            cross_atoms_index.append(i)

    if len(cross_atoms_index)%2 != 0:
        cross_atoms_index.pop(len(cross_atoms_index)-1)

    for i in range(0, len(cross_atoms_index), 2):
        pos = np.random.randint(1, bits_var * 2 - 1)
        population[i] = population[i][:pos] + population[i+1][pos:]
        population[i+1] = population[i+1][:pos] + population[i][pos:]

    return population


# Perform mutation
def mutate(population):
    new_population = []
    for atom in population:
        for i in range(len(atom)):
            if random.random() < mutation_rate:
                if atom[i] == '0':
                    atom = atom[:i] + '1' + atom[i+1:]
                else:
                    atom = atom[:i] + '0' + atom[i+1:]
        new_population.append(atom)
    return new_population


# Genetic Algorithm
def genetic_algorithm(population_size, crossover_rate, mutation_rate, num_iterations):
    population = initialize_population(population_size)
    #print(population)
    for _ in range(num_generations):
        fitness_values = get_fitness(population)
        #print(fitness_values)
        new_population = []
        new_population = select_atoms(fitness_values, population)
        #print(new_population)
        new_population = crossover(new_population)
        #print(new_population)
        new_population = mutate(new_population)
        population = new_population
        #print(new_population)
    
    # get final results
    fitness_final = get_fitness(population)
    fitness_normalized = fitness_final / np.sum(fitness_final)
    output = []
    for i in range(population_size):
        output.append([population[i], convert_bin_t_real(population[i][:bits_var]), convert_bin_t_real(population[i][bits_var:]), fitness_final[i], fitness_normalized[i]])
    
    # Print Genotype
    print("Genotype in Binary\tx1\t\tx2\t\tFitness\t\tNormalized Fitness")
    for out in output:
        print(f"{out[0]}\t\t{out[1]:.1f}\t\t{out[2]:.1f}\t\t{out[3]:.2f}\t\t{out[4]:.2f}")

    # Print best genotype
    best_index = np.argmax(fitness_final)
    best_gen = population[best_index]
    best_x1 = convert_bin_t_real(best_gen[:bits_var])
    best_x2 = convert_bin_t_real(best_gen[bits_var:])
    best_fitness = fitness_final[best_index]

    print("\nBest Genotype (Binary):", best_gen)
    print(f"Best Phenotype: x1 = {best_x1:.1f}, x2 = {best_x2:.1f}")
    print("Best Fitness:", best_fitness)

# Parameters
population_size = 20
crossover_rate = 0.60
mutation_rate = 0.015
num_generations = 200
bits_var = 7  # Calculated with (b-a)*10^q <= mi-1

# Run the genetic algorithm
genetic_algorithm(population_size, crossover_rate, mutation_rate, num_generations)
