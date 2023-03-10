
class Node:

    def __init__(self, x, y, cost=None, heuristic=None, value=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.value = 0
        self.branches = []

    # Add child to the node
    def addChild(self, node):
        self.branches.append(node)

    def __eq__(self, other): # to allow comparison
        if isinstance(other, self.__class__):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __ne__(self, other): # to allow comparison
        return not self.__eq__(other)

    def __hash__(self): # to allow iterations
        return hash((self.x, self.y))

    def __lt__(self, other): # to allow < comparison
        if isinstance(other, self.__class__):
            return (self.x < other.x) and (self.y < other.y)
        else:
            return False
    def __le__(self, other): # to allow <= comparison
        if isinstance(other, self.__class__):
            return (self.x <= other.x) and (self.y <= other.y)
        else:
            return False

# Convert a maze to the correspondent tree
def mazeToTree(maze, node, visited=None):
    if visited is None:
        visited = []
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

# Get neighbors of a node from the maze
def getNeighbors(maze, node):
    neighbors = set()
    x, y = node.x, node.y
    if y > 0 and maze[x][y - 1] != '*':  # check left neighbor
        neighbors.add(Node(x, y - 1))
    if y < len(maze[0]) - 1 and maze[x][y + 1] != '*':  # check right neighbor
        neighbors.add(Node(x, y + 1))
    if x > 0 and maze[x - 1][y] != '*':  # check top neighbor
        neighbors.add(Node(x - 1, y))
    if x < len(maze) - 1 and maze[x + 1][y] != '*':  # check bottom neighbor
        neighbors.add(Node(x + 1, y))
    return neighbors

# Get not shared elements
def diff(list1, list2):
    out = []
    for node in list1:
        if node not in list2:
            out.append(node)
    return out