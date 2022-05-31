def connectedCount(graph):
    count = 0
    visited = set()
    for node in graph:
        count += 1 if explore(graph, node, visited) else 0

    return count


def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    # ONLY return True once for loop completes since
    # exiting for loop indicates that we've fully
    # explored all possible paths of the node
    return True


sample = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(connectedCount(sample))
