from mazeGenerator import MazeGenerator

from node import Node
from node import mazeToTree

from search import getPath
from search import depthFirstSearch
from search import breadthFirstSearch
from search import getHeuristic

from timeit import default_timer as timer


# Define height and width of the maze
height = 30
width = 30
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
tree = mazeToTree(maze, root)
# Define the goal as a node
goal = Node(end[0], end[1])

# Save the time before executing search
startTimeDFS = timer()
# Run DFS
resultDFS = depthFirstSearch(tree, goal)
# Calculate execution time
endTimeDFS = timer()
timeDFS = endTimeDFS - startTimeDFS

# Save the time before executing search
startTimeBFS = timer()
# Run DFS
resultBFS = breadthFirstSearch(tree, goal)
# Calculate execution time
endTimeBFS = timer()
timeBFS = endTimeBFS - startTimeBFS


path = getPath(tree, goal)
mazeGenerator.printSolvedMaze(path, resultDFS)
mazeGenerator.printSolvedMaze(path, resultBFS)

print("DFS exec time: ", timeDFS)
print(" Number of nodes visited: ", len(resultDFS))
print("BFS exec time: ", timeBFS)
print(" Number of nodes visited: ", len(resultBFS))

# heuristicTree = generateHeuristic(tree, goal, maze)
#nodes = getNodes(tree)
#heuristicNodes = generateHeuristic(nodes, goal, maze)

#root = Node(start[0], start[1])
#tree = mazeToTree(maze, root)
#saveCost(tree, heuristicNodes)
#getHeuristic(tree, goal, maze)
print()
