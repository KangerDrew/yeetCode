# First algorithm uses DFS to count the number of components (islands).
# While this is relatively efficient O(e + v), this isn't the most
# efficient way to count components:
def countComponentsDFS(n, edges):
    graph = {i: [] for i in range(n)}
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    count = 0
    visited = set()

    def dfs(current):
        if current in visited:
            return False

        visited.add(current)

        for neighbor in graph[current]:
            dfs(neighbor)

        # ONLY return True once for loop completes since
        # exiting for loop indicates that we've fully
        # explored all possible paths of the node
        return True

    for node in graph:
        count += 1 if dfs(node) else 0

    return count


