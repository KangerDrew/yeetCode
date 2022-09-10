# Coped & modified from the original variant problem:

def uniquePathsIIBottomUp(obstacleGrid):

    if obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid[0]), len(obstacleGrid)

    grid = [[0 for j in range(n + 1)] for i in range(m + 1)]
    grid[1][1] = 1

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if obstacleGrid[j - 1][i - 1] == 1:
                continue
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]


print(uniquePathsIIBottomUp([[0, 0]]))
