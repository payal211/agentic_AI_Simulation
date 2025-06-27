import pygad
import numpy as np
from model import EvolvingModel
from visualization import launch_visualization
from utils import save_genome, load_genome
from config import *  # Import all configuration constants

def fitness_func(ga_instance, solution, solution_idx):
    """Fitness function for genetic algorithm"""
    # Create multiple agents with the same genome
    genomes = [solution for _ in range(NUM_AGENTS)]
    model = EvolvingModel(genomes, width=GRID_WIDTH, height=GRID_HEIGHT)
    
    # Run simulation
    for _ in range(SIMULATION_STEPS):
        model.step()
    
    # Return total fitness (unique cells explored)
    return model.get_total_fitness()

def run_genetic_algorithm():
    """Run genetic algorithm to evolve optimal genome"""
    if VERBOSE_GA:
        print("🧬 Starting Genetic Algorithm Evolution...")
    
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
        keep_parents=GA_KEEP_PARENTS,
        parent_selection_type="sss",
        crossover_type="single_point",
        mutation_by_replacement=True,
    )

    ga_instance.run()
    
    best_solution, best_fitness, _ = ga_instance.best_solution()
    
    if VERBOSE_GA:
        print(f"🏆 Evolution Complete!")
        print(f"   Best Genome: [Speed: {best_solution[0]:.2f}, Exploration: {best_solution[1]:.2f}]")
        print(f"   Best Fitness: {best_fitness:.1f} cells explored")
    
    return best_solution

def create_diverse_genomes(best_genome, num_agents):
    """Create diverse genomes for more interesting visualization"""
    import random
    genomes = []
    
    for i in range(num_agents):
        if i == 0:
            # Keep one agent with the best genome
            genomes.append(best_genome.copy())
        else:
            # Create variations
            varied_genome = [
                best_genome[0] + random.uniform(-0.8, 0.8),  # Vary speed more
                best_genome[1] + random.uniform(-0.5, 0.5)   # Vary exploration
            ]
            # Clamp to valid ranges
            varied_genome[0] = max(0.1, min(3.0, varied_genome[0]))
            varied_genome[1] = max(0.1, min(3.0, varied_genome[1]))
            genomes.append(varied_genome)
    
    return genomes

def main():
    """Main execution function"""
    print("🤖 Evolving Agentic AI Simulation")
    print("=" * 40)
    
    if DEBUG_MODE:
        print(f"🔧 Config: {NUM_AGENTS} agents, {SIMULATION_STEPS} steps, {GA_GENERATIONS} generations")
    
    # Try to load existing genome
    saved_genome = load_genome()
    
    if saved_genome:
        print(f"📁 Found saved genome, using it for simulation with {NUM_AGENTS} agents")
        best_genome = saved_genome
    else:
        print(f"🔬 No saved genome found, running evolution with {NUM_AGENTS} agents...")
        best_genome = run_genetic_algorithm()
        save_genome(best_genome.tolist())
        print("💾 Genome saved for future use")
    
    print(f"\n🎮 Launching Visualization with {NUM_AGENTS} agents...")
    print("   Watch the agents explore and coordinate!")
    print("   - Blue agents: Slow (Speed 1)")
    print("   - Orange agents: Medium (Speed 2)")  
    print("   - Red agents: Fast (Speed 3)")
    print("   - Size indicates exploration tendency")
    
    # Create genomes for visualization
    # genomes = [best_genome for _ in range(NUM_AGENTS)]
    genomes = create_diverse_genomes(best_genome, NUM_AGENTS)
    
    if DEBUG_MODE:
        print(f"🔍 Debug: Created {len(genomes)} genomes for {NUM_AGENTS} agents")
    
    # Launch interactive visualization
    launch_visualization(genomes)

if __name__ == '__main__':
    main()