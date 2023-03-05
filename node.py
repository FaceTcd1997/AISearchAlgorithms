
class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.branches = []

    def addChild(self, node):
        self.branches.append(node)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y))


def getNeighbors(maze, node):
    neighbors = []
    x, y = node.x, node.y
    if y > 0 and maze[x][y - 1] == 'o':  # check left neighbor
        neighbors.append(Node(x, y - 1))
    if y < len(maze[0]) - 1 and maze[x][y + 1] == 'o':  # check right neighbor
        neighbors.append(Node(x, y + 1))
    if x > 0 and maze[x - 1][y] == 'o':  # check top neighbor
        neighbors.append(Node(x - 1, y))
    if x < len(maze) - 1 and maze[x + 1][y] == 'o':  # check bottom neighbor
        neighbors.append(Node(x + 1, y))
    return neighbors

def diff(list1, list2):
    out = []
    for node in list1:
        if node not in list2:
            out.append(node)
    return out

def mazeToTree(maze, node, visited):
    # Add to visited nodes
    visited.append(node)
    # Get unvisited neighbors
    neighbors = getNeighbors(maze, node)
    # Remove already visited nodes
    neighbors = diff(neighbors, visited)

    if not neighbors:
        return node
    else:
        for neighbor in neighbors:
            mazeToTree(maze, neighbor, visited)  # visit neighbor recursively
            node.addChild(neighbor)  # add neighbor to the tree as a child of the current node

    return node