
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

"""  Recursive depth-first search algorithm for trees that keeps track of visited nodes
     and the correct path to the goal.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       path: a list of nodes that represent the path to the current node (default to an empty list)
     RETURN:
       tuple containing the list of nodes composing the path to the goal and the list of nodes visited"""
def depthFirstSearch(node, goal, visited=None):

    if visited is None:
        visited = set()

    # Add the current node to the visited set
    visited.add(node)

    # If the goal node is found, return the path to it and the visited set
    if node == goal:
        return list(visited)

    # Recursively search for the goal node in the branches of the current node
    for child in node.branches:
        if child not in visited:
            result = depthFirstSearch(child, goal, visited)
            if result is not None:
                return result

    # Return None if the goal node is not found in the tree
    return None

"""  Recursive depth-first search algorithm for trees that keeps track of visited nodes
     and the correct path to the goal.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       visited: a set of visited nodes (default to an empty set)
       path: a list of nodes that represent the path to the current node (default to an empty list)
     RETURN:
       tuple containing the list of nodes composing the path to the goal and the list of nodes visited"""
def breadthFirstSearch(node, goal, visited=None, queue=None):

    if visited is None:
        visited = set()
    if queue is None:
        queue = []

    visited.add(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)

        if current == goal:
            return list(visited)

        for child in current.branches:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return list(visited)


