"""
This is a skeleton file for the implementation of your Genetic Algorithm (GA).
You can add functions to the file and implement your logic inside genetic_algorithm(),
but do not modify the other functions. print_generation_info() must be called on each iteration of the GA.
"""

# <--- ADD ADDITONAL IMPORTS HERE --->
import argparse
import random

# <---------------------------------->

# Population size: Defines how many individuals are in the initial population.
# (You can change this value)
POPULATION_SIZE = 100  # use this value for the generation of your inital population.

QUEEN_AMOUNT = 512

KNIGHT_OFFSETS = [
    (1, 2), (2, 1), (1, -2), (2, -1),
    (-1, 2), (-2, 1), (-1, -2), (-2, -1)
]
# <---------------------------------->

# <--- ADD ADDITONAL FUNCTIONS HERE --->

def _print_board(board: list):
  size = len(board)

  for row in range(size):
    for column in range(size):
      if board[column] == row:
        print("@", end=" ")
      else:
        print(".", end=" ")
    print()


def _check_diagonal(board: list) -> set:
    conflicts = set()

    # Uses arrays instead of dicts now, store queen col as value
    rising = [-1] * len(board) * 2
    falling = [-1] * len(board) * 2

    for col, row in enumerate(board):
        r = row + col
        f = row - col + len(board) # prevents -1 as a valid value

        if rising[r] != -1:
            conflicts.add(col)
            conflicts.add(rising[r])
        else:
            rising[r] = col

        if falling[f] != -1:
            conflicts.add(col)
            conflicts.add(falling[f])
        else:
            falling[f] = col

    return conflicts


def _check_knight_move(board: list) -> set:
    conflicts = set()
    board_size = len(board)

    for col_a, row_a in enumerate(board):

        for col_moves, row_moves in KNIGHT_OFFSETS:
            target_col = col_a + col_moves
            target_row = row_a + row_moves

            # ist die Zielspalte/zeile auf dem Brett?
            if 0 <= target_col < board_size and 0 <= target_row < board_size:
                # Steht die Dame in der Zielspalte auf der Zielzeile?
                if board[target_col] == target_row:
                    conflicts.add(col_a)
                    conflicts.add(target_col)

    return conflicts


def _generate() -> list:
    population = list(range(QUEEN_AMOUNT))
    random.shuffle(population)
    return population


def _mutate(board, conflicts):
    if not conflicts:
        return (QUEEN_AMOUNT, board, set())
        
    board = board.copy()
    current_conflicts = len(conflicts)
    conflict_list = list(conflicts)
    random.shuffle(conflict_list)

    for y in conflict_list:
        for x in range(len(board)):
            if x == y:
                continue
      
            board[y], board[x] = board[x], board[y]

            set1 = _check_diagonal(board)
            set2 = _check_knight_move(board) 
            new_conflicts = len(set1 | set2)
        
            if new_conflicts < current_conflicts:
                fitness = QUEEN_AMOUNT - new_conflicts
                return (fitness, board, (set1 | set2))
                
            board[y], board[x] = board[x], board[y]
            fitness = QUEEN_AMOUNT - current_conflicts

    return (fitness, board, conflicts)


# combines two random segments of parent1 and parent2 into child
def _crossover(parent1: list, parent2: list) -> list:
    board_size = len(parent1)
    child = [-1] * board_size

    # fill random segment with parent1
    start_idx = random.randint(0, board_size - 2)
    end_idx = random.randint(start_idx, board_size - 1)

    child[start_idx:end_idx] = parent1[start_idx:end_idx]

    # set because it's faster than list (col in child:)
    used = set(child)

    # fill rest with parent2, skip already used rows in parent2
    parent2_idx = 0
    for i in range(board_size):
        if child[i] == -1:
            while parent2[parent2_idx] in used:
                parent2_idx += 1
            child[i] = parent2[parent2_idx]
            used.add(parent2[parent2_idx])

    return child

# <------------------------------------>

def genetic_algorithm(gui_mode=False):
    
    list_of_boards = [_generate() for i in range(POPULATION_SIZE)]

    best_fitness = 0
   
    for gen in range(10000):
        current_gen_total_fitness = 0
        gens_ranked = []
        
        for i, board in enumerate(list_of_boards):
        
            # Prevent local maxima, just restarting
            if gen > 0 and gen % 500 == 0:
                list_of_boards[i] = _generate()
                board = list_of_boards[i]
        
            set1: set = _check_diagonal(board)
            set2: set = _check_knight_move(board)
            
            conflicts = set1 | set2
        
            fitness = QUEEN_AMOUNT - len(conflicts)
            gens_ranked.append((fitness, board, conflicts))
            current_gen_total_fitness += fitness
        
            if fitness > best_fitness:
                best_fitness = fitness
            
            if fitness == QUEEN_AMOUNT:
                print(f"Generation {gen} solved the problem!")
                if gui_mode:
                    _print_board(board)
                    input()
                return
                
        # Beste 10% überleben, den rest aus den besten kreuzen
        gens_ranked.sort(reverse=True, key=lambda x: x[0])
        fittest = gens_ranked[:POPULATION_SIZE//10]

        for i, board in enumerate(fittest):
            fittest[i] = _mutate(board[1], board[2])

        new_population = []
        for fitness, board, conflicts in fittest:
            new_population.append(board)

        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(fittest)[1]
            parent2 = random.choice(fittest)[1]

            child = _crossover(parent1, parent2)

            new_population.append(child)

        list_of_boards = new_population

        mean_fitness = current_gen_total_fitness / POPULATION_SIZE
        print_generation_info(gen, best_fitness, mean_fitness)
     

def print_generation_info(generation: int, best_fitness: float, mean_fitness: float) -> None:
    """
    Displays the statistics of the current population in a structured format.
    Args:
        generation (int): The current generation number.
        best_fitness (float): The best fitness value in the current population.
        mean_fitness (float): The arithmetic mean (average) fitness value of the current population.
    """

    N = 100  # Print every 100 generations (adjustable)
    if generation % N == 0:
        print(f" Generation {generation:>7} | Best Fitness: {best_fitness:.2f} | Mean Fitness: {mean_fitness:.2f} ")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Genetic Algorithm for solving the 1024-Queens Problem.")
    parser.add_argument("--gui", action="store_true", help="Enable GUI mode for visualization.")

    genetic_algorithm(gui_mode=parser.parse_args().gui)
