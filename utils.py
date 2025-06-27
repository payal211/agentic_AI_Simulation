import json
import os
from config import GENOME_SAVE_FILE, DEBUG_MODE

def save_genome(genome):
    """Save the best genome to file"""
    try:
        with open(GENOME_SAVE_FILE, 'w') as f:
            json.dump({
                "genome": genome,
                "timestamp": "2025-06-27",
                "version": "1.0"
            }, f, indent=2)
        
        message = f"✅ Genome saved to {GENOME_SAVE_FILE}"
        if DEBUG_MODE:
            message += f" - Values: {genome}"
        print(message)
        
    except Exception as e:
        print(f"❌ Error saving genome: {e}")

def load_genome():
    """Load the best genome from file"""
    try:
        if os.path.exists(GENOME_SAVE_FILE):
            with open(GENOME_SAVE_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict) and "genome" in data:
                    genome = data["genome"]
                else:
                    genome = data  # Old format compatibility
                
                if DEBUG_MODE:
                    print(f"🔍 Loaded genome: {genome}")
                return genome
        return None
    except Exception as e:
        print(f"⚠️  Error loading genome: {e}")
        return None