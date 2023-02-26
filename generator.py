import random

def generate_maze(width, height):
    # Create a grid of cells
    grid = [[{'visited': False, 'walls': [True, True, True, True]} for y in range(height)] for x in range(width)]

    # Define the starting cell
    current_x, current_y = random.randint(0, width-1), random.randint(0, height-1)
    grid[current_x][current_y]['visited'] = True

    # Define the DFS algorithm to carve out the maze
    def dfs(x, y):
        neighbors = []
        if x > 0 and not grid[x-1][y]['visited']:
            neighbors.append((x-1, y, 0, 2)) # (neighbor_x, neighbor_y, current wall, neighbor wall)
        if x < width-1 and not grid[x+1][y]['visited']:
            neighbors.append((x+1, y, 2, 0))
        if y > 0 and not grid[x][y-1]['visited']:
            neighbors.append((x, y-1, 1, 3))
        if y < height-1 and not grid[x][y+1]['visited']:
            neighbors.append((x, y+1, 3, 1))
        if not neighbors:
            return

        # Choose a random neighbor and remove the wall between it and the current cell
        neighbor_x, neighbor_y, current_wall, neighbor_wall = random.choice(neighbors)
        grid[neighbor_x][neighbor_y]['visited'] = True
        grid[x][y]['walls'][current_wall] = False
        grid[neighbor_x][neighbor_y]['walls'][neighbor_wall] = False

        # Recursively visit the chosen neighbor
        dfs(neighbor_x, neighbor_y)

    # Start the DFS algorithm from the starting cell
    dfs(current_x, current_y)

    # Convert the grid of cells to a grid of walls and spaces
    maze = [['#' for y in range(width*2+1)] for x in range(height*2+1)]
    for x in range(width):
        for y in range(height):
            maze[x*2+1][y*2+1] = ' '
            if not grid[x][y]['walls'][0]:
                maze[x*2+1][y*2] = ' '
            if not grid[x][y]['walls'][1]:
                maze[x*2+2][y*2+1] = ' '
            if not grid[x][y]['walls'][2]:
                maze[x*2+1][y*2+2] = ' '
            if not grid[x][y]['walls'][3]:
                maze[x*2][y*2+1] = ' '

    # Convert the maze to a string
    maze_str = '\n'.join([''.join(row) for row in maze])
    return maze_str
