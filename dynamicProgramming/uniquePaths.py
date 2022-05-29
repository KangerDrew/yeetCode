def uniquePaths(m, n):

    grid = []

    for i in range(m + 1):
        grid.append([0] * (n + 1))

    grid[1][1] = 1

    for i in range(1, m + 1):

        for j in range(1, n + 1):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]


print(uniquePaths(2, 3))


def uniquePathsRecursive(m, n):

    if n == 1 or m == 1:
        return 1

    return uniquePathsRecursive(m - 1, n) + uniquePathsRecursive(m, n - 1)


print(uniquePathsRecursive(2, 3))
