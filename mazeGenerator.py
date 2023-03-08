import random
from colorama import init
from colorama import Fore
import numpy as np


class MazeGenerator:
    def __init__(self, height, width):
        # Init variables
        self.wall = '*'
        self.cell = 'o'
        self.unvisited = 'u'
        self.height = height
        self.width = width
        self.maze = []
        self.start = []
        self.end = []


    ## Methods
    def printMaze(self, maze):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if maze[i][j] == 'u':
                    print(Fore.BLUE + str(maze[i][j]), end="  ")
                elif maze[i][j] == 'o':
                    print(Fore.RESET + str(maze[i][j]), end="  ")
                elif maze[i][j] == 'v':
                    print(Fore.BLUE + str(maze[i][j]), end="  ")
                elif maze[i][j] == 'S' or maze[i][j] == 'G' or maze[i][j] == 'p':
                    print(Fore.LIGHTGREEN_EX + str(maze[i][j]), end="  ")
                else:
                    print(Fore.RED + str(maze[i][j]), end="  ")

            print('')
        print(Fore.RESET)

    def printMazeSmooth(self, maze):
        out = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                if maze[i][j] == 'u':
                    out = out + Fore.BLUE + str(maze[i][j]) + "  "
                elif maze[i][j] == 'o':
                    out = out + Fore.RESET + str(maze[i][j]) + "  "
                elif maze[i][j] == 'v':
                    out = out + Fore.BLUE + str(maze[i][j]) + "  "
                elif maze[i][j] == 'S' or maze[i][j] == 'G' or maze[i][j] == 'p':
                    out = out + Fore.LIGHTGREEN_EX + str(maze[i][j]) + "  "
                else:
                    out = out + Fore.RED + str(maze[i][j]) + "  "
            out = out + '\n'
        print(Fore.RESET)
        # print(out, end='\r')
        return out

    # Find number of surrounding cells
    def surroundingCells(self, rand_wall):
        s_cells = 0
        if self.maze[rand_wall[0] - 1][rand_wall[1]] == 'o':
            s_cells += 1
        if self.maze[rand_wall[0] + 1][rand_wall[1]] == 'o':
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1] - 1] == 'o':
            s_cells += 1
        if self.maze[rand_wall[0]][rand_wall[1] + 1] == 'o':
            s_cells += 1

        return s_cells

    # Generate the maze
    def generateMaze(self):

        # Initialize colorama
        init()

        # Denote all cells as unvisited
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append(self.unvisited)
            self.maze.append(line)

        # Randomize starting point and set it a cell
        starting_height = int(random.random() * self.height)
        starting_width = int(random.random() * self.width)
        if starting_height == 0:
            starting_height += 1
        if starting_height == self.height - 1:
            starting_height -= 1
        if starting_width == 0:
            starting_width += 1
        if starting_width == self.width - 1:
            starting_width -= 1

        # Mark it as cell and add surrounding walls to the list
        self.maze[starting_height][starting_width] = self.cell
        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        # Denote walls in maze
        self.maze[starting_height - 1][starting_width] = '*'
        self.maze[starting_height][starting_width - 1] = '*'
        self.maze[starting_height][starting_width + 1] = '*'
        self.maze[starting_height + 1][starting_width] = '*'

        while walls:
            # Pick a random wall
            rand_wall = walls[int(random.random() * len(walls)) - 1]

            # Check if it is a left wall
            if rand_wall[1] != 0:
                if self.maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] + 1] == 'o':
                    # Find the number of surrounding cells
                    s_cells = self.surroundingCells(rand_wall)

                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'o'

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '*'
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Bottom cell
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '*'
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '*'
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check if it is an upper wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] + 1][rand_wall[1]] == 'o':

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'o'

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '*'
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '*'
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                        # Rightmost cell
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '*'
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check the bottom wall
            if rand_wall[0] != self.height - 1:
                if self.maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] - 1][rand_wall[1]] == 'o':

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'o'

                        # Mark the new walls
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '*'
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '*'
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '*'
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Check the right wall
            if rand_wall[1] != self.width - 1:
                if self.maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] - 1] == 'o':

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'o'

                        # Mark the new walls
                        if rand_wall[1] != self.width - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != 'o':
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '*'
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])
                        if rand_wall[0] != self.height - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '*'
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != 'o':
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '*'
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                            walls.remove(wall)

                    continue

            # Delete the wall from the list anyway
            for wall in walls:
                if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                    walls.remove(wall)

        # Mark the remaining unvisited cells as walls
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.maze[i][j] == 'u':
                    self.maze[i][j] = '*'

        #TODO
        # Set random entrance and exit

        # Set entrance and exit
        # for i in range(0, self.width):
        #     if self.maze[1][i] == 'o':
        #         self.maze[0][i] = 'o'
        #         self.start = [0, i]
        #         break
        #
        # for i in range(self.width - 1, 0, -1):
        #     if self.maze[self.height - 2][i] == 'o':
        #         self.maze[self.height - 1][i] = 'o'
        #         self.end = [self.height - 1, i]
        #         break

        rnd = random.randint(0, self.width - 1)
        while not self.maze[1][rnd] == 'o':
            rnd = random.randint(0, self.width - 1)
        self.maze[0][rnd] = 'o'
        self.start = [0, rnd]

        rnd = random.randint(0, self.width - 1)
        while not self.maze[self.height - 2][rnd] == 'o':
            rnd = random.randint(0, self.width - 1)
        self.maze[self.height - 1][rnd] = 'o'
        self.end = [self.height - 1, rnd]


        # Print final maze
        self.printMaze(self.maze)
        return self.maze

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getNumberOfNodes(self):
        n = 0
        for h in range(0, self.height):
            for w in range(0, self.width):
                if self.maze[h][w] == 'o':
                    n += 1
        return n

    def printSolvedMaze(self, path, visited):
        # Generate a copy of maze instead of referencing it (avoids override)
        copy = np.array(self.maze)
        for node in visited:
            copy[node.x][node.y] = 'v'
        for node in path:
            copy[node.x][node.y] = 'p'

        start = self.getStart()
        goal = self.getEnd()
        copy[start[0]][start[1]] = 'S'
        copy[goal[0]][goal[1]] = 'G'
        self.printMaze(copy)

    def getValues(self, node, copy = None):
        if copy is None:
            copy = []
            for h in range(0, self.height):
                row = []
                for w in range(0, self.width):
                    row.append(str(self.maze[h][w]))
                copy.append(row)

        copy[node.x][node.y] = str(node.value)

        for child in node.branches:
            self.getValues(child, copy)

        return copy

    def printMDP(self, root):
        maze = self.getValues(root)
        for i in range(0, self.height):
            for j in range(0, self.width):
                if maze[i][j] != '*':
                    if float(maze[i][j]) > 0:
                        print("  ",Fore.LIGHTGREEN_EX + str("%.2f" % float(maze[i][j])), end="")
                    elif float(maze[i][j]) == 0:
                        print("  ", Fore.RESET + str("%.2f" % float(maze[i][j])), end="")
                    elif float(maze[i][j]) < 0:
                        print(" ", Fore.RED + str("%.2f" % float(maze[i][j])), end="")
                else:
                    print("   ", Fore.LIGHTYELLOW_EX + str(maze[i][j]), end="  ")
            print('\n')
        print(Fore.RESET)