import time, math, random
from puzzle import Puzzle

class PuzzleGenerator:
    def __init__(self, n_rows: int, n_columns: int, min_val: int, max_val: int):
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.min_val = min_val
        self.max_val = max_val
        self.max_time = 59.9  # To make sure we don't exceed a minute

    def generate_puzzle(self) -> Puzzle:
        start_time = time.time()
        best_puzzle = None
        best_value = float('-inf')        
        
        while time.time() - start_time < self.max_time:
            
            time_left = self.max_time - (time.time() - start_time)
            run_limit = min(5.0, time_left - 1.0)
            if run_limit <= 0:
                break
            
            candidate = self.simulated_annealing(run_limit)
            polish_time = min(1.0, time_left - run_limit)
            if polish_time > 0.1:
                candidate = self.hill_climb(candidate, time_limit=polish_time)

            val = candidate.get_value()
            if val > best_value:
                best_value = val
                best_puzzle = candidate

        return best_puzzle

    def simulated_annealing(self, time_limit: float) -> Puzzle:

        p = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)
        while not p.has_solution():
            p.randomize()
        current_value = p.get_value()
        best_puzzle, best_value = p, current_value

        T_initial = 100.0
        T = T_initial
        alpha = 0.80
        K = 10
        start_time = time.time()

        while time.time() - start_time < time_limit - 0.1:

            batch = []
            for _ in range(K):
                n = p.get_random_successor()
                batch.append((n, n.get_value()))

            best_neighbor, neighbor_value = batch[0]
            for candidate, val in batch[1:]:
                if val > neighbor_value:
                    best_neighbor, neighbor_value = candidate, val

            delta = neighbor_value - current_value
            if delta > 0 or random.random() < math.exp(delta / T):
                p = best_neighbor
                current_value = neighbor_value

                if neighbor_value > best_value:
                    best_puzzle, best_value = p, current_value

            T *= alpha
            if T < 0.001:
                T = T_initial

        return best_puzzle
    
    def hill_climb(self, p: Puzzle, time_limit: float) -> Puzzle:
        start_time = time.time()
        best_p = p 
        best_val = p.get_value()
        
        while time.time() - start_time < time_limit:
            improved = False
            
            for succ in best_p.get_all_successors():
                v = succ.get_value()
                
                if v > best_val:
                    best_p, best_val = succ, v
                    improved = True
                    
            if not improved:
                break
                
        return best_p

    def random_walk(self, time_limit: float) -> Puzzle:
        # A very simple function that starts at a random configuration and keeps randomly modifying it
        # until it hits the time limit. Returns the best solution found so far.
        
        p = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)  # Generate a random puzzle
        
        # Keep track of the best puzzle found so far (and its value)
        best_puzzle = p
        best_value = p.get_value()
        
        # Keep track of the time so we don't exceed it
        start_time = time.time()
        
        # Loop until we hit the time limit
        while time.time() - start_time < time_limit - 0.1:  # To make sure we don't exceed the time limit
            # Generate a successor of p by randomly changing the value of a random cell
            # (since we are doing a random walk, we just replace p with its successor)
            p = p.get_random_successor()
            value = p.get_value() 
            
            # Update the current best solution
            if value > best_value:  
                best_value = value  
                best_puzzle = p
        
        return best_puzzle