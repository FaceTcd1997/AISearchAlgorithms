from mazeGenerator import MazeGenerator
from node import Node
from node import mazeToTree
from search import getPath
from search import depthFirstSearch
from search import breadthFirstSearch
from timeit import default_timer as timer


# Define height and width of the maze
height = 10
width = 10
# Initialize generator
mazeGenerator = MazeGenerator(height, width)

# Generate maze and retrieve start and end
maze = mazeGenerator.generateMaze()
start = mazeGenerator.getStart()
end = mazeGenerator.getEnd()
# Print info of the maze
print("Start ", start)
print("End ", end)
print("Number of nodes", mazeGenerator.getNumberOfNodes())

# Initialize root of the tree
root = Node(start[0], start[1])
# Convert maze to tree
tree = mazeToTree(maze, root, [])
# Define the goal as a node
goal = Node(end[0], end[1])

# Save the time before executing search
startTime = timer()
# Run DFS
resultDFS = depthFirstSearch(tree, goal)
# Calculate execution time
timeDFS = timer() - startTime
print(timeDFS)


# Save the time before executing search
startTime = timer()
# Run DFS
resultBFS = breadthFirstSearch(tree, goal)
# Calculate execution time
timeBFS = timer() - startTime
print(timeBFS)

path = getPath(tree, goal)
# Print as a maze the results from DFS execution
#mazeGenerator.printSolvedMaze(path, resultBFS)

mazeGenerator.printSolvedMaze(path, resultDFS)
mazeGenerator.printSolvedMaze(path, resultBFS)
print()


