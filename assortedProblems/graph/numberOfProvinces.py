# Another problem you can solve by using union find! This is exact same code
# as the one shown in connectedComponentsUndirected problem...

def numberOfProvince(isConnected):

    parent = [i for i in range(len(isConnected))]
    rank = [1 for i in range(len(isConnected))]

    def find(n):
        res = n

        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]

        return res

    def union(p1, p2):

        if p1 == p2:
            return 0

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]

        return 1

    total_comp = len(isConnected)

    for r in range(len(isConnected)):
        for c in range(len(isConnected[0])):

            # Only perform union if there is a connection
            if isConnected[r][c] == 1:
                parent1, parent2 = find(r), find(c)
                total_comp -= union(parent1, parent2)

    return total_comp


