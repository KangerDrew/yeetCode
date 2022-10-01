# Coped & modified from the original variant problem:

# The introduction of "obstacle" means we need to make following adjustments
# to the original solution:

# 1) We are given a grid instead of just the dimension. Get the dimension.
# 2) In our for loop, we need to introduce an if condition to skip over the
# loop if there is an obstacle, as it would mean there's 0 ways to reach that
# position of the grid.
# 3) Edge case - If the starting point is an obstacle, that means the grid is
# impossible to traverse. Immediately return 0.

def uniquePathsIIBottomUp(obstacleGrid):
    # Edge case - If the starting point is an obstacle, that means the grid is
    # impossible to traverse. Immediately return 0.
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
