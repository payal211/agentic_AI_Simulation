import pygad
import numpy as np
from model import EvolvingModel
from utils import save_genome, load_genome
from config import *  # Import all configuration constants

def fitness_func(ga_instance, solution, solution_idx):
    genomes = [solution for _ in range(NUM_AGENTS)]
    model = EvolvingModel(genomes, width=GRID_WIDTH, height=GRID_HEIGHT)
    for _ in range(SIMULATION_STEPS):
        model.step()
    total_fitness = sum(len(agent.visited) for agent in model.schedule.agents)
    return total_fitness

def run_ga_and_visualize():
    saved = load_genome()
    if saved:
        print("Loaded saved genome. Skipping GA.")
        genomes = [saved for _ in range(NUM_AGENTS)]
        model = EvolvingModel(genomes, width=GRID_WIDTH, height=GRID_HEIGHT)
        for _ in range(SIMULATION_STEPS):
            model.step()
    else:
        ga_instance = pygad.GA(
            num_generations=GA_GENERATIONS,
            num_parents_mating=GA_PARENTS_MATING,
            fitness_func=fitness_func,
            sol_per_pop=GA_POPULATION_SIZE,
            num_genes=GENOME_LENGTH,
            init_range_low=SPEED_MIN,
            init_range_high=SPEED_MAX,
            mutation_percent_genes=GA_MUTATION_RATE,
            mutation_type="random",
            random_mutation_min_val=EXPLORATION_MIN,
            random_mutation_max_val=EXPLORATION_MAX,
        )

        ga_instance.run()
        best_solution, _, _ = ga_instance.best_solution()
        save_genome(best_solution.tolist())

        genomes = [best_solution for _ in range(NUM_AGENTS)]
        model = EvolvingModel(genomes, width=GRID_WIDTH, height=GRID_HEIGHT)
        for _ in range(SIMULATION_STEPS):
            model.step()

if __name__ == '__main__':
    run_ga_and_visualize()