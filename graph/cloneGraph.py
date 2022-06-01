from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraphDFS(node):
    oldToNew = {}

    def dfs(node_input):
        # if node is already mapped (traveled), simply
        # return the copied node:
        if node_input in oldToNew:
            return oldToNew[node_input]

        # If node was not travelled, we create a new copy node:
        node_copy = Node(node_input.val)
        # Add the copy to the hash map:
        oldToNew[node_input] = node_copy

        # Loop through each adjacent node (neighbor) of the original node,
        # and add them to the neighbors of the copy node:
        node_copy.neighbors = [dfs(n) for n in node_input.neighbors]

        # return the copied node:
        return node_copy

    return dfs(node) if node else None


def cloneGraphBFS(node):

    # If first node is None, don't iterate through just return it:
    if not node:
        return node

    # Same dictionary (hash map) as DFS:
    oldToNew = {}

    # Use python's deque, which is a specialized list with constant
    # lookup for first element:
    queue = deque([node])

    # Add the current node to the hash map:
    oldToNew[node] = Node(node.val)

    while queue:

        # Grab the first node currently in the queue:
        n = queue.popleft()

        # loop through the connecting nodes,
        for neighbor in n.neighbors:
            # if a neighbor node of n is not in the hash map, create and add it
            # to the map, then append the original to the queue:
            if neighbor not in oldToNew:

                oldToNew[neighbor] = Node(neighbor.val)

                queue.append(neighbor)

            # Append the copied neighbor to the neighbor list of the copied node:
            oldToNew[n].neighbors.append(oldToNew[neighbor])

    return oldToNew[node]


