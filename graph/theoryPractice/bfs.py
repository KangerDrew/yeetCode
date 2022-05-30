def BFS(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)  # Remove FIRST element
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

    return None


sample = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

BFS(sample, "a")

# Pretty much same function as DFS, except we're popping the
# first element using queue (First In First Out). This data
# structure prevents us from using recursion!
