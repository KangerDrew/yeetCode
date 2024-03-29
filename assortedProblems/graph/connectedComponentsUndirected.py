# This function uses DFS to count the number of components (same as the
# problem from theory practice). While this is relatively decent method
# O(n + e), this isn't the most efficient way to count components...
# (n = # of nodes, e = # of edges)
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


# The below function uses Union Find to determine the number of connected
# components, in a constant time O(n)!
def countComponentsUnion(n, edges):
    # We need "parents" array in order to keep track of which nodes
    # are grouped together. Initially, each node will be their own
    # parent. However as they are joined, a single node (parent) will
    # be selected to "represent" the joined component:
    parents = [i for i in range(n)]

    # "rank" array is used to determine which parent will become the newest
    # parent when a union between two components occur. When it does, the
    # parent node with the larger rank will become the new parent:
    rank = [1] * n

    # find() function returns the "parent" of the given node:
    def find(node):

        # If current node's parent its own parent:
        if node == parents[node]:
            return node

        # Otherwise, we must recursively track the
        # parent of the node:
        parents[node] = find(parents[node])
        return parents[node]

    # union() function will combine two components into one, and
    # return 1 if union did occur. If no union can occur (i.e.
    # two nodes have the same parent), then we return 0:
    def union(node1, node2):

        # If the nodes have the same parent, they already belong to
        # the same component. Thus no union occurs, and we return 0:
        if node1 == node2:
            return 0

        # Check which parent node has a higher rank. The parent with
        # lower rank will take the larger ranking parent as its new parent!
        # Furthermore, we will increase the rank of the larger parent by
        # the rank of the smaller parent:
        if rank[node2] > rank[node1]:
            parents[node1] = node2
            rank[node2] += rank[node1]
        else:
            parents[node2] = node1
            rank[node1] += rank[node2]

        # After union process is successful, we return 1, signifying that
        # there are now 1 less component!
        return 1

    # Initially, there are n number of components since each nodes are their
    # own independent component:
    total_components = n

    # We loop through the provided edge list, and perform union() on them.
    # If union does occur (i.e. New component is created), union() returns 1
    # and we decrement total_components count by 1 as such:
    for n1, n2 in edges:
        # Get the parents of node1 and node 2:
        p1, p2 = find(n1), find(n2)
        total_components -= union(p1, p2)

    # Return total_components
    return total_components

