from mesa import Model
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
from agent import EvolvingAgent
from collections import defaultdict

class EvolvingModel(Model):
    def __init__(self, genomes, width=10, height=10):
        super().__init__()
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = SimultaneousActivation(self)
        self.messages = []
        self.move_conflicts = defaultdict(list)  # Track conflicting moves
        
        # Create agents from genomes
        for i, genome in enumerate(genomes):
            agent = EvolvingAgent(i, self, genome)
            self.schedule.add(agent)
            
            # Place agent at random position
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))
            agent.visited.add((x, y))

        self.running = True

    def step(self):
        """Execute one time step with enhanced collision resolution"""
        # Phase 1: Clear previous step data
        self.messages = []
        self.move_conflicts.clear()
        
        # Phase 2: All agents sense and communicate
        for agent in self.schedule.agents:
            agent.send_position()
            agent.intended_move = None  # Reset intended moves
        
        # Phase 3: All agents receive messages and plan moves
        for agent in self.schedule.agents:
            agent.receive_positions()
            agent.plan_move()  # New method: plan but don't execute yet
        
        # Phase 4: Resolve move conflicts
        self.resolve_move_conflicts()
        
        # Phase 5: Execute all moves
        for agent in self.schedule.agents:
            if hasattr(agent, 'intended_move') and agent.intended_move:
                if agent.intended_move != agent.pos:  # Only move if different position
                    self.grid.move_agent(agent, agent.intended_move)
                    agent.visited.add(agent.intended_move)

    def resolve_move_conflicts(self):
        """Resolve cases where multiple agents want the same cell"""
        # Group agents by their intended moves
        move_groups = defaultdict(list)
        for agent in self.schedule.agents:
            if hasattr(agent, 'intended_move') and agent.intended_move:
                move_groups[agent.intended_move].append(agent)
        
        # Resolve conflicts
        for destination, competing_agents in move_groups.items():
            if len(competing_agents) > 1:
                # Conflict! Multiple agents want the same cell
                
                # Strategy 1: Priority based on agent fitness
                competing_agents.sort(key=lambda a: a.get_fitness(), reverse=True)
                winner = competing_agents[0]
                losers = competing_agents[1:]
                
                # Winner keeps their intended move
                # Losers must choose alternative moves
                for loser in losers:
                    loser.intended_move = self.find_alternative_move(loser, destination)
    
    def find_alternative_move(self, agent, blocked_position):
        """Find alternative move when preferred position is blocked"""
        x, y = agent.pos
        
        # Generate alternative moves (exclude the blocked position)
        alternatives = []
        for dx in range(-agent.speed, agent.speed + 1):
            for dy in range(-agent.speed, agent.speed + 1):
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                new_x = new_x % self.grid.width
                new_y = new_y % self.grid.height
                new_pos = (new_x, new_y)
                
                # Skip the blocked position and current positions of other agents
                if (new_pos != blocked_position and 
                    new_pos not in [pos for uid, pos in self.messages if uid != agent.unique_id]):
                    alternatives.append(new_pos)
        
        if alternatives:
            # Prefer unvisited cells
            unvisited = [pos for pos in alternatives if pos not in agent.visited]
            if unvisited:
                return agent.random.choice(unvisited)
            else:
                return agent.random.choice(alternatives)
        else:
            # No alternatives available, stay put
            return agent.pos

    def get_total_fitness(self):
        """Get combined fitness of all agents"""
        return sum(agent.get_fitness() for agent in self.schedule.agents)