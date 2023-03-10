import copy
import sys
from timeit import default_timer as timer
from mazeGenerator import MazeGenerator
from node import Node
from node import mazeToTree
from search import getPath
from search import depthFirstSearch
from search import breadthFirstSearch
from search import getHeuristic
from search import aStarSearch
from mdp import valueIteration
from mdp import policyIteration

# Define height and width of the maze from args
height = int(sys.argv[1])
width = int(sys.argv[2])

# Initialize generator
mazeGenerator = MazeGenerator(height, width)

# Generate maze and retrieve start and end and number of nodes
print("Maze:")
maze = mazeGenerator.generateMaze()
start = mazeGenerator.getStart()
end = mazeGenerator.getEnd()
nNodes = mazeGenerator.getNumberOfNodes()

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
timeDFS = timer() - startTimeDFS

# Save the time before executing search
startTimeBFS = timer()
# Run DFS
resultBFS = breadthFirstSearch(tree, goal)
# Calculate execution time
timeBFS = timer() - startTimeBFS

# Calculate heuristic and add to the nodes
getHeuristic(tree, goal, maze)

# Save the time before executing search
startTimeA = timer()
# Run DFS
resultA = aStarSearch(tree, goal)
# Calculate execution time
timeA = timer() - startTimeA

# Avoid policy iteration to run with values previously calculated by value iteration
treeVI = copy.deepcopy(tree)
treePI = copy.deepcopy(tree)

# Save the time before executing search
startTimeVI = timer()
# Execute value iteration
resultVI = valueIteration(treeVI, goal, 0.9)
# Calculate execution time
timeVI = timer() - startTimeVI

# Save the time before executing search
startTimePI = timer()
# Execute policy iteration
resultPI = policyIteration(treePI, goal, 0.9)
# Calculate execution time
timePI = timer() - startTimePI

# Retrieve the path to print with DFS
path = getPath(tree, goal)
# Print solved mazes for all the algorithms
print("DFS:")
mazeGenerator.printSolvedMaze(path, resultDFS)
print("BFS:")
mazeGenerator.printSolvedMaze(path, resultBFS)
print("A*:")
mazeGenerator.printSolvedMaze(path, resultA)
print("Value Iteration:")
mazeGenerator.printSolvedMaze(resultVI[2], [])
print("Policy Iteration:")
mazeGenerator.printSolvedMaze(resultPI[2], [])

# Print output V values of nodes for Value Iteration and Policy Iteration
print("Value Iteration - Nodes values")
mazeGenerator.printMDP(resultVI[0])
print("Policy Iteration - Nodes values")
mazeGenerator.printMDP(resultPI[0])

# Print metrics for all the algorithms
print("---------------TREE SEARCH---------------")
print("DFS:")
print("     Exec time: %.10f" % timeDFS, "s")
print("     Number of nodes visited:", len(resultDFS))
print("     Percentage of nodes visited:",int(len(resultDFS)/nNodes * 100), "%")
print("BFS:")
print("     Exec time: %.10f" % timeBFS, "s")
print("     Number of nodes visited:", len(resultBFS))
print("     Percentage of nodes visited:", int(len(resultBFS)/nNodes * 100), "%")
print("A*:")
print("     Exec time: %.10f" % timeA, "s")
print("     Number of nodes visited:", len(resultA))
print("     Percentage of nodes visited:", int(len(resultA)/nNodes * 100), "%")
print("-------------------MDP-------------------")
print("Value Iteration:")
print("     Exec time: %.10f" % timeVI, "s")
print("     Number of iterations:", resultVI[1])
print("     Number of nodes visited:", nNodes * resultVI[1])
print("Policy Iteration:")
print("     Exec time: %.10f" % timePI, "s")
print("     Number of iterations:", resultPI[1])
print("     Number of nodes visited:", nNodes * resultPI[1])
print()
exit(1)
