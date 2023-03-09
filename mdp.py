
"""  Value Iteration algorithm for MDP search on trees that calculates values, number of iterations and the best path.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       discount: the discount value for the given problem
     RETURN:
       tree: the tree with values of nodes
       iterations: the number of iterations executed
       path: the optimal path individuated"""
def valueIteration(node, goal, discount):
    iterations = 0
    oldValues = []

    while True:
        # Compute new values
        newValues = compute(node, goal, discount)
        iterations += 1

        # Value iteration algorithm converges when values don't chance
        if oldValues == newValues:
            break
        else:
            oldValues = newValues

    # Once algorithm converge extract the optimal path
    path, goalReached = policyExtraction(node, goal) # goalReached is ignored (used for policy iteration)

    return node, iterations, path

"""  Policy Iteration algorithm for MDP search on trees that calculates values, number of iterations and the best path.

     INPUT:
       node: the root node of the tree
       goal: the goal node to search for
       discount: the discount value for the given problem
     RETURN:
       tree: the tree with values of nodes
       iterations: the number of iterations executed
       path: the optimal path individuated"""
def policyIteration(node, goal, discount):
    iterations = 0
    oldPath = []

    while True:
        # Compute new values
        compute(node, goal, discount)
        # Retrieve the policy for new values
        newPath, goalReached = policyExtraction(node, goal)
        iterations += 1

        # Value iteration algorithm converges when policy don't change
        if goalReached and oldPath == newPath:
            break
        else:
            oldPath = newPath

    return node, iterations, oldPath

# For all the nodes calculate the values with Bellman equation
def compute(node, goal, discount, values=None):
    if values is None:
        values = []

    if node.branches:
        Q = []
        for child in node.branches:
            # Bellman equation for deterministic environment
            Q.append(getReward(node, goal) + (discount * child.value))
        # Select max
        node.value = max(Q)
    else:
        node.value = getReward(node, goal)

    values.append(node.value)

    # Recursive call to compute all nodes
    for child in node.branches:
        compute(child, goal, discount, values)

    return values

# Retrieve the reward of a node
def getReward(node, goal):
    # Reward for goal is 1
    if node == goal:
        return 1
    # Reward for dead ends is -1
    elif node != goal and not node.branches:
        return -1
    else:
        return 0

# Retrieve the best path from the nodes based on nodes values
def policyExtraction(node, goal, path=None, goalReached=None):
    if path is None:
        path = []
    if goalReached is None:
        goalReached = False

    # Add node to the path
    path.append(node)
    # If goal is met stop
    if node == goal:
        goalReached = True
        return path, goalReached

    nextNode = None

    if node.branches:
        # If there is one optimum value select as next
        bestNode = [child for child in node.branches if child.value > node.value]
        if len(bestNode) == 1:
            nextNode = bestNode[0]
        else:
            # If there is only one non-negative value select as next
            goodNodes = [child for child in node.branches if child.value >= node.value]
            if len(goodNodes) == 1:
                nextNode = goodNodes[0]
        # If next node is identified continue
        if nextNode is not None:
            path, goalReached = policyExtraction(nextNode, goal, path, goalReached)

    return path, goalReached