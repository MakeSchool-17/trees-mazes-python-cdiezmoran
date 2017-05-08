import maze
import random

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # Implement create_dfs
    backtrack_stack = []
    current_cell = random.randint(0, m.total_cells - 1)
    visited_cells = 1

    while visited_cells < m.total_cells:
        neighbors = m.cell_neighbors(current_cell)
        if len(neighbors) > 0:
            #Choose random neighbor to be new cell
            random_index = random.randint(0, len(neighbors) - 1)
            neighbor = neighbors[random_index]
            new_cell = neighbor[0]
            # knock down walls
            m.connect_cells(current_cell, new_cell, neighbor[1])
            # push current cell to stack
            backtrack_stack.append(current_cell)
            # set current_cell to new_cell
            current_cell = new_cell
            # add one to visited_cells
            visited_cells += 1
        else:
            current_cell = backtrack_stack.pop()
        m.refresh_maze_view()
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
