from mesa import Agent
import random

class EvolvingAgent(Agent):
    def __init__(self, unique_id, model, genome):
        super().__init__(unique_id, model)
        
        # Properly convert genome values to usable parameters
        self.speed = max(1, min(3, int(genome[0])))
        # Normalize exploration chance to 0-1 range if it's outside
        raw_exploration = genome[1]
        if raw_exploration > 1.0:
            self.exploration_chance = raw_exploration / 3.0  # Scale down from 0-3 to 0-1
        else:
            self.exploration_chance = raw_exploration
        self.exploration_chance = max(0.0, min(1.0, self.exploration_chance))
        
        self.genome = genome
        self.visited = set()
        self.visited.add(self.pos if hasattr(self, 'pos') else (0, 0))
        self.intended_move = None
        self.other_positions = []
        
        # Debug info (remove in production)
        print(f"🤖 Agent {unique_id}: Speed={self.speed}, Exploration={self.exploration_chance:.2f} (from genome {genome})")

    def step(self):
        """Execute one step: this is now handled by the model's coordinated approach"""
        pass  # The model now coordinates all phases

    def send_position(self):
        """Broadcast current position to other agents"""
        if hasattr(self, 'pos'):
            self.model.messages.append((self.unique_id, self.pos))

    def receive_positions(self):
        """Receive positions from other agents"""
        self.other_positions = [pos for uid, pos in self.model.messages 
                               if uid != self.unique_id]

    def plan_move(self):
        """Plan next move without executing it"""
        if not hasattr(self, 'pos'):
            return
            
        x, y = self.pos
        
        # Generate possible moves based on speed
        options = []
        for dx in range(-self.speed, self.speed + 1):
            for dy in range(-self.speed, self.speed + 1):
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                new_x = new_x % self.model.grid.width
                new_y = new_y % self.model.grid.height
                options.append((new_x, new_y))

        # Filter out positions currently occupied by other agents
        safe_moves = [pos for pos in options if pos not in self.other_positions]
        
        if not safe_moves:
            # If all moves blocked, stay put rather than collide
            self.intended_move = self.pos
            return

        # Choose move based on exploration strategy
        if random.random() < self.exploration_chance:
            # Exploration mode: prefer unvisited cells
            unvisited_moves = [pos for pos in safe_moves if pos not in self.visited]
            if unvisited_moves:
                self.intended_move = random.choice(unvisited_moves)
            else:
                self.intended_move = random.choice(safe_moves)
        else:
            # Strategic mode: choose best move for coverage
            self.intended_move = self.choose_strategic_move(safe_moves)

    def choose_strategic_move(self, safe_moves):
        """Choose move that maximizes exploration efficiency"""
        if not safe_moves:
            return self.pos
        
        best_move = safe_moves[0]
        best_score = -float('inf')
        
        for move in safe_moves:
            score = 0
            mx, my = move
            
            # High bonus for unvisited cells
            if move not in self.visited:
                score += 100
            
            # Bonus for distance from other agents (spread out)
            min_distance = float('inf')
            for other_pos in self.other_positions:
                if other_pos:
                    ox, oy = other_pos
                    # Use torus distance calculation
                    dx = min(abs(mx - ox), self.model.grid.width - abs(mx - ox))
                    dy = min(abs(my - oy), self.model.grid.height - abs(my - oy))
                    distance = dx + dy
                    min_distance = min(min_distance, distance)
            
            if min_distance != float('inf'):
                score += min_distance * 10
                
            # Small penalty for being too close to edges (encourages central exploration)
            edge_distance = min(mx, self.model.grid.width - mx - 1, 
                              my, self.model.grid.height - my - 1)
            score += edge_distance * 2
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move

    def get_fitness(self):
        """Return fitness (number of unique cells visited)"""
        return len(self.visited)