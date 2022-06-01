class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraphDFS(node):
    oldToNew = {}

    def dfs(node_input):
        if node_input in oldToNew:
            return oldToNew[node_input]

        node_copy = Node(node_input.val)
        oldToNew[node_input] = node_copy

        node_copy.neighbors = [dfs(n) for n in node_input.neighbors]

        return node_copy

    return dfs(node) if node else None
