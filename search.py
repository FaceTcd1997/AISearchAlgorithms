import random
from node import mazeToTree
from node import Node

"""  Recursive depth-first search algorithm for trees that keeps track of visited nodes
     and the correct path to the goal.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       path: a list of nodes that represent the path to the current node (default to an empty list)
     RETURN:
       tuple containing the list of nodes composing the path to the goal and the list of nodes visited"""
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

def getHeuristic(node, goal, maze):
    getCost(node, goal, maze)

    for child in node.branches:
        getHeuristic(child, goal, maze)

    return

def getCost(start, goal, maze):
    shadow = Node(start.x, start.y)
    tree = mazeToTree(maze, shadow)

    start.cost = len(getPath(tree, goal)) - 1
    # To be optimal heuristic has to be admissible (heuristic < cost)
    if start.cost > 0:
        start.heuristic = random.randint(0, start.cost - 1)
    else:
        start.heuristic = 0
    return



#TODO
# fix comments

"""  Recursive depth-first search algorithm for trees that keeps track of visited nodes
     and the correct path to the goal.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       path: a list of nodes that represent the path to the current node (default to an empty list)
     RETURN:
       tuple containing the list of nodes composing the path to the goal and the list of nodes visited"""
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

    depthFirstSearch(queue.pop(len(queue) - 1), goal, visited, queue)

    return visited

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

    breadthFirstSearch(queue.pop(0), goal, visited, queue)

    return visited

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

    #TODO
    # Sorting queue influence execution time ?!?
    queue.sort(key=lambda tup: tup[1])
    aStarSearch(queue.pop(0)[0], goal, visited, queue)

    return visited