# Evolving Agentic AI Simulation

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Mesa](https://img.shields.io/badge/Mesa-1.2.1-green.svg)](https://mesa.readthedocs.io/)

A sophisticated simulation where autonomous agents evolve intelligent behaviors through genetic algorithms. Watch as simple agents learn to explore a grid world efficiently while communicating to avoid collisions.

![Simulation Preview](https://via.placeholder.com/600x400/4a90e2/ffffff?text=Grid+Simulation+Preview)

## What This Project Does

This isn't just another simulation—it's a **research platform** that demonstrates how artificial intelligence can emerge from the intersection of:

- **Agentic AI**: Fully autonomous agents that perceive, communicate, decide, and act independently
- **Genetic Evolution**: Agent behaviors evolve over generations without explicit programming
- **Multi-Agent Communication**: Distributed coordination through real-time message passing
- **Collision Avoidance**: Sophisticated conflict resolution for multi-agent environments
- **Emergent Intelligence**: Complex group behaviors arising from simple individual rules

## The Magic in Action

1. Agents explore a 10×10 toroidal grid world, racing to visit unique cells
2. They communicate positions every step to coordinate and avoid collisions
3. Genetic algorithms evolve their speed and exploration strategies over 30 generations
4. Optimal behaviors emerge naturally - no hand-coded strategies needed!

## How It Works

### Agent Architecture
Each agent operates with a simple but effective architecture:

```
Environment → Perception → Communication → Decision → Action
     ↑                                                   ↓
     ←←←←←←←←←←← Feedback Loop ←←←←←←←←←←←←←←←←←←←←←←←←←
```

### 🔄 Agent Decision Loop Process

1. **Sense Environment**: Perceive current position and surroundings
2. **Broadcast Position**: Send location to all other agents
3. **Receive Messages**: Get positions from other agents
4. **Plan Movement**: Generate possible moves based on speed genome
5. **Filter Conflicts**: Remove moves that would cause collisions
6. **Strategic Selection**: Choose optimal move based on exploration strategy
7. **Conflict Resolution**: Handle cases where multiple agents want same cell
8. **Execute Move**: Update position and mark cell as visited


### Genome Structure
Every agent carries a **2-gene genome** that defines its behavior:
- **Gene 1 (Speed)**: How many grid cells the agent can move per step (1-3)
- **Gene 2 (Exploration Chance)**: Probability of random vs. calculated movement (0.0-1.0)

### Evolution Process
1. **Population**: 15 different genomes compete across generations
2. **Simulation**: Each genome controls 10 agents for 50 time steps
3. **Fitness**: Total unique cells explored by all agents in the group
4. **Selection**: Top 6 genomes survive and reproduce
5. **Crossover**: Parent genomes combine to create offspring
6. **Mutation**: Random variations introduce behavioral diversity
7. **Iteration**: Process repeats for 30 generations until optimal behavior emerges

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/payal211/agentic_AI_Simulation.git
cd evolving-agentic-ai-sim

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Simulation

```bash
python main.py
```

**First run**: The genetic algorithm will evolve optimal behaviors (takes ~2-3 minutes)
**Subsequent runs**: Uses the saved best genome for immediate simulation

The simulation opens in your browser at `http://localhost:8521`

## What You'll See

### In the Terminal
```
Generation 1/20: Best fitness = 45.2
Generation 2/20: Best fitness = 52.1
...
Generation 20/20: Best fitness = 78.3
Best genome saved: [2.1, 0.67]
```

### In the Browser
- **Colored circles**: Each agent with distinct colors
- **Real-time movement**: Agents exploring the grid
- **Collision avoidance**: Watch them coordinate to avoid overlap
- **Coverage patterns**: Efficient exploration strategies emerge

## 📁 Project Structure

```
evolving-agentic-ai-sim/
├── agent.py              # EvolvingAgent class with behavior logic
├── model.py              # EvolvingModel class (environment + scheduler)
├── visualization.py      # Mesa visualization setup
├── main.py               # Main script with genetic algorithm
├── utils.py              # Genome save/load utilities
├── requirements.txt      # Python dependencies
├── best_genome.json      # Saved optimal genome (auto-generated)
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
└── README.md             # This file
```

## Key Components Explained

### EvolvingAgent (`agent.py`)
- **Autonomous decision-making**: Each step involves sensing, communicating, and moving
- **Memory system**: Tracks visited locations to avoid redundant exploration
- **Communication protocol**: Broadcasts position and receives others' locations
- **Collision avoidance**: Filters out moves that would conflict with other agents

### EvolvingModel (`model.py`)
- **Environment management**: 10×10 grid with wraparound boundaries
- **Message passing system**: Central communication hub for all agents
- **Simultaneous activation**: All agents perceive, then all agents act (prevents order bias)

### Visualization (`visualization.py`)
- **Real-time display**: Interactive Mesa-based web visualization
- **Agent differentiation**: Colors represent speed, size represents exploration tendency
- **Live updates**: Watch agents coordinate and explore in real-time

### Genetic Algorithm (`main.py`)
- **PyGAD integration**: Professional-grade genetic algorithm implementation
- **Fitness evaluation**: Rewards genomes that lead to better exploration coverage
- **Persistence**: Best genomes are saved and reused across sessions

## Configuration Options

### Key Components Deep Dive
1. EvolvingAgent (agent.py)
The heart of the simulation - autonomous AI agents with:

- **Memory System**: Tracks all visited locations to avoid redundancy
- **Communication Protocol**: Broadcasts position and receives neighbor locations
- **Strategic Planning**: Balances exploration vs. exploitation based on genome
- **Collision Avoidance**: Filters moves to prevent agent overlap
- **Adaptive Behavior**: Adjusts strategy based on environment and other agents

2. EvolvingModel (model.py)
The environment that orchestrates agent interactions:

- **Coordinated Execution**: 5-phase step process prevents race conditions
- **Message Passing Hub**: Central communication system for all agents
- **Conflict Resolution**: Sophisticated system for handling movement conflicts
- **Toroidal Grid**: Wraparound boundaries create seamless exploration space

3. Interactive Visualization (visualization.py)
Real-time web-based visualization featuring:

- **Color-coded Agents**: Speed determines color (Blue→Orange→Red)
- **Size Indicators**: Exploration tendency affects agent size
- **Live Updates**: Real-time movement and coordination
- **Professional UI**: Clean, informative display with legend

4. Genetic Algorithm (main.py)
Advanced evolution system using PyGAD:

- **Smart Initialization**: Population starts with diverse behavioral strategies
- **Fitness-based Selection**: Rewards effective exploration coverage
- **Single-point Crossover**: Combines successful parent strategies
- **Adaptive Mutation**: Maintains diversity while converging on optimal solutions


Want to experiment? Here are key parameters you can modify:

```python
# In config.py
NUM_AGENTS = 5           # Number of agents per simulation
GENOME_LENGTH = 2        # Genes per agent (speed, exploration_chance)
SIMULATION_STEPS = 50    # Steps per fitness evaluation
GA_GENERATIONS = 30      # Evolution cycles

# In the GA configuration
sol_per_pop=15          # Population size
mutation_percent_genes=25 # Mutation rate

# In model.py
width=10, height=10     # Grid dimensions
```

## Research Applications

This simulation serves as a foundation for exploring:

### Multi-Agent Systems Research
- **Distributed coordination**: How agents coordinate without central control
- **Communication protocols**: Efficiency of different message-passing strategies
- **Scalability**: Performance as agent populations grow

### Evolutionary Computation
- **Behavior evolution**: How complex strategies emerge from simple parameters
- **Fitness landscapes**: Understanding what makes some behaviors better than others
- **Population dynamics**: How diversity and selection pressure interact

### Emergent Intelligence
- **Swarm intelligence**: Collective problem-solving capabilities
- **Adaptive behavior**: How agents adjust to environmental constraints
- **Robustness**: System performance under different conditions

## Extension Ideas

Ready to take this further? Try implementing:

### Enhanced Behaviors
- **Vision range**: Agents can see N steps ahead
- **Memory decay**: Agents gradually forget old information
- **Energy systems**: Movement costs energy, rest restores it
- **Specialization**: Different agent types with unique abilities

### Complex Environments
- **Obstacles**: Static barriers that block movement
- **Resources**: Collectible items that provide rewards
- **Dynamic environments**: Walls that move or disappear
- **Multi-level grids**: 3D exploration spaces

### Advanced AI
- **Neural networks**: Replace simple logic with trainable networks
- **Reinforcement learning**: Agents learn from rewards/penalties
- **Hierarchical behaviors**: High-level strategies controlling low-level actions
- **Social learning**: Agents learn by observing successful neighbors

### 📊 Analysis Tools
- **Performance visualization**: Charts showing evolution progress
- **Behavior analysis**: Heatmaps of movement patterns
- **Network analysis**: Communication patterns between agents
- **Statistical reporting**: Automated experiment analysis


### Development Setup
```bash
# Fork the repository on GitHub
git clone https://github.com/payal211/agentic_AI_Simulation.git
cd evolving-agentic-ai-sim

# Create a development branch
git checkout -b feature/your-feature-name

# Make your changes and test
python agentic_ai_sim.py

# Commit and push
git commit -m "Add amazing feature"
git push origin feature/your-feature-name
```

## 📚 Learn More

### Related Concepts
- [Agent-Based Modeling](https://en.wikipedia.org/wiki/Agent-based_model)
- [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Emergent Behavior](https://en.wikipedia.org/wiki/Emergent_behavior)

### Recommended Reading
- "Introduction to Multi-Agent Systems" by Michael Wooldridge
- "Genetic Algorithms in Search, Optimization, and Machine Learning" by David Goldberg
- "Growing Artificial Societies" by Epstein & Axtell

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **[Mesa Framework](https://mesa.readthedocs.io/)**: Excellent agent-based modeling platform
- **[PyGAD](https://github.com/ahmadfora/GeneticAlgorithmPython)**: Powerful genetic algorithm library
- **Complexity Science Community**: For inspiration and foundational research

