# Topdown memoization solution:
def uniquePathsTopdown(m, n):

    # Initialize memoization hash map:
    memo = {}

    def helper(r, c):
        # Base case - If the input is a grid dimension where
        # it's a single row or a single column, there can only
        # be one way to reach the end:
        if r == 1 or c == 1:
            return 1

        # Check if current dimension has already been solved:
        if (r, c) in memo:
            return memo[(r, c)]

        # Calculate the possible solution - two possible routes,
        # go down or go to the right:
        sol = helper(r - 1, c) + helper(r, c - 1)
        # Store the calculated result and return it:
        memo[(r, c)] = sol
        return sol

    # Use helper:
    return helper(m, n)


# Bottom up approach to the same problem:
def uniquePathsBottomUp(m, n):

    grid = [[0 for j in range(n + 1)] for i in range(m + 1)]
    grid[1][1] = 1

    for i in range(1, m + 1):

        for j in range(1, n + 1):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]

# Same bottom up approach, w less memory usage
def uniquePathsBottomUpLessMem(m, n):
    row = [0 for i in range(n + 1)]
    row[1] = 1

    for j in range(m):

        newRow = [0 for k in range(n + 1)]

        for cur in range(1, n + 1):
            newRow[cur] = newRow[cur - 1] + row[cur]

        row = newRow

    return newRow[-1]
