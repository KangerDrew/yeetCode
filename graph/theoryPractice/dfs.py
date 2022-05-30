def DFS(graph, source):

    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

    return None


sample = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

DFS(sample, "a")


def DFSRecursive(graph, source):
    print(source)

    for item in graph[source]:
        DFSRecursive(graph, item)

    return None


DFSRecursive(sample, "a")

# DFS uses stack (Last In First Out) to traverse the graph

# Note how DFSRecursive traversed b first instead of c,
# this is because regular DFS uses stack, where it appended
# b first, which led to c being "popped off" earlier and
# getting traversed before c!
