# Configuration file for Evolving Agentic AI Simulation
# All simulation parameters in one place

# === SIMULATION PARAMETERS ===
NUM_AGENTS = 10          # Number of agents in each simulation
GENOME_LENGTH = 2        # Number of genes per agent (speed, exploration_chance)
SIMULATION_STEPS = 50    # Steps per fitness evaluation
GRID_WIDTH = 10          # Grid width
GRID_HEIGHT = 10         # Grid height

# === GENETIC ALGORITHM PARAMETERS ===
GA_GENERATIONS = 30      # Number of evolution cycles
GA_POPULATION_SIZE = 15  # Population size for GA
GA_PARENTS_MATING = 6    # Number of parents for mating
GA_MUTATION_RATE = 25    # Mutation percentage
GA_KEEP_PARENTS = 2      # Number of parents to keep each generation

# === GENOME CONSTRAINTS ===
SPEED_MIN = 0.1          # Minimum speed value
SPEED_MAX = 3.0          # Maximum speed value
EXPLORATION_MIN = 0.1    # Minimum exploration chance
EXPLORATION_MAX = 3.0    # Maximum exploration chance

# === VISUALIZATION PARAMETERS ===
VISUALIZATION_PORT = 8521 # Port for Mesa visualization server
CANVAS_SIZE = 500        # Canvas size in pixels

# === FILE PATHS ===
GENOME_SAVE_FILE = "best_genome.json"

# === DEBUGGING ===
DEBUG_MODE = False       # Enable debug prints
VERBOSE_GA = True        # Show GA progress