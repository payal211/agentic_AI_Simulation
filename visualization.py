from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import EvolvingModel

def agent_portrayal(agent):
    """Define how agents appear in visualization"""
    
    # Ensure we have the agent's actual speed (should be 1, 2, or 3)
    actual_speed = max(1, min(3, int(agent.speed)))
    
    # More vibrant colors based on speed
    speed_colors = {
        1: "#2980b9",  # Bright Blue (slow)
        2: "#e67e22",  # Bright Orange (medium) 
        3: "#c0392b"   # Bright Red (fast)
    }
    
    # Get color, with fallback
    color = speed_colors.get(actual_speed, "#95a5a6")
    
    # Size based on exploration chance (clamped to reasonable range)
    exploration_normalized = max(0.0, min(1.0, agent.exploration_chance))
    size = 0.3 + (exploration_normalized * 0.5)  # Size between 0.3 and 0.8
    
    # Add a border to make agents more visible
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "r": size,
        "Color": color,
        "stroke_color": "#2c3e50",  # Dark border
        "stroke_width": 2,
        "Layer": 0,
        "text": f"{actual_speed}",
        "text_color": "white",
        "text_size": 12
    }
    
    return portrayal

def launch_visualization(genomes):
    """Launch Mesa visualization server"""
    print(f"🔍 Visualization Debug: Received {len(genomes)} genomes")
    
    # Debug: Show what we're working with
    if genomes:
        sample_genome = genomes[0]
        sample_speed = max(1, min(3, int(sample_genome[0])))
        sample_exploration = max(0.0, min(1.0, sample_genome[1]))
        print(f"📊 Sample agent will have: Speed={sample_speed}, Exploration={sample_exploration:.2f}")
    
    # Create the grid visualization
    grid = CanvasGrid(
        agent_portrayal, 
        10, 10,           # Grid dimensions
        600, 600          # Canvas size (larger for better visibility)
    )
    
    server = ModularServer(
        EvolvingModel,
        [grid],
        f"Evolving Agentic AI Simulation ({len(genomes)} agents)",
        {"genomes": genomes}
    )
    
    server.port = 8521
    
    print(f"🚀 Starting visualization with {len(genomes)} agents at http://localhost:8521")
    print("🎨 Color Legend:")
    print("   🔵 Blue circles = Speed 1 (slow)")
    print("   🟠 Orange circles = Speed 2 (medium)")
    print("   🔴 Red circles = Speed 3 (fast)")
    print("   📏 Larger circles = Higher exploration tendency")
    
    server.launch()