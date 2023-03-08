from timeit import default_timer as timer
from mazeGenerator import MazeGenerator
from node import Node
from node import mazeToTree
from search import getPath
from search import depthFirstSearch
from search import breadthFirstSearch
from search import getHeuristic
from search import aStarSearch
from mdp import getDeadEnds
from mdp import valueIteration
from mdp import policyExtraction



# Define height and width of the maze
height = 20
width = 20
# Initialize generator
mazeGenerator = MazeGenerator(height, width)

# Generate maze and retrieve start and end
maze = mazeGenerator.generateMaze()
start = mazeGenerator.getStart()
end = mazeGenerator.getEnd()
nNodes = mazeGenerator.getNumberOfNodes()
# Print info of the maze
print("Start ", start)
print("End ", end)
print("Number of nodes", nNodes)

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

# Include heuristic to the nodes
getHeuristic(tree, goal, maze)
# Save the time before executing search
startTimeA = timer()
# Run DFS
resultA = aStarSearch(tree, goal)
# Calculate execution time
endTimeA = timer()
timeA = endTimeA - startTimeA


path = getPath(tree, goal)
mazeGenerator.printSolvedMaze(path, resultDFS)
mazeGenerator.printSolvedMaze(path, resultBFS)
mazeGenerator.printSolvedMaze(path, resultA)


print("DFS exec time: %.10f" % timeDFS, "s")
print("     Number of nodes visited:", len(resultDFS))
print("     Percentage of nodes visited:",int(len(resultDFS)/nNodes * 100), "%")
print("BFS exec time: %.10f" % timeBFS, "s")
print("     Number of nodes visited:", len(resultBFS))
print("     Percentage of nodes visited:", int(len(resultBFS)/nNodes * 100), "%")
print("A* exec time: %.10f" % timeA, "s")
print("     Number of nodes visited:", len(resultA))
print("     Percentage of nodes visited:", int(len(resultA)/nNodes * 100), "%")

valueIteration(tree, goal, 0.9, 100)
mazeGenerator.printMDP(tree)
#pathVI = policyExtraction(tree)
#mazeGenerator.printSolvedMaze(pathVI, [])

print()
