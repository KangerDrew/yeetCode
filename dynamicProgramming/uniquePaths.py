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
