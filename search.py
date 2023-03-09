import random
from node import mazeToTree
from node import Node

"""  Recursive depth-first search algorithm for trees that keeps track of visited nodes.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       queue: a list of nodes to iterate on (default to an empty list)
     RETURN:
       list of nodes visited"""
def depthFirstSearch(node, goal, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = []

    visited.add(node)

    if node == goal:
        return visited

    for child in node.branches:
        queue.append(child)

    # DFS uses a LIFO queue
    depthFirstSearch(queue.pop(len(queue) - 1), goal, visited, queue)

    return visited

"""  Recursive breadth-first search algorithm for trees that keeps track of visited nodes.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       queue: a list of nodes to iterate on (default to an empty list)
     RETURN:
       list of nodes visited"""
def breadthFirstSearch(node, goal, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = []

    visited.add(node)

    if node == goal:
        return visited

    for child in node.branches:
        queue.append(child)

    # BFS uses a FIFO queue
    breadthFirstSearch(queue.pop(0), goal, visited, queue)

    return visited

"""  Recursive A-star search algorithm for trees that keeps track of visited nodes.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       queue: a list of nodes to iterate on (default to an empty list)
     RETURN:
       list of nodes visited"""
def aStarSearch(node, goal, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = []

    visited.add(node)

    if node == goal:
        return visited

    for child in node.branches:
        queue.append([child, child.cost + child.heuristic])

    # A* search uses a priority queue
    # priority is given to the node with the smaller sum of cost and heuristic
    queue.sort(key=lambda tup: tup[1])
    aStarSearch(queue.pop(0)[0], goal, visited, queue)

    return visited

# Retrieve path to the goal using DFS
def getPath(node, goal, visited=None, path=None):

    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Add the current node to the path and visited set
    path.append(node)
    visited.add(node)

    # If the goal node is found, return the path to it and the visited set
    if node == goal:
        return path

    # Recursively search for the goal node in the branches of the current node
    for child in node.branches:
        if child not in visited:
            result = getPath(child, goal, visited, path)
            if result is not None:
                return result

    # If the goal node is not found in any child node, backtrack and remove the current node from the path
    path.pop()

    # Return None if the goal node is not found in the tree
    return None

# Add real cost and heuristic cost to all the nodes
def getHeuristic(node, goal, maze):
    getCost(node, goal, maze)

    for child in node.branches:
        getHeuristic(child, goal, maze)

    return

# Calculate real cost and heuristic of a node
def getCost(start, goal, maze):
    # Create a copy of the node to dereference it
    shadow = Node(start.x, start.y)
    # Create the tree from the maze using the current node as start
    tree = mazeToTree(maze, shadow)

    # Real cost of the node is the distance to the goal
    start.cost = len(getPath(tree, goal)) - 1
    # Random generate an admissible heuristic for the node (heuristic < cost)
    if start.cost > 0:
        start.heuristic = random.randint(0, start.cost - 1)
    else:
        start.heuristic = 0
    return