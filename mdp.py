import copy

def getDeadEnds(node, goal):
    if node != goal and not node.branches:
        node.value = -1
    else:
        for child in node.branches:
            getDeadEnds(child, goal)
    return

def getReward(node, goal):
    if node == goal:
        return 1
    elif node != goal and not node.branches:
        return -1
    else:
        return 0

def compute(node, goal, discount):

    Q = []
    if node.branches:
        for child in node.branches:
            Q.append(getReward(node, goal) + (discount * child.value))
        node.value = max(Q)
    else:
        node.value = getReward(node, goal)

    # Recursive call to compute all nodes
    for child in node.branches:
        compute(child, goal, discount)

    return

def valueIteration(node, goal, discount, iterations):
    max_iter = iterations

    for i in range(0, max_iter):
        compute(node, goal, discount)

    return node


def policyExtraction(node, path=None):
    if path is None:
        path= [node]

    nextNone = None
    if node.branches:
        for child in node.branches:
            if nextNone is None:
                nextNone = child
            else:
                if child.value > nextNone.value:
                    nextNone = child

        path.append(nextNone)
        policyExtraction(nextNone, path)

    return path