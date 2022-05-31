def largestComponent(graph):
    largest = 0
    visited = set()
    for node in graph:
        largest = max(explore(graph, node, visited), largest)

    return largest


def explore(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)
    count = 1

    for neighbor in graph[current]:
        count += explore(graph, neighbor, visited)

    return count


sample = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(largestComponent(sample))
