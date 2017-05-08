import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    backtrack_stack = []
    current_cell = 0
    visited_cells = 0
    goal = m.total_cells - 1

    while current_cell != goal:
        neighbors = m.cell_neighbors(current_cell)
        if len(neighbors) > 0:
            #Choose random neighbor to be new cell
            random_index = random.randint(0, len(neighbors) - 1)
            neighbor = neighbors[random_index]
            new_cell, compass_index = neighbor[0], neighbor[1]
            # Visit new cell
            m.visit_cell(current_cell, new_cell, compass_index)
            # Push current cell to stack
            backtrack_stack.append(current_cell)
            # set current_cell to new_cell
            current_cell = new_cell
            # add one to visited_cells
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = backtrack_stack.pop()
        m.refresh_maze_view()
    m.state = 'idle'

# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
