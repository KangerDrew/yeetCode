# Topdown memoization solution:

def uniquePathsTopdown(m, n):
    memo = {}

    def helper(r, c):
        if r == 1 or c == 1:
            return 1

        if (r, c) in memo:
            return memo[(r, c)]

        sol = helper(r - 1, c) + helper(r, c - 1)
        memo[(r, c)] = sol
        return sol

    return helper(m, n)
