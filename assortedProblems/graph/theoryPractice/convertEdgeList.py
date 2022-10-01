def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge[0], edge[1]

        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


sample = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
print(buildGraph(sample))
