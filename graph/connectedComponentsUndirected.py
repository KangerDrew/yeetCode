# This function uses DFS to count the number of components (same as the
# problem from theory practice). While this is relatively decent method
# O(e + v), this isn't the most efficient way to count components...
def countComponentsDFS(n, edges):

    # Build adjacency list:
    graph = {i: [] for i in range(n)}
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # count variable keeps track of number of components:
    count = 0
    # visited set keeps track of which nodes are already travelled:
    visited = set()

    def dfs(current):
        # Base Case: if node is travelled, return false
        if current in visited:
            return False

        # Add node to visited:
        visited.add(current)

        # Travel to adjacent nodes and recursively
        # add them to visited set:
        for neighbor in graph[current]:
            dfs(neighbor)

        # ONLY return True once for loop completes since
        # exiting for loop indicates that we've fully
        # explored all possible paths of the node
        return True

    # Finally, use dfs function on each node and increment count
    # by 1 everytime a new unexplored component is found:
    for node in graph:
        count += 1 if dfs(node) else 0

    return count


