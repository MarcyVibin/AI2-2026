"""
This is a skeleton file for the implementation of your Genetic Algorithm (GA).
You can add functions to the file and implement your logic inside genetic_algorithm(),
but do not modify the other functions. print_generation_info() must be called on each iteration of the GA.
"""

# <--- ADD ADDITONAL IMPORTS HERE --->
import argparse
import random

# <---------------------------------->

# row indices, e.g. 5
vertical_rows = set()

# row + column e.g. 5+512 = 517
rising_diagonals = set()

# row - column
falling_diagonals = set()

# have to figure this out: other sets + 1  and + 2?
knight_threats = set()


# Population size: Defines how many individuals are in the initial population.
# (You can change this value)
POPULATION_SIZE = 100  # use this value for the generation of your inital population.
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

    # each diagonal can be occupied by exactly 1 queen (store pos in dictionary)
    rising_diag = {}
    falling_diag = {}

    for col, row in enumerate(board):
        rise = row + col
        fall = row - col

        if rise in rising_diag:
            conflicts.add(col)
            conflicts.add(rising_diag[rise])
        else:
            rising_diag[rise] = col

        if fall in falling_diag:
            conflicts.add(col)
            conflicts.add(falling_diag[fall])
        else:
            falling_diag[fall] = col

    return conflicts


def _check_knight_move(board: list) -> set:
    conflicts = set()
    board_size = len(board)

    for column_a in range(board_size):
        row_a = board[column_a]

        for column_b in range(column_a + 1, board_size):
            row_b = board[column_b]

            row_diff = abs(row_a - row_b)
            column_diff = abs(column_a - column_b)

            knight_attack = ((row_diff == 1 and column_diff == 2) or (row_diff == 2 and column_diff == 1))
            
            if knight_attack:
                conflicts.add(column_a)
                conflicts.add(column_b)

    return conflicts


def _generate() -> list:
    population = list(range(512))
    random.shuffle(population)
    return population


# TODO: currently swaps random conflicts, should choose good pos instead, maybe store amount of conflicts per queen?
def _mutate(population, conflicts):

    x, y = random.sample(list(conflicts), 2)

    population[x], population[y] = population[y], population[x]


# <------------------------------------>

def genetic_algorithm(gui_mode=False):

    board = _generate()

    best_fitness = 0
    total_fitness = 0
    mean_fitness = 0

    for gen in range(10000):
        print_generation_info(gen, best_fitness, mean_fitness)

        # Prevent local maxima, is just restarting a good idea?
        if gen % 2000 == 0:
            board = _generate()

        set1: set = _check_diagonal(board)
        set2: set = _check_knight_move(board)
        
        conflicts = set1 | set2
    
        fitness = 512 - len(conflicts)
        total_fitness += fitness
        mean_fitness = total_fitness / (gen + 1)

        if fitness > best_fitness:
            best_fitness = fitness

        _mutate(board, conflicts)

    if gui_mode:
        _print_board(board)
        input()


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